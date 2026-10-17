# <Objective title> — lesson template

Plan-owned, self-contained teacher-executable block following `03_Agents/references/LESSON_CONTENT.md`. This template is not a lesson or observed learner evidence. Replace all placeholders before marking ready. Explain omitted categories as not applicable; do not leave key/rubric reasoning to the teaching model.

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
  "lesson_content_contract": "self-contained-lessons-v1",
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

Concrete motivating question; intuitive model; definitions; notation with units; assumptions; limits and boundaries. Embed the full relevant existing note explanation with reused/adapted provenance, exact origin and necessary assumptions. Preserve language/notation; map any changes. Supply missing bridges with plan-created provenance and verified citations where needed. No required explanation may be replaced by a locator or short excerpt.

## Explanation steps

Reuse the complete relevant derivation and its justifications, result, interpretation, checks and exceptions. Identify adaptations and any plan-created intermediate reasoning. Verify additional claims with authoritative sources and precise citations under `LESSON_CONTENT.md`; distinguish supplementary explanation from assessed scope. Include usable figures, captions/interpretation and checked asset paths. Delivery must not require opening original notes.

## Worked example

Reuse a suitable full worked example from the notes and record its origin; design a new one only when needed. `item_id`/version; setup; conditions; labelled steps; result; interpretation; lesson. Clearly label agent-created hypothetical numbers or context as an instantiation of note-supported reasoning.

## Practice with fading assistance

Each task has stable item ID/version, role, exact prompt, allowed help and tools, full key/worked solution, essential rubric components, acceptable alternatives, critical errors and outcome rules. At least a completion task and two distinct independent checks unless a justified alternative is explicitly defined. State which components each tests and assistance fade criteria. Prepared variants include their exact changed inputs and keys; do not leave the main exercise bank or keys to teach. Declare permitted generated-item roles/component coverage under `LESSON_CONTENT.md`; teach may add verified items within those bounds, freezing the key/criteria before presentation.

## Rubric and independence

Cross-task essential components; acceptable notation/methods; critical conceptual errors; arithmetic-slip policy; pass/partial/fail/unscorable rules; exact acquisition rule and required item roles. State why conditions are adequate. Unknown access/help never becomes independent evidence. Every component must map to one or more prepared questions on **every allowed acquisition route**. List permitted substitutions and verify that each supplies the full role or an explicitly prepared additional component check; a shorter correction question cannot silently replace a fuller assessment.

## Misconceptions and correction

For each likely misconception: diagnostic sign; tentative versus established interpretation; route to an included explanation/prepared prerequisite lesson; optional prepared hints, with teach free to phrase responsive feedback; fresh follow-up task + complete key/rubric. Score the initial response before help. After two ineffective hints show the necessary step or pause; after repeated unsuccessful independent attempts stop quizzing and use the prepared repair route.

## Immediate and delayed checks

Distinct prepared immediate versus delayed items, minimum elapsed condition and no-solution-before-answer rule. Normally two delayed variants with keys; include explanation, application, discrimination or changed-context transfer when warranted. Indicate item relation (`parallel_variant`, `near_transfer`, etc.) and limits of the inference. Repeated same-item recall is not an independent fresh check.

## Advance, revisit, pause, and escalate

Rules for advancing after qualifying acquisition evidence; delayed review after a real interval; returning to named prerequisite; closing a session without claiming completion; blocked source; alternative requiring changed standards/ambiguous rubric or new objective/method -> `plan_issue`. Exhausted variants may use eligible checked generated items; difficult/uncertain cases need stronger assessment support. Valid unlisted methods meeting unchanged criteria may receive credit. Exact course/version/objective/item information and responsible recipient.

## Content provenance and generation boundaries

Map each substantive explanation/example/figure to reused, adapted or plan-created origin; exact note locators, fingerprints and adaptation/notation reasons belong in the manifest. Cite actually verified authoritative support for additional claims. Mark supplementary explanation versus assessed content. Prerequisite routes point to complete prepared lessons rather than repeating every foundation. Specify generated-item roles, essential component coverage and verification boundaries; preserve exact named reassessment items unless substitution is expressly defined.

## Answer-free recall handoff

Topic/title and actionable start instruction with lesson/objective link; no solution, answer key or proposed due date. Teach passes committed evidence IDs; recall owns scheduling and Todoist.
