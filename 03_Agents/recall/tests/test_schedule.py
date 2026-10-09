"""Fictional, in-memory contracts. Never imports a connector or writes learner records."""
from copy import deepcopy
from datetime import date
import importlib.util
from pathlib import Path
import unittest

SPEC = importlib.util.spec_from_file_location("schedule", Path(__file__).parents[1] / "scripts" / "schedule.py")
s = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(s)

CURRENT = dict(course_id="TEST/Semester/CODE_Topic", objective_id="O001", objective_revision=1,
               criterion_version="O001-C1", plan_version="P001", source_version="V001", ingestion_revision=1, minimum_delay_hours=24)


def result(eid="A1", at="2026-10-03T12:00:00+02:00", **changes):
    e = {**CURRENT, "event_type": "attempt_result", "event_id": eid, "committed": True,
         "writer": "teach", "transaction_id": "T-TEST-" + eid,
         "occurred_at": at, "outcome": "pass", "independent": True, "assistance": {"level": "none", "count": 0, "content": None},
         "review_kind": "immediate", "response_evidence": "Fictional response"}
    e.update(changes)
    return e


def acquisition(eid="G1", at="2026-10-03T12:00:00+02:00", ids=None, **changes):
    e = {**CURRENT, "event_type": "acquisition_met", "event_id": eid, "committed": True,
         "writer": "teach", "transaction_id": "T-TEST-" + eid,
         "occurred_at": at, "evidence_event_ids": ids or ["A1"]}
    e.update(changes)
    return e


def delayed(events, eid="D1", at="2026-10-04T13:00:00+02:00", **changes):
    prior = s.derive_schedule(events, CURRENT)
    return result(eid, at, review_kind="delayed", review_id=prior["review_id"],
                  last_relevant_exposure_at=prior["last_observed_response_at"],
                  intervening_exposure="none", **changes)


class SchedulingTests(unittest.TestCase):
    def setUp(self):
        self.events = [result(), acquisition()]

    def test_calendar_and_rounding(self):
        self.assertEqual(s.next_review("initial", None, date(2026, 10, 3))["due_date"], "2026-10-04")
        self.assertEqual([s.next_review("success", i, date(2026, 10, 3))["interval_days"] for i in [1, 6, 15, 38]], [6, 15, 38, 95])
        self.assertEqual(s.next_review("failure", 95, date(2026, 10, 3))["interval_days"], 1)
        with self.assertRaises(ValueError):
            s.next_review("success", None, date(2026, 10, 3))

    def test_prague_boundary_and_dst(self):
        self.assertEqual(s.answer_date("2026-10-03T22:30:00Z"), date(2026, 10, 4))
        self.assertEqual(s.answer_date("2026-03-28T23:30:00Z"), date(2026, 3, 29))
        self.assertEqual(s.answer_date("2026-10-25T23:30:00Z"), date(2026, 10, 26))
        self.assertEqual(s.answer_date("2026-10-25T02:30:00+02:00"), s.answer_date("2026-10-25T02:30:00+01:00"))
        with self.assertRaises(ValueError):
            s.answer_date("2026-10-03T12:00:00")

    def test_explicit_stage_controls_first_success(self):
        self.assertEqual(s.next_review("success", 1, date(2026, 10, 3), previous_successes=0)["interval_days"], 6)
        self.assertEqual(s.next_review("success", 1, date(2026, 10, 3), previous_successes=2)["interval_days"], 3)
        with self.assertRaises(ValueError):
            s.next_review("success", 1, date(2026, 10, 3), previous_successes=True)

    def test_initial_is_actual_response_date(self):
        events = [result(at="2026-10-03T23:59:00+02:00"), acquisition(at="2026-10-04T00:01:00+02:00")]
        self.assertEqual(s.derive_schedule(events, CURRENT)["due_date"], "2026-10-04")

    def test_uncommitted_legacy_assisted_and_unsupported_never_acquire(self):
        for changes in [{"committed": False}, {"independent": False}, {"assistance": {"level": "cue"}}, {"outcome": "partial"}, {"criterion_version": "old"}]:
            with self.subTest(changes=changes):
                self.assertIsNone(s.derive_schedule([result(**changes), acquisition()], CURRENT)["due_date"])
        self.assertIsNone(s.derive_schedule([result()], CURRENT)["due_date"])

    def test_no_response_or_repeated_acquisition_preserves_due(self):
        schedule = s.derive_schedule(self.events, CURRENT)
        self.assertEqual(s.derive_schedule(self.events, CURRENT, schedule), schedule)
        later = self.events + [result("A2", "2026-10-09T12:00:00+02:00"), acquisition("G2", "2026-10-09T12:00:00+02:00", ["A2"])]
        self.assertEqual(s.derive_schedule(later, CURRENT)["due_date"], "2026-10-04")

    def test_overdue_success_anchors_actual_answer(self):
        events = self.events + [delayed(self.events, at="2026-10-10T12:00:00+02:00")]
        schedule = s.derive_schedule(events, CURRENT)
        self.assertEqual((schedule["interval_days"], schedule["due_date"]), (6, "2026-10-16"))
        events.append(delayed(events, "D2", "2026-10-16T12:00:00+02:00"))
        self.assertEqual(s.derive_schedule(events, CURRENT)["due_date"], "2026-10-31")

    def test_midnight_is_not_delayed_retention(self):
        events = [result(at="2026-10-03T23:59:00+02:00"), acquisition(at="2026-10-03T23:59:00+02:00")]
        events.append(delayed(events, at="2026-10-04T00:01:00+02:00"))
        self.assertEqual(s.derive_schedule(events, CURRENT)["interval_days"], 1)

    def test_missing_delay_or_exposure_does_not_extend(self):
        events = self.events + [delayed(self.events)]
        for current in [dict(CURRENT, minimum_delay_hours=None), dict(CURRENT, minimum_delay_hours=0)]:
            self.assertEqual(s.derive_schedule(events, current)["due_date"], "2026-10-04")
        events[-1]["intervening_exposure"] = "unknown"
        self.assertEqual(s.derive_schedule(events, CURRENT)["due_date"], "2026-10-04")

    def test_wrong_review_or_early_success_not_credited(self):
        for kwargs in [{"review_id": "OTHER"}, {"at": "2026-10-03T18:00:00+02:00"}]:
            if "review_id" in kwargs:
                d = delayed(self.events)
                d.update(kwargs)
            else:
                d = delayed(self.events, **kwargs)
            self.assertEqual(s.derive_schedule(self.events + [d], CURRENT)["due_date"], "2026-10-04")

    def test_fail_partial_or_assisted_reset_and_require_reacquisition(self):
        for changes in [{"outcome": "fail"}, {"outcome": "partial"}, {"assistance": {"level": "cue"}, "independent": False}]:
            events = self.events + [delayed(self.events, at="2026-10-08T12:00:00+02:00", **changes)]
            schedule = s.derive_schedule(events, CURRENT)
            self.assertEqual((schedule["status"], schedule["due_date"]), ("reassessment_required", "2026-10-09"))
            events += [result("A2", "2026-10-09T12:00:00+02:00"), acquisition("G2", "2026-10-09T12:00:00+02:00", ["A2"])]
            self.assertEqual((s.derive_schedule(events, CURRENT)["status"], s.derive_schedule(events, CURRENT)["due_date"]), ("scheduled", "2026-10-10"))

    def test_incomplete_is_not_failure(self):
        self.assertEqual(s.derive_schedule(self.events + [delayed(self.events, outcome="incomplete")], CURRENT)["due_date"], "2026-10-04")

    def test_version_gate_keeps_historical_date(self):
        prior = s.derive_schedule(self.events, CURRENT)
        new = dict(CURRENT, source_version="V002")
        gated = s.derive_schedule(self.events, new, prior)
        self.assertEqual((gated["status"], gated["due_date"]), ("version_gate", "2026-10-04"))
        self.assertEqual(prior["source_version"], "V001")

    def test_correction_invalidates_unsupported_acquisition(self):
        prior = s.derive_schedule(self.events, CURRENT)
        corrected = {"event_id": "C1", "event_type": "correction", "committed": True,
                     "writer": "teach", "transaction_id": "T-TEST-C1",
                     "supersedes_event_id": "A1", "corrected_fields": {"outcome": "partial"}}
        gated = s.derive_schedule(self.events + [corrected], CURRENT, prior)
        self.assertEqual(gated["status"], "evidence_gate")
        self.assertEqual(gated["due_date"], "2026-10-04")

    def test_explicit_plan_approved_path_change_preserves_evidence_and_review_id(self):
        prior = s.derive_schedule(self.events, CURRENT)
        new = dict(CURRENT, source_version="V002", plan_version="P002", ingestion_revision=2,
                   compatible_versions=[{**{k: CURRENT[k] for k in s.VERSIONS}, "requires_reassessment": False,
                                         "change_class": "path_only", "reason": "Same claims/rubric; verified anchor move"}])
        schedule = s.derive_schedule(self.events, new, prior)
        self.assertEqual((schedule["status"], schedule["review_id"]), ("scheduled", prior["review_id"]))
        event = delayed(self.events)
        event.update({k: new[k] for k in s.VERSIONS})
        self.assertEqual(s.derive_schedule(self.events + [event], new, prior)["interval_days"], 6)

    def test_invalid_correction_identity_or_forward_target_rejected(self):
        correction = {"event_id": "C1", "event_type": "correction", "committed": True,
                      "writer": "teach", "transaction_id": "T-TEST-C1",
                      "supersedes_event_id": "A1", "corrected_fields": {"outcome": "partial"}}
        with self.assertRaises(ValueError):
            s.effective_events([correction, result()])
        correction["corrected_fields"] = {"criterion_version": "new"}
        with self.assertRaises(ValueError):
            s.effective_events([result(), correction])

    def test_chained_correction_preserves_actual_time_and_ids(self):
        first = {"event_id": "C1", "event_type": "correction", "committed": True,
                 "writer": "teach", "transaction_id": "T-TEST-C1",
                 "supersedes_event_id": "A1", "corrected_fields": {"outcome": "partial"}}
        second = {"event_id": "C2", "event_type": "correction", "committed": True,
                  "writer": "teach", "transaction_id": "T-TEST-C2",
                  "supersedes_event_id": "C1", "corrected_fields": {"outcome": "pass"}}
        effective = s.effective_events([result(), first, second])[0]
        self.assertEqual(effective["occurred_at"], result()["occurred_at"])
        self.assertEqual(effective["correction_event_ids"], ["C1", "C2"])

    def test_retry_ids_are_idempotent_conflicts_rejected(self):
        self.assertEqual(s.derive_schedule(self.events + deepcopy(self.events), CURRENT), s.derive_schedule(self.events, CURRENT))
        with self.assertRaises(ValueError):
            s.derive_schedule(self.events + [result(outcome="fail")], CURRENT)

    def test_named_reassessment_gate_consumes_actual_prepared_new_evidence(self):
        current = dict(CURRENT, reassessment_requirement={"requirement_id": "RG1"})
        support = result(review_kind="reassessment")
        declared = acquisition()
        self.assertEqual(s.derive_schedule([support, declared], current)["status"], "version_gate")
        gate = {**declared, "event_type": "reassessment_met", "requirement_id": "RG1"}
        schedule = s.derive_schedule([support, gate], current)
        self.assertEqual((schedule["status"], schedule["due_date"]), ("scheduled", "2026-10-04"))
        gate["requirement_id"] = "OTHER"
        self.assertEqual(s.derive_schedule([support, gate], current)["status"], "version_gate")

    def test_invalid_ingest_type_and_non_teacher_evidence_rejected(self):
        for revision in ["I001", True, 0]:
            with self.assertRaises(ValueError):
                s.derive_schedule(self.events, dict(CURRENT, ingestion_revision=revision))
        with self.assertRaises(ValueError):
            s.derive_schedule([result(writer="recall")], CURRENT)


class ProjectTests(unittest.TestCase):
    def test_unicode_code_and_underscores(self):
        projects = [{"id": "1", "name": "JEB109_Économie_I"}]
        self.assertEqual(s.match_projects(projects, "Économie I", "JEB109")["status"], "unique")
        self.assertEqual(s.match_projects(projects, "Economie I", "JEB109")["status"], "missing")

    def test_no_guess_from_partial_or_other_course(self):
        self.assertEqual(s.match_projects([{"id": "II", "name": "Econometrics II"}], "Econometrics I", "JEB109")["status"], "missing")
        projects = [{"id": "1", "name": "Econometrics I"}, {"id": "2", "name": "JEB109 Econometrics I"}]
        self.assertEqual(s.match_projects(projects, "Econometrics I", "JEB109")["status"], "ambiguous")


class SynchronizationTests(unittest.TestCase):
    def setUp(self):
        self.schedule = s.derive_schedule([result(), acquisition()], CURRENT)
        self.marker = self.schedule["logical_key"]
        self.desired = s.task_fields(self.schedule, "Test Course", "Test Topic", "03_Agents/TEST/learning_plan.md", "P1")
        self.task = {"id": "T1", "content": self.desired["content"], "description": self.desired["description"],
                     "projectId": "P1", "dueDate": self.desired["dueString"], "checked": False, "recurring": False}
        self.sync = s.confirm_task({"tasks": [self.task]}, self.desired, self.marker)

    def decide(self, sync=None, active=None, completed=None, complete=True, desired=None):
        return s.sync_decision(self.sync if sync is None else sync, desired or self.desired, self.marker,
                               [self.task] if active is None else active, completed or [], inventories_complete=complete)

    def test_fresh_create_confirm_then_rerun_is_noop(self):
        self.assertEqual(self.decide(sync={}, active=[])["action"], "create")
        self.assertEqual(self.decide()["action"], "confirmed_noop")
        self.assertNotIn("Fictional response", self.desired["description"])

    def test_new_evidence_updates_only_owned_changed_fields(self):
        desired = {**self.desired, "dueString": "2026-10-10"}
        decision = self.decide(desired=desired)
        self.assertEqual(decision["arguments"], {"tasks": [{"id": "T1", "dueString": "2026-10-10"}]})

    def test_ambiguous_create_cannot_blind_retry(self):
        uncertain = {"pending_operation": {"action": "create", "phase": "uncertain", "intended_fields": self.desired}}
        self.assertEqual(self.decide(sync=uncertain, active=[])["reason"], "ambiguous_creation_requires_resolution")
        self.assertEqual(self.decide(sync=uncertain)["action"], "adopt")

    def test_unknown_marker_and_wrong_intent_cannot_establish_ownership(self):
        self.assertEqual(self.decide(sync={})["reason"], "unverified_marked_task")
        pending = {"pending_operation": {"action": "create", "phase": "uncertain", "intended_fields": {**self.desired, "dueString": "2026-12-31"}}}
        self.assertEqual(self.decide(sync=pending)["reason"], "unverified_marked_task")

    def test_created_then_completed_during_uncertain_sync_recovers_no_duplicate(self):
        pending = {"pending_operation": {"action": "create", "phase": "uncertain", "intended_fields": self.desired}}
        completed = {**self.task, "checked": True}
        self.assertEqual(self.decide(sync=pending, active=[], completed=[completed])["action"], "recover_completed")

    def test_matching_completed_marker_without_journal_is_not_recreated(self):
        self.assertEqual(self.decide(sync={}, active=[], completed=[{**self.task, "checked": True}])["reason"], "unverified_marked_completed_task")

    def test_incomplete_pagination_and_duplicates_hold(self):
        self.assertEqual(self.decide(complete=False)["reason"], "incomplete_inventory")
        self.assertEqual(self.decide(active=[self.task, {**self.task, "id": "T2"}])["reason"], "duplicate_owned_tasks")

    def test_user_edits_and_removed_marker_preserved(self):
        for field, value in [("content", "My title"), ("dueDate", "2026-12-31"), ("projectId", "OTHER")]:
            self.assertEqual(self.decide(active=[{**self.task, field: value}])["reason"], "user_edit_or_unconfirmed_baseline")
        self.assertEqual(self.decide(active=[{**self.task, "description": "User removed marker"}])["reason"], "ownership_marker_removed")

    def test_completed_task_is_not_learning_or_duplicate_create(self):
        self.assertEqual(self.decide(active=[], completed=[{**self.task, "checked": True}])["reason"], "completed_without_new_assessment")

    def test_deleted_or_missing_known_task_no_recreate(self):
        self.assertEqual(self.decide(active=[{**self.task, "isDeleted": True}])["reason"], "user_deleted")
        self.assertEqual(self.decide(active=[])["reason"], "missing_task_not_proven_deleted")

    def test_partial_failure_wrong_dates_no_confirmation(self):
        for response in [{"failureCount": 1, "tasks": []}, {"tasks": [{**self.task, "dueDate": "2026-10-04T09:00:00"}]}, {"tasks": [{**self.task, "projectId": "OTHER"}]}]:
            with self.assertRaises(ValueError):
                s.confirm_task(response, self.desired, self.marker)

    def test_interrupted_update_readback_is_recoverable(self):
        updated = {**self.task, "dueDate": "2026-10-10"}
        sync = {**self.sync, "pending_operation": {"action": "update", "phase": "uncertain", "intended_fields": {"dueString": "2026-10-10"}}}
        desired = {**self.desired, "dueString": "2026-10-10"}
        self.assertEqual(self.decide(sync=sync, active=[updated], desired=desired)["action"], "confirmed_noop")

    def test_marker_must_be_exact_line(self):
        fake = {**self.task, "description": "Ownership: " + self.marker + "-other"}
        self.assertFalse(s.owns_marker(fake, self.marker))


if __name__ == "__main__":
    unittest.main()
