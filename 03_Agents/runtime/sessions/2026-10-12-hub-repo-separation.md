# App audit and repository separation

Status: in_progress

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

Checkpoint status: ready_for_merge. Independent Astra/high reviewer rechecked e80d135; no material findings, original smoke issue resolved. App bytes unchanged after tests/review; additional commit records only review metadata and PR handoff. PR URL will be inserted before merge. Separation remains in_progress and follows checkpoint integration.
