# H02 typed foundation contracts

Input accepted integration: `fcedead7def791b589817063f91245475c03835b`. Checkout: `/Users/slavomirhoricka/.codex/worktrees/hub-foundation/University_notes`, branch `codex/hub-foundation`. Requested native role: hub_foundation, gpt-6.1-sol/high. Host declaration confirms fixed role configuration; independent execution telemetry is unknown. No canonical course writes or production course fixture registrations.

API version v1 / OpenAPI application version 1.0.0 / bundle schema revision 1 are proposed for root interface review. Canonical schema 4 is proposed-only. The H09 exact maintained patch and production validation are in [h09-canonical-proposal.md](h09-canonical-proposal.md).

## Contracts and seams

Strict frozen Pydantic contracts forbid extra fields, use discriminated response/finalization/event unions, complete version tuples and real prefixed UUIDv4 IDs. Course identity uses full exact Unicode path and a separate opaque key; NFC collisions cannot silently merge. The private manifest validates dependency graphs, question/component/coverage/section/blueprint/activity references and prepared point sums. Decimal strings are bounded grammar inputs; sums use precision 80. Public allowlist projections exclude the bank, targets/keys/rubrics/feedback and future retention prompts; selected retention delivery requires a later explicit authorization path.

Typed ports expose receipt replay, actual evidence intent/proof, curriculum/publication/source inventory, local authorization, protected credential store, provider run/cancel/status, course reservations, Git integration inspection, durable requested jobs and event replay. H01 injects local authorization/credential/provider seams without waiting for H03. H07 can use `SQLiteRequestedJobs` to durably queue work before H08 worker execution exists. No provider or owner implementation is fabricated.

EvidenceIntent carries exact typed uncommitted event payloads, stable IDs, owner transaction and digest. Proposed events retain existing vocabulary. Operational draft/upload/job/provider/approval receipts and bookmarks cannot become evidence. Progress and pending grading preserve unknown outcomes. Draft-snapshot/existing-response finalization modes are distinct contracts; H11 implements the one-transaction receipt/response/freeze behavior. H02 validates manifest, blanks, selection and revision conflicts without submitting academic evidence.

OpenAPI's explicit public registry exports downstream command/response components while the health endpoint remains the sole implemented route. It excludes private prepared items, credentials and owner intents. `scripts/export_contracts.py` owns both generated artifacts; `--check` independently regenerates and compares exact OpenAPI/TS bytes. Consumers request model/schema changes from foundation before using them.

## Operational schema and upgrades

```mermaid
flowchart LR
  Course --> Snapshot --> Bundle --> Pointer
  Bundle --> Session --> Assessment --> Draft
  Session --> Attempt --> Response
  Command --> Receipt --> Response
  Receipt --> Outbox --> Commit --> Result
  Attempt --> Result
  Assessment --> Reservation
  Course --> Job --> Step
  Job --> Proposal --> Decision
  Command --> Decision
  Course --> Exposure
```

Five ordered SQL migrations implement the normative catalogue. Foreign keys, STRICT tables, JSON syntax, exact enums/uniqueness, immutable histories, publication CAS, same-course guards, auth terminal state, immutable digest-bound human approvals and draft guards apply in the version that introduces each feature. v3 already guards exposure/reservation/review course relationships. Completed checkpoints cannot be deleted before exact-input invalidation, and lease rows retain fences across acquisitions. v4 seeds recommended academic role settings from the accepted canonical `.codex/agents/uni_*.toml` registry; rows are requested defaults, never provider eligibility or actual-runtime proof.

Forward final-result detail accepted by root: v2 supports assessment active/submitted rows but rejects any non-null final_result_id on INSERT and UPDATE. v3 introduces verified grading results then replaces that prohibition with existence/assessment/session guards. A non-null assignment requires finalized state and a result from an actual response and matching verified commit. Upgrade preserves the original v2 assessment rows.

`connect_database` sets foreign_keys ON, WAL, FULL synchronous and busy timeout 5000; it registers deterministic NFC matching and creates owner-only storage. `migrate` checks immutable ledger names/SHA-256 checksums and integrity, rejects unknown newer/unversioned/downgrade cases, requires a new absolute consistent backup for an existing upgrade, and runs each numbered migration in its own immediate transaction. Failed versions roll back; earlier versions remain usable. H14 must quiesce workers and separately preserve/reconcile canonical history and bundle/upload manifests before swap. SQLite restoration is not proof of canonical reconciliation.

## Acceptance evidence

- H02-A1: strict tuple/UUID/unknown-field tests and dangling question/component/activity/dependency reference failures.
- H02-A2: reviewable public bundle snapshot and private sentinel/target/key/rubric/retention exclusion; actual public OpenAPI registry exclusions.
- H02-A3: fixture-only union reader verifies byte-identical legacy/schema-3 history and metadata boundaries; malformed extension/components/conditions rejected; live gate stays false.
- H02-A4: actual export generation/drift target plus clean/prior-version/checksum/conflict/crash/backup/immutable SQL tests.

Final verification (project-local Python 3.12.15 / Node 24.21.0): `make check-all build` exited 0 (6 unit, 39 contract, 19 integration, 2 UI component and 1 real Playwright tests, strict lint/type checks, export drift and both builds). After final earliest-version/DELETE/precision fixes, Ruff/mypy and `pytest tests/contracts tests/integration -q` exited 0 with 63 tests (40 contract / 23 integration); `make check-contracts build` exited 0. Five migration resources are present in the built wheel. Final `git diff --check` and exact baseline vault-report comparison are recorded in the completion receipt. The pre-existing vault checker fails remain unchanged; upstream Starlette/httpx deprecation stays visible. H02 stops for independent interface review; no H03 work begins before acceptance.


## Independent-review repair candidate

The initial integrated candidate `22f5750cb3d92762f8e5e2d5ec068bcca0a83828` was reviewed independently. These fixes build on foundation commit `5c722fb94fb05a71baf4f3a955ddd5aeed087b48`; root will integrate a new candidate and recheck all findings before dependent use.

| Finding | Repair and regression evidence |
| --- | --- |
| Approval command could authorize unrelated/two proposals | v4 guard now matches `commands.aggregate_id` to the exact proposal and `approval_decisions.command_id` is UNIQUE, alongside existing digest/principal/kind/revision guards. Tests reject unrelated/reused commands in v4/v5 and accept separate commands for distinct proposals. |
| Essential rule reachable only in global bank; route identities/types incomplete | Essential components must occur in that blueprint's selected item set. Lesson and weekly blueprint references enforce their respective kinds; duplicate week/route IDs fail. A retention-only excluded essential fixture fails. |
| Missing public downstream DTOs and aggregate states | Added strict exported EvidenceViewV1, StartReviewV1, UploadReceiptV1, JobSummaryV1, PreferencesV1/PreferenceCommand, plus explicit aggregate result/denominator/essential states described below. Tests cover strictness, unknown/pending/partial truth, cross-course and exact exported registry. |
| Immutable source revision blocked pending extraction | v1 permits only extraction_state to mutate. Every identity, byte/hash, source, size, MIME, storage and timestamp field remains update-guarded; DELETE stays prohibited. Tests cover v1/v4/v5 operational transition and every protected field. |
| Sparse correction serialization manufactured null replacements | CorrectedFieldsV4 serializer includes exactly model_fields_set. Omitted fields stay omitted, explicit nulls remain explicit through nested dump/reparse and canonical payload hashing. Tests apply the exact sparse replacement and prove response/conditions remain unchanged. |

Missing-seam shapes approved by root for exact-candidate review:

- `EvidenceViewV1` has exact course ID, nullable canonical cursor, owner_verified, independent git_sync_state (`unknown/pending/local_committed/pushed/merged/conflict`), typed per-definition applicability/acquisition/result references and typed activity/progress references. Unverified views cannot claim canonical outcomes or completion; owner verification requires a cursor. Git pending remains compatible with verified local owner evidence and never implies remote durability.
- `StartReviewV1` requires recommendation ID, pinned bundle ID and expected projection cursor. No score/mastery or due-date mutation.
- `UploadReceiptV1` wraps the nonacademic common upload receipt, course key, durable immutable source revision/hash/size/MIME/storage references, and exact duplicate revision IDs. All sources belong to its course; duplicate references cannot manufacture acceptance.
- `JobSummaryV1` includes job/course/kind/state/revision/time, measured current step/counts, requested/nullable actual settings, next eligible time and safe error code. No generated narrative, prompt or credential payload.
- `PreferencesV1` schema 1 contains presentation-only theme (system/light/dark), text_size (normal/large), reduced_motion, outline_visible and revision. `PreferenceCommand` requires this typed presentation object plus expected revision; extra learning-state fields are forbidden.
- `AssessmentViewV1` contains frozen max_points (unknown only while assembling), required/finalized counts, explicit result union and essential-state references plus owner commit status. Provisional results are labelled partial with earned/graded-possible points and contain no pass/attention flags; full frozen denominator remains visible. A final result requires every selected item and essential rule finalized, verified commit, unchanged denominator and precision-80 unrounded percentage. Pass/attention must agree with 80/90 thresholds and essential/committed review facts. Pending/unscorable never masquerades as finalized. Server calculated percentages may retain 80 significant digits; learner numeric input remains limited to 50.

The two existing migration checksums deliberately change before H02 acceptance; no runtime operational database has been deployed. This is not a silent upgrade of an accepted live migration. Production writes remain disabled. New regression files are `tests/contracts/test_h02_review_repairs.py` and `tests/integration/foundation/test_h02_review_storage.py`.

Repair verification: actual `make export-contracts` and `make check-all build` exited 0 on the repaired bytes: 6 unit, 65 contract and 28 integration tests (99 backend total), 2 UI component tests and 1 real Chromium E2E. Ruff format/check, strict mypy (67 sources), ESLint/TypeScript, regenerated byte drift, Python distribution and frontend production build passed. The 30 added review regressions cover all five findings. Final vault report remains byte-identical to the original baseline (checker exit 1 on existing failures only).
