# Learning log — TEMPLATE

The teach skill initializes this file for a selected course. This is a template, not learner history. The log is the only record of observed performance; plan and notes contain no current learner status.

- schema_version: 2
- course_id: null
- timezone: Europe/Prague
- record_revision: 0
- transaction_id: null

## Current state

- updated_at: null
- session_id: null
- session_status: not_started
- requested_scope: null
- time_budget_minutes: null
- plan_version: null
- source_version: null
- current_objective_id: null
- last_committed_event_id: null
- pending_attempt_id: null
- stopped_at: null
- next_intended_step: null
- time_deferred_objective_ids: []
- unresolved_misconception_event_ids: []
- plan_issue_event_ids: []
- note_issue_event_ids: []

## Objective status — derived from committed events

Maintain a compact row for objectives touched by learning. Events, not this summary, are authoritative. Learning states are unassessed, practicing, or independent; retention states are untested, pending, observed, or gap.

| Objective ID | Criterion version | Learning | Retention | Evidence event IDs | Last observed review | Active review proposal |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — |

## Chronological events — append only

Append only observed session events and scheduler proposals with stable IDs and actual timestamps. An attempt without an answer is incomplete, not wrong. A schedule proposal is not a completed review.

~~~yaml
event_id: <unique ID>
recorded_at: <actual ISO 8601 timestamp with local offset>
occurred_at: null
timezone: Europe/Prague
writer: <agent identifier>
role: tutor
type: attempt_result
session_id: <existing session ID>
plan_version: <plan version>
source_version: <note version>
objective_ids: []
criterion_versions: []
attempt_id: <existing attempt ID>
phase: <diagnostic|initial_learning|immediate_practice|delayed_retrieval|reassessment>
task_text_or_digest: null
response_evidence: null
outcome: <met|partial|not_met|incomplete|unscorable>
assistance: unknown
note_access: unknown
feedback: null
previous_attempt_id: null
intervening_exposure: unknown
~~~

Other event types include session_started, session_plan, attempt_started, instruction_or_feedback, session_paused, session_closed, plan_issue, note_issue, correction, schedule_proposal, schedule_update, and commit. A scheduler proposal needs objective ID, supporting result event IDs, due date, interval days, rationale, proposal ID/state, and any superseded proposal ID. Do not mutate historical events to correct them; append a correction referring to the original ID.
