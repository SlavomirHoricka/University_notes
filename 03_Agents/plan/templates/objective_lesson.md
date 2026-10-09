# <Objective title> — lesson template

Plan-owned, teacher-executable block. This template is not a lesson or observed learner evidence. Replace all placeholders before marking ready. Explain omitted categories as not applicable; do not leave key/rubric reasoning to the teaching model.

```json
{
  "schema_version": 3,
  "owner": "plan",
  "course_id": "<course_id>",
  "transaction_id": "<matching plan transaction>",
  "plan_version": "P001",
  "source_version": "V001",
  "ingestion_revision": null,
  "objective_id": "O001",
  "objective_revision": 1,
  "criterion_version": "O001-C1",
  "status": "ready",
  "knowledge_components": ["conceptual", "procedural", "interpretation"],
  "prerequisite_ids": [],
  "compatible_versions": [],
  "note_locations": [],
  "acquisition_rule": {"distinct_independent_passes": 2, "required_item_roles": []},
  "delayed_rule": {"minimum_elapsed_hours": 24, "fresh_item": true, "independent_required": true},
  "review_topic": "<answer-free topic>",
  "review_instruction": "Begin a closed-note review with teach for <ID>; request the prepared delayed item."
}
```

Production `ingestion_revision` is the matching actual ingest integer; null is an unready placeholder. `compatible_versions` mirrors the exact approved old tuple rows in the plan index; leave empty unless plan has justified unchanged capability/criteria.

`minimum_elapsed_hours: 24` is a pragmatic validity guard for a next-calendar-day task, not a discovered biological optimum. Plan may set a documented longer delay for the topic/goal. Recall dates tasks; teach records actual elapsed time and does not certify an early answer as delayed retention.

## Outcome and conditions

Observable action, topic, conditions, required conceptual/procedural/interpretive components. Exact finished-note path + heading/block and assumptions/limits. Define allowed notes, calculator/tools, solution exposure and independence. A declaration of confidence or familiarity cannot meet the outcome.

## Prerequisites and checks

For each needed capability: dependency reason; prepared check `item_id`/`item_version`, exact question, expected reasoning/answer, pass/partial/fail rubric, correction and route to its prepared lesson. Explain how adequate prior committed evidence permits skipping the check. Missing prerequisite content triggers plan/ingest handoff, never improvised curriculum.

## Teaching order and rationale

Numbered small blocks and reasons: motivation; intuition; definitions/notation/assumptions; explanation steps; worked example; supported task; reduced assistance; independent tasks; delayed/transfer. Provide exact block anchors for targeted retrieval and skip/return decisions.

## Motivation, intuition, and definitions

Concrete motivating question; intuitive model; definitions; notation with units; assumptions; limits and boundaries. Link fuller note content while supplying the reasoning needed for this lesson.

## Explanation steps

Intermediate reasoning or derivation with each step's justification; result; interpretation; checks and exceptions. Identify what follows from assumptions versus source observations. Do not add externally sourced course claims.

## Worked example

`item_id`/version; setup; conditions; labelled steps; result; interpretation; lesson. Clearly label agent-created hypothetical numbers or context as an instantiation of note-supported reasoning.

## Practice with fading assistance

Each task has stable item ID/version, role, exact prompt, allowed help and tools, full key/worked solution, essential rubric components, acceptable alternatives, critical errors and outcome rules. At least a completion task and two distinct independent checks unless a justified alternative is explicitly defined. State which components each tests and assistance fade criteria. Prepared variants include their exact changed inputs and keys; no “make up a similar question.”

## Rubric and independence

Cross-task essential components; acceptable notation/methods; critical conceptual errors; arithmetic-slip policy; pass/partial/fail/unscorable rules; exact acquisition rule and required item roles. State why conditions are adequate. Unknown access/help never becomes independent evidence. Every component must map to one or more prepared questions on **every allowed acquisition route**. List permitted substitutions and verify that each supplies the full role or an explicitly prepared additional component check; a shorter correction question cannot silently replace a fuller assessment.

## Misconceptions and correction

For each likely misconception: diagnostic sign; tentative versus established interpretation; specific corrective explanation; hint 1/2 if used; fresh follow-up task + complete key/rubric. Score the initial response before help. After two ineffective hints show the necessary step or pause; after repeated unsuccessful independent attempts stop quizzing and use the prepared repair route.

## Immediate and delayed checks

Distinct prepared immediate versus delayed items, minimum elapsed condition and no-solution-before-answer rule. Normally two delayed variants with keys; include explanation, application, discrimination or changed-context transfer when warranted. Indicate item relation (`parallel_variant`, `near_transfer`, etc.) and limits of the inference. Repeated same-item recall is not an independent fresh check.

## Advance, revisit, pause, and escalate

Rules for advancing after qualifying acquisition evidence; delayed review after a real interval; returning to named prerequisite; closing a session without claiming completion; blocked source; unsupported answer alternative/ambiguous rubric or exhausted prepared variants -> `plan_issue`. Exact course/version/objective/item information and responsible recipient.

## Answer-free recall handoff

Topic/title and actionable start instruction with lesson/objective link; no solution, answer key or proposed due date. Teach passes committed evidence IDs; recall owns scheduling and Todoist.
