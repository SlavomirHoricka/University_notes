# Ingestion priorities, foundations, and independent review

- Status: ready_for_merge
- Objective: implement flexible topic prioritization, reliable reference checking, prerequisite reasoning, and rigorous independent helper review in the ingestion skill.
- Scope: canonical `03_Agents/ingest/SKILL.md`, generated Uni plugin package/version, private plugin release receipt, and this maintenance record. No course notes, raw materials, learner evidence, curriculum, or ingestion completion state changes.
- Branch: `codex/ingest-concept-priorities`
- Worktree: `/Users/slavomirhoricka/.codex/worktrees/ingest-concept-priorities/University_notes`
- Base: `cedae1399ee146242d01778bfafd6f3a903c3280`, freshly fetched `origin/main`.
- Prior context: [[03_Agents/LEARNING_ARCHITECTURE]], [[03_Agents/runtime/sessions/2026-10-09-repository-instructions]], and the existing ingestion index/pass records. The incomplete Week 2 ingestion remains separate and untouched.

## Decisions

- 80/20 guides emphasis, with no fixed proportions, scores, topic quotas, or performance promises. Full supplied-source coverage remains required.
- Course evidence establishes relevance; read academic references support verification, conceptual importance, and necessary foundations. Record consulted passages and access limitations; preserve disagreements.
- Ingest supplies a conceptual reading path and self-contained explanations. Plan retains ownership of executable lessons, objectives, assessments, sequence, and compatibility.
- Independent helpers assess accuracy/coverage, priorities, foundations/explanation, and simplification; report exact inspected scope and findings and recheck substantive repairs.
- Resolve ingestion paths against the actual selected checkout, replacing the legacy fixed vault path in the changed skill.
- Prepare version 0.3.1 for the existing private USER-scope plugin; preserve identity, audience, other skills, assets, and default prompts. Publishing and host activation are separately verified.

## Validation and review

- Baseline: `python3 03_Agents/check_vault.py` exited 1, checking 4,446 links. Existing findings: four missing concept links, two missing heading anchors, eleven course-mirror differences due to absent empty directories in fresh Git checkouts. No placeholder course records created.
- Independent reviewer: `/root/review_ingest_behavior`. Read the whole changed skill, repository instructions and ownership contract; exercised a synthetic eight-slide elasticity lecture, unspecified Mankiw edition, actually consulted OpenStax reference passages, a no-external-research request with an unsupported additional claim, and a full textbook supplied only as bounded supporting context. Produced a worked note excerpt and independently checked its arithmetic. Final initial result: no material findings. Non-runtime rehearsal only; no real course readiness or learner evidence certified.
- Clarified the reference-check sentence to expressly require routine online checking. The same reviewer rechecked the changed wording and affected source-trust, coverage, priority, prerequisite and reviewer context; confirmed no other source behavior changed and no material findings remain. Final canonical/generated skill SHA-256: `7bc0a98893334bcfa345d0605ca0d2a6b618685a86e228fbc9ab8a5cce8dfa15`.
- `quick_validate.py 03_Agents/ingest`: passed using PyYAML installed only under `/private/tmp/ingest-skill-validation-deps` because neither system nor bundled Python supplied it. No global dependency changes.
- `python3 03_Agents/scripts/sync_plugin.py --check`: passed, 21 generated source files, version 0.3.1. Verified manifest/interface preservation, all 25 archive entries against package bytes, and inventory SHA-256 values. `git diff --check`: passed.
- Final vault audit: identical existing issue identities/targets; valid maintenance-record links raised checked-link count from 4,446 to 4,448. Unrelated four missing concept links, two missing heading anchors and eleven absent empty course mirrors remain; no introduced findings.
- This is skill maintenance; academic source/curriculum transactions and raw-source/curriculum reviews are inapplicable because those artifacts remain unchanged. No scripts or record schemas changed, so maintenance code tests are unnecessary.

## Handoff

- Private release published through Plugin Creator with expected prior release `pluginrel_6ac246d6604c81918bc495ff5e7da99f`; confirmed new release `pluginrel_6ac9385a91b881919ae8106bc7f535e1`, version 0.3.1. All 25 files read back; preserved default prompts, assets, scope and audience. Receipt: `03_Agents/plugins/uni-teach-release.json`. Durable full release archive: `03_Agents/plugins/uni-teach-0.3.1.zip`.
- Host cache activation remains unverified; observed installed cache is 0.3.0. Do not edit generated installed caches. Refresh the plugin release in the host and start a new chat to load it.
- The standalone `~/.agents/skills/ingest` registration still targets the legacy vault at inspection time. After confirmed merge and primary synchronization, align only this existing registration with `/Users/slavomirhoricka/Desktop/University_notes/03_Agents/ingest`; preserve other registrations and original materials.
- Next: commit explicit task-owned paths, push/create the PR, record its actual URL, check the validated PR head/required checks, then merge. Verify actual remote merge and clean primary-checkout fast-forward before registration alignment and branch/worktree cleanup. Preserve the published receipt and archive if repository integration is blocked.
