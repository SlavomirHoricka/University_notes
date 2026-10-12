# Standalone learning app instructions

Scope: this app package and any clone/export of it. Explicit human instructions and host policy take precedence. Read README.md, MIGRATION.md and docs/learning-hub/CURRENT_STATE.md before work.

## Resolve the two roots

PACKAGE_ROOT is the absolute directory containing this AGENTS.md, apps/, docs/ and 03_Agents/. It is the app project root even when git rev-parse returns the enclosing notes repository. Resolve app source, plan, roles and checks from PACKAGE_ROOT. Git commands still use the actual enclosing checkout/worktree and preserve unrelated changes.

RUNTIME_DATA_ROOT is a separately configured app-owned data directory. It is not PACKAGE_ROOT, the parent notes repository, or a legacy hardcoded vault path. The runtime workflow bridge is not implemented yet. Do not run copied ingest/plan/teach/recall skills against the parent vault or infer a runtime data root from Git. Academic owner dispatch/writes are blocked until an explicit data-root contract and checked owner bridge exist; continue unaffected engineering work.

## Engineering ownership and gates

Use docs/learning-hub/START_HERE.md and task_graph.json for authorized implementation, fixed hub roles, dependencies and independent review. Historical plan assumptions about vault layout/backward Markdown compatibility are pending reconciliation under MIGRATION.md before H07-H10 implementation; do not silently implement them as current product requirements. Do not infer milestone completion from fixture tests.

In this package, 03_Agents/{ingest,plan,teach,recall}, references/, scripts/, agents/ and LEARNING_ARCHITECTURE.md are a maintained fork of workflow sources, currently a legacy checkpoint for adapting the app. Preserve source-grounding, independent academic reviews, safe writes, actual learner evidence and immutable history. Their vault-root/Obsidian instructions are historical and subordinate to this root's explicit dispatch block. Generated 03_Agents/plugins/uni-teach and .codex/agents/uni_*.toml are rebuilt by sync_plugin.py; never hand-edit generated copies or installed caches. Hub profiles are maintained directly.

Never read/write a sibling notes checkout as an implicit dependency, copy real sources or learner records into app source, fabricate course state, buy API credits, enable paid fallback, expose remote listeners, autostart services or synchronize external tasks without human authorization. Current scope is PC-only loopback with the subscription provider route still incomplete.

Use isolated task branches/worktrees for substantial changes, preserve other work, record app engineering sessions under docs/learning-hub/history/, stage explicit owned paths and follow normal PR protections. Independent hub_reviewer checks exact integration commits. No fabricated GitHub approvals. User-authorized completion includes ordinary commit/push/merge after gates, subject to host rules.

## Checks and export

See MIGRATION.md for locked app checks, plan/workflow-source checks and the hash-verified export command. Refresh MIGRATION_MANIFEST.json from reviewed Git-tracked source after package changes; do not add runtime data or secrets to its inventory. Runtime files, dependencies, caches and build output are excluded from exports. Tests use fictional temporary data only. check_vault.py is a legacy utility, not an app readiness check; never fabricate course mirrors to make it pass.
