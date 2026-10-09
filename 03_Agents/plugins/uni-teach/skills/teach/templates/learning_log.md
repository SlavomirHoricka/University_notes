<!-- uni-teach-log:3 -->
# Learning log — template

Teach is the sole writer. This template is not learner history. Initialize only for an authorized real session; never copy example events into real course records. Evidence lives in committed events, not in plan status or Todoist task completion.

```json
{
  "schema_version": 3,
  "owner": "teach",
  "course_id": "<course_id>",
  "timezone": "Europe/Prague",
  "record_revision": 1,
  "transaction_id": "<this log write transaction>"
}
```

## Current state

One compact derived summary; events are authoritative. Values are unknown/null until observed.

```json
{
  "updated_at": null,
  "session_id": null,
  "session_status": "not_started",
  "requested_scope": null,
  "time_budget_minutes": null,
  "plan_version": null,
  "source_version": null,
  "ingestion_revision": null,
  "current_objective_id": null,
  "current_block": null,
  "last_committed_event_id": null,
  "pending_attempt_id": null,
  "last_completed_step": null,
  "stopped_at": null,
  "next_intended_step": null,
  "time_deferred_objective_ids": [],
  "unresolved_issue_event_ids": []
}
```

## Evidence index — derived only

No due dates or scheduler fields. Add only touched objectives with actual event IDs and exact definition versions. Acquisition and delayed results are separate; a delayed pass reports actual interval/conditions rather than a universal mastery label. Plan-defined reassessment gates point to their qualifying new evidence or remain unsatisfied.

| Objective/revision/criterion | Acquisition evidence | Concept/procedure/interpretation | Delayed observation and actual interval | Gate evidence | Definition version |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

## Events — append only

Each event is its own fenced JSON object. Required common fields: `event_id`, `event_type`, `committed`, `transaction_id`, `writer` (`teach`), `occurred_at` (actual ISO 8601 offset or null only if unknown), `recorded_at`, `timezone`, `session_id` (or null), and definition tuple (`objective_id`, `objective_revision`, `criterion_version`, `plan_version`, `source_version`, `ingestion_revision`; nullable only for a session-wide event). IDs remain stable on retry. A schema-3 event is usable only after its utility journal is committed; staged intent is not evidence.

Attempt-result fields:

```json
{
  "event_id": "<unique stable id>",
  "event_type": "attempt_result",
  "committed": true,
  "transaction_id": "<committed utility transaction>",
  "writer": "teach",
  "occurred_at": "<observed response time with offset>",
  "recorded_at": "<actual persistence time with offset>",
  "timezone": "Europe/Prague",
  "session_id": "<session id>",
  "objective_id": "<stable objective id>",
  "objective_revision": 1,
  "criterion_version": "<current criterion>",
  "plan_version": "<current plan>",
  "source_version": "<current notes version>",
  "ingestion_revision": null,
  "attempt_id": "<already started attempt>",
  "item_id": "<prepared item id>",
  "item_version": 1,
  "item_text": "<exact presented prompt>",
  "task_relation": "parallel_variant",
  "review_kind": "immediate",
  "review_id": null,
  "response_evidence": "<actual answer/reasoning, never invented>",
  "component_outcomes": {},
  "outcome": "partial",
  "independent": false,
  "assistance": {"level": "unknown", "count": null, "content": null},
  "note_access": "unknown",
  "tools": [],
  "solution_exposure": "unknown",
  "previous_attempt_id": null,
  "last_relevant_exposure_at": null,
  "elapsed_hours_since_exposure": null,
  "intervening_exposure": "unknown",
  "intervening_exposure_details": null,
  "observed_errors": [],
  "feedback_event_id": null
}
```

This is a schema example, not an event to copy. Allowed outcome: `pass`, `partial`, `fail`, `incomplete`, `unscorable`. Allowed review_kind: `diagnostic`, `immediate`, `delayed`, `reassessment`. Allowed assistance level: `none`, `cue`, `strategy_hint`, `partial_worked`, `full_solution`, `unknown`. Notes: `closed`, `open`, `unknown`; tools include actual allowed/used tool identifiers and unknown condition if needed. Solution exposure: `none`, `prior_same_session`, `during_attempt`, `unknown`. Intervening exposure uses `none`, `reported`, or `unknown`, with actual details in `intervening_exposure_details`; clean delayed extension requires known conditions and a reliable relevant-exposure timestamp. Independence requires known rubric-allowed conditions; it is not inferred from prose.

Production evidence copies the actual integer ingest revision; null is an unready placeholder. A `correction` uses `corrected_fields` containing teach-assessed field replacements and `supersedes_event_id`. Corrections cannot manufacture learner answers or acquisition.

An `acquisition_met` event references `evidence_event_ids`, the exact `acquisition_rule` and current objective/criterion tuple. Normally these are two distinct independent passing current-criterion attempts with required item roles. `reassessment_met` references its plan `requirement_id`, current-version qualifying evidence IDs and rule. Neither event is created from confidence, restudy, a reminder or a passed same-item retry.

Other teach-owned types: `session_started`, `session_route`, `attempt_started`, `instruction_or_feedback`, `exposure_reported`, `attempt_abandoned`, `session_paused`, `session_closed`, `plan_issue`, `note_issue`, `correction`. A correction cites `supersedes_event_id`, reason and corrected fields while preserving original. A `session_route`/pause preserves unresolved time deferrals and reason. Scheduler events are prohibited here; recall owns `recall_state.json`.

## Legacy history

For existing logs, retain the entire original content/events and append an explicit schema-3 boundary with new metadata/events. Link corresponding archived plan/criterion definitions. Do not translate historical attempts, invent timestamps, mark old events committed, reinterpret original statuses or remove scheduler history from old records. Legacy scheduler fields remain read-only historical data, not active scheduling state. Current summaries cite only interpretable evidence with versions and a compatibility mapping.
