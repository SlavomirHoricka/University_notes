# App workflow source fork

These are the maintained Uni workflow sources copied from the reviewed notes repository checkpoint. They preserve the academic methods, roles, review gates, record utilities and packaging sources needed to adapt the standalone learning app. They are independent of the sibling vault; edits here do not update its skills or installed plugin.

Canonical sources in this app: ingest/, plan/, teach/, recall/, references/, scripts/, agents/ and LEARNING_ARCHITECTURE.md. Generated distribution: plugins/uni-teach/ plus ../.codex/agents/uni_*.toml. Verify with `python3 scripts/sync_plugin.py --check`; regenerate only after an authorized canonical change.

No real course state, ingestion passes, learner evidence or notes are included. Templates and tests contain synthetic/example data. [VAULT_MAP.md](VAULT_MAP.md) explains the absent runtime tree.

**Dispatch boundary:** read ../AGENTS.md and ../MIGRATION.md. Copied skill instructions still describe the original vault contract and must not be executed against the enclosing notes checkout. The app owner bridge and explicit runtime data-root selection must be implemented/reviewed before academic workflow writes. No filesystem compatibility requirement is introduced by retaining these sources.

LEARNING_ARCHITECTURE.md and NAMING_CONVENTIONS.md are preserved historical workflow contracts, not a promise that the future app uses Obsidian or mirrors its folders. Adaptation must retain source support, independent reviews and real learner evidence while making app-native persistence authoritative.
