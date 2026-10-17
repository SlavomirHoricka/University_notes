# Teaching records contract

## Contents

| Section | GitHub | Obsidian |
|---|---|---|
| **1. Purpose and authority** | [Jump](#1-purpose-and-authority) | [Jump](#1.%20Purpose%20and%20authority) |
| **2. Ownership and versions** | [Jump](#2-ownership-and-versions) | [Jump](#2.%20Ownership%20and%20versions) |
| Exclusive records and versions | [Jump](#exclusive-records-and-versions) | [Jump](#Exclusive%20records%20and%20versions) |
| **3. Record format** | [Jump](#3-record-format) | [Jump](#3.%20Record%20format) |
| **4. Assessment evidence** | [Jump](#4-assessment-evidence) | [Jump](#4.%20Assessment%20evidence) |
| Evidence, help, and assessment identity | [Jump](#evidence-help-and-assessment-identity) | [Jump](#Evidence%2C%20help%2C%20and%20assessment%20identity) |
| **5. Generated-item contracts** | [Jump](#5-generated-item-contracts) | [Jump](#5.%20Generated-item%20contracts) |
| Generated items and alternative methods | [Jump](#generated-items-and-alternative-methods) | [Jump](#Generated%20items%20and%20alternative%20methods) |
| **6. Derived state** | [Jump](#6-derived-state) | [Jump](#6.%20Derived%20state) |
| Current state and safe writing | [Jump](#current-state-and-safe-writing) | [Jump](#Current%20state%20and%20safe%20writing) |
| **7. Transactions and recovery** | [Jump](#7-transactions-and-recovery) | [Jump](#7.%20Transactions%20and%20recovery) |
| **8. Legacy preservation and handoffs** | [Jump](#8-legacy-preservation-and-handoffs) | [Jump](#8.%20Legacy%20preservation%20and%20handoffs) |
| Legacy preservation and handoffs | [Jump](#legacy-preservation-and-handoffs) | [Jump](#Legacy%20preservation%20and%20handoffs) |

## 1. Purpose and authority

Version 3, 2026-10-03. This is the active teach-owned event/record contract. Historical v2 guidance is archived in `03_Agents/history/2026-10-03-audit/original_agents/teach/references/RECORDS.md`; it does not grant teaching or scheduling agents curriculum/freshness ownership.

## 2. Ownership and versions

### Exclusive records and versions

Ingest owns course `ingestion_state.json` and runtime ingestion coverage; plan owns `learning_plan.md`, `source_manifest.md`, `lessons/` and immutable `curriculum_history/`; teach alone owns `learning_log.md`; recall alone owns `recall_state.json` and positively identified Todoist tasks. Teach reads freshness metadata; it never hashes/reconciles notes or watches raw sources. All files are in `03_Agents/<year>/<semester>/<course>/` except the explicit runtime index/pass paths.

`course_id` is the exact full course path, code separately null if unknown. Objective IDs are course-local, never recycled. Every assessed event captures objective revision, criterion version, plan/source version and ingestion revision. Preserve historical definitions via the plan's immutable snapshots, and never score an old answer against a new rubric.

A compatible plan migration can preserve old evidence applicability; the planning record supplies its reason/mapping. Uncertain or changed scope requires prepared reassessment before current credit.

## 3. Record format

New logs start with the exact marker `<!-- uni-teach-log:3 -->` followed by schema-3 owner metadata as their first fenced JSON object; each event is a separate fenced JSON object. Preserve every legacy log byte as an exact prefix forever, including after schema-3 appends; do not prepend this new-log marker to legacy content.

Locate schema-3 metadata after its explicit migration boundary in legacy logs, not by assuming the first historical JSON object is current metadata. Legacy derived state updates must append rather than rewrite their preserved prefix. See `templates/learning_log.md`. JSON avoids ambiguous YAML coercion and permits stdlib parsing.

On retry, an existing event ID with identical content is skipped (never append a duplicate fenced object); same ID/different content is a conflict. Event timestamps are actual ISO-8601 offsets plus `timezone: Europe/Prague`, including winter/summer transitions; UTC-based IDs may still be used. `null` is unknown, `[]` known empty. A missing response is incomplete, not wrong.

A learner-reported blank answer can be assessed under the rubric; it is not missing telemetry.

## 4. Assessment evidence

### Evidence, help, and assessment identity

#### Attempt identity and original response

An attempt starts before the prompt is displayed. Its ID, item ID/version/text, conditions and objective tuple persist; after a response, append the original result before subsequent feedback. Record exact reasoning or a faithful compact quotation/summary sufficient to interpret essential rubric components. An optional numeric score needs an explicit prepared denominator/scale; do not create one.

#### Assistance, conditions and exposure

Record assistance level, actual hints, note access, tools and solution exposure. Independence requires positively known permitted conditions. Unknown access/help never becomes `independent: true`. Notes closed by learner report is not proctoring. Preserve initial wrong/partial response even when correction succeeds. Instruction/feedback/restudy is exposure, not performance. Known independent-study reports include actual reported times or unknown/null, never file modification time.

`intervening_exposure` is `none`, `reported`, or `unknown`, with the actual report in `intervening_exposure_details`; unknown/absent exposure information cannot qualify for a clean delayed interval extension.

#### Acquisition and delayed observations

`acquisition_met` is a declaration backed by actual qualifying result IDs and the prepared rule, normally two distinct current-criterion independent passes.

Conceptual, procedural and interpretive components can differ; record them rather than a single vague “knows topic.” A delayed `attempt_result` additionally records actual elapsed time since last relevant exposure and known intervening exposure, and meets the lesson's default 24h minimum plus fresh/independent conditions. A date change at midnight alone does not meet that gate.

A delayed pass is evidence at that interval/context; retention is never inferred from task completion or confidence.

#### Correction and reassessment

An observed partial/failure gets the prepared correction route and new item. A hint-assisted correct answer is assisted performance, not independent retrieval. Unknown exposure qualifies any retention interpretation. `reassessment_met` may satisfy only the plan's named requirement with prepared current-version evidence; this does not edit the gate or erase old evidence.

Correction of mistaken scoring appends `correction` with `supersedes_event_id`, preserved original and explicit reason and `corrected_fields` (the faithful teach-assessed replacement fields). A correction cannot invent a response or acquisition; recall replays the explicitly corrected effective outcome and cites original/correction IDs without grading. Recall consumes the corrected effective evidence by reference, never regrades the response.

## 5. Generated-item contracts

### Generated items and alternative methods

#### Pre-prompt contract and field requirements

Follow `03_Agents/references/LESSON_CONTENT.md`. New teach-generated items use existing schema-3 `attempt_started`/`attempt_result` events, not curriculum files.

| Field group | Existing requirement |
|---|---|
| Snapshot contents | Before prompt display, commit `item_origin: teach_generated` and an `item_contract` containing `prompt`, complete `solution`, `rubric`, nonempty `component_ids`, `item_role`, `task_relation`, `source_basis` and `verification`. |
| Field types | Snapshot prompt, solution, role, task relation and verification are nonempty strings; component IDs and source basis are nonempty string lists. |
| Component mapping and rubric | Map components/role to the unchanged lesson standard before the answer; `rubric.components` maps each component ID to a nonempty decision rule; `rubric.outcome_rules` supplies pass/partial/fail/unscorable rules. |

Keep stable item ID/version and exact `item_text` matching the prompt. Verification records the actual solution check and any assessor findings. The start also carries matching `task_relation`. Store keys privately in the log, never in the learner relay prompt. Generated items cannot replace exact named checks without explicit plan permission.

#### Result matching and alternative methods

An `attempt_result` for that item must follow its start, match attempt/item/version and definition tuple, and use its frozen contract. Do not change an item contract under the same item ID/version or criteria after seeing the answer. Reference the start via `attempt_id`; do not duplicate the key in feedback before the answer.

Optional `assessment_basis` records why an unlisted solution meets the existing essential criteria and any assessor findings. A changed standard requires plan reconciliation; ambiguous assessments stay unscorable. No old event requires these additive fields, and no historical result is regraded. Recall consumes existing committed outcome events and rules without inspecting/rewriting keys.

## 6. Derived state

### Current state and safe writing

The current-state/evidence index is a small derived view; committed events win. State contains session route, learner-reported budget, objective/block, last committed event, unanswered attempt, stopping point, next step and time-deferred IDs/issues. A new session reconsiders time deferrals alongside requested scope, blocking prerequisites and recall reason; it does not silently delete or always prioritize them.

No due dates, scheduler proposal state or Todoist completion belong in new log fields.

## 7. Transactions and recovery

Use `03_Agents/scripts/records.py commit COURSE_DIR teach DRAFT_JSON`, after constructing exact log text with append-only events and updated summary. Draft expected hashes refer to the old log bytes or null if absent. The utility lock is `.learning-write.lock` shared across owners, with owner/token/host/PID; `.transactions/<id>/journal.json` tracks staged replacements.

Read utility status and use `records.py verify-record COURSE_DIR teach learning_log.md` to match current log bytes to an actual committed teach-owned journal, including summary-only changes and exact-prefix legacy appends. Status, a claimed ID or the latest event transaction alone is insufficient. `committed: true` in staged JSON is insufficient before the owning transaction commits.

Cooperating writers use the same utility; a non-cooperating editor can still cause a detected conflict. Keep its content and reconcile, never overwrite it.

Do not steal a lock by age. Interrupted transaction requires inspection then owner-only `recover COURSE_DIR teach TRANSACTION_ID`. Report any preserved pending transaction path. Unanswered attempts may resume if unexposed, or be explicitly abandoned for an indexed fresh variant. A persisted response can be recovered; an unsaved response cannot be inferred. Unknown interruption/end/duration stays unknown.

Rebuild a stale summary from committed events instead of fabricating a closing event.

## 8. Legacy preservation and handoffs

### Legacy preservation and handoffs

Do not rewrite, normalize or delete legacy attempts/status/scheduler events. Preserve original complete log content and append a clearly labelled schema-3 section/boundary, new common metadata and new events. Old scheduler entries are historical only; recall's active state is separate.

Old unstructured prose is not silently promoted to schema-3 committed results; if interpretation/conditions/versions are absent, preserve the uncertainty and perform a prepared new diagnostic when needed.

A plan issue includes course/versions, exact lesson/item/criterion gap, quoted actual response if relevant, related event IDs and requested repair. A note issue includes precise note/heading and encountered contradiction/provenance change; ingest verifies sources. A recall handoff includes log path/committed event IDs, review ID, objective tuple, observed time, assistance/exposure qualification and unresolved gates. Handoff does not create a background scheduler.

Todoist completion without a committed response does not create a teach outcome; the next real review still begins with a fresh prepared item.
