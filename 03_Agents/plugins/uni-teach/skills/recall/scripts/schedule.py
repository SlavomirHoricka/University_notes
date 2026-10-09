#!/usr/bin/env python3
"""Pure recall calculations and conservative synchronization decisions; no network/writes.

Transparent fixed-factor heuristic, not published SM-2. The agent uses the
installed Todoist harness and the shared records writer separately.
"""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import date, datetime, timedelta
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata
from zoneinfo import ZoneInfo

ZONE = ZoneInfo("Europe/Prague")
VERSIONS = ("objective_revision", "criterion_version", "plan_version", "source_version", "ingestion_revision")


def normalize_identity(value: str) -> str:
    """Normalize Unicode composition, case, underscores/whitespace, not meaning."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("identity must be a nonempty string")
    return " ".join(unicodedata.normalize("NFC", value).replace("_", " ").casefold().split())


def match_projects(projects: list[dict], course_title: str, course_code: str | None) -> dict:
    names = {normalize_identity(course_title)}
    if course_code:
        names.update((normalize_identity(course_code), normalize_identity(course_code + " " + course_title)))
    matches = [p for p in projects if not p.get("isArchived", False)
               and normalize_identity(p["name"]) in names]
    return {"status": "unique" if len(matches) == 1 else "missing" if not matches else "ambiguous",
            "matches": [{"id": str(p["id"]), "name": p["name"]} for p in matches],
            "accepted_normalized_names": sorted(names)}


def answer_date(occurred_at: str) -> date:
    """Observed instant's Prague date, requiring an explicit offset."""
    stamp = datetime.fromisoformat(occurred_at.replace("Z", "+00:00"))
    if stamp.tzinfo is None:
        raise ValueError("occurred_at needs an actual timezone offset")
    return stamp.astimezone(ZONE).date()


def next_review(outcome: str, previous_interval: int | None, reviewed_on: date,
                previous_successes: int | None = None) -> dict:
    """Half-up rounding uses integer arithmetic, never bankers' rounding."""
    if outcome in {"initial", "failure"}:
        interval = 1
    elif outcome == "success":
        if not isinstance(previous_interval, int) or isinstance(previous_interval, bool) or previous_interval < 1:
            raise ValueError("success needs a positive integer previous interval")
        if previous_successes is not None and (not isinstance(previous_successes, int)
                or isinstance(previous_successes, bool) or previous_successes < 0):
            raise ValueError("previous_successes must be a nonnegative integer")
        first_delayed_pass = previous_successes == 0 if previous_successes is not None else previous_interval == 1
        interval = 6 if first_delayed_pass else max(previous_interval + 1, (previous_interval * 5 + 1) // 2)
    else:
        raise ValueError("outcome must be initial, success, or failure")
    return {"interval_days": interval, "due_date": (reviewed_on + timedelta(days=interval)).isoformat()}


def logical_key(course_id: str, objective_id: str) -> str:
    return "uni-recall:v1:" + hashlib.sha256((course_id + "\n" + objective_id).encode()).hexdigest()[:24]


def review_id(current: dict, trigger_id: str, kind: str) -> str:
    data = [current["course_id"], current["objective_id"], *[current[v] for v in VERSIONS], trigger_id, kind]
    return "R-" + hashlib.sha256(json.dumps(data, ensure_ascii=False).encode()).hexdigest()[:24]


def events_from_markdown(text: str) -> list[dict]:
    """Structured JSON only; legacy prose/YAML is never upgraded into evidence."""
    events = []
    for raw in re.findall(r"(?m)^```json\s*\n(.*?)\n```\s*$", text, flags=re.S):
        value = json.loads(raw)
        if isinstance(value, dict) and "event_id" in value:
            events.append(value)
    return events


def effective_events(events: list[dict]) -> list[dict]:
    """Replay explicit recorded-fact corrections, retaining original IDs and provenance.

    The original stored event is never changed. corrected_fields cannot change
    its definition tuple/time/item: that would reinterpret a historical attempt.
    """
    unique, order = {}, []
    for event in events:
        event_id = event.get("event_id")
        if not isinstance(event_id, str) or not event_id:
            raise ValueError("event_id missing")
        if event_id in unique:
            if json.dumps(unique[event_id], sort_keys=True) != json.dumps(event, sort_keys=True):
                raise ValueError("conflicting event_id: " + event_id)
            continue
        unique[event_id] = event
        order.append(event_id)
    allowed = {"outcome", "component_outcomes", "independent", "assistance", "response_evidence",
               "observed_errors", "note_access", "tools", "solution_exposure", "last_relevant_exposure_at",
               "elapsed_hours_since_exposure", "intervening_exposure", "intervening_exposure_details"}
    effective, aliases, result_order = {}, {}, []
    for eid in order:
        event = unique[eid]
        if event.get("committed") is not True:
            continue
        if event.get("writer") != "teach" or not event.get("transaction_id"):
            raise ValueError("committed learning event lacks teach ownership/transaction")
        if event.get("event_type") == "correction":
            target_id = event.get("supersedes_event_id")
            target_id = aliases.get(target_id, target_id)
            target = effective.get(target_id)
            fields = event.get("corrected_fields")
            if target is None or target.get("event_type") != "attempt_result":
                raise ValueError("correction references absent/uncommitted prior attempt")
            if not isinstance(fields, dict) or not fields or not set(fields).issubset(allowed):
                raise ValueError("correction fields absent or change historical identity")
            target.update(deepcopy(fields))
            target.setdefault("correction_event_ids", []).append(eid)
            aliases[eid] = target_id
        else:
            if event.get("supersedes_event_id"):
                raise ValueError("only correction events may supersede recorded facts")
            effective[eid] = deepcopy(event)
            result_order.append(eid)
    return [effective[eid] for eid in result_order]


def _current_event(event: dict, current: dict) -> bool:
    return (event.get("objective_id") == current["objective_id"]
            and event.get("course_id", current["course_id"]) == current["course_id"]
            and compatible_tuple(event, current))


def compatible_tuple(value: dict, current: dict) -> bool:
    if all(type(value.get(v)) is type(current[v]) and value.get(v) == current[v] for v in VERSIONS):
        return True
    # Plan, not recall, approves semantic equivalence and exact historical tuples.
    return any(approval.get("requires_reassessment") is False and bool(approval.get("reason"))
               and approval.get("change_class") in {"unchanged", "formatting_only", "path_only"}
               and all(type(value.get(v)) is type(approval.get(v)) and value.get(v) == approval.get(v) for v in VERSIONS)
               for approval in current.get("compatible_versions", []))


def _independent_pass(event: dict) -> bool:
    assistance = event.get("assistance")
    return (event.get("outcome") == "pass" and event.get("independent") is True
            and isinstance(assistance, dict) and assistance.get("level") == "none"
            and event.get("response_evidence") is not None and event.get("response_evidence") != "")


def derive_schedule(events: list[dict], current: dict, previous: dict | None = None) -> dict:
    """Replay teach-owned facts, without grading or inventing acquisition.

    current comes from a ready plan/manifest, matched to ingest revision.
    acquisition_met is teach's assertion that the prepared rule is met;
    support references are checked here, not re-graded.
    """
    for field in ("course_id", "objective_id", *VERSIONS):
        if current.get(field) is None:
            raise ValueError("missing current identity: " + field)
    if not isinstance(current["ingestion_revision"], int) or isinstance(current["ingestion_revision"], bool) or current["ingestion_revision"] < 1:
        raise ValueError("ingestion_revision must be a positive integer")
    result = {"logical_key": logical_key(current["course_id"], current["objective_id"]),
              **{k: current[k] for k in ("course_id", "objective_id", *VERSIONS)},
              "status": "acquisition_required", "kind": "continuation", "due_date": None,
              "interval_days": None, "delayed_successes": 0, "supporting_event_ids": [],
              "review_id": None, "last_observed_response_at": None,
              "processed_event_ids": [], "warnings": []}
    prior = previous or {}
    requirement = current.get("reassessment_requirement")
    if requirement is not None and (not isinstance(requirement, dict) or not requirement.get("requirement_id")):
        raise ValueError("named plan reassessment requirement missing identity")
    named_gate_met = requirement is None
    if requirement is not None:
        result.update(status="version_gate", kind="reassessment")
    if prior.get("due_date") and not compatible_tuple(prior, current):
        result.update(status="version_gate", kind="reassessment", due_date=prior["due_date"],
                      interval_days=prior.get("interval_days"), supersedes_review_id=prior.get("review_id"))
    resolved = effective_events(events)
    facts = {e["event_id"]: e for e in resolved}
    # Appended scoring corrections can refer to an older response instant.
    # Replay observed time, retaining append order for identical instants.
    resolved = sorted(resolved, key=lambda e: datetime.fromisoformat(e["occurred_at"].replace("Z", "+00:00"))
                      if e.get("occurred_at") else datetime.min.replace(tzinfo=ZONE))
    last_instant = None
    for event in resolved:
        if event.get("event_type") not in {"attempt_result", "acquisition_met", "reassessment_met"} or not _current_event(event, current):
            continue
        stamp = event.get("occurred_at")
        if not stamp:
            result["warnings"].append(event["event_id"] + ": no observed timestamp; not scheduled")
            continue
        on = answer_date(stamp)
        instant = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if last_instant is not None and instant < last_instant:
            raise ValueError("matching events out of observed chronological order")
        last_instant = instant
        if event["event_type"] in {"acquisition_met", "reassessment_met"}:
            if event["event_type"] == "reassessment_met":
                if requirement is None or event.get("requirement_id") != requirement["requirement_id"]:
                    result["warnings"].append(event["event_id"] + ": no matching prepared reassessment requirement")
                    continue
            elif not named_gate_met:
                result["warnings"].append(event["event_id"] + ": named reassessment requirement still open")
                continue
            ids = event.get("evidence_event_ids", [])
            supports = [facts.get(eid) for eid in ids]
            if not ids or len(set(ids)) != len(ids) or any(s is None or s["event_type"] != "attempt_result" or not _current_event(s, current)
                              or not _independent_pass(s) or s.get("review_kind") not in {"immediate", "reassessment"}
                              or not s.get("occurred_at") for s in supports):
                result["warnings"].append(event["event_id"] + ": acquisition support incomplete/incompatible")
                continue
            if any(datetime.fromisoformat(s["occurred_at"].replace("Z", "+00:00")) > instant for s in supports):
                raise ValueError("acquisition precedes supporting responses")
            named_gate_met = True
            if result["status"] == "scheduled":
                # Repeated exposure/acquisition does not postpone an outstanding review.
                result["processed_event_ids"].append(event["event_id"])
                continue
            latest_support = max(datetime.fromisoformat(s["occurred_at"].replace("Z", "+00:00")) for s in supports)
            result.update(next_review("initial", None, latest_support.astimezone(ZONE).date()), status="scheduled", kind="delayed",
                          delayed_successes=0, supporting_event_ids=ids + [event["event_id"]]
                          + [cid for support in supports for cid in support.get("correction_event_ids", [])],
                          review_id=review_id({**current, **{v: event[v] for v in VERSIONS}}, event["event_id"], "delayed"),
                          last_observed_response_at=latest_support.isoformat())
            result["processed_event_ids"].append(event["event_id"])
            continue
        if event.get("outcome") not in {"pass", "partial", "fail"}:
            result["warnings"].append(event["event_id"] + ": incomplete/unscorable is not a lapse")
            continue
        if event.get("review_kind") != "delayed":
            continue
        if result["status"] != "scheduled" or event.get("review_id") != result["review_id"]:
            result["warnings"].append(event["event_id"] + ": no matching active delayed review")
            continue
        success = _independent_pass(event)
        if success:
            exposure = event.get("last_relevant_exposure_at")
            minimum = current.get("minimum_delay_hours")
            if exposure is None or not isinstance(minimum, (int, float)) or isinstance(minimum, bool) or minimum <= 0:
                result["warnings"].append(event["event_id"] + ": delayed separation unknown; due unchanged")
                continue
            answer_date(exposure)  # validates the offset before arithmetic
            basis = max(datetime.fromisoformat(exposure.replace("Z", "+00:00")),
                        datetime.fromisoformat(result["last_observed_response_at"]))
            elapsed = (instant - basis).total_seconds() / 3600
            if (on < date.fromisoformat(result["due_date"]) or elapsed < minimum
                    or event.get("intervening_exposure") in {None, "unknown"}):
                result["warnings"].append(event["event_id"] + ": delayed eligibility not met; due unchanged")
                continue
        result.update(next_review("success" if success else "failure", result["interval_days"], on,
                                  previous_successes=result["delayed_successes"]),
                      status="scheduled" if success else "reassessment_required",
                      kind="delayed" if success else "reassessment",
                      delayed_successes=result["delayed_successes"] + 1 if success else 0,
                      supporting_event_ids=result["supporting_event_ids"] + [event["event_id"]]
                      + event.get("correction_event_ids", []),
                      review_id=review_id({**current, **{v: event[v] for v in VERSIONS}}, event["event_id"], "delayed" if success else "reassessment"),
                      last_observed_response_at=stamp)
        result["processed_event_ids"].append(event["event_id"])
    if prior.get("due_date") and result["due_date"] is None:
        # Corrections/missing history never silently dismiss an outstanding task.
        result.update(status="evidence_gate", kind="reassessment", due_date=prior["due_date"],
                      interval_days=prior.get("interval_days"), supersedes_review_id=prior.get("review_id"))
    return result


def task_fields(schedule: dict, course_title: str, objective_title: str, plan_path: str,
                project_id: str, vault_name: str = "Uni") -> dict:
    """No prompts/keys: references lead to teach's assessed-session workflow."""
    from urllib.parse import quote
    action = "Begin delayed review with teach" if schedule["kind"] == "delayed" else "Begin corrective reassessment with teach"
    ref = "obsidian://open?vault=" + quote(vault_name, safe="") + "&file=" + quote(plan_path, safe="")
    description = (f"Course: {course_title} ({schedule['course_id']})\n"
                   f"Objective: {schedule['objective_id']} r{schedule['objective_revision']}; criterion {schedule['criterion_version']}\n"
                   f"{action}: ‘Review {schedule['objective_id']} in {schedule['course_id']}.’\n"
                   f"[Open plan]({ref}) — {plan_path}\n"
                   f"Review ID: {schedule['review_id']}\nOwnership: {schedule['logical_key']}")
    if not schedule.get("due_date"):
        raise ValueError("unscheduled continuation must not create a recall task")
    return {"content": f"Review {objective_title} — {course_title}", "description": description,
            "dueString": schedule["due_date"], "projectId": project_id}


def sync_decision(sync: dict, desired: dict, marker: str, active: list[dict], completed: list[dict],
                  *, inventories_complete: bool) -> dict:
    """Return a harness operation or hold; never claim an operation occurred."""
    if not inventories_complete:
        return {"action": "hold", "reason": "incomplete_inventory"}
    owned = [t for t in active if owns_marker(t, marker)
             and not t.get("checked") and not t.get("isDeleted")]
    if len(owned) > 1:
        return {"action": "hold", "reason": "duplicate_owned_tasks", "task_ids": [t["id"] for t in owned]}
    known_id = sync.get("task_id")
    found = next((t for t in active + completed if t["id"] == known_id), None) if known_id else None
    if found and not owns_marker(found, marker):
        return {"action": "hold", "reason": "ownership_marker_removed", "task_id": known_id}
    if found and found.get("isDeleted"):
        return {"action": "hold", "reason": "user_deleted", "task_id": known_id}
    if found and found.get("checked"):
        return {"action": "hold", "reason": "completed_without_new_assessment", "task_id": known_id}
    task = owned[0] if owned else found
    if known_id and task and task["id"] != known_id:
        return {"action": "hold", "reason": "conflicting_task_identity"}
    pending = sync.get("pending_operation") or {}
    if sync.get("suppressed"):
        return {"action": "hold", "reason": "user_suppressed"}
    if task:
        if task.get("recurring") or task.get("isUncompletable"):
            return {"action": "hold", "reason": "user_changed_task_type"}
        if not known_id:
            intended = pending.get("intended_fields", {})
            if (pending.get("action") != "create" or pending.get("phase") not in {"submitted", "uncertain"}
                    or not task_matches_intent(task, intended)):
                return {"action": "hold", "reason": "unverified_marked_task", "task_id": task["id"]}
            return {"action": "adopt", "task_id": task["id"], "task": deepcopy(task)}
        baseline = sync.get("last_confirmed_fields", {})
        for field in ("content", "description", "projectId", "dueDate"):
            if field not in baseline or task.get(field) != baseline[field]:
                intended = pending.get("intended_fields", {})
                expected = intended.get("dueString") if field == "dueDate" else intended.get(field)
                if pending.get("action") == "update" and expected is not None and task.get(field) == expected:
                    continue
                return {"action": "hold", "reason": "user_edit_or_unconfirmed_baseline", "field": field}
        changes = {k: v for k, v in desired.items()
                   if (task.get("dueDate") if k == "dueString" else task.get(k)) != v}
        if not changes:
            return {"action": "confirmed_noop", "task_id": task["id"]}
        return {"action": "update", "task_id": task["id"], "arguments": {"tasks": [{"id": task["id"], **changes}]}}
    if known_id:
        return {"action": "hold", "reason": "missing_task_not_proven_deleted", "task_id": known_id}
    if pending.get("phase") in {"submitted", "uncertain"}:
        recovered = [t for t in completed if owns_marker(t, marker) and not t.get("isDeleted")
                     and task_matches_intent(t, pending.get("intended_fields", {}))]
        if len(recovered) == 1 and pending.get("action") == "create":
            return {"action": "recover_completed", "task_id": recovered[0]["id"], "task": deepcopy(recovered[0])}
        return {"action": "hold", "reason": "ambiguous_creation_requires_resolution"}
    if any(owns_marker(t, marker) and task_matches_intent(t, desired) for t in completed):
        return {"action": "hold", "reason": "unverified_marked_completed_task"}
    return {"action": "create", "arguments": {"tasks": [deepcopy(desired)]}}


def owns_marker(task: dict, marker: str) -> bool:
    return "Ownership: " + marker in task.get("description", "").splitlines()


def task_matches_intent(task: dict, intended: dict) -> bool:
    return all(field in intended and task.get("dueDate" if field == "dueString" else field) == intended[field]
               for field in ("content", "description", "projectId", "dueString"))


def confirm_task(response: dict, desired: dict, marker: str, task_id: str | None = None) -> dict:
    """Only returned task data agreeing with intent constitutes confirmation."""
    if response.get("isError"):
        raise ValueError("connector reported error")
    matches = [t for t in response.get("tasks", []) if (task_id is None or t.get("id") == task_id)
               and owns_marker(t, marker)]
    if len(matches) != 1:
        raise ValueError("no unique connector-confirmed task")
    task = matches[0]
    for field in ("content", "description", "projectId"):
        if task.get(field) != desired[field]:
            raise ValueError("connector readback mismatch: " + field)
    if task.get("dueDate") != desired["dueString"] or task.get("checked") or task.get("recurring"):
        raise ValueError("due date, completion or recurrence mismatch")
    return {"task_id": str(task["id"]), "status": "synchronized",
            "last_confirmed_fields": {k: task.get(k) for k in ("content", "description", "projectId", "dueDate")}}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    calc = sub.add_parser("calculate")
    calc.add_argument("outcome", choices=["initial", "success", "failure"])
    calc.add_argument("--previous-interval", type=int)
    calc.add_argument("--previous-successes", type=int, help="explicit delayed-success stage; omitted calculator fallback uses interval 1")
    dates = calc.add_mutually_exclusive_group(required=True)
    dates.add_argument("--occurred-at")
    dates.add_argument("--review-date", type=date.fromisoformat)
    derive = sub.add_parser("derive", help="candidate schedule from bounded JSON; writes nothing")
    derive.add_argument("input", type=Path, help="JSON: events/current/previous?")
    args = parser.parse_args()
    if args.command == "calculate":
        result = next_review(args.outcome, args.previous_interval,
                             answer_date(args.occurred_at) if args.occurred_at else args.review_date,
                             previous_successes=args.previous_successes)
    else:
        value = json.loads(args.input.read_text())
        result = derive_schedule(value["events"], value["current"], value.get("previous"))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        import unittest
        suite = unittest.defaultTestLoader.discover(str(Path(__file__).parents[1] / "tests"), pattern="test_*.py")
        sys.exit(0 if unittest.TextTestRunner(verbosity=1).run(suite).wasSuccessful() else 1)
    main()
