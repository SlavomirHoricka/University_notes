# Master plugin architecture and future learning hub

- Status: in_progress
- Objective: establish the canonical University Assistant overview and document the proposed personal learning hub, using existing maintained contracts. Architecture/documentation only.
- Scope: `03_Agents/LEARNING_ARCHITECTURE.md`, `03_Agents/README.md`, root `README.md`, and this engineering record. No course notes, sources, curricula, learner evidence, ingestion records, skill bodies/templates/utilities, generated packages, registrations, releases or application code changed. Flashcards excluded.
- Primary repository inspected: `/Users/slavomirhoricka/Desktop/University_notes`, clean `main`.
- Branch: `codex/learning-hub-architecture`
- Worktree: `/Users/slavomirhoricka/.codex/worktrees/learning-hub-architecture/University_notes`
- Base: `a7b1149289d6cef310b373edba18cfaff6209986`, freshly fetched `origin/main`.
- Prior records: [[03_Agents/runtime/sessions/2026-10-09-repository-instructions]], [[03_Agents/runtime/sessions/2026-10-09-ingest-concept-priorities]], [[03_Agents/runtime/sessions/2026-10-09-uni-workflow-swimlanes]], and [[03_Agents/runtime/ingest/ingestion_log]] with all four linked passes. No existing unfinished architecture task found. The incomplete Week 2 ingestion is separate and untouched; its detail records FMI/Econometrics completion while Green Deal stays blocked.

## Decisions and inspected authority

- Extend [[03_Agents/LEARNING_ARCHITECTURE]] as the existing canonical owner of cross-skill boundaries/storage; do not create a competing overview. Preserve the operational contract and clearly label future goals as proposed, not implemented.
- Read actual root AGENTS.md, both READMEs, architecture, vault map/naming, all four maintained skill bodies and supporting templates, records utility and package synchronizer/manifest. Exactly four current skills; no learning-site skill exists.
- Describe exclusive owners, reads/writes, inputs/outputs, repair and review handoffs from maintained contracts. No workflow behavior or schema changes.
- Record PC-only localhost scope; independent content/progress/scheduling/presentation boundaries; proposed learning-site ownership of presentation/generated views only; no chosen framework, database, server, generator or deployment.
- No academic/curriculum work or source/criterion changes; independent source/curriculum reviewers and new owner-record transactions are inapplicable. Documentation review is performed by the author against maintained sources and actual metadata; no separate agent review claimed.

## Baseline and validation

- Baseline `python3 03_Agents/check_vault.py`: exit 1; 4,448 checked links; four pre-existing conceptual targets missing (`Descriptive_Statistics_Overview`, `Bernoulli_Distribution`, `Kolmogorov_Smirnov_Test`, `Standard_Error`), two pre-existing note anchors missing (Measures of Dispersion / Interquartile Range; Kolmogorov Axioms / Inclusion-Exclusion Principle), eleven absent empty agent course mirrors in a fresh checkout. No course records fabricated.
- Read-only `records.py status` for all five current course ingestion directories: unlocked/no pending journals. `records.py verify` passed for all five current ingestion states and each of the 36 indexed ready lesson bundle transactions (41 verification calls). Commitment integrity is distinct from current readiness: ECOX/FMI plans capture ingestion 1 versus current 2; Green Deal captures 1 versus blocked 2. Behavioral/Comparative capture matching revisions. No academic review or plan reconciliation performed.
- Baseline `python3 03_Agents/scripts/sync_plugin.py --check`: exit 1, package inventory mismatch. Inventory embeds the prior source checkout's absolute root. This task must leave generated packaging intact; extending its copied architecture will create an additional expected documentation mismatch, deferred to a later authorized packaging/release task. No skill/package update is claimed.
- Final author review compared the expanded matrices/handoffs to all four maintained skill bodies, root review gates, templates and current record metadata. Preserved existing operational sections; added the already-defined plan-to-recall handoff. Corrected one draft ordering sentence to describe completion requirements without prescribing a different ingestion finalization order. Proposed sections introduce no execution contract or technology selection.
- Final `check_vault.py`: exit 1 with identical baseline issue identities/targets; new documentation links resolve. No introduced findings. Final checked-link count will be recorded after this session update.
- Final `sync_plugin.py --check`: exit 1 with expected `LEARNING_ARCHITECTURE.md` difference plus the baseline absolute-root inventory mismatch. Generated copies/releases remain untouched per user scope. A later authorized packaging task may synchronize the documentation copy; current distribution is not claimed updated.
- `git diff --check`: passed. Changed-path review: only master document, two READMEs and this session record. Academic content/records, skill behavior, generated packaging and code are unchanged. No implementation tests needed. Mermaid diagrams were manually checked for node/edge syntax and ownership consistency; native rendering was not verified.

## Handoff

Current status: documentation drafted; review the final diff, compare vault issue identities/targets to baseline, verify documentation links and unchanged protected paths, then follow the authorized Git/PR integration gates. No implementation follows from this task.
