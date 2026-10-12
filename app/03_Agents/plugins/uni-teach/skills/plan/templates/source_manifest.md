# Finished-note manifest — template

Plan is the exclusive writer. It fingerprints the finished notes used by this curriculum; it does not audit or hash raw academic materials. Preserve previous snapshots and semantic baselines in immutable curriculum history.

```json
{
  "schema_version": 3,
  "owner": "plan",
  "course_id": "<year>/<semester>/<actual_course_folder>",
  "record_revision": 1,
  "transaction_id": "<same id as learning_plan.md>",
  "plan_version": "P001",
  "source_version": "V001",
  "ingestion_revision": null,
  "updated_at": "<actual ISO timestamp with offset>",
  "timezone": "Europe/Prague",
  "ingestion_pass_refs": [],
  "entries": []
}
```

Production `ingestion_revision` is the actual ingest integer (no string conversion); null is an unready placeholder.

Each entry: `path` (exact vault-relative existing path), `sha256`, `bytes`, `note_sections` (actual headings/block IDs), `objective_ids`, `semantic_baseline` (relevant claims, conditions, symbols, limitations needed to judge later changes), `change_class`, `previous_path`, `previous_hash`, `affected_objective_ids`, and `inspection_status`. Include only selected finished notes and explicitly necessary dependencies/assets; note newly enumerated candidates outside scope in the coverage section. `null` with an access reason is different from deletion. Retain the actual current path after Unicode-normalized lookup.

## Completion provenance and scope

Link `03_Agents/<course_id>/ingestion_state.json` and relevant complete/no-change passes in `03_Agents/runtime/ingest/logs/`. State selected coverage and excluded topics. Missing provenance/state blocks production readiness; a validation artifact must say so explicitly.

## Snapshot and semantic changes

| Current path/locator | SHA-256/bytes | Objective mapping | Relevant semantic baseline | Change class and consequences |
|---|---|---|---|---|
| <note> | <actual hash> | <IDs> | <claims/conditions/limitations> | initial/unchanged/formatting_only/path_only/new_content/substantive_correction/deleted/uncertain |

Hash changes require inspecting finished-note meaning before classifying impact. Record additions, missing paths, access errors, anchor movement and uncertainty explicitly. A renamed file with identical bytes can preserve identity only when the match is unique; rename plus edit needs additional evidence. Do not silently advance a baseline while the semantic change is unresolved.

## Prior versions and commit

Link exact prior manifest/definitions under `curriculum_history/<old_plan_version>/`; do not mutate them. The active manifest and plan must share transaction ID, plan/source versions and ingestion revision and have a committed utility journal. Runtime agents compare metadata/state tokens; plan alone hashes and reconciles notes.
