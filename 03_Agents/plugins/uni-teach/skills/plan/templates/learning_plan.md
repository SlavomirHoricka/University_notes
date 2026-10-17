# Learning plan — template

Plan-owned template. Copy only for an authorized scope with finished notes; replace every placeholder. This file contains curriculum definitions, never learner status or due dates. Metadata is the first fenced JSON block for deterministic parsing.

## Record metadata

```json
{
  "schema_version": 3,
  "owner": "plan",
  "course_id": "<year>/<semester>/<actual_course_folder>",
  "course_code": null,
  "course_name": "<verified full course name>",
  "record_revision": 1,
  "transaction_id": "<stable plan transaction id>",
  "plan_version": "P001",
  "source_version": "V001",
  "ingestion_revision": null,
  "updated_at": "<actual ISO timestamp with offset>",
  "timezone": "Europe/Prague",
  "plan_status": "ready",
  "requested_scope": "<bounded requested content>",
  "requested_outcome": "<learner goal>",
  "deadline_or_retention_horizon": null,
  "source_manifest": "source_manifest.md",
  "objectives": []
}
```

## Contents

| Section | GitHub | Obsidian |
|---|---|---|
| **Record metadata** | [Jump](#record-metadata) | [Jump](#Record%20metadata) |
| **Metadata rules** | [Jump](#metadata-rules) | [Jump](#Metadata%20rules) |
| Readiness statuses and objective index | [Jump](#readiness-statuses-and-objective-index) | [Jump](#Readiness%20statuses%20and%20objective%20index) |
| Revision and compatibility rules | [Jump](#revision-and-compatibility-rules) | [Jump](#Revision%20and%20compatibility%20rules) |
| **Scope and coverage** | [Jump](#scope-and-coverage) | [Jump](#Scope%20and%20coverage) |
| **Teaching sequence** | [Jump](#teaching-sequence) | [Jump](#Teaching%20sequence) |
| **Execution and assessment contract** | [Jump](#execution-and-assessment-contract) | [Jump](#Execution%20and%20assessment%20contract) |
| **Revisions and evidence compatibility** | [Jump](#revisions-and-evidence-compatibility) | [Jump](#Revisions%20and%20evidence%20compatibility) |
| **Validation and readiness** | [Jump](#validation-and-readiness) | [Jump](#Validation%20and%20readiness) |


## Metadata rules

### Readiness statuses and objective index

Allowed status: `ready`, `partial`, `blocked`. For partial readiness the `objectives` index must explicitly declare each lesson's status; runtime agents execute only ready blocks with matching metadata. An objective index row contains

- `objective_id`
- `objective_revision`
- `criterion_version`
- `lesson_path`
- `status`
- `title`
- `knowledge_components`
- `prerequisite_ids`
- `review_topic`
- `review_instruction`
- `compatible_versions` (normally empty; exact approved old tuples only)
- and `reassessment_requirement` (null or stable `requirement_id`, reason, old/new versions, prepared item IDs and qualifying evidence conditions).

Include exact heading links in the table below. Never substitute a due date for the review instruction.

### Revision and compatibility rules

Production `ingestion_revision` must be the actual integer from ingest state, copied without type conversion; null is an unready placeholder. Each approved `compatible_versions` row contains `objective_revision`, `criterion_version`, `plan_version`, `source_version`, integer `ingestion_revision`, `reason`, `change_class`, and `requires_reassessment: false`. Approve only exact old tuples whose capability/criteria/conditions are unchanged after finished-note inspection; never wildcards or implicit version ranges.

Changed substantive content/criteria are gated, not approved by this list.

## Scope and coverage

Requested scope and its authoritative finished-note mapping:

| Requested capability/material | Finished note + exact heading/block | Objectives | Coverage | Exclusion/gap/dependency |
|---|---|---|---|---|
| <topic> | <vault-relative existing target> | <IDs> | covered/partial/absent | <specific reason> |

Link the selected ingestion completion record and `source_manifest.md`. List uncaptured notes/candidates and unresolved prerequisites. State whether syllabus/exam coverage is supported and by which finished input. Silence means unknown, never complete coverage.

## Teaching sequence

| Order | Objective and exact lesson anchor | Necessary prerequisite + reason | Route entry/diagnostic | Status |
|---|---|---|---|---|
| 1 | <lessons/ID.md#Outcome and conditions> | <capability/reason> | <prepared item/step> | ready/blocked |

Explain the order in a short paragraph. Identify independent branches and when an already-satisfied prerequisite permits skipping prepared support. Link only populated blocks.

## Execution and assessment contract

Each indexed lesson follows `03_Agents/plan/templates/objective_lesson.md` and `03_Agents/references/LESSON_CONTENT.md`. Embed complete relevant existing explanations/derivations/examples, supply verified additions, and design the main questions/solutions/criteria. Ordinary delivery retrieves the index, one self-contained lesson and its assets/prerequisite lessons, without original notes. No ready row may delegate its main assessment preparation to teach. Bounded checked generated items and valid alternative methods remain permitted under unchanged standards.

A topic/week is prepared completely; a whole-course route may be partial with explicit unprepared units. Preserve existing curricula until substantive revision and reconcile ingestion changes through the normal freshness gates.

## Revisions and evidence compatibility

| Plan/source versions | Objective old/new revision and criterion | Note-change class/claim | Compatibility + reassessment requirement | Preserved definition |
|---|---|---|---|---|
| P001/V001 | <initial> | initial scoped baseline | no historical learning inferred | <none or exact prior snapshot> |

Define compatibility without regrading learner responses. Record split/merge predecessor IDs and retired IDs; never recycle. Link exact immutable `curriculum_history/<old_plan_version>/` definitions before replacing them. Distinguish inherited unsupported legacy status from actual committed evidence. New topics start with no claimed learner result.

## Validation and readiness

Record checked links/anchors, dependency graph, mandatory blocks, keys/arithmetic/assumptions, task-to-rubric mappings, preserved versions, matching transaction tuple and utility status. Record specific blockers and handoff recipients. Template existence alone does not establish readiness.
