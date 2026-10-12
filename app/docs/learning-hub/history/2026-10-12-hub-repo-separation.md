# App audit and repository separation

Status: ready_for_merge

## Scope and checkout

Human request: audit the repository, merge safe existing app work, then make a copyable standalone app folder before creating another repository. Localhost-only; preserve notes, learner evidence, existing workflow registrations, credentials and unfinished work. No provider inference or paid API fallback authorized.

Checkout: /Users/slavomirhoricka/.codex/worktrees/hub-repo-separation/University_notes
Branch: codex/hub-repo-separation
Base: 0be10333b0139633ebdd443fe54ea667d109457c (existing integration candidate); origin/main initially 2d7a8215aa7e08bfc5155f4ad9fa133c2e6e97c0.

## Findings and decisions

Independent hub_reviewer (native gpt-6-astra/high) audited exact 0be1033, H00/H02 acceptance, additive provider state and H04 UI. Only material issue: stale H00 Playwright heading/status locators; hub_qa owns repair. 134 backend tests, Ruff, mypy and original migration checks passed independently. Candidate is a partial engineering checkpoint, not a usable app release.

Independent dependency audit (hub_workflows, native gpt-6.1-sol/high) found current executable app largely independent; vault coupling is in future adapters and canonical workflows. Preserve original notes and 03_Agents paths because personal ingest/teach registrations point there. Move engineering code/docs/roles into app/ and include an explicitly bounded workflow-source fork. No real sources, learner records or runtime secrets go in the copyable app.

Existing integration session and H01-support/H04 receipts copied byte-for-byte from their originating worktree for preservation. Provider adapter has 14 untracked files in hub-provider worktree; not reviewed/accepted or imported into production. All existing worktrees remain untouched.

## Checks and next step

Primary vault baseline: four missing links and two missing anchors, unrelated to this task. Fresh-checkout missing empty course mirrors are additional known baseline artifacts. Compare exact identities before/after; do not modify notes to quiet checks.

Next: QA smoke repair, complete checkpoint checks/review, merge checkpoint, then package and independently verify separation in a temporary standalone checkout. PR references and final results added at milestones.

Checkpoint checks: locked install; Ruff/format; mypy (72 sources); 10 unit + 76 contract + 48 integration Python cases; 24 frontend cases; ESLint/typecheck; schema drift; backend wheel/sdist and Vite build; diagnostic all passed. QA real Chromium/loopback smoke passed (one case). Plan validator passed using installed Python3.12 (system Python lacks tomllib); canonical package check passed. Vault before/after byte-identical. Final exact-commit recheck requested next.

## Checkpoint integration gate

Checkpoint status: ready_for_merge. Independent Astra/high reviewer rechecked e80d135; no material findings, original smoke issue resolved. App bytes unchanged after tests/review; additional commit records only review metadata and PR handoff. Checkpoint PR: https://github.com/SlavomirHoricka/University_notes/pull/9. Verified CLEAN with no required status checks/reviews at inspection. Separation remains in_progress and follows checkpoint integration.

## Package separation phase

Verified PR #9 merged at 4272b77d3b9aa4080116b4ba022b82bd7864ba2f; primary main fast-forwarded cleanly. Second branch: codex/hub-app-package, based on that merged checkpoint, same dedicated worktree. Engineering paths/history moved to app/; curated canonical workflow sources and generated package copied as an explicitly maintained fork. Academic notes/materials/records and original canonical workflow sources remain byte-identical. Copied academic dispatch blocked until explicit runtime data-root bridge; no new repository or global registrations changed. Separation status: ready_for_merge.

## Standalone verification

Export rehearsal: /private/tmp/hub-standalone-audit-20261012, 265 source files plus unchanged hash manifest. Separate local Git repository, no remote or copied notes/Git history. Fresh locked Python/frontend dependencies installed there. All 122 moved implementation files byte-identical to checkpoint; original canonical skills, academic sources/notes/records untouched.

Plan validator and 9 plan tests; 18 model-routing/record/vault-utility tests without skips on Python3.12; 35 schedule self-tests; 14 export defense/re-export tests; original and copied sync_plugin --check all pass. Export tests verify unsafe paths, symlinks, hash tamper, refusal to overwrite, excluded unlisted secrets and export-to-export without Git.

Original vault issue identities exactly unchanged after restoring navigation stubs for moved engineering sessions. Checked link count falls only because full engineering history moved outside the vault scan. No academic repairs made.

Standalone app QA results and independent separation review recorded next. Future migration step is creating a new repository from app export and revising app-native data/owner contracts; current scope does not move/import course content or enable copied legacy workflows.

Standalone hub_qa (native Sol/high) passed 134 backend cases, 24 UI cases and one actual Chromium/loopback smoke; static/schema checks, wheel/sdist, Vite build and diagnostic pass. Initial sandbox denied port bind; permitted escalated retry passed. No services retained. The source package is independently runnable/buildable as today's incomplete shell; copied workflows remain gated. A hash inventory preserves the identity/location of 14 excluded unfinished provider files for later transfer. No notes, evidence or secrets were added.

## Final separation integration gate

Status: ready_for_merge. PR: https://github.com/SlavomirHoricka/University_notes/pull/10. Independent Astra/high reviewer inspected caeca6f against4272b77, including full source/manifest/workflow closure and14WIP hashes: no material findings. Final additional changes only record this review/PR handoff and refresh manifest; no application/tool source changes. No release claim. Primary synchronization and task-only cleanup follow actual confirmed merge, not a predicted result. Existing role branches/worktrees and provider WIP must remain. Reproducible ignored dependencies/build/test outputs in this task worktree need no migration; standalone QA screenshots/logs remain in /private/tmp for inspection.
