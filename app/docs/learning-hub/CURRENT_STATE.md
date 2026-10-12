# Audited implementation checkpoint — 2026-10-12

This is a partial implementation, not a finished learning app. Health deliberately returns `ready: false`, `reason: scaffold_only`.

## Committed implementation

- H00: locked Python/FastAPI and React/TypeScript scaffold, loopback isolation, diagnostic and build/test tooling.
- H02: typed contracts, generated OpenAPI/TypeScript, SQLite migrations/storage and evidence-safety foundation. Previously accepted H02 repairs are included.
- H01 support: additive private provider-account/authorization/run-state storage and interfaces. This does not prove real subscription sign-in/inference.
- H04 partial: responsive course/materials UI, typed transport and safe error/unknown states. Real catalogue/auth/upload handlers remain unavailable; fictional fixtures exist only in tests.

Existing integration candidate: `0be10333b0139633ebdd443fe54ea667d109457c`. Includes foundation `da9ec0d`, frontend `659be37`, and reviewed H00/H02 history. A QA-owned repair updates the actual loopback smoke to the current heading and named service-status region without weakening the readiness assertion.

## Still required

H01 real provider integration/proof; H03 durable application/evidence services; H05 lesson player; H06 visuals; H07 uploads; H08 jobs; H09 owner bridge; H10 checked publication; H11 assessments; H12 reviews; H13 agent/settings controls; H14 launcher/backup/restore; H15 full QA; H16 real bounded pilot/release. These milestones remain incomplete. No actual learner evidence, academic readiness, OAuth completion or successful production upload is claimed.

Run the frontend/backend foreground commands in the implementation README to inspect today's shell. `make launch`/`make stop` still intentionally fail until H14. Course fixtures do not appear in production.

## Repository audit

- Foundation/frontend/review/provider committed branches are incorporated by ancestry in the reviewed integration candidate.
- Role branches with only the older main base have no implementation to merge.
- Technical-plan/contracts/workflows/reviewer plan branches are already integrated in main.
- Academic recovery `codex/uni-paths-week2-recovery` was squash-merged in PR #6 (`031ea76c4fbb052d70e841bb1f7684ec1c4e5c4f`). Its old branch must not be merged again over newer skills/course state.
- Provider worktree contains 14 untracked adapter/route/test files. They are unfinished and outside the reviewed candidate; preserved at `/Users/slavomirhoricka/.codex/worktrees/hub-provider/University_notes`. Future resumption requires a fresh scope/security review before acceptance.
- Original integration worktree's edited engineering session and untracked H01-support/H04 receipts are preserved in this checkpoint. Historical receipt blockers describe their original review state; this document and later audit receipts describe current acceptance.
- Original notes, materials, academic records, workflow registrations and existing worktrees are preserved. Six unrelated academic checker issues remain (four links, two anchors); fresh worktrees also lack eleven empty course mirrors.

## Review and validation

Independent `hub_reviewer` (native Astra/high) reviewed exact `0be1033`: 134 backend tests, Ruff, mypy and unchanged accepted migrations passed; only material finding was the stale smoke selectors. `hub_qa` (native Sol/high) repaired that test and passed one real Chromium/loopback smoke with `ready:false`. Runtime model-setting telemetry is unavailable beyond host role declarations.

No release readiness is inferred from the build or these checks. No paid API fallback or remote binding was enabled.

## Verified checkpoint integration and package scope

PR #9 merged on 2026-10-12 at `4272b77d3b9aa4080116b4ba022b82bd7864ba2f`; clean primary main was fast-forwarded. The next commit separates source under app/ without changing app runtime behavior. App workflow sources are a bounded legacy fork and are not enabled to read/write the parent vault. See ../../MIGRATION.md before continuing ownership/storage work. Historical task branch/absolute worktree paths in receipts are provenance, not live dispatch instructions.
