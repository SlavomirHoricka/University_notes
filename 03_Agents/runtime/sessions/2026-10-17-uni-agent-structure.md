# University Assistant agent-role structure

- Status: ready_for_merge
- Objective: apply the approved six-section structure to all 14 canonical agent-role TOML files, strictly preserving instructions and configuration.
- Branch: codex/uni-agent-structure
- Worktree: /Users/slavomirhoricka/.codex/worktrees/uni-agent-structure/University_notes
- Base: freshly fetched origin/main, 4f88aeb5f66c2d77f91b2ae939b8145356b34a01.
- Prior work: 2026-10-17-uni-supporting-structure.md; private release 0.5.2 remains published separately.
- Scope: 03_Agents/agents/*.toml; regenerated .codex/agents/*.toml and packaged agents/*.toml; package inventory; this session record. No source notes, curricula, learner evidence or app profiles are in scope.
- Method: retain every original instruction sentence verbatim, regroup under six common headings, add comments/blank lines around unchanged TOML configuration and descriptive subheadings for complex roles. Preserve separate variants and existing sandbox declarations exactly.
- Baseline: sync_plugin.py --check passes for 37 sources at version 0.5.2. Vault checker baseline is /private/tmp/uni-agent-baseline.json; compare issue identities/targets after changes.
- Packaging boundary: regenerate loose distribution copies, preserve published 0.5.2 archive, manifests and release receipt byte-for-byte. No archive release, account upload or cache/global configuration update is requested.
- Validation planned: parsed TOML configuration equality; exact sentence inventory equality; paired-variant instruction equality; scoped diff review; model-routing/maintenance tests; generated parity; before/after vault issue comparison; git diff --check. No course transactions changed, so academic reviews/record verification are outside this maintenance task.

## Final validation and review

- All 14 TOMLs parse with bundled Python 3. Every configuration key/value, description and presence/absence of sandbox_mode matches the base exactly. All 228 original instruction sentences remain verbatim with original multiplicity. Five paired variants retain identical instruction bodies.
- Primary agent reviewed all final role families against their original instructions: author/checker separation, source-first checking, finished-note-only curriculum scope, item contracts before generated prompts, assessor wait before result commit, result persistence before feedback, delivery acknowledgements, lock release and interrupted transaction IDs remain intact. No semantic findings remain. This is a formatting-maintenance review, not an academic source/curriculum review or independent GitHub approval.
- All 22 maintenance tests pass without skips using bundled Python, including model-routing and packaging collision/parity tests. sync_plugin.py --check passes for all 37 sources. All 42 canonical/project/package role files agree. Only the 14 role hashes change in package_inventory.json. git diff --check passes.
- Vault checker remains exit 1 with exactly the same issue identities/targets: four missing note links, two missing anchors, four session redirects to removed app paths, eleven absent empty course mirrors. No introduced issues. Reports and sentence-preservation tooling remain in /private/tmp/uni-agent-* and /private/tmp/format_uni_roles.py.
- Published archive remains byte-identical: 0.5.2 SHA256 ad6dc0dc73902aab9282bcd2e4c48845a37067ca8e3b8292b824bd867c94510b. Loose source/generated copies contain this new unreleased formatting; the published archive is intentionally the prior release snapshot. Manifests and release receipt are unchanged. No native host reload or private upload was performed.
- Remote main refetched before integration and still equals base 4f88aeb5f66c2d77f91b2ae939b8145356b34a01. Next: commit scoped paths, push/open PR, record ready_for_merge with its URL, confirm validated head and gates, merge normally, verify remote main, synchronize clean primary and remove only this task branch/worktree.

## Integration handoff

- PR: https://github.com/SlavomirHoricka/University_notes/pull/16, targeting main.
- Implementation commit: ea1a3fb. This handoff changes only the session record; all final validated role/configuration/package bytes are unchanged.
- Ready for merge after confirming the final pushed PR head, current remote base and required CI/review gates. Merge using a normal allowed method, verify actual merged state and remote-main ancestry, fast-forward primary only if clean/on main, then delete this task branch and archive/remove its clean worktree.

## Updated-main integration and final gates

- Main advanced through unrelated repository-navigation PR15 to 82833a50c3e4d06cf8676373aea0a6f8faa0a359 before integration. Merged it into this published branch without rewriting history; package inventory merged automatically and was inspected/validated. No role files changed upstream or during this integration.
- Revalidation: 24 maintenance tests pass without skips; generated parity passes for all 37 sources at upstream package version 0.5.3; all 228 sentences/configuration values still match current main; all 14 role bodies remain byte-identical to validated implementation ea1a3fb; git diff --check passes. The only task changes relative to updated main are 42 role files, their 14 inventory hashes and this session record.
- Updated checker baseline is the committed final report from PR15. Issue identities/targets match it exactly: four missing note links, two anchors and eleven absent empty mirrors. PR15 removed the four dead support redirects; this task introduces no issue.
- Preserve both upstream ZIP snapshots (published 0.5.2 and repository-cleanup 0.5.3), manifests and receipt byte-for-byte relative to updated main. This formatting task updates loose canonical/generated role sources only; neither existing ZIP contains the new role formatting. A future release needs a new version/archive before publication. No synchronizer regeneration was run after integrating upstream metadata.
- Status remains ready_for_merge for PR16. Require final pushed head/gates before merging; then verify actual integration, synchronize the clean primary and clean only this task branch/worktree.
