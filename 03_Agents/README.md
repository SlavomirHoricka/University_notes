# University Assistant workspace

Canonical master plugin document: [[03_Agents/LEARNING_ARCHITECTURE|University Assistant architecture]] — current skill ownership, checked handoffs, and the proposed PC-only localhost learning hub. The hub and learning-site skill are architectural goals, not implemented components. Paths below are relative to this folder. Academic notes/raw materials and real learner history remain in place.

| Category | Maintained / runtime path | Meaning |
|---|---|---|
| Skill source | `ingest/`, `plan/`, `teach/`, `recall/` | Sole maintained instruction/template/skill utility copies |
| Shared instructions | `LEARNING_ARCHITECTURE.md`, `VAULT_MAP.md`, `NAMING_CONVENTIONS.md` | Ownership, navigation, naming |
| Methodology / maintenance utilities | `references/LEARNING_METHODS.md`, `scripts/` | Evidence/limits, safe writes, packaging checks |
| Ingestion records | `runtime/ingest/ingestion_log.md`, `runtime/ingest/logs/` | ingest-owned index and completion passes |
| Per-course records | `<year>/<semester>/<course>/` | Mirrors notes; created only when genuine workflow needs them |
| Curriculum | course `learning_plan.md`, `source_manifest.md`, `lessons/`, `curriculum_history/` | plan-owned, versioned definitions |
| Learning evidence | course `learning_log.md` | teach-owned, observed responses/session state |
| Review state | course `recall_state.json`, `runtime/recall/project_map.json` | recall-owned schedules/outbox/task IDs and verified factual project mappings |
| Ingestion freshness | course `ingestion_state.json` | ingest-owned completion/revision gate |
| Generated plugin | `plugins/uni-teach/` | Copies generated from canonical sources; never edit directly |
| Release receipt | `plugins/uni-teach-release.json` | Confirmed private backend release and separate host status |
| Validation | `validation/` | Demonstration/rehearsal only, not learner history |
| Historical records | `history/` | Reviews, migrations, snapshots/release ZIPs, baseline/final checks |

Existing standalone registrations `~/.agents/skills/ingest` and `~/.agents/skills/teach` still resolve here. Plan/recall use plugin registration. Model choice is made by the user/host; skills cannot switch models. Use a capable model for ingest/plan and a faster model for prepared teaching/recall.

Invoke:

- `$ingest 00_Materials/<year>/<semester>/<course>/<scope>`: inspect source, create/check notes, record completion; use exact folder.
- `$uni-teach:plan Prepare a learning plan for <full course path>, <topic/scope>`: finished ingestion required; creates executable lesson blocks, no learner outcomes.
- `$teach Teach/resume/review <full course path>, <topic>; I have <budget>` (or `$uni-teach:teach`): execute prepared curriculum, record actual responses; missing/stale curriculum returns to plan.
- `$uni-teach:recall Synchronize my committed course reviews with Todoist`: consume evidence, derive due dates and synchronize uniquely matched existing projects. No qualifying evidence means no task. Ambiguous projects require explicit mapping.

Teach invokes recall after committing qualifying results when available. This creates no watcher/background service. Run recall again after evidence or schedule changes; already synchronized tasks appear on Todoist due dates. No push notification or periodic automation was configured.

Maintenance: `python3 03_Agents/check_vault.py`; `python3 -m unittest discover -s 03_Agents/scripts -p 'test_*.py'`; recall tests are listed in its skill. Build `python3 03_Agents/scripts/sync_plugin.py`, verify `--check`, then use the guarded existing private account update workflow. Editing a cache is not a release. Legacy course records require ingest adoption/plan reconciliation before schema-3 readiness; installation does not fabricate that work.

Migration map and audit results: [[03_Agents/history/2026-10-03-audit/MIGRATION]] and [[03_Agents/history/2026-10-03-audit/REPORT]]. Historical top-level review/report filenames remain navigation redirects, not maintained instructions. Older immutable maintenance backups remain under `03_Agents/.backups/`; they are excluded from live skill discovery and target indexing.
