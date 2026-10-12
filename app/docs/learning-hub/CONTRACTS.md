# Learning hub implementation contracts

Status: proposed implementation instructions, 2026-10-10. No application, schema extension, migration or owner bridge described here is implemented by this document. The approved personal learning hub plan v1.0 supplies product requirements; the existing [master architecture](../../03_Agents/LEARNING_ARCHITECTURE.md), [teaching records contract](../../03_Agents/teach/references/RECORDS.md), [learning log template](../../03_Agents/teach/templates/learning_log.md), [objective lesson template](../../03_Agents/plan/templates/objective_lesson.md) and `records.py` supply current authority. Implement extensions through the maintained canonical owners before enabling real evidence. Do not edit generated plugin/cache copies or existing historical events.

## 1. Ownership, modules and implementation order

`B` below means `apps/learning_hub/backend/learning_hub/`. Each module is a concrete implementation destination, not a current file. API models use Pydantic with strict types, forbidden extra fields on commands, discriminated unions and generated OpenAPI/TypeScript. Domain code does not import FastAPI, SQLite or provider SDKs. Application services receive interfaces; adapters perform IO. No course business decisions belong in frontend handlers.

| Task / owner | Owned modules (exact registry prefixes) | DAG predecessors |
|---|---|---|
| H00 / hub_foundation | Minimal package/tool scaffold; root records bootstrap exceptions and future ownership | None |
| H01 / hub_provider | `B/adapters/codex/`, `B/api/provider/` | H00,H02; real sign-in/completed inference gate |
| H02 / hub_foundation | `B/domain/{models,ports}/`, `B/adapters/storage/`, generated frontend API | H00 |
| H03 / hub_foundation | `B/application/core/`, `B/adapters/evidence/`, `B/api/{core,courses,lessons}/` | H02; fixture-only owner port acceptance |
| H04 / hub_frontend | Frontend app, courses, styles | H02 |
| H05 / hub_frontend | Frontend lesson/assessment/review screens, maths/outline/questions | H03,H04 |
| H06 / hub_visuals | Frontend visuals/tests; `B/domain/visuals/` | H05 |
| H07 / hub_workflows | `B/application/uploads/`, `B/adapters/extraction/`, `B/api/workflows/` | H02 |
| H08 / hub_workflows | `B/worker/`, workflow job endpoints | H01,H03 |
| H09 / hub_workflows | `B/adapters/{vault,repository}/`; separately assigned maintained canonical patch | H02,H03,H08 |
| H10 / hub_workflows | `B/application/{ingestion,publication}/` | H07,H09 |
| H11 / hub_assessment | `B/domain/grading/`, `B/application/{attempts,assessments}/`, `B/api/assessments/` | H03,H05,H09 |
| H12 / hub_assessment | `B/domain/{selection,review_policy}/`, `B/application/reviews/` | H10,H11 |
| H13 / hub_frontend | Frontend Agents/settings and final API integration | H04,H08,H10 |
| H14 / hub_operations | `B/operations/`, operations scripts/docs | H01,H03,H08 |
| H15 / hub_qa | Cross-feature e2e, fixtures and validation receipts | H06,H12,H13,H14 |
| H16 / hub_coordinator | Release and integration; exact root-assigned release receipt | H15 |
| hub_reviewer | Read-only engineering review, no mutation ownership | Exact integrated candidate |

Task registry controls fixed requested model/effort settings: implementation engineering owners use GPT-6.1 Sol/high; independent engineering reviewer uses GPT-6 Astra/high. Maintained engineering role files are `.codex/agents/hub_*.toml`; these are separate from academic Uni roles. This table does not override the registry or academic model routing. Owners coordinate interface changes before modifying another owner's module. Foundation owns receipt/outbox mechanics; assessment owns scoring and selection; workflows owns publication and academic workflow invocation. The evidence bridge executes logical **teach** ownership even when deterministic code scores an item. Recall alone schedules canonical due dates and writes Todoist. App recommendations are derived route suggestions, never a second recall scheduler.

Implementation dispatch follows the JSON DAG. H02 specifies and tests proposed compatibility models/migration fixtures without changing maintained records. H03 implements receipt/outbox/projection mechanics through the typed EvidenceWriter port and a fault-injected fixture owner; its acceptance is explicitly fixture-only. H09 later owns the root-assigned maintained canonical patch and production owner adapter, then reruns H03 crash/idempotency cases against actual compatible records tools in an isolated vault. H08 scheduling can use the port before H09 exists, with production owner writes disabled. No H02/H03 receipt claims live schema-4 support. H09 production acceptance is a hard prerequisite for live sessions and H10/H11. Keep real-course import disabled until canonical/readiness checks pass. Provider feasibility runs early in parallel with fixture work; offline rendering of already published content remains available.

## 2. Identity, times and immutable references

Identifiers are strings in transport. New operational IDs use prefixed UUIDv4 (`ses_…`, `att_…`, `del_…`, `job_…`, `rec_…`, `pub_…`); validate prefix and UUID. Generate once before first persistence and retain on replay. Academic IDs remain their existing course-local values (e.g. `O001`, prepared `item_id`); do not convert them or infer them from titles/indexes.

```json
{
  "course_id": "2026_2027/Winter_Semester/Financial_Markets_Instruments_I",
  "academic_year": "2026_2027",
  "semester": "Winter_Semester",
  "course_folder": "Financial_Markets_Instruments_I",
  "course_code": null,
  "objective_id": "O001",
  "objective_revision": 1,
  "criterion_version": "O001-C1",
  "plan_version": "P001",
  "source_version": "V001",
  "ingestion_revision": 2,
  "bundle_id": "pub_65a90e42-7cb8-4ba5-9571-3fb30c33bc9e",
  "bundle_schema_version": 1,
  "item_id": "O001-I02",
  "item_version": 1,
  "variant_id": "var_0866c2b8-6fe2-40fd-97ad-4fc46c246bd4",
  "variant_version": 1
}
```

This is illustrative identity, not a statement that that real course has a site-ready bundle. A `DefinitionRef` is the complete course/objective/revision/criterion/plan/source/ingestion tuple. `ItemRef` adds prepared item and variant versions; `BundleRef` adds immutable bundle ID/schema/public/private digest. Never use only `O001` as a cross-course key. Week, web lesson, section and assessment IDs are stable course-local authoring IDs (`W001`, `L001`, `L001-S001`, `A001`) with integer revisions. A week number is display metadata; week ID is not a date. Splits/merges allocate new IDs and explicit predecessor mappings. Public API course routing uses an opaque `course_key` registered to the exact `course_id`, avoiding slash/Unicode path parsing.

Course identity equals the actual relative folder spelling. NFC lookup may find the directory; persist actual spelling and refuse collisions rather than normalize two courses into one. Unknown course code stays null. Plan compatibility lists exact old `DefinitionRef` tuples with reason and `compatible`, `requires_reassessment`, `retired`, or `uncertain`; no wildcard/version-range approval. Preserve old tuples and history, never regrade old answers because new content appears.

Persist server times as UTC ISO-8601 strings ending `Z`; transport accepts only offset-aware ISO-8601 and retains the original offset in reported-time fields. Canonical events include actual offset-aware `occurred_at`, `recorded_at` and `timezone: Europe/Prague`. Use UTC instants for elapsed hours; Europe/Prague for recall calendar dates. Server receipt time is authoritative for receipt, not proof of display or answer production. Browser-reported times are explicitly reported; absent/ambiguous values remain null. Reject a claimed future display time outside a 5-minute clock-skew window and retain timing as unknown; do not reject the response solely for bad client clock.

Hash bytes with SHA-256; store lowercase 64-character hex. For JSON command/digest comparison use one canonical serialization: UTF-8, sorted object keys, compact separators, no NaN/Infinity, Unicode retained, Decimal values encoded as strings. Never use a float or localized title in a stable key.

## 3. Checked bundle contract and public/private separation

Plan owns a proposed `site_bundle_v1` extension stored under `03_Agents/<course_id>/lessons/site/<plan_version>/`. Proposed maintained validator contract: `03_Agents/plan/references/SITE_BUNDLES.md`. These paths require H09's maintained contract/template/records-validator changes and tests before use; directory ownership alone is insufficient. Canonical immutable history must retain the exact private assessment definitions and note excerpts needed to interpret old results. Runtime exported copies are replaceable; canonical plan history is not.

Use this staged layout in operational storage:

```text
bundles/<bundle_id>/
  manifest.json          # Full server-only manifest
  public/catalogue.json # Answer-free scope/navigation
  public/lessons/*.json  # Only released teaching sections
  public/assets/*       # Verified allowlisted assets
  private/items.json    # Full prompt bank, keys, feedback, rubrics
  private/blueprints.json
  validation.json       # Checks, reviewer references, integration evidence
```

Store runtime bundles outside the web static directory. `GET /assets/{asset_id}` resolves an allowlisted **public** asset via the pinned manifest; never accept a filesystem path. Private bank files, hints, solutions and unreleased prompts cannot be served through static mounting, source maps, catalogue exports, SSR hydration, client bundles, errors or job logs. Ordinary lesson JSON excludes question-bank prompts; prompt delivery returns only selected items. A future section containing a worked solution is released through the section-delivery protocol so its exposure is tracked. Private files use owner-only permissions. This avoids accidental disclosure in normal use; it is not proctoring against the machine's owner.

`BundleManifestV1` mandatory fields:

- `bundle_id`, schema version 1, `course_id`, source snapshot ID, exact plan/source/ingestion tuple, created time, public/private file SHA-256 map, plan and ingest transaction IDs, integrated Git commit, owner/reviewer references, required/optional scope and blocked scope.
- Objective index with exact `DefinitionRef`, dependencies, ready status, note path+heading/block references, acquisition/delayed rules, compatibility rows and reassessment requirement IDs.
- Weeks with ordered lesson refs, separate lesson-quiz refs and weekly-test blueprint refs. Required/optional flags and bounded available scope. Teaching estimate defaults to 25 minutes per coherent lesson, quiz 5–10, weekly test 25–35; estimates never gate completion.
- Coverage rows `note_locator → required_concept_id → DefinitionRef → section_ref → checkpoint_refs → assessment_component_refs`; optional concepts have reason/provenance. Every required row has teaching and appropriate assessment. Declare capabilities a final number cannot demonstrate.
- Instructional routes with required sections/checkpoints and prepared correction-route activities; each route executable without improvised content. Each choice and each declared matching/numeric misconception has prepared feedback; correct feedback explains the result.
- Assessment blueprints with item roles, Decimal point denominator, essential rules, allowed notes/tools, variant families, feedback release policy, expected duration, retry routes and unseen bank sufficiency.
- Visual configs: component enum, formula/reference relation, source support, assumptions, units, bounds, accessible description, reference cases and static fallback. Components run maintained code; config cannot contain JavaScript, HTML event handlers or arbitrary imports.

Validate all references, sanitization, KaTeX-supported formulas, point/component sums, essential reachability, misconception feedback, allowed alternatives, cross-route coverage, compatibility/history, visual reference cases and bank variants. H09 must obtain a separate independent curriculum review of all changed routes against **finished checked notes**, not raw sources. Publication verifies actual owner journals and Git integration; presence of `validation.json` alone is no proof.

Publish files into a new immutable bundle directory, fsync files/directories, verify hashes, then change `publication_pointers` in one SQLite transaction with expected generation and source snapshot. A reader either receives the complete old or complete new bundle. Pointer changes never edit active `sessions.bundle_id`. If a crash leaves an unreferenced staged bundle, verify/reuse it or quarantine; never infer publication from directory existence. If SQLite commit succeeds but SSE does not emit, replay the persisted event. Keep at least the previous valid pointer and every bundle referenced by sessions, attempts, canonical history or pending receipts. H14's garbage collector deletes only unreferenced regenerable exports after reconciliation; never canonical history.

A new session requires current complete ingestion, indexed ready plan and verified transactions for selected scope. A pinned session may continue its previously verified immutable snapshot during a normal compatible update. An explicit material validity issue pauses new affected items/results and records affected bundle/objectives; it cannot silently issue evidence from invalid content. Unaffected scope continues. Pending submitted responses remain preserved and are reviewed under the original definitions, with results held if validity is uncertain.

## 4. Question, rubric and deterministic grading models

All examples in this document are fictional fixtures. Fixture courses use `fixture/…`, live in test temp vaults and never enter learner records.

`PrivateItemV1` contains `ItemRef`, `exposure_equivalence_id`, family ID, purpose (`checkpoint`, `lesson_quiz`, `weekly_test`, `immediate_repair`, `retention`, `reassessment`), task relation, exact prompt AST, response union, allowed conditions, prepared points/components/key/alternatives/feedback and source-note support. An item may assess multiple objectives only with separate explicit component mappings and exact tuples. `max_points` equals the sum of non-overlapping scoring components; do not count one point twice. Essential rules point to exact component/item IDs; an objective labelled essential does not automatically require 90%.

`PublicPromptV1` contains only item/delivery IDs, pinned bundle, answer-free prompt AST, response type/constraints, choices/left/right labels, public units/rounding/representation, allowed notes/tools and optional estimate. It never includes keys, accepted-answer sets, hidden numeric target/tolerance, solved matches, correctness, rubric text that reveals solutions, feedback or future retention items. A declared rounding/precision rule must remain visible even though the target is private.

### Multiple choice and matching

- `single_choice`: response `{kind:"single_choice", option_id:"o2"}`; one prepared correct option, all-or-nothing points. Reject unknown/multiple IDs as 422, preserve no attempt result from malformed transport. Every option, including correct, has prepared explanation and correction route.
- `multiple_choice`: response `{kind:"multiple_choice", option_ids:["o1","o3"]}`; unique IDs. Default is exact set, all-or-nothing, no negative marking. Partial-credit policy is permitted only when explicitly prepared/versioned with per-option components; never improvise it at runtime.
- `matching`: response `{kind:"matching", pairs:[{left_id:"l1",right_id:"r2"},…]}`; each left appears once, right uniqueness/reuse follows published constraint. Default one prepared point component per pair; correct pair earns its points. Missing explicit pair in final submitted response earns zero for that component; malformed duplicate/unknown IDs are 422. Feedback identifies each actual pairing with prepared correct relationship/misconception; a verified generic wrong-pair explanation may cover otherwise unlisted pair combinations. A blank intentionally submitted matching answer is distinguishable from an unreceived response.

Choice presentation order is a recorded permutation, not a variant. Validate immutable option IDs; grading never uses screen index or display text.

### Final numeric answer

Response `{kind:"numeric", value:"5.25", representation:"percentage_points", unit:"percent"}`. Accept signed base-10 decimal strings and optional exponent, at most 128 characters and 50 significant digits. No evaluation, commas/thousands separators, NaN/Infinity, arithmetic expressions or implicit unit conversion. Display input examples for supported formats. A parser error returns 422 and keeps the draft; it is not a wrong answer. Empty string explicitly submitted as a blank is an intentional blank under the prepared rubric.

Prepared private numeric spec contains target Decimal, unit enum, representation enum, accepted explicit conversions if any, absolute tolerance, relative tolerance and rounding policy. Defaults: one final-value component, no derivation credit, no tolerance unless authoring provides it; publication rejects missing tolerance declarations; authoring explicitly declares zero for exact comparison. Compare in prepared canonical units:

```text
abs(submitted - target) <= max(abs_tolerance, rel_tolerance * abs(target))
```

Use Decimal arithmetic with context precision 80, then exact declared rounding where needed; do not round the submitted number to make a wrong answer pass. At target zero the relative term is zero. Inclusive boundary passes. Fixture: target `5.25` percentage points, absolute tolerance `0.01`, relative `0`; `5.24` passes, `5.239` fails. `0.0525` with decimal-fraction representation does not silently pass unless an explicit permitted conversion exists. A correct final number satisfies only its prepared value component; derivation/concept/interpretation require other mapped items. Wrong feedback chooses prepared misconception predicates in declared priority order, then a prepared general explanation. No runtime equation/answer generation.

### Scenario interaction and response composition

`ScenarioQuestion` composes one approved visual config with a response kind from `single_choice`, `multiple_choice`, `matching` or `numeric`. Its private item explicitly maps interaction/config version to the same prepared key/components and validates permitted parameter bounds. A slider state may be submitted as operational interaction telemetry but is never a scored answer; the learner's explicit conclusion/value is graded through the existing response union. No arbitrary scenario evaluator, executable predicate or new response kind is implied. H06/H11 test config→response mapping and invalid/missing conclusions.

### Written response and essential criteria

Response `{kind:"short_text", text:"…"}` with max 20,000 UTF-8 bytes. Preserve verbatim text including an intentional blank. Prepared private rubric contains component IDs, integer/Decimal point maxima, essential boolean/rule, required claims, acceptable alternatives, critical errors, source-note locators and outcome rules. An assessor receives the exact prompt/response/conditions/tuple and this rubric. It returns a strict `AssessmentDecisionV1` with each component (`met`, `partial`, `unmet`, `unscorable`), earned points, supporting response spans or a blank-answer reason, observed errors, prepared-rule references and concise feedback. Validate spans, totals, denominator, component IDs and earned bounds. Model supplies assessment under prepared rules; it cannot add criteria, rewrite definitions or grant acquisition.

Ambiguous/incomplete output is pending for bounded repair, then `unscorable`; a plausible unprepared answer alternative becomes an owner `plan_issue`, not zero points. H11 routine assessment uses the configured routine assessor, with explicit difficult-case adjudication through prepared rubric; actual model/effort remains recorded in operational job metadata. Unsupported capabilities, quota or sign-in failures leave grading pending. No client score accepted.

For an assessment, `percentage = 100 * earned_points / max_points` using Decimal; compare the unrounded value, render to one decimal place. All required items must be finalized/scorable to compute a final result. Return provisional earned/possible only clearly labelled partial; `passed`/`needs_attention` remain null while pending/unscorable. A valid intentional blank receives prepared zero/unmet components and is a received answer. Do not remove an unscorable item's denominator and silently make the test easier.

Prepared essential rule union:

```json
{"kind":"all_components_met","component_refs":["i1:c1","i3:c2"]}
{"kind":"points_at_least","component_refs":["i2:c1","i2:c2"],"minimum_points":"3"}
{"kind":"all_of","rules":[{"kind":"all_components_met","component_refs":["i1:c1"]}]}
```

No arbitrary executable expressions. Every referenced component must be covered by every permitted selection/variant route; validate rule bounds. Finalized site `passed = percentage >= 80 AND every essential rule met`; `needs_attention = percentage < 90 OR any essential rule unmet OR active committed review weakness`. Test fixture: 85%, all essential met → completed/passed/attention; 95%, essential unmet → completed/not passed/attention; 90%, essential met and no review weakness → no attention. The site's percentage result is separate from canonical objective `pass/partial/fail` and acquisition/delay rules. Only prepared per-objective rubric outcomes enter canonical evidence; an overall site pass cannot become an objective acquisition declaration.

## 5. Activity, attempts and assessment state machines

Persist states; application transitions execute in `BEGIN IMMEDIATE` with optimistic row revision and appropriate unique constraints. Clients send expected revisions but never transition targets, scores, completion booleans or canonical events. Duplicate same command returns the original receipt/result; differing body under the same key is 409.

| Entity | Allowed states/transitions | Guard |
|---|---|---|
| Session | active → paused → active; active/paused → closed; active/paused → validity_hold | Pinned bundle retained; closure is navigation state, not pass |
| Prompt delivery | prepared → offered → displayed; offered → display_unknown | Canonical `attempt_started` verified before offering; only acknowledged rendered prompt is known displayed |
| Attempt | started → response_received → grading_pending → assessed → evidence_committed → feedback_available; started → abandoned; grading_pending → unscorable/validity_hold | Result needs actual immutable response; no inferred answer; feedback withheld until response/result transaction verified |
| Feedback delivery | prepared → offered → displayed; offered → display_unknown | Released under feedback policy; generated/queued feedback is not known exposure |
| Assessment | assembling → active → submitted → grading_pending → finalized; submitted/grading_pending → unscorable/validity_hold; active → abandoned | Final submission freezes exact responses/blank declarations and denominator |
| Receipt | pending → committing → committed; pending/committing → conflict/blocked; conflict/blocked → pending after explicit resolved recovery | Only actual verified owner journal authorizes committed; nonacademic commands use canonical state `not_applicable` |

`assessed` and `evidence_committed` are separate boundaries. An unscorable decision may be owner-committed as an `unscorable` result/issue, then proceed to released explanatory feedback while retaining `grading_state:unscorable`; it never becomes a scored final result. A validity hold restores the prior permitted state only after a checked owner clearance, preserving the hold record. Display-unknown delivery may reconcile to displayed from a genuine acknowledgement, but uncertain times remain uncertain. SQL row updates cannot edit a prior response or finalized result; a grading correction produces a new decision with `supersedes_result_id` and canonical `correction`, preserving originals. Workflow repair does not reuse a terminal attempt. A new retry has a new attempt ID with `previous_attempt_id`, its own response and exact prepared variant. Preserve first attempt, hint assistance, immediate retry and delayed attempt in separate views. Never derive performance solely from best score.

`LessonProgressV1` is a derived view with independent fields:

```json
{
  "instruction_state":"finished",
  "assessment_submission_state":"submitted",
  "assessment_grading_state":"pending",
  "completed":true,
  "passed":null,
  "needs_attention":null,
  "evidence_state":"current",
  "canonical_commit_state":"verified"
}
```

Required section process activity is a rendered section acknowledgement plus navigation to its next prepared activity. Required checkpoints require actual response, verified result/feedback delivery and any required prepared correction-route activity. Scrolling, elapsed time or a lesson-close button cannot create completion. This acknowledges instructional participation; it does not prove comprehension. Quiz submission must be durably received and canonically recorded to show verified completion; grading may remain pending. While owner commit is pending show “submission received; evidence pending” and never claim canonically saved progress. Week completion requires every required lesson process/quiz submission plus weekly-test submission; optional activities excluded. Course denominator covers only declared currently available required scope and labels partial semester coverage.

No `mark_complete` endpoint exists. Section advancement is an activity command with delivery acknowledgement and route validation, not arbitrary completion. Replay committed section/response/submission receipts to rebuild progress. Preserve bookmarks separately when no evidence receipt exists.

Checkpoint feedback is immediate after verified result. Lesson quiz feedback is per-item after that item's explicit immutable answer submission and verified result; it does not wait for whole-quiz finalization. Weekly-test feedback is withheld until final submission of the entire test. No draft is graded or exposed as a result. Written per-item grading may finish later; weekly feedback still respects the whole-test gate. Canonical start events may exist for unanswered items; no result until response/intentional blank receipt. Original responses, assisted corrections and later attempts remain distinct.

### Editable weekly drafts, atomic submission and bookmarks

An active weekly assessment has one operational `AssessmentDraftV1` per selected item: assessment/item/attempt IDs, response union or explicit blank, draft revision, received timestamp and optional reported conditions. Drafts are editable, ungraded and not canonical answer evidence. Previously frozen original responses cannot become drafts. Saving a draft requires idempotency, expected assessment revision and expected draft revision (zero if absent); one transaction upserts the draft and increments the assessment revision. A second tab/stale save gets a conflict with current revisions; preserve its unsaved input.

Weekly finalization uses `mode:"draft_snapshot"`, expected assessment revision, an exact item→draft-revision manifest and explicit blank-item IDs. In one SQLite transaction check active state, frozen selection/pinned tuple, all current draft revisions and complete response/blank coverage, then insert immutable child responses/receipts/outbox, parent submission receipt and submitted assessment state. Store the manifest/digest as its replay result. Any mismatch aborts the entire freeze; no partial submission. Blank declarations create typed blank responses under the prepared policy. Only after freeze does teach receive the actual submission/response events and grading begin. Never copy a half-saved browser form into canonical evidence.

Lesson-quiz finalization uses `mode:"existing_responses"` with already immutable response receipt IDs and explicit outstanding blanks; item feedback may already have been released. It freezes aggregate coverage/denominator and records the whole-quiz submission, preserving each first response/assistance. These are strict discriminated finalization commands; a weekly route cannot use existing-responses mode to bypass editable-draft/final-feedback rules.

`BookmarkCommandV1{section_ref,anchor_id?,expected_revision}` updates only the pinned session bookmark through authenticated idempotent PATCH. Validate the section/anchor belongs to that session, increment its revision and return a nonacademic receipt. It emits no completion, score or exposure fact; actual rendered-section acknowledgement uses the existing delivery endpoint. Debounced saves never overwrite newer answers or evidence.

## 6. Delivery, idempotency and crash protocol

Every mutation except auth bootstrap uses `Idempotency-Key` (UUIDv4) and an expected aggregate revision/tuple. Nonacademic mutations still persist idempotency receipts but return `canonical_commit_state:"not_applicable"`; they cannot write learning evidence. Scope uniqueness is `(local_principal, command_kind, idempotency_key)`; local principal is the single learner, not a provider account identifier. Include route/body/pinned session in canonical request hash. Store original receipt and replay response; never expire keys while retained commands/evidence can be retried. Reusing a key with a new command/body is `IDEMPOTENCY_CONFLICT`. Reusing an attempt with a different response is `ATTEMPT_ALREADY_SUBMITTED`. Original answer immutability beats newer browser state.

Protocol implemented by H03:

1. Start/resume pins bundle and ready selection. Reserve attempt/item and `delivery_id` in SQLite, enqueue stable teach `attempt_started` event intent. Do not expose prompt yet. Owner bridge validates canonical extension and readiness, takes shared course coordination lock then `records.py` course lock, commits the start and verifies current log bytes/journal. Set delivery offered and serialize only public prompt. Release locks before waiting for learner.
2. Browser renders prompt/section/feedback, then sends delivery acknowledgement with receipt ID, content digest, reported display time and observed visibility/conditions. Receipt is durable before ACK. Canonical teach records displayed `exposure_reported` or `instruction_or_feedback` with exact content ref and known/unknown time. Server transmission alone is not actual display. If acknowledgement is lost, retain `display_unknown`/possible exposure and exclude that item from fresh retention until reconciled.
3. Answer POST includes attempt/item/session versions, response discriminated union, original delivery ID, reported conditions/assistance and reported answer time. In one SQLite transaction validate identity, freeze verbatim response, insert submission receipt/outbox, idempotency result, grading work and operational event. fsync via SQLite commit before returning 202. The response says `durable_receipt:true`, `canonical_commit_state:"pending"`; it never falsely says evidence saved. A 202 remains replayable after browser/service restart.
4. Commit a teach-owned `session_route` site submission receipt (exact response, versions and receipt ID) before scoring. This records actual receipt without inventing outcome. Deterministic grading may run locally; written job can wait. Append `attempt_result` only after a valid prepared decision. All projected component results point to canonical event IDs and verified journal references. Completion-submission receipts are owner-committed even when grading is pending.
5. Only after canonical result verification make eligible feedback available; retain response before any correction/help. Delivery ledger records offered/displayed feedback separately. Correction attempts and help receipts are new events, never replacement of original answer. Recall handoff waits for committed qualified evidence and owner scheduling; an outbox row alone changes no dates.

The owner bridge assigns stable `event_id` and proposed `T-site-<UUID>` transaction IDs **before** its write. Current `records.py commit` accepts `transaction_id` through draft JSON (`commit(..., transaction_id=None)`); no new CLI flag is assumed. Draft `{changes:{"learning_log.md":"…"},expected:{"learning_log.md":"<sha256 or null>"},transaction_id:"T-site-…"}` lives privately outside tracked paths. Before retry check existing event ID and journal: same ID/identical payload means reuse; same ID/different payload means conflict. Never call commit a second time with an existing transaction directory. Recover only the original owner's known transaction after process/lock inspection. `verify-record COURSE_DIR teach learning_log.md` verifies current bytes; historical receipt validation also checks retained journal stages/event hashes because later valid log appends change its current file digest.

| Crash cut | Recovery assertion/test |
|---|---|
| Before SQLite answer COMMIT | No durable acceptance; browser retries same key; no result/outcome |
| After COMMIT, before HTTP ACK | Retry returns same receipt/attempt; one outbox and one response |
| After attempt reservation, before start commit | Prompt still hidden; resume same intent/item |
| After owner start commit, before delivery offered | Reconcile event/journal; offer same prompt/attempt |
| After HTTP prompt/feedback transmission, before display ACK | Possible exposure retained; no claim of display/clean unseen status |
| After display receipt commit, before canonical exposure commit | Durable outbox blocks retention eligibility; owner bridge replays once |
| After owner journal prepared or partial file replacement | Preserve journal/lock; inspect dead process, owner recover, verify; never build a new competing write |
| After owner commit, before SQLite receipt committed | Discover stable canonical event and matching journal; mark receipt committed without duplicate |
| After assessor completed, before result persistence | No accepted result; retry bounded job under same rubric; no guessed score |
| After result COMMIT, before feedback ACK | Replay eligible feedback; record actual delivery separately; original result remains |
| After pointer commit, before publication event delivered | Catalogue reads new complete bundle; SSE replays persisted publication event |
| During migration/restore | Old database or transactional rollback remains usable; owner journals/evidence preserved and reconciled |

SQLite/WAL, owner filesystem transactions and Git are distinct commit boundaries. No claim of distributed atomicity. Outbox reconciliation provides at-least-once delivery with exactly-once **logical** stable-event effect. Receipts remain pending until verified, and conflicts remain visible; never silently drop a poison intent or use dead-letter state as completion.

## 7. Teach/recall extension gate and evidence authority

H09 must implement and independently verify the root-assigned maintained canonical extensions before real sessions; H10 consumes only that accepted production bridge. Proposed **canonical evidence schema 4** uses the existing teach event-type vocabulary with a typed `site_extension_version:1` envelope. A new schema-4 log starts with `<!-- uni-teach-log:4 -->` and first metadata `{schema_version:4,owner:"teach",course_id,timezone,record_revision,transaction_id}`. For an existing schema-3 or legacy log, preserve its entire original bytes as an exact prefix, then append an explicit `## Schema 4 boundary` with schema-4 metadata and new events; never rewrite its old marker/header/events. Each new event carries `schema_version:4` plus existing required common fields. Future derived summaries append after this boundary, never replace the preserved prefix. Add a maintained `03_Agents/teach/references/SITE_EVIDENCE.md` plus validators/tests; update packaging only through canonical synchronizer. A future change to event vocabulary or field semantics requires a separately versioned migration, not a quiet reader change. Current `records.py` recognizes schema-3 markers/core event types but does **not** validate schema 4. H02 defines the union contract/migration fixtures; H09 exclusively implements root-assigned maintained records/readers and the production bridge, then reruns H03 port cases before consumers enable live writes. Validation must locate the latest explicit metadata boundary, enforce schema-4 fields, preserve old prefix/history, and retain owner path restrictions. Permissive acceptance of extra fields is not readiness.

Map site facts to existing teach types:

| Fact | Existing event / proposed `site` fields |
|---|---|
| Session pin/route | `session_started` / `session_route`; bundle ref, week/lesson/assessment refs, route and receipt IDs |
| Item reserved before presentation | `attempt_started`; exact prompt/item/variant, conditions, stable attempt/delivery IDs |
| Actual prompt displayed | `exposure_reported`; delivery content digest, equivalence ID, reported display time and unknown conditions |
| Section activity/navigation | `session_route`; section ref, actual delivery receipt and next prepared route activity; no pass |
| Verbatim response/submission received | `session_route`; phase `response_received` or `assessment_submitted`, submission receipt ID, immutable actual response union/text, received/reported times, blank policy |
| Final assessment component outcome | `attempt_result`; full existing common tuple/conditions, `site` component point scale, item/bundle/receipt/result IDs and outcome-rule reference |
| Feedback/hint/worked example actually displayed | `instruction_or_feedback`; exact content/equivalence/objective refs, delivery/time/assistance; not generated-but-undelivered feedback |
| Correction of a wrong grading decision | `correction`; `supersedes_event_id`, allowed corrected fields, reason, retained original response and new decision ID |
| Acquisition/reassessment qualification | `acquisition_met` / `reassessment_met`; existing prepared rule and qualifying canonical event IDs |
| Missing variant/rubric or invalid content | `plan_issue` / `note_issue`; exact definitions, affected item/response and responsible route |

Example proposed extension (inside a genuine existing event, not a full record to copy):

```json
{
  "site_extension_version":1,
  "site":{
    "bundle_id":"pub_65a90e42-7cb8-4ba5-9571-3fb30c33bc9e",
    "receipt_id":"rec_368b7658-6b8a-497e-b5d0-b013d7b2d68d",
    "phase":"response_received",
    "attempt_id":"att_655de4b3-c399-4d71-ae23-9c4ffb4530a1",
    "response":{"kind":"numeric","value":"5.25","representation":"percentage_points","unit":"percent"},
    "received_at":"2026-10-10T12:00:00Z",
    "reported_answered_at":null
  }
}
```

Canonical logs retain actual responses sufficient to reproduce evidence; SQLite must not be the only long-term copy. Per-component `attempt_result` events for multi-objective items reference one shared actual attempt/receipt and distinct objective tuples; define stable IDs `<UUID>-<objective-id>` and ensure acquisition requires distinct **attempt IDs**, not duplicated component rows. Assessment-level percentages are a derived site view over these committed point/result facts, never scheduler signals. Updated canonical evidence and recall readers must explicitly support the schema-3/schema-4 union without promoting old incomplete history. Unupdated readers cannot be assumed compatible. Test recall against both old and extended events; unsupported site-only activity cannot schedule reviews.

The bridge uses records expected-hash writes and preserves schema-3 event order/JSON meaning plus the complete pre-migration prefix, including legacy bytes. Derived summaries can be rebuilt, but event history cannot be replaced. A grading correction must follow existing allowed corrected-fields policy; extending numeric component fields requires maintained correction-reader changes/tests. No learning state is written directly by API routes or arbitrary workers. A source scanner never writes teach events; teach never hashes raw sources.

All cooperating workers coordinate one course across worktrees via the shared operational `course_leases` table and coordinator service, then the selected checkout's records lock. Lease fencing protects job/publication state; it is **not** permission to steal a filesystem lock. Before an authoritative owner mutation, ensure current fence, checkout/scope, no conflicting active task and no pending owner journal. If another host/non-cooperating writer or unknown lock exists, block and report. Do not expire `.learning-write.lock` by age. Recovery verifies recorded host/PID is inactive and inspects journals before authorized release; PID reuse/unknown host needs explicit resolution.

Read mastery and recall projections only from verified committed canonical records. Rebuild by event ID/version and append-only corrections, with exact plan compatibility. Owner commit status is separate from Git commit/sync status; expose both. Background academic branches must integrate through required review/PR gates before publication. Runtime evidence journaling must preserve and surface its Git synchronization state without staging unrelated owner files or claiming remote durability from a filesystem commit.

## 8. Selection, exposure and course review

`exposure_equivalence_id` identifies the substantive prompt/solution lineage across versions/permutations. Changing option order, formatting or a typo keeps it. A materially new prepared application/context may receive a new ID only after plan review. A family groups equivalent skills; exposure of one family member does not automatically exhaust every changed-context variant, but authoring explicitly maps revealing worked examples/hints/solutions to the IDs they reveal. Ambiguity defaults to conservative exclusion, not fresh status.

Track prompt, worked example, hint, solution and independent-study exposures by course/objective/tuple/equivalence and time quality. Offered-but-unacknowledged delivery is possible exposure and excludes fresh retention. Unknown intervening exposure/notes/tools prevents clean independent delayed qualification even if an item is unseen. SQLite exposure projection is rebuilt from canonical receipts; pending delivery outbox overlays exclude candidates until commit/reconciliation. Do not delete exposure because an attempt was abandoned, the browser reloaded or a rubric changed.

Selection use case is transactional:

1. Validate session/course/blueprint and exact bundle; filter only checked ready variants with required component coverage/conditions.
2. For retention, exclude all definite/possible/reported relevant exposures and current reservations by equivalence ID; assess actual interval against plan minimum (default 24 elapsed hours) using last relevant **objective** exposure, not merely this item's date. Ask unseen retrieval/application before refresher/hints; follow-up after feedback is immediate assisted practice.
3. For retries choose a prepared fresh equivalent variant and retain original attempt relation; no waiting requirement. Same-item correction remains available instructional practice but cannot become independent fresh evidence.
4. Solve required component/essential blueprint coverage first, then deterministic tie-break by SHA-256 of persisted selection seed + variant ID. Persist selected list, seed and versioned algorithm; no LLM choice or browser reshuffle. Seed UUID is generated once per assessment and replayed on resume.
5. Reserve candidates with a unique active reservation per session/equivalence. Release undelivered reservation on genuine cancellation only after delivery uncertainty inspection. Exposed candidates remain excluded.

Weekly default blueprint weighs current and earlier same-course available points 50/50; select by points/required capabilities, not count. Use exact equality when prepared point totals permit; otherwise accept 45–55% current weighting and disclose actual weights/reason. Week 1 is 100% current. Insufficient earlier checked pool creates a checked/versioned explicit exception blueprint; never silently borrow another course or invent items. Earlier unstudied content is labelled in the blueprint/UI. Reject an unexplained noncompliant blueprint at publication. Selecting the pool does not send future prompts/keys to the browser.

If no valid fresh coverage exists, return `VARIANT_POOL_EXHAUSTED` with answer-free objective/reason, queue bounded plan preparation/review, and offer corrective practice/new lessons. Never relabel an exposed item unseen or block unrelated/new study. Repeated ineffective checkpoint attempts follow prepared repair route after the existing stop rules (two ineffective hints; three unsuccessful independent same-objective attempts in a session), not an endless scoring loop.

`ReviewRecommendationV1` has one `course_id`, trigger canonical event IDs, objective tuples, reason, route (`corrective_refresh`, `retention_check`, `reassessment`), prepared activity refs, justified estimated minutes, recall review ID/due date when owner supplies them, readiness and blockers. Cards may show multiple courses; a review session contains exactly one. No duration cap. Reviews remain nonblocking. Estimates sum prepared activities and disclose approximation. Return empty/unknown honestly; do not generate due tasks from a site attention score alone. H10 routes committed evidence to recall through its own safe writes/project verification; H12 displays read-only schedules and recommends prepared routes.

## 9. SQLite operational schema and migrations

Storage location defaults to `~/Library/Application Support/UniLearningHub/` on this macOS first release, configurable by launcher. Resolve against the current user's profile; never hardcode the developer's home. `state.sqlite3`, WAL/SHM, private submissions, upload staging, bundles, extraction scratch and OAuth material are excluded from Git. Runtime application state outlives frontend builds. Credential storage uses OS credential facilities where supported; never SQLite/plain logs/browser.

Open SQLite with `foreign_keys=ON`, `journal_mode=WAL`, `synchronous=FULL`, `busy_timeout=5000`. One short write transaction at a time; never hold SQLite transaction during inference, browser wait or owner IO. Queue on busy then return typed retryable 503 if bounded deadline expires. All state mutation SQL is parameterized. JSON columns are validated by Pydantic on read/write; SQL `json_valid` protects syntax, not academic validity. Money/points/tolerances use decimal strings; no binary floats. Table timestamps use UTC; revision is integer ≥1. Immutable tables have update/delete guard triggers with narrowly controlled migration access; do not add `ON DELETE CASCADE` on evidence/receipt histories.

The following tables/columns are required. `PK` = primary key; `FK` = foreign key; `UQ` = unique; `J` = TEXT with `CHECK(json_valid(column))`; nullable is explicitly stated. Text keys default NOT NULL. H02 turns this catalogue into numbered SQL migrations and matches these exact relationships in migration tests.

| Table | Columns, constraints and purpose |
|---|---|
| `schema_migrations` | `version INTEGER PK`, `name`, `checksum`, `applied_at`; immutable checksum per applied migration |
| `courses` | `course_key PK`, `course_id UQ`, `academic_year`, `semester CHECK IN Winter/Summer enums`, `course_folder`, nullable `course_code`, `display_name`; exact full identity UQ, no fuzzy merge |
| `source_files` | `source_id PK`, `course_key FK courses`, `original_name`, `managed_relpath`, `week_ref J`, `created_at`, nullable `archived_at`; UQ(course_key,managed_relpath) for live sources via partial index |
| `source_revisions` | `source_revision_id PK`, `source_id FK`, `revision INTEGER CHECK >0`, `sha256 CHECK length=64`, `byte_size INTEGER CHECK >=0`, `media_type`, `storage_ref`, `extraction_state`, `created_at`; UQ(source_id,revision); immutable bytes/provenance |
| `source_snapshots` | `snapshot_id PK`, `course_key FK`, `generation INTEGER CHECK >0`, `snapshot_digest`, `entries J`, `created_at`; UQ(course_key,generation); immutable inventory input |
| `bundles` | `bundle_id PK`, `course_key FK`, `snapshot_id FK`, `schema_version CHECK =1`, `plan_version`, `source_version`, `ingestion_revision CHECK >0`, `manifest J`, public/private digests, `storage_ref`, `validation_state`, nullable `integrated_commit`, `created_at`; immutable validated body |
| `publication_pointers` | `course_key PK/FK`, `bundle_id FK bundles`, `generation CHECK >0`, `changed_at`; compare-and-swap expected generation and snapshot; transactionally assert bundle course matches |
| `bundle_validity` | `validity_id PK`, `bundle_id FK`, `affected_definitions J`, `kind CHECK IN ('validity_hold','cleared')`, `reason`, owner references J, `recorded_at`; append-only; clearing requires checked owner decision |
| `sessions` | `session_id PK`, `course_key FK`, `bundle_id FK`, `route_kind`, route_ref J, `status CHECK session states`, `revision CHECK >0`, bookmark J, `created_at`, `updated_at`; pinned bundle/course immutable |
| `assessment_drafts` | `(assessment_id FK,item_id) PK`, attempt_id FK, draft_revision CHECK >0, response J or explicit_blank, reported_conditions nullable J, updated_at; mutable only while parent assessment active, correct selected-item/course guards; never evidence/result |
| `approval_proposals` | proposal_id PK, job_id FK, course_key FK, kind, proposal_digest, source_snapshot_id FK, expected_hashes J, scope J, preserved_version_refs J, safe_preview J, created_at; immutable proposal body; revised proposal gets new ID |
| `approval_decisions` | decision_id PK, proposal_id FK, command_id FK, principal, decision CHECK IN ('approve','reject'), proposal_digest, expected_job_revision, decided_at; immutable audit, UQ(proposal_id); no implicit grant from retry/source content |
| `provider_auth_flows` | flow_id PK, requested_action, state, registration/host refs J, state_digest/nonce_digest, expires_at, terminal_at nullable, subject_ref nullable; protected credential/PKCE material in credential store, never public JSON; no eligibility before validated terminal auth |
| `assessments` | `assessment_id PK`, `session_id FK`, prepared_ref J, blueprint_digest, selected_items J, selection_seed, algorithm_version, `status CHECK assessment states`, `revision CHECK >0`, nullable `submitted_at`, nullable `final_result_id`; exact selected list immutable after activation |
| `attempts` | `attempt_id PK`, `session_id FK`, nullable `assessment_id FK`, item_ref J, equivalence_id, nullable `previous_attempt_id FK attempts`, `status CHECK attempt states`, `revision CHECK >0`, `created_at`; item/bundle/parent immutable; no self-parent |
| `receipts` | `receipt_id PK`, `command_id FK commands`, kind CHECK IN ('response','delivery','activity','assessment_submission','assessment_draft','session','job_action','upload','approval_decision','provider_action'), aggregate_id, immutable payload J/digest, received_at; UQ(command_id,kind,aggregate_id); durable command receipt independent of owner commit |
| `responses` | `receipt_id PK/FK receipts`, `attempt_id UQ/FK`, `command_id FK commands`, `response J`, response_digest, conditions J, `received_at`, nullable reported_answered_at; immutable original, no updates/deletes |
| `deliveries` | `delivery_id PK`, `session_id FK`, nullable `attempt_id FK`, `kind CHECK IN ('prompt','section','feedback','hint','worked_example')`, content_ref J, content_digest, equivalence_refs J, `state CHECK delivery states`, `offered_at` nullable; no raw private key unless eligible feedback reference |
| `delivery_receipts` | `receipt_id PK/FK receipts`, `delivery_id UQ/FK`, `command_id UQ/FK`, reported_display_at nullable, timing_quality, observed_conditions J, `received_at`; immutable acknowledgements; identical replay only |
| `commands` | `command_id PK`, local_principal, kind, idempotency_key, request_digest, aggregate_id, `status CHECK IN ('accepted','completed','blocked')`, response_status INTEGER, replay_response J, `created_at`; UQ(local_principal,kind,idempotency_key) |
| `evidence_outbox` | `intent_id PK`, receipt_id FK receipts, `course_key FK`, `session_id FK`, owner CHECK ='teach', stable_event_ids J, payload J, payload_digest, `transaction_id UQ`, `state CHECK receipt states`, attempt_count CHECK >=0, nullable next_eligible_at/error_code; UQ(course_key,intent_id); payload immutable |
| `evidence_commits` | `commit_id PK`, intent_id UQ/FK, `transaction_id UQ`, canonical_path, event_ids J, event_digests J, committed_log_digest, `verified_at`; immutable proof, not outcome authority |
| `grading_results` | `result_id PK`, `attempt_id FK`, `decision_revision CHECK >0`, `decision J`, decision_digest, nullable supersedes_result_id FK same table, evidence_commit_id FK, `created_at`; UQ(attempt_id,decision_revision); append-only verified decisions |
| `activity_projection` | `session_id PK/FK`, canonical_cursor, canonical_digest, progress J, `rebuilt_at`; replaceable; never source of canonical writes |
| `exposure_projection` | `projection_id PK`, `course_key FK`, equivalence_id, objective_ref J, canonical_event_id, time nullable, timing_quality, exposure_kind; UQ(course_key,canonical_event_id,equivalence_id); replaceable; index(course_key,equivalence_id) |
| `variant_reservations` | `reservation_id PK`, session_id FK, assessment_id nullable FK, equivalence_id, variant_ref J, state CHECK IN ('reserved','offered','exposed','released'), created_at; partial UQ(session_id,equivalence_id) WHERE state !='released' |
| `review_projection` | `recommendation_id PK`, course_key FK, canonical_cursor, recommendation J, `rebuilt_at`; replaceable; each JSON course matches parent |
| `jobs` | job_id PK, course_key nullable FK, kind, dedupe_key UQ, input_ref J, requested_settings J, actual_settings nullable J, state, revision CHECK >0, created_at, next_eligible_at nullable, error nullable J; checked state enum from WORKFLOWS; no credentials |
| `job_steps` | `(job_id FK,step_key) PK`, ordinal CHECK >=0, input_digest, state, output_ref nullable J, checkpoint nullable J, attempt_count CHECK >=0, last_error nullable J; completed checkpoint immutable unless invalidated by exact new inputs |
| `course_leases` | `course_key PK/FK`, holder_id, fence INTEGER CHECK >0, owner_checkout, acquired_at, renewed_at, expires_at; monotonic fence on new acquisition; coordinates operational writers only |
| `events` | `seq INTEGER PK AUTOINCREMENT`, event_id UQ, course_key nullable FK, aggregate_kind, aggregate_id, event_type, safe_payload J, occurred_at; append-only redacted SSE facts |
| `role_settings` | `role_key PK`, requested_model, requested_effort, speed CHECK ='standard' initially, revision CHECK >0, updated_at; validated provider capability; future runs only |
| `local_auth_sessions` | session_digest PK, local_principal, csrf_digest, created_at, last_used_at, expires_at, revoked_at nullable; no raw cookie/CSRF in database; replaceable local authentication state |
| `bootstrap_capabilities` | capability_digest PK, expires_at, consumed_at nullable; one-time CAS exchange, process-local launcher only; never OAuth material |
| `preferences` | `local_principal PK`, schema_version, preferences J, revision; UI preferences only, no evidence/mastery |

Draft-save receipts use assessment_draft; approval decisions use approval_decision; provider start/grant/sign-out uses provider_action; bookmark uses session. These operational receipt kinds return canonical_commit_state not_applicable and cannot be promoted into teach events.

For final-submission intentional blanks, the command creates one parent assessment receipt plus immutable child response receipts keyed by each attempt, in the same transaction; child receipts share the originating command and do not count as independent command replays. Each response still has a unique attempt ID. Command replay returns the parent and the original child IDs; owner intents reference their exact receipts. Response payloads require the same originating command ID as their common receipt. Circular FK between responses/commands is avoided by inserting command first and updating its replay receipt within the same transaction. `grading_results.evidence_commit_id` refers only to a verified result intent; in-progress decisions live in `job_steps.output_ref`/private staging until canonical verification. Outbox receipt kinds require application validation against response/delivery/assessment command and immutable IDs; use the normalized common `receipts` parent table above. Do not weaken a FK to solve insert ordering.

Essential SQL patterns:

```sql
CREATE UNIQUE INDEX command_idempotency
  ON commands(local_principal, kind, idempotency_key);
CREATE UNIQUE INDEX one_response_per_attempt ON responses(attempt_id);
CREATE INDEX outbox_ready ON evidence_outbox(state, next_eligible_at);
CREATE INDEX event_replay ON events(seq);
-- Application asserts pointer candidate course/snapshot/validation before this CAS.
UPDATE publication_pointers SET bundle_id=:new, generation=generation+1,
  changed_at=:now WHERE course_key=:course AND generation=:expected;
-- rowcount must be 1, else PUBLICATION_CONFLICT.
```

Migration order (owner H02; H14 executes runtime upgrade):

1. `0001_identity_publication.sql`: migration ledger, courses, sources/revisions/snapshots, bundles/pointers/validity. Test new DB and immutable bundle/pointer CAS.
2. `0002_delivery_evidence.sql`: commands/common receipts, sessions, assessments/editable drafts, attempts, responses, deliveries/receipts, outbox/commit proof and activity projection. Add response immutability/uniqueness. Fixture canonical bridge tests gate real usage.
3. `0003_assessment_exposure.sql`: verified results, exposure/reservations/review projections; migrate existing fixture records without fabricating exposure/outcomes. Backfill only from verified canonical events; unknown remains unknown.
4. `0004_jobs_events_settings.sql`: jobs/steps/leases/events/preferences/settings/local auth, provider auth flows, immutable approval proposals/decisions and state/uniqueness indexes. Seed recommended role settings from fixed registry; actual provider capability remains separately probed.
5. `0005_integrity_guards.sql`: append-only triggers, same-course relationship guards, indexes, immutable-reference guards, and full `PRAGMA foreign_key_check`/`integrity_check`. Do not defer all validation until this migration: earlier versions already enforce their own invariants.

Pause mutations/workers for upgrade, inspect pending owner transactions, make consistent SQLite backup using backup API with WAL included logically, copy immutable bundle/upload manifests and canonical evidence/journals separately, then apply each migration transactionally. Verify checksum ledger/foreign keys/integrity/schema version before restarting. No destructive down migration; restore prior backup into an isolated directory and reconcile canonical commits that occurred since backup before swap. Unknown newer schema is startup-blocking read-only diagnostic, never auto-downgrade. Test upgrades from every supported prior version and interruption between migrations; migration must not touch canonical logs/curriculum/history.

## 10. Typed HTTP, authentication and events

API base `/api/v1`, JSON UTF-8, OpenAPI generated by FastAPI and committed schema fixture after owner review. Generate frontend types/client into `apps/learning_hub/frontend/src/api/generated/`; CI fails drift. Endpoint handlers validate, authorize and dispatch named application use cases. Use `X-Request-ID` in response/errors. `ETag` on immutable/read aggregate representations; mutation `If-Match` carries aggregate revision where shown. Idempotency replay takes precedence over stale If-Match for the same original command.

Single local learner, loopback only (`127.0.0.1`/`::1`), default port 8765. Production local launcher serves frontend and API on one origin. Reject arbitrary Host/Origin, remote bindings and wildcard CORS. Development Vite origin is explicit launcher configuration, never `*`. Session bootstrap requires a one-time launcher capability (256-bit random, short-lived) exchanged by POST; it is not an OAuth token. Browser opener may use a URL fragment so it is not in server/access logs, immediately clears it, and sends JSON body. Backend sets `HttpOnly; SameSite=Strict; Path=/` random local session cookie, 24-hour idle expiry, plus separate random CSRF token returned once and retained by the client. Secure cookie is enabled under HTTPS; initial loopback HTTP documents its local boundary. Every mutation validates cookie, allowed Origin and `X-CSRF-Token`; SSE uses same-origin cookie. Never place auth tokens in SSE URL, public bundles or provider payload/logs. Bootstrap does not grant AI account eligibility; H01's supported local OAuth/Codex sign-in gate does that. No browser cookie scraping or automatically billed API fallback.

`GET /auth/session` rotates/reissues CSRF for a valid local cookie after reload, reports local-session state, not provider credentials. Sign-out invalidates local cookie/server session and CSRF; provider sign-in remains separately explicit. Local bootstrap is required again if cookie expires. Provider auth secrets remain in its adapter; API emits only `signed_in`, eligibility/capability state and unknown/reported reset metadata.

All mutations require Idempotency-Key except bootstrap/session authentication exchange; mutable aggregates also require If-Match and pinned tuple as applicable. Below `202 Receipt` is durable acceptance, not completed academic work. GET/HEAD never mutate owner evidence, generate fresh questions or run inference.

| Method and route | Request / response | Semantics |
|---|---|---|
| POST `/auth/bootstrap` | `BootstrapCommand{capability}` → `LocalSession{csrf_token,expires_at}` | One-time launcher secret; no Idempotency-Key |
| GET `/auth/session`; POST `/auth/logout` | `LocalSessionState`; empty command → 204 | Logout CSRF required; no academic mutation |
| POST `/provider/auth-flows` | `ProviderAuthStartV1{action:'sign_in'|'grant',expected_account_revision?}` → 202 `ProviderAuthFlowViewV1{flow_id,status,authorization_url?}` | Explicit user action; validated loopback redirect and supported registration; no shell/credentials in UI |
| GET `/provider/auth-flows/{id}`; GET `/provider/status`; GET `/provider/models` | Redacted flow/account/actual capabilities and supported model-effort choices | Status does not equal successful inference; no tokens/state secrets |
| GET `/provider/oauth/callback` | Supported registered loopback OAuth code/state callback, protocol-only response | Provider-owned exact redirect; state/nonce/PKCE/identity checks, clean status redirect, bound-flow exception to local-cookie/CSRF |
| POST `/provider/sign-out` | `ProviderSignOutV1{expected_account_revision}` → receipt | Stop future account dispatch, safe-boundary reconcile in-flight jobs, revoke/clear selected credentials through supported flow; preserve outputs/evidence |
| GET `/capabilities` | `Capabilities{provider_state,roles,offline_features,usage?:ReportedUsage}` | Actual/unknown settings; no guessed account eligibility |
| GET `/courses`; GET `/courses/{course_key}/weeks` | `CourseCatalogueV1[]`, `WeekSummaryV1[]` | Explicit ready/partial/stale/blocked scope/current bundle |
| POST `/sessions` | `StartSessionCommand{course_key,bundle_id,route_kind,route_ref,expected_publication_generation}` → 202 `ReceiptV1` | Pins valid content; can wait for owner session commit |
| GET `/sessions/{session_id}` | `SessionViewV1` | Frozen refs, process/projection freshness, pending receipt IDs |
| PATCH `/sessions/{id}/bookmark` | `BookmarkCommandV1{section_ref,anchor_id?,expected_revision}` → receipt/session revision | Navigation state only; pinned-anchor validation, no learning evidence |
| POST `/sessions/{id}/pause`; POST `/sessions/{id}/resume`; POST `/sessions/{id}/close` | `SessionActionCommand{expected_revision}` → `ReceiptV1` | No completion/pass side effect |
| POST `/sessions/{id}/activities/advance` | `AdvanceCommand{section_ref,delivery_receipt_id,next_activity_ref,expected_revision}` → `ReceiptV1` | Only prepared route transitions; creates process receipt |
| POST `/sessions/{id}/deliveries` | `RequestDeliveryCommand{activity_ref,expected_revision}` → 202 `ReceiptV1` | Reserves/start-commits before release; select only prepared route |
| GET `/deliveries/{delivery_id}` | `DeliveryViewV1{state,payload?:PublicPromptV1|PublicSectionV1|ReleasedFeedbackV1}` | 202 while preparation pending; payload only when authorized offered |
| POST `/deliveries/{id}/ack` | `DisplayAckCommand{digest,reported_display_at?,conditions}` → 202 `ReceiptV1` | Durable actual display report; no inferred comprehension |
| POST `/attempts/{attempt_id}/responses` | `SubmitResponseV1{session_id,item_ref,delivery_id,response,conditions,reported_answered_at?,expected_revision}` → 202 `ReceiptV1` | Original immutable response; scores ignored/rejected |
| GET `/attempts/{id}` | `AttemptViewV1` | Pending/committed result; feedback gating enforced |
| GET `/receipts/{receipt_id}` | `ReceiptV1` | Canonical pending/committed/conflict with safe refs |
| POST `/sessions/{id}/assessments` | `StartAssessmentV1{prepared_assessment_ref,expected_revision}` → 202 `ReceiptV1` | Freeze selected list/blueprint; prompt release separately |
| GET `/assessments/{id}/drafts` | `AssessmentDraftV1[]` plus assessment revision | Learner's active weekly drafts only; no keys or grade |
| PATCH `/assessments/{id}/drafts/{item_id}` | `SaveDraftV1{response?,explicit_blank,expected_revision,expected_draft_revision,conditions?}` → saved draft/revisions/nonacademic receipt | Active selected weekly item only; no grading/canonical response |
| POST `/assessments/{id}/submit` | Discriminated `FinalizeAssessmentV1{mode,expected_revision,draft_revision_manifest?|response_receipt_ids?,blank_item_ids,conditions}` → 202 `ReceiptV1` | Atomic complete weekly-draft snapshot or quiz response finalization; §5 guards and feedback gate |
| GET `/assessments/{id}` | `AssessmentViewV1` | Aggregate denominator, pending/final result/essential states; no unearned keys |
| GET `/courses/{key}/evidence` | `EvidenceViewV1{canonical_cursor,owner_verified,git_sync_state,definitions,activity}` | Projection plus explicit freshness; no manual mastery edit |
| GET `/courses/{key}/reviews` | `ReviewRecommendationV1[]` | Course only; owner due dates/route readiness |
| POST `/courses/{key}/review-sessions` | `StartReviewV1{recommendation_id,bundle_id,expected_projection_cursor}` → 202 `ReceiptV1` | One course; retention selection before recap |
| POST `/courses/{key}/uploads` | Multipart `UploadV1{week_id,replace_source_id?,expected_source_revision?,files[]}` → 202 `UploadReceiptV1` | 100 MiB/file, 20 files/500 MiB total per batch; durable original hash; duplicate bytes no-op |
| GET `/jobs/{id}/approval-proposals`; GET `/approval-proposals/{id}` | `ApprovalProposalV1{kind,digest,course_key,snapshot,scope,expected_hashes,preserved_versions,safe_preview,status}` | Concrete owner-required preservation/replacement proposal; private banks excluded |
| POST `/approval-proposals/{id}/decisions` | `ApprovalDecisionV1{decision,proposal_digest,expected_job_revision}` → receipt | Authenticated human explicit decision; recheck scope/snapshot/hashes/CAS before accepting; changed proposal invalidates grant |
| GET `/jobs`; GET `/jobs/{id}` | `JobSummaryV1[]`, `JobViewV1` | Recorded stages/steps; redact content/secrets |
| POST `/jobs/{id}/pause|resume|cancel|retry` | `JobActionV1{expected_revision}` → 202 `ReceiptV1` | Safe boundary controls from WORKFLOWS; no forced Ready |
| GET `/settings/roles`; PATCH `/settings/roles/{role}` | `RoleSettingsV1[]`; `RoleSettingCommand{model,effort,expected_revision}` → updated view | Capability validation, future runs only; cannot change rubric/review gates |
| GET/PATCH `/preferences` | `PreferencesV1`; `PreferenceCommand{preferences,expected_revision}` | Presentation only |
| GET `/assets/{asset_id}` | Validated MIME file, ETag | Only public allowlist within pinned/valid permitted bundle |
| GET `/events` | SSE `OperationalEventV1` | Redacted status; no prompt/key/answer/chain-of-thought |

GET collection pagination uses opaque keyset `cursor`, `limit` default 50/max 200; stable ordering and cursor scope version. Never expose arbitrary vault path/file-reader endpoints, completion/mastery setters, execute-tool endpoints or a public private-rubric route. Upload limits are concrete first-release defaults, configurable by documented trusted launcher setting; oversized material can be split/explicitly adjusted, never silently truncated. Detect magic/MIME, traversal and symlink escape; an upload does not authorize deletion of old notes/history. Originals/provenance durable before upload acceptance. H07 specifies extraction type handling in WORKFLOWS.

### In-site approval and provider control boundaries

Approval is required only when the owning workflow actually needs missing explicit authorization (for example ambiguous source selection or preserved-version substantive replacement); already-authorized safe updates continue automatically. The job publishes a concrete immutable proposal binding kind, full course/snapshot/scope, expected bytes, preservation plan and safe diff digest. It waits without writer locks. Approve/reject is an authenticated human command, never inferred from source contents, generic Retry or an AI message. Revalidate proposal/snapshot/hashes and job revision before writing; a changed candidate needs a new proposal/decision. Rejection preserves old artifacts and records the blocker. Preview access is possible study exposure: record observed preview/source regions and later map them conservatively to checked objective lineage; do not subsequently call an exposed variant fresh retention.

Provider sign-in/grant begins inside Settings/Agents, opens only the validated supported authorization URL, and exposes redacted flow status. A provider-owned registered loopback OAuth callback validates the original flow/state/nonce/PKCE/identity before activating credentials; its protocol callback is exempt from local-cookie/CSRF/idempotency requirements because the bound OAuth flow supplies its authorization, never from state/redirect/identity checks. Callback responses redirect to a clean status URL without codes/tokens in app history/logs. Sign-out blocks future inference and reconciles current effects safely; it does not erase jobs/answers or sign the learner out of local offline study. H01 must prove terminal inference separately from signed-in status.

`ReceiptV1` mandatory fields:

```json
{
  "receipt_id":"rec_368b7658-6b8a-497e-b5d0-b013d7b2d68d",
  "command_id":"cmd_750f1767-cb90-4e3f-9d77-ca02ff3d58d4",
  "aggregate_id":"att_655de4b3-c399-4d71-ae23-9c4ffb4530a1",
  "durable_receipt":true,
  "canonical_commit_state":"pending",
  "processing_state":"grading_pending",
  "received_at":"2026-10-10T12:00:00Z",
  "aggregate_revision":3,
  "canonical_event_ids":[],
  "status_url":"/api/v1/receipts/rec_368b7658-6b8a-497e-b5d0-b013d7b2d68d"
}
```

Errors use `application/problem+json` with `type`, `title`, HTTP `status`, stable `code`, `detail`, `request_id`, retryable boolean, safe context (`aggregate_id`, expected/actual revision), optional known `retry_after_at`. Never return SQL/file paths/secrets/source instructions/private keys. Endpoint errors are transport/guard failures, not learner failures.

| HTTP | Stable codes / required behavior |
|---|---|
| 400 | `MALFORMED_JSON`, `INVALID_CURSOR`; cannot create attempt outcome |
| 401 | `LOCAL_SESSION_REQUIRED`, `LOCAL_SESSION_EXPIRED`; provider failure is separate job state |
| 403 | `ORIGIN_FORBIDDEN`, `CSRF_INVALID`, `DELIVERY_NOT_RELEASED`, `ASSET_FORBIDDEN` |
| 404 | `COURSE_NOT_FOUND`, `SESSION_NOT_FOUND`, `ITEM_NOT_FOUND`, `RECEIPT_NOT_FOUND`; never fallback to another course |
| 409 | `IDEMPOTENCY_CONFLICT`, `ATTEMPT_ALREADY_SUBMITTED`, `INVALID_TRANSITION`, `PINNED_VERSION_MISMATCH`, `PUBLICATION_CONFLICT`, `VARIANT_POOL_EXHAUSTED`, `VALIDITY_HOLD`, `CANONICAL_WRITE_CONFLICT` |
| 410 | `EVENT_CURSOR_EXPIRED`, `RETIRED_ROUTE`; retain historical evidence, return read-only/history recovery refs |
| 412 | `REVISION_MISMATCH`; body actual revision/refresh ref; no mutation |
| 413 | `UPLOAD_TOO_LARGE`, `RESPONSE_TOO_LARGE` |
| 415 | `UNSUPPORTED_MEDIA_TYPE` |
| 422 | `RESPONSE_SHAPE_INVALID`, `NUMERIC_FORMAT_INVALID`, `UNSUPPORTED_MODEL_EFFORT`, `BLUEPRINT_INVALID` |
| 428 | `EXPECTED_REVISION_REQUIRED`, `IDEMPOTENCY_KEY_REQUIRED` |
| 429 | Local bounded request throttle only with measured Retry-After; provider quota recorded as waiting job, received answers remain 202 |
| 503 | `STORAGE_BUSY`, `OWNER_BRIDGE_UNAVAILABLE`, `SERVICE_STOPPING`; do not ACK durable answer before commit; already received receipt stays available |

SSE events have monotonic SQLite `seq` as `id`, `event` enum (`job_state_changed`, `step_completed`, `receipt_committed`, `assessment_updated`, `publication_changed`, `projection_updated`, `provider_state_changed`, `service_state_changed`) and JSON `data {schema_version:1,event_id,seq,occurred_at,aggregate_kind,aggregate_id,course_key?,payload}`. Insert event in the same transaction as its operational state change. Safe payload contains measured counts/status/refs, not generated narration as a tool fact. Client can read details through authorized GET.

Client sends `Last-Event-ID` on reconnect (or first-fetch `after` cursor); server validates integer cursor and scope, replays all later persisted events in order, then streams. Client deduplicates by event ID/seq and reconciles aggregate GET after gaps. Heartbeat comment every 15 seconds; reconnect exponential backoff 1,2,4,8,16,30 seconds with jitter, max 30. Stream close is not job cancellation. Retain event transport history for 30 days; before compaction preserve current aggregate snapshot and earliest available seq. Expired cursor gets HTTP 410 before stream with `EVENT_CURSOR_EXPIRED`, snapshot URLs and current cursor; client refreshes and reconnects. Operational SSE compaction never deletes canonical evidence/receipts. New publication events may update catalogue, but frontend queues content-update notice until active lesson finishes; pinned session remains unchanged.

## 11. Required implementation verification and handoff artifacts

Use `apps/learning_hub/tests/unit/` for pure state/scoring/selection, `contracts/` for schemas/OpenAPI/key exclusion, `integration/` for real temp SQLite/filesystem/owner journal, and `e2e/` for learner flow. Tests use deterministic fake provider transport and fictional isolated vaults. Software tests do not establish academic correctness; source/curriculum reviewers remain required for content publication.

| Test destination | Required assertions |
|---|---|
| `unit/test_identity_versions.py` | Same objective ID in two courses never collides; Unicode collision blocked; tuple incomplete/null ingest unready; compatibility exact; history never regraded |
| `unit/test_grading.py` | Numeric inclusive tolerance/zero/negative/scientific decimal/units/percent convention/intentional blank/parser rejection; MC exact set/choice permutations; matching malformed vs wrong; Decimal threshold boundaries; essential unmet at 95%; 85% passed/attention; number grants no derivation credit |
| `unit/test_state_machines.py` | Every allowed transition and rejected skip; no result without response; pending cannot pass/fail; correction/retry preserves original; completed with pending grading separate |
| `unit/test_selection_exposure.py` | Retention pre-recap; shuffled item excluded; possible display excluded; worked/hint lineage exclusion; 23h59 vs 24h/DST UTC interval; unknown access/conditions not independent; family coverage/essential rules; exhausted pool queues repair and permits new study |
| `contracts/test_public_schemas.py` | Public projection has no target/key/rubric/feedback/unseen bank; errors/SSE/build/source maps no keys; private asset traversal forbidden; strict response discriminators; generated TS matches OpenAPI |
| `contracts/test_canonical_extension.py` | Schema-3/schema-4 union, boundary metadata resolution, new v4 marker and migration gate; schema-3/legacy exact prefix; unknown unchanged statuses; extension envelope validates; old events immutable; malformed components/score/receipt fail; old and extended recall fixtures agree on qualified core outcomes; no schedule from activity/site score |
| `integration/test_submission_crash.py` | Every crash cut in §6; concurrent duplicate POST → one response/outbox/event; same key/new body 409; lost ACK same receipt; canonical commit/SQLite crash reconciles; pending response still recoverable; no feedback before verified original result |
| `integration/test_records_bridge.py` | Expected-hash conflict preserved; owner write scope; stable tx recovery; active lock not stolen; non-cooperating edit detected; historical receipt verifies against retained event/journal while current log changed; per-objective duplicate components cannot manufacture distinct acquisition |
| `integration/test_publication.py` | Atomic old/new pointer; stale snapshot fence rejected; material invalidity hold; pinned old session survives compatible refresh; pending/new source revision cannot publish; unreviewed/unintegrated/pending journal rejected; unreferenced directory never treated published |
| `integration/test_migrations_restore.py` | Clean and each prior-version upgrade; rollback crash; checksum mismatch/unknown newer version blocked; foreign-key/integrity checks; restore pending receipt and canonical commit reconciliation; no history/exposure loss |
| `integration/test_auth_events.py` | Wrong Host/Origin/CSRF/bootstrap reuse blocked; cookie reload; OAuth not served; loopback only; SSE replay duplicates/gap/410; stream closure leaves worker running; no sensitive content |
| `integration/test_assessment_review.py` | Received written answer survives quota/restart; malformed AI result stays pending/unscorable; unknown alternative plan issue; weekly feedback waits final submission; blank and unknown distinct; 50/50 points/Week1/checked exceptions; per-course reviews no cap/block |
| `e2e/learning_resume.spec.ts` | Prompt→answer→prepared feedback→correction→reload; original preserved; section progression not manual completion; frozen old bundle/new catalogue; pending grading continues navigation; review retrieval before recap; no new-study lock; browser closure vs explicit service stop |

H00 hands off model/identity fixtures and error enums. H02 hands off migration files/schema diagram, repository protocols and restore evidence. H03 hands off request/response fixtures, canonical-extension validator/review results, crash-test matrix and receipt journal. H11/H12 hand off golden scoring/selection fixtures and rubric/retention invariants. H07–H10 hand off bundle validation report, academic owner transaction/reviewer/Git references and publication recovery tests. H15 verifies the final combined interfaces independently. H16 integrates only validated heads and reconciles any interface change across OpenAPI/TypeScript/migrations/canonical validators together.

Real-course enablement checklist: Plus supported sign-in and actual request proved; canonical site extension maintained and backward-compatible; matching current owner transactions verified; checked prepared site bundle and variants reviewed; no key leak; durable acceptance/recovery demonstrated; sole evidence authority and recall reader compatible; active snapshot/version preservation proven; scoped repository checks and protected integration passed. Failures hold the affected feature/scope with a concrete reason, not a fabricated Ready state.
