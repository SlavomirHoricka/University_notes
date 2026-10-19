# Resource navigation cleanup

- Status: ready_for_merge
- Objective: simplify repository navigation by moving the editable Excalidraw folder under 02_Resources and updating current references/settings.
- Requested scope: .claudian, .codex/agents, .obsidian and Excalidraw. Retain application configuration at its existing discovery paths; no supported relocation has been established for Claudian. Official Codex documentation specifies .codex/agents for project profiles; Obsidian documents root configuration profiles and an app restart.
- Branch: codex/resource-navigation
- Worktree: /Users/slavomirhoricka/.codex/worktrees/e625/University_notes (clean checkout supplied to this task).
- Base: ee7f86fdb3973eb990bb8494ad72887408e149b8, freshly fetched origin/main.
- Prior work: 2026-10-18-agents-folder-audit; its generated role layout remains unchanged. No academic notes, curricula, learner evidence, workflow transactions, skill sources or package snapshots are in scope.
- Affected paths: Excalidraw → 02_Resources/Excalidraw; README.md; 03_Agents/VAULT_MAP.md; Excalidraw plugin data.json; this session record.
- Baseline: check_vault.py reports no broken links/anchors or metadata issues; nine absent empty course mirrors in this Git checkout, recorded in the comparison below. No pending workflow transactions affected.
- Validation planned: preserve diagram hashes, validate plugin JSON/path settings, compare exact before/after vault issue identities, review scoped diff and git diff --check.
- Primary checkout: unrelated workspace.json/DS_Store changes and untracked supplied source folders; synchronization must remain deferred while dirty.
- Validation: before/after check_vault.py compared by exact issue identities (8,314 links each): no broken links, anchors, malformed source links or source metadata findings; identical nine pre-existing absent empty course mirrors. Both editable diagram SHA-256 hashes match the baseline exactly. Architecture companion changes only its vault-relative drawing link. Plugin JSON parses and all five folder/path settings use 02_Resources/Excalidraw. Scoped self-review and git diff --check pass; academic reviews and workflow record verification are inapplicable to this navigation/settings-only change.
- Known limitations: no live Obsidian session was exercised; close/reopen Obsidian after the updated checkout is available so the plugin reloads its settings. Primary synchronization remains deferred while dirty.
- Sources: https://learn.chatgpt.com/docs/agent-configuration/subagents (project TOMLs); https://github.com/obsidianmd/obsidian-help/blob/master/en/Files%20and%20folders/Configuration%20folder.md (root config profiles).
- Next: commit, push, open a PR, record its URL and ready_for_merge, then verify normal merge and clean up this task branch.

## Pre-existing empty course mirrors

- `2024_2025/Summer_Semester/JEB104_Microeconomics_I`
- `2025_2026/Summer_Semester/JEB010_Makroekonomie_II`
- `2025_2026/Summer_Semester/JEB050_International_Finance`
- `2025_2026/Summer_Semester/JEB160_Auctions_and_Game_Theory`
- `2025_2026/Winter_Semester/JEB009_Makroekonomie_I`
- `2025_2026/Winter_Semester/JEB027_Finanční_Ekonomie`
- `2025_2026/Winter_Semester/JEB044_Financial_Accounting`
- `2025_2026/Winter_Semester/JEB108_Microeconomics_II`
- `2026_2027/Winter_Semester/JEM231_Mergers_and_Acquisitions`

## Integration handoff

- PR: https://github.com/SlavomirHoricka/University_notes/pull/23, targeting main. Implementation: 47cd452.
- Final content has passed scoped maintenance self-review; source/curriculum review does not apply.
- Next: confirm the PR head matches the committed validated tree and CI/review gates permit normal merging; verify actual remote merge, delete only this task branch and clean up this task worktree. Primary fast-forward remains deferred while its unrelated changes are present.
