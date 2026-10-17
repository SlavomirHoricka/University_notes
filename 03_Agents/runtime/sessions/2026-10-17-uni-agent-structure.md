# University Assistant agent-role structure

- Status: in_progress
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
