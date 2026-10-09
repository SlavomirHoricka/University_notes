# Hold-up — validation finished-note manifest

```json
{
  "schema_version": 3,
  "owner": "plan",
  "course_id": "2026_2027/Winter_Semester/Comparative_Economics",
  "record_revision": 5,
  "transaction_id": "VALIDATION-PLAN-005",
  "plan_version": "P005",
  "source_version": "V001",
  "ingestion_revision": "VALIDATION-complete-pass-20261003T142217",
  "updated_at": "2026-10-04T14:26:50+02:00",
  "timezone": "Europe/Prague",
  "validation_artifact": true,
  "production_ready": false,
  "ingestion_pass_refs": [
    "03_Agents/runtime/ingest/logs/20261003T142217+0200_behavioral_week1.md"
  ],
  "entries": [
    {
      "path": "01_Notes/2026_2027/Winter_Semester/Comparative_Economics/Week_1/Institutions_and_Economic_Development.md",
      "sha256": "ad6b2563b63aec9f5d51f12a6c628859bde634c2452e0f90c2fac1f939f0b79f",
      "bytes": 44075,
      "note_sections": [
        "2. Hold-up: investment changes bargaining power",
        "3. Commitment: promises can become unattractive to keep",
        "1. Information: hidden quality and hidden action"
      ],
      "objective_ids": [
        "O001",
        "O002"
      ],
      "semantic_baseline": "Hold-up requires relation-specific sunk investment and weakened outside option; current operating surplus (p-c)q differs from total project profit (p-c)q-I; axle source inputs I=10000,q=1000,c=20,p=30,pprime=25 imply promise total0, cut operating5000, produce total-5000, refuse-10000. Initial break-even c+I/q; current production strictly beneficial if pprime>c under no-alternative/no-extra-cost assumptions. Pure commitment need not require specific investment; hidden information is distinct though mechanisms can overlap. Contracts/integration/alternatives have enforcement, efficiency or financing limits.",
      "change_class": "initial",
      "previous_path": null,
      "previous_hash": null,
      "affected_objective_ids": [
        "O001",
        "O002"
      ],
      "inspection_status": "selected headings inspected; rest of full note not claimed as curriculum coverage"
    }
  ]
}
```

## Completion provenance and scope

[Completed independent-check record](../../runtime/ingest/logs/20261003T142217+0200_behavioral_week1.md) documents finished Comparative Economics notes and no remaining material findings. The pass's initial Behavioral folder is not the final course identity. This manifest uses finished-note bytes/locations; it does not reopen or hash original PDFs.

The selected headings supply all academic mechanism/accounting/contrasts used by this artifact. Entire note bytes are fingerprinted to detect change, while only selected heading coverage is claimed. Other note content, notes and course syllabus remain outside curriculum scope. The validation-local revision identifies this provenance; production still requires an actual ingest-issued course state token.

## Snapshot and semantic changes

Initial V001; actual SHA-256/size and bounded semantic baseline are in metadata above. Exact P001 manifest and lesson definitions are preserved in [prior manifest](curriculum_history/P001/source_manifest.md); exact P002 is also preserved under [P002 manifest](curriculum_history/P002/source_manifest.md). P003 changes assessment coverage only, retaining V001 and all note bytes; no learner evidence exists to reinterpret. A future changed byte hash would require plan to inspect finished-note meaning and preserve this version, not a runtime tutor hash/audit. Academic corrections remain ingest's responsibility.

## Commit status

Plan, manifest and both lesson blocks share VALIDATION-PLAN-005/P005/V001/validation provenance revision. The utility journal records the validation-local bundle. A committed local bundle establishes durable files; it does not override the production freshness gate or create learner knowledge.
