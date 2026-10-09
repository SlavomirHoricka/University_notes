# Note manifest — TEMPLATE

The planning skill maintains this file as source_manifest.md beside learning_plan.md. It tracks finished ingestion notes used by the plan; it does not re-audit raw course material.

- schema_version: 2
- record_revision: 0
- transaction_id: null
- course_id: null
- current_source_version: null
- updated_at: null
- timezone: Europe/Prague
- ingestion_pass_ref: null

## Note snapshots — append only

For each note version, record the relevant finished notes with vault-relative path, SHA-256 hash, inspected headings, linked objective IDs, and change class. Retain earlier snapshots so old plan and attempt versions remain interpretable.

~~~yaml
source_version: V001
captured_at: null
previous_source_version: null
entries:
  - path: null
    sha256: null
    inspected_headings: []
    objective_ids: []
    change_class: initial # unchanged, changed, new, deleted, or uncertain
    previous_hash: null
    affected_objective_ids: []
~~~

If a note was modified outside a completed ingestion pass, mark its provenance uncertain and route it to ingest before revising affected claims.
