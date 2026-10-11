# Executable implementation tickets

The task graph is definitive for dependencies and dispatch. Each ticket is performed by its fixed role on its separate branch. Models/effort below are coding settings; runtime course preparation uses the distinct canonical Uni profiles. Steps and acceptance are requirements, not completed work. Read detailed interface algorithms in CONTRACTS/WORKFLOWS and UI behavior in UI_IMPLEMENTATION.

Foundation H00 creates `make -C apps/learning_hub` targets `check-unit`, `check-contracts`, `check-integration`, `check-ui`, `check-e2e`, `check-all`, `build`, `export-contracts`, `launch`, `stop`. Run applicable targets on each feature; no placeholder target that succeeds without checks. Owners add tests in their owned feature directories; root serializes shared migrations/composition edits. H09's canonical patch is a separately reviewed parent assignment, not an unrestricted source-write allowance.

Staged evidence acceptance: H02 compatibility acceptance uses proposed contracts/isolated migration fixtures, with no maintained schema change. H03 completes against a typed fault-injected EvidenceWriter fixture; production canonical writes remain disabled. H09 implements the separately assigned maintained schema/readers/production bridge and reruns the H03 crash/idempotency suite against real records tools in an isolated vault. No H02/H03 fixture receipt claims live support. This sequencing avoids an implicit H03→H09→H03 completion cycle.

## H00 — Scaffold and locked quality tooling

Role `hub_foundation`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-foundation`. Requires: none. External gate: none.

Procedure:

1. Read package; record supported runtime/dependency versions. Create Python package with backend package-dir and React/TS frontend; lock dependencies and document baseline. No production fake content.
2. Create composition entry point and health route, typed Clock/IDs and test transports, feature namespaces, temporary-vault fixtures and private/runtime ignore rules scoped to app.
3. Create Makefile targets check-unit, check-contracts, check-integration, check-ui, check-e2e, check-all, build, export-contracts, launch and stop; targets must invoke real tools and propagate failure.
4. Establish Ruff, one static Python type checker, pytest, ESLint/TS strict, component tests and Playwright. Cross-language API types generated, not hand-copied.
5. Produce initial development README and install diagnostic. Shared scaffold edit ownership transfers explicitly to later role owners.

Deliverables:

- `apps/learning_hub/pyproject.toml`
- `apps/learning_hub/Makefile`
- `apps/learning_hub/frontend/package.json`
- `apps/learning_hub/backend/learning_hub/application/core/bootstrap.py`

Acceptance:

- H00-A1: Fresh checkout install/build works with documented locked dependencies.
- H00-A2: Health serves loopback and no course/learner records are fabricated.
- H00-A3: Deliberately failing check exits nonzero; no catch-all disabled tests.
- H00-A4: App runtime secrets/database/temp outputs are ignored without ignoring canonical journals.

Checks: all initialized quality targets and build. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H01 — Prove supported Plus sign-in and provider adapter

Role `hub_provider`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-provider`. Requires: H00. External gate: user_sign_in_and_account_eligibility.

Procedure:

1. Implement ProviderClient against supported SIWC registration/sign-in. Validate state/nonce/PKCE, redirect origin and ID token/scopes. Persist opaque host/client IDs and credentials in protected local storage.
2. Implement length-bounded newline JSON-RPC stdio framing, initialize/initialized handshake, thread start/resume, turn start/cancel and terminal event mapping. Pin compatible app-server binary/version.
3. Implement account-specific model/effort access verification, redacted provider events, refresh/restart/resume and typed error taxonomy. Do not equate model catalog with access.
4. Perform one real subscribed inference with explicit model+effort after user sign-in. No browser cookie scraping, backend-api routes, API key fallback or purchased credits.
5. Return supported/unsupported capabilities to core and worker. Store receipt without tokens; pause unavailable eligibility rather than retry endlessly.
6. Implement typed in-site provider auth-flow start/status/model choices/sign-out API and registered loopback callback; local offline auth remains separate. Use exact CONTRACTS seams and never log OAuth secrets.

Deliverables:

- `apps/learning_hub/backend/learning_hub/adapters/codex/`
- `apps/learning_hub/backend/learning_hub/api/provider/`

Acceptance:

- H01-A1: Mock OAuth wrong state/nonce/redirect/expired token rejected; secrets absent from UI/logs.
- H01-A2: Real terminal completed request proves selected subscription access; revoked login remains blocked.
- H01-A3: Interrupted/failed turn never marked successful; fragmented RPC/events handled.
- H01-A4: Auth refresh resumes correct thread without duplicating a logical task.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H02 — Typed contracts and compatibility gate

Role `hub_foundation`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-foundation`. Requires: H00. External gate: none.

Procedure:

1. Implement CONTRACTS canonical models (strict/discriminated unions, ID/version types, allowed states) and public/private serialization.
2. Create SQLite migrations/constraints, repository protocols and generated OpenAPI/TypeScript types. Add proposed web bundle/evidence extension schemas only after compatibility review.
3. Write exact migration proposal for current records contract: legacy prefix preservation, schema3 immutable event acceptance, appended web facts, owner fields/validation. Root assigns canonical patches in H09. This ticket accepts only proposed contract/migration fixtures; maintained reader/writer support is H09, not an implicit H02 prerequisite.
4. Generate controlled illustrative synthetic bundles/questions and contract fixtures. No ingestion readiness or learner outcome inferred from fixtures.
5. Freeze API version v1/schema revision; root reviews exported interface before dependent tasks merge it.
6. Include operational weekly assessment drafts, immutable approval proposals/decisions and provider auth flows in the normative migrations/contracts; enforce revision/selected-item/human-decision constraints.

Deliverables:

- `apps/learning_hub/backend/learning_hub/domain/models/`
- `apps/learning_hub/backend/learning_hub/adapters/storage/migrations/`
- `apps/learning_hub/frontend/src/api/generated/`

Acceptance:

- H02-A1: Unknown fields/invalid version tuple/dangling question IDs rejected.
- H02-A2: Private keys and retention items excluded from learner payload snapshot tests.
- H02-A3: Proposed migration/union-reader fixtures preserve byte-identical legacy/schema3 events; no live canonical extension claimed.
- H02-A4: Generated TS matches OpenAPI; migration empty/upgrade/conflict tests pass.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H03 — Durable receipts, owner evidence and projections

Role `hub_foundation`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-foundation`. Requires: H02. External gate: none.

Procedure:

1. Implement receipt command boundary and request hash uniqueness, actual timestamps, pending outbox and response replay. Server creates attempt/item/version identity.
2. Checkpoint prepared prompt through teach owner before delivery; store display acknowledgement separately. Actual raw answer persisted before AI dispatch.
3. Implement typed EvidenceWriter port and a fault-injected fixture owner; verify outbox acknowledgement and projections in isolated tests. H09 supplies the production maintained-reader/writer adapter and reruns these cases before live sessions.
4. Handle crash cuts before/after canonical commit and DB acknowledgement with stable event/transaction IDs and recovery inspection. Preserve unsaved pending intent.
5. Expose catalog/session/resume/readiness and receipt endpoints with legal transitions. Completion derives from received process facts; result pending/absent is not fail/pass.
6. Implement authenticated idempotent bookmark PATCH as navigation-only state, with pinned-anchor/aggregate revision checks; no completion/exposure evidence.

Deliverables:

- `apps/learning_hub/backend/learning_hub/adapters/evidence/`
- `apps/learning_hub/backend/learning_hub/application/core/`
- `apps/learning_hub/backend/learning_hub/api/lessons/`

Acceptance:

- H03-A1: Repeated same key/body replays; different body returns conflict.
- H03-A2: Fault-injected fixture owner replay after canonical commit yields no duplicate; uncertain journal blocks projection. H09 must repeat against actual compatible records tools.
- H03-A3: 85%-style status projection never rewrites objective acquisition evidence.
- H03-A4: Refresh/second tab/version conflict preserves exact attempt and learner response.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H04 — Typed UI shell, courses/weeks and upload surface

Role `hub_frontend`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-frontend`. Requires: H02. External gate: none.

Procedure:

1. Port design reference into modular shared tokens/layout/semantic components and generated API client.
2. Implement routes, full identity catalog, week/lesson lists, truthful readiness/completion/attention badges and empty/pending/error states.
3. Replace localStorage course/lesson counters; expose no manual completion UI/mutation.
4. Build course/week upload picker/dropzone and per-file states using contract fake transport until H07 is integrated; mocks only in development/tests.
5. Implement responsive navigation and provider/health status view, preserve keyboard/focus and error retry behavior.

Deliverables:

- `apps/learning_hub/frontend/src/app/`
- `apps/learning_hub/frontend/src/features/courses/`
- `apps/learning_hub/frontend/src/styles/`

Acceptance:

- H04-A1: All published weeks accessible without score locks.
- H04-A2: Partial coverage denominator is explicit; missing evidence shows unknown.
- H04-A3: Desktop/narrow/empty/error screenshots inspected; no demo statistics.
- H04-A4: Upload saved state is distinguishable from ingested/published state.

Checks: check-ui, focused component/integration tests and build; applicable contract tests. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H05 — Section lesson player, maths and deterministic checkpoint UI

Role `hub_frontend`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-frontend`. Requires: H03,H04. External gate: none.

Procedure:

1. Implement structured section renderer and pinned lesson sessions; navigation/heading IDs come from bundle contract.
2. Implement active outline IntersectionObserver with reduced-motion behavior and accessible scroll/focus handling.
3. Render sanitized prose, maths, source assets, worked steps and generic visuals. Validate supported math and no arbitrary HTML.
4. Implement numeric/matching/choice question inputs, receipt lifecycle, prepared feedback/correction flow, assistance and resume bookmark.
5. Implement separate prepared quiz/test/review UI states; final assessment/selection services from H11/H12 integrate through unchanged contracts.
6. Build weekly editable saved-draft and atomic-submit UI from typed API, including unsaved/conflict states; quiz feedback is per committed item, weekly feedback after whole-test freeze. H15 later tests real backend integration.

Deliverables:

- `apps/learning_hub/frontend/src/features/lessons/`
- `apps/learning_hub/frontend/src/components/math/`
- `apps/learning_hub/frontend/src/components/questions/`

Acceptance:

- H05-A1: Scrolling/navigation alone never verifies completion.
- H05-A2: Wrong/correct feedback displayed after persisted response and repeat submits are idempotent.
- H05-A3: New publication mid-session cannot swap key/content; reload resumes outstanding item.
- H05-A4: Long maths/headings/reduced motion/keyboard matching supported.

Checks: check-ui, focused component/integration tests and build; applicable contract tests. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H06 — Validated interactive visual component library

Role `hub_visuals`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-visuals`. Requires: H05. External gate: none.

Procedure:

1. Implement versioned safe visual registry and typed configurations for timeline, relationship/payoff plots, scenario table, derivation reveal and annotations.
2. Use controlled numeric functions; declare units/domains/assumptions/reference cases. Never eval arbitrary generated expressions/scripts.
3. Coordinate required model/schema additions through foundation; align public rendering and backend publication validators.
4. Provide keyboard controls, semantic text/table alternatives and bounded parameter input.
5. Prepare synthetic reference fixtures with checked numerical cases; actual course instances await academic review.

Deliverables:

- `apps/learning_hub/frontend/src/components/visuals/`
- `apps/learning_hub/backend/learning_hub/domain/visuals/`

Acceptance:

- H06-A1: Invalid parameter/domain/formula config is rejected, not rendered as credible content.
- H06-A2: Reference cases below/at/above strike and bond domain examples pass when supported.
- H06-A3: Interactions do not fabricate mastery; accessibility alternatives work.
- H06-A4: No component introduces a new course topic without finished-note support.

Checks: check-ui, focused component/integration tests and build; applicable contract tests. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H07 — Uploads, stable source revisions and previous-week delta inventory

Role `hub_workflows`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-workflows`. Requires: H02. External gate: none.

Procedure:

1. Persist staged bytes durably, inspect actual media type/size, sanitize path and assign stable source ID/course/week; preserve immutable revisions.
2. Implement managed-source and primary 00_Materials same-course scans on upload/startup plus debounced watcher; hash bytes/record relevant dependencies.
3. Handle duplicate/replacement/rename/deletion explicitly; never delete notes/evidence due to file removal.
4. Coalesce batches into source snapshot, mark affected dependency scope and create durable requested job using H08 repository port.
5. Implement local extraction/render/OCR adapter inventory with page/slide locator and failure coverage. Preserve figures/tables/maths.

Deliverables:

- `apps/learning_hub/backend/learning_hub/application/uploads/`
- `apps/learning_hub/backend/learning_hub/adapters/extraction/`
- `apps/learning_hub/backend/learning_hub/api/workflows/`

Acceptance:

- H07-A1: Identical upload triggers no extra AI step; earlier-week bytes change is detected.
- H07-A2: Traversal/symlink/type mismatch/oversize rejected; original revisions preserved.
- H07-A3: Unreadable page remains unresolved; partial extraction cannot certify coverage.
- H07-A4: Rename-only delta preserves identity and missing-file conflict does not delete learner records.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H08 — Durable worker, quota recovery and serialized course reservations

Role `hub_workflows`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-workflows`. Requires: H01,H03. External gate: none.

Procedure:

1. Implement job/step transition graph, atomic leases/fencing, heartbeats, expired worker recovery and input/output fingerprinted checkpoints.
2. Serialize course owner mutations across checkout roots with configured global coordinator reservation and existing local records lock; do not steal active locks.
3. Handle quota eligibility with reported reset time or bounded unknown-reset probes; distinguish auth/permanent/input/provider-transient errors.
4. Yield safely for pause/cancel and interactive grading priority, release course locks while waiting. Persist every next eligible run time.
5. Expose job reads/events/legal commands, retention-safe cleanup and dependency invalidation; no in-memory-only FastAPI background queue.

Deliverables:

- `apps/learning_hub/backend/learning_hub/worker/`
- `apps/learning_hub/backend/learning_hub/api/workflows/`

Acceptance:

- H08-A1: Browser closure does not stop worker and restart recovers exact eligible pending step.
- H08-A2: Crash/expired lease cannot allow stale worker publish or duplicate canonical write.
- H08-A3: Unknown reset is not assumed 5h; low-frequency probes do not rerun full job.
- H08-A4: Cancelled/paused/limit-wait job releases locks and preserves staged artifacts.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H09 — Canonical owner-contract support and bounded Uni runtime adapters

Role `hub_workflows`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-workflows`. Requires: H02,H03,H08. External gate: canonical_contract_independent_review.

Procedure:

1. Have root explicitly serialize and assign the canonical extension patch proposed by H02. Scope exact maintained records/templates/validators and generated package checks, no installed cache edits or private plugin release.
2. Implement strict SkillRunRequest/Result with selected absolute vault root, full course/source scope, transaction/review IDs, allowed owned tools and compatibility.
3. Dispatch existing Uni owners and separate reviewers with fixed model/effort and no competing writers; required source reviews use originals, curriculum reviews use checked notes.
4. Bridge deterministic web facts to teach logical ownership without LLM per checkpoint and without unsupported current schema fields; verify owner transaction.
5. Support plan/ingest repair and exhausted-item-bank handoffs, pending intent recovery and source approvals inside site. Return blockers honestly.
6. Re-run H03 durability/crash/idempotency acceptance against actual maintained compatible records tools in an isolated vault before enabling real session mutations; fixture receipts alone cannot open this gate.
7. Implement owner-required in-site approval proposals and explicit human decision bound to snapshot/scope/expected bytes/proposal digest; no source-text or Retry approval, new proposal invalidates old grant.

Deliverables:

- `apps/learning_hub/backend/learning_hub/adapters/vault/`
- `apps/learning_hub/backend/learning_hub/adapters/repository/`
- `canonical-extension patch explicitly assigned by root`

Acceptance:

- H09-A1: Legacy/schema3 fixture bytes/events unchanged through migration and replay.
- H09-A2: Tools cannot target another checkout, source text cannot expand permission, wrong owner rejected.
- H09-A3: No ready plan or completed ingestion if independent review absent/material findings remain.
- H09-A4: Grade/journal failure leaves answer pending; no fabricated source/learner evidence.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H10 — Checked ingestion/planning pipeline and atomic publication

Role `hub_workflows`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-workflows`. Requires: H07,H09. External gate: none.

Procedure:

1. Implement snapshot->ingest review->plan review->structural/transaction/Git gate->export->publish DAG with coverage matrix.
2. Prepare 25min sections, checkpoints/all-option feedback, sample-assessment-inspired keys/variants/visual specs via canonical plan owner.
3. Verify input revision and dependency fingerprints before each handoff; superseded job cannot publish against newer sources.
4. Stage public/private bundle/assets, validate schema/links/math/visuals/required content/versions, fsync then atomically publish pointer.
5. Freeze active sessions, preserve previous definitions/evidence and derive compatibility/delta routes. Queue noncritical notification until lesson end.

Deliverables:

- `apps/learning_hub/backend/learning_hub/application/ingestion/`
- `apps/learning_hub/backend/learning_hub/application/publication/`

Acceptance:

- H10-A1: Every required finished-note concept maps to taught/assessed objective or remains an explicit blocked gap.
- H10-A2: Fault between staging/pointer leaves complete old or new bundle, never mixed files.
- H10-A3: Unreviewed/stale/partial academic output or repository integration blocker cannot publish Ready.
- H10-A4: Changed criterion does not regrade old attempts or reset course progress.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H11 — Prepared quizzes, scoring and short-answer assessment

Role `hub_assessment`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-assessment`. Requires: H03,H05,H09. External gate: none.

Procedure:

1. Implement deterministic exact-choice/matching/numeric grading using prepared tolerances/units with Decimal-safe parsing.
2. Implement prepared quiz sessions and weekly blueprint50/50 points, current/historical scope rules, no repeated exposed independent questions.
3. Implement short-answer grader bounded to exact rubric/version and actual response; validate structured component result; escalate ambiguous supported cases to Sol/high runtime assessor.
4. Separate submitted/completed/graded/passed/attention/unscorable and essential criteria. <90 attention, >=80+essentials pass; existing acquisition rules remain separate.
5. Support immediate retry variants, delayed classification and feedback only after canonical result committed. Slow/limit-limited grade remains pending while other study continues.
6. Implement weekly draft GET/PATCH and atomic revision-manifest finalization into immutable child responses/outbox; drafts are operational and never graded/canonical before submit. Quiz existing-response finalization uses distinct mode and per-item feedback.

Deliverables:

- `apps/learning_hub/backend/learning_hub/domain/grading/`
- `apps/learning_hub/backend/learning_hub/application/assessments/`
- `apps/learning_hub/backend/learning_hub/api/assessments/`

Acceptance:

- H11-A1: 85%+essentials: pass+attention;95% with missing essential: no pass.
- H11-A2: Malformed/ambiguous AI score can't commit, invent new rubric or turn missing answer into fail.
- H11-A3: Numeric rounding/decimal-v-percent/tolerance cases explicitly tested.
- H11-A4: Weekly50/50 score weight and Week1 exception tested; original/assisted/retry results remain separate.
- H11-A5: Stale/double-tab weekly draft conflict aborts full finalization without partial evidence; restart restores drafts, exact final-submit replay returns same child receipts.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H12 — Exposure-aware course-specific review and recommendation adaptation

Role `hub_assessment`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-assessment`. Requires: H10,H11. External gate: none.

Procedure:

1. Implement selection from prechecked unseen banks using item and family relation/exposure metadata; option shuffle alone never fresh.
2. Implement recall-owned evidence replay/date/gates via existing deterministic policy, no AI arithmetic or invented acquisition.
3. Implement corrective refresh vs retention pre-recap routes, estimates based on included topics, no fixed duration cap and no score locks.
4. Derive per-course Needs attention queues and adaptive next-study recommendations without rewriting canonical requirements.
5. Trigger background plan bank extension when variants exhausted; incoming checked version reconciles exact compatibilities/reassessment.

Deliverables:

- `apps/learning_hub/backend/learning_hub/domain/selection/`
- `apps/learning_hub/backend/learning_hub/domain/review_policy/`
- `apps/learning_hub/backend/learning_hub/application/reviews/`

Acceptance:

- H12-A1: Review session never mixes courses; weak-topic reason/evidence visible.
- H12-A2: Fresh retrieval shown before recap; exposed/too-early/unknown-condition answer cannot become delayed retention.
- H12-A3: Unseen bank exhaustion queues checked preparation rather than repeats marked fresh.
- H12-A4: Recall updates derived only from committed results; retries/pending grades don't fabricate schedule evidence.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H13 — Agents UI and role/model controls

Role `hub_frontend`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-frontend`. Requires: H04,H08,H10. External gate: none.

Procedure:

1. Implement resumable job timeline/events, source/review/publication details and changed-lesson summaries.
2. Display requested/actual model+effort and known usage/reset separately, never guessed cost/ETA.
3. Implement legal pause/resume/cancel/retry and future-job role settings through backend; validate supported choices.
4. Use post-lesson information queue, no progress toasts while reading; credential/private-reasoning redaction.
5. Exercise restart/reconnect/cursor gap states against integrated worker, not mock-only production behavior.
6. Wire approval preview/Approve/Reject and provider Connect/Grant/Sign out into Agents/Settings; show exact proposed scope/revisions and no secret/cookie/terminal dependency.

Deliverables:

- `apps/learning_hub/frontend/src/features/agents/`

Acceptance:

- H13-A1: SSE duplicate/gap handled via event dedup/resnapshot.
- H13-A2: Unknown usage shown unknown, reviews not falsely labelled approved.
- H13-A3: Changing role config cannot alter running attempt/key/rubric or disable required academic checks.
- H13-A4: Browser lesson uninterrupted by routine publication jobs.

Checks: check-ui, focused component/integration tests and build; applicable contract tests. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H14 — Manual launcher, supervision, diagnostics and backup/restore

Role `hub_operations`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-operations`. Requires: H01,H03,H08. External gate: none.

Procedure:

1. Implement installed local CLI and double-click launcher, single-instance lock/health discovery, detached supervisor and explicit stop.
2. Bind only loopback, enforce allowed origin/local mutation session, keep secrets in protected store and runtime outside Git.
3. Implement graceful shutdown, child cleanup, quota/sleep/restart recovery, log rotation and redacted diagnostic output.
4. Implement consistent operational DB+canonical records/bundles backup with manifest and restore into isolated directory; verify pending intents/version links.
5. Write setup/start/stop/update/troubleshooting/restore runbooks; no login autostart or machine waking.

Deliverables:

- `apps/learning_hub/backend/learning_hub/operations/`
- `apps/learning_hub/scripts/operations/`
- `apps/learning_hub/docs/operations/`

Acceptance:

- H14-A1: Manual launch->browser close->worker continues; explicit stop->launch resumes safely.
- H14-A2: Existing unrelated port process never killed and no wildcard origin exposure.
- H14-A3: Restore preserves attempts/history/pending outbox/private assets; invalid backup fails safely.
- H14-A4: Launcher usable by learner without opening terminal/Obsidian.

Checks: check-unit, check-contracts, feature check-integration; affected vault/records checks if canonical files change. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H15 — Integrated behavioral, security and recovery QA

Role `hub_qa`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-qa`. Requires: H06,H12,H13,H14. External gate: none.

Procedure:

1. Build end-to-end Playwright and fault matrices in VALIDATION against exact integrated SHA with fake provider/temporary isolated vault.
2. Test origin/path/auth/secret/answer-key boundaries, concurrent tabs/workers, upload versions, journal crashes and publication pointer cuts.
3. Verify all agreed learner flows and responsive/math/visual accessibility screenshots; route bugs to owners, do not patch their modules.
4. Run repository before/after issue identity comparison, records fixture suite, all app check/build targets and migrations/restore.
5. Produce redacted release evidence and unresolved issues; no claim academic fact check from engineering tests.
6. Test bookmark without false evidence, editable draft/restart/conflict/atomic freeze, per-item quiz versus whole-test feedback, approval proposal mutation/rejection and provider lifecycle from UI.

Deliverables:

- `apps/learning_hub/tests/e2e/`
- `apps/learning_hub/docs/validation/`

Acceptance:

- H15-A1: Every V01–V16 acceptance case mapped to actual result; material failures block release.
- H15-A2: Injected loss/duplication/version/quota cases pass without fake grades or lost evidence.
- H15-A3: Native displayed UI inspected with long/empty/pending/error scenarios.
- H15-A4: No production fixture authority, skipped critical checks or secret in bundle/log.

Checks: check-all, build, full V01–V16 ledger and required observed pilot/review evidence. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.

## H16 — Independent review, bounded real pilot and completed release

Role `hub_coordinator`, model `gpt-6.1-sol`, effort `high`, branch `codex/hub-integration`. Requires: H15. External gate: real_subscription_and_academic_pilot.

Procedure:

1. Have fresh hub_reviewer inspect exact candidate SHA, security/data/role/Git boundaries, task receipts and acceptance evidence. Repair/recheck all material findings.
2. Prove supported real account integration and one bounded permissioned real-course upload->independent source check->independent plan check->publication->lesson UI flow. Do not fabricate a learner answer to populate dashboard.
3. If learner assessment behavior needs real answers, use isolated fictional rehearsal tagged test-only; record pilot limits and validate real app response plumbing without inventing evidence.
4. Open/update protected PR, verify exact head/checks, record ready_for_merge, merge/read back remote main, sync clean primary and preserve role branches/needed artifacts.
5. Deliver working manual launcher, runbook and final scope/checks/limits/commit/merge refs. If external source/signin/review gate fails, preserve work and report blocker, not finished app.

Deliverables:

- `integrated app release`
- `apps/learning_hub/docs/validation/release.md`
- `03_Agents/runtime/sessions/<implementation-session>.md`

Acceptance:

- H16-A1: All prior task acceptance validated on exact integrated SHA and reviewed final content.
- H16-A2: Real source/curriculum reviewers report exact scope/final result; no inferred learner mastery.
- H16-A3: Launcher and complete upload-to-study flow work with verified subscription access.
- H16-A4: Actual PR merge/main sync/branch provenance confirmed.

Checks: check-all, build, full V01–V16 ledger and required observed pilot/review evidence. Include actual commands/exits, exact changed paths and input/output commit IDs in the receipt. No manual marking of an acceptance case without its stated evidence.
