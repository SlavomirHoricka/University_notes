# H09 canonical extension proposal — review required

H02 proposes API v1 / bundle schema 1 / evidence schema 4. It changes no maintained academic file and enables no canonical writes. The app compatibility gate is explicitly `maintained_schema4_supported=false`, `live_writes_enabled=false`, `pending_owner_task=H09`. Test readers and synthetic history are isolated in app tests. Current maintained `records.py` only recognizes the schema-3 marker and checks vocabulary/history; accepting extra fields is insufficient schema-4 support.

Root must serialize and explicitly assign the following exact maintained-source patch set to H09. Other canonical paths require a new assignment. These paths are proposals, not files changed by H02:

| Exact path | Proposed change |
| --- | --- |
| `03_Agents/teach/references/RECORDS.md` | State schema-3/schema-4 union, strict envelope and common fields, literal append boundary, verified journal/receipt semantics and component identities. Preserve schema-3 meaning. |
| `03_Agents/teach/references/SITE_EVIDENCE.md` (new) | Specify actual response/submission/activity/exposure/result facts, phases mapped to existing vocabulary, Decimal component scales, immutable response retention, digest/retry/correction rules and unknown conditions. |
| `03_Agents/teach/templates/learning_log.md` | Add explicit migration guidance and reference the separate site template; preserve the existing schema-3 marker/example semantics. |
| `03_Agents/teach/templates/site_learning_log.md` (new) | Schema-4 new-log marker, full metadata, empty state and explicitly illustrative event structure; no fabricated outcomes. |
| `03_Agents/teach/SKILL.md` | Gate site writes on accepted maintained contracts and verified actual receipt facts; teach remains sole learning-log owner. |
| `03_Agents/plan/references/SITE_BUNDLES.md` (new) | Bundle schema 1, source-grounded coverage, stable routes and question bank, private/public maps, keys/rubrics/conditions, history and review requirements. |
| `03_Agents/plan/templates/site_bundle_v1.json` (new) | Controlled illustrative manifest; placeholders cannot establish readiness. Canonical bundles belong under `lessons/site/<plan_version>/`. |
| `03_Agents/plan/templates/objective_lesson.md` | Add optional versioned web-route/bundle references; keep existing prepared routes and historical versions intact. |
| `03_Agents/plan/SKILL.md` | Define preparation/reconciliation and independent finished-note curriculum review for every changed web route. |
| `03_Agents/recall/SKILL.md` | Explicitly consume the verified schema union, apply compatible corrections, deduplicate by actual attempt rather than component count, ignore activity/aggregate percentages. |
| `03_Agents/recall/scripts/schedule.py` | Validate normalized core observations from the union and exact verified transaction references, typed component correction support, distinct-attempt qualification; no scoring or scheduling from site activity. |
| `03_Agents/recall/tests/test_schedule.py` | Schema-3 parity, schema-4 component/attempt identity, corrected effective outcomes, unknowns and activity exclusions. |
| `03_Agents/scripts/records.py` | Strict schema-4 new-marker/latest-boundary validation, required common fields and typed site phases, immutable exact original prefix for schema-3 as well as legacy, owner path restrictions, stable event replay/conflicts, narrow correction allowlist. |
| `03_Agents/scripts/test_records.py` | Actual maintained-reader/writer union fixtures, prefix bytes/order/meaning, owner/hash conflicts, journal verification, invalid envelopes and unknown versions. |

After maintained sources are accepted, regenerate only the repository package paths listed by `03_Agents/scripts/sync_plugin.py`; use its normal synchronization/check commands. No installed cache or global config edits. The exact generated-path delta must be reviewed and returned in H09's receipt. Do not run plugin releases. Any new maintained helper module requires root to extend the assignment first.

## Compatibility and owner write rules

For a new log, use `<!-- uni-teach-log:4 -->` followed by metadata `{schema_version:4, owner:teach, course_id, timezone:Europe/Prague, record_revision, transaction_id}`. For existing schema-3 or legacy logs preserve **every original byte as a prefix**, including CRLF, Unicode, unknown fields/statuses and old metadata; append `## Schema 4 boundary` then explicit metadata/new events. Read latest metadata only from an explicit boundary. Append derived summaries after the boundary. Do not serialize/rewrite old JSON or promote incomplete legacy data.

Every new event retains existing vocabulary/common fields and uses `schema_version:4`, `site_extension_version:1`. Response receipt is `session_route/response_received`; original actual response persists independently of grading. Activity has no performance outcome. Attempt result records the prepared complete tuple, original response, observed conditions, component scale and exact actual attempt/receipt/result IDs. Component event IDs are `<UUID>-<objective-id>`. Acquisition and delayed qualification require distinct actual attempts, verified compatible core outcomes and existing prepared rules. Unknown clocks/help/exposure remain unknown.

A correction appends, retains original attempt/item/time/definition/response identity, and targets prior verified result/correction IDs. Preserve current corrected-field semantics; proposed additional `component_result` is typed, refers to the same actual attempt/component, and cannot change original response. Add explicit Decimal precision-80 and scale validation. It is not permission to introduce arbitrary corrected keys.

Use records utility expected hashes and owner locks/journals, not direct writes. Production EvidenceWriter verifies returned event IDs/digests/current log hash against a committed teach journal. The app never treats SQLite proof alone, `committed:true` in staging, a marker, review JSON or directory existence as authority. Canonical schemas remain behind the production compatibility gate until all maintained readers, bridge and independent reviews pass.

## Required H09 validation before live writes

1. Exercise maintained `records.py` commit/verify-record/replay in an isolated fictional course; schema-3 and legacy bytes remain exact prefixes, event order/JSON meaning unchanged, latest explicit metadata correct. Reject unsupported versions, missing/incomplete tuples, extra site fields, unknown receipt kinds, invalid component points, cross-course data, wrong owner and same-ID/different-data conflicts.
2. Replay qualified existing schema-3 and extended schema-4 outcomes through maintained recall. Require equal eligible core conclusions, distinct-attempt qualification, stable correction provenance, and no review schedule from scores, drafts/bookmarks or site activity. Preserve unknown old statuses and incomplete histories.
3. Run the complete H03 crash/idempotency matrix against the real isolated owner adapter: receipt before dispatch, canonical commit before/after acknowledgement, restart reconciliation, duplicate response, conflict/hash mismatch, canonical proof verification. No live course needed for these tests.
4. Verify immutable plan/bank/history exports and owner transactions; independently check every changed route against finished checked notes. Academic content work remains assigned to Uni owners/checkers, not an engineering writer.
5. Run `03_Agents/scripts/test_records.py`, recall maintenance tests, applicable app targets and plugin synchronization check. Compare before/after vault issue identities. Obtain fresh canonical compatibility and exact-candidate engineering reviews. Only then may root accept the production gate and enable downstream real sessions.

H02 fixtures demonstrate the proposed contract; they do not satisfy these production gates.
