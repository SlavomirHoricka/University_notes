# Learning plan — TEMPLATE

Copy for a selected course after ingestion notes are finished. The planning skill alone creates and revises this file. Replace placeholders; do not copy the example objective as a real objective.

- schema_version: 2
- record_revision: 0
- transaction_id: null
- course_id: null
- notes_directory: null
- plan_version: P001
- source_version: null
- updated_at: null
- timezone: Europe/Prague
- plan_scope: null
- requested_outcome: null
- deadline_or_retention_horizon: null
- plan_status: provisional

## Coverage

Link source_manifest.md. State which finished note sections are covered and which requested topics are absent. Notes are the curriculum source; this section is not a note-quality audit or learner assessment.

## Sequence

List objective IDs in teaching order with only necessary prerequisite dependencies and reasons.

## Objectives

For each objective, use a block like this:

~~~yaml
objective_id: O001
objective_revision: 1
criterion_version: O001-C1
goal: <observable action, content, and conditions>
note_sections: [] # exact vault paths and headings
prerequisites: [] # objective IDs with reasons
teaching_route:
  motivation: null
  explanation_outline: null
  worked_example_ref: null
  first_practice_task: null
  likely_error_and_response: null
assessment:
  essential_components: []
  acceptable_alternatives: []
  critical_errors: []
  allowed_notes_and_tools: null
  independence_rule: <normally two distinct unaided checks>
  delayed_prompts: [] # at least two distinct questions or task forms
  transfer_prompt: null
~~~

## Plan revisions

Append plan and note versions, affected objective IDs, old/new criterion references, source-change reasons, and any reassessment implications. Preserve earlier definitions needed to interpret recorded attempts. Learner status, attempts, and current session position belong in learning_log.md.
