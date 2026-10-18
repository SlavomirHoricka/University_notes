# University Assistant workspace

This folder contains four core learning skills, the optional HTML-course skill, course records, shared contracts and maintenance tools. Start with the task you want to perform; current course records establish readiness, while maps and old reports provide navigation.

Only `README.md` and `VAULT_MAP.md` are files at this folder’s top level. All five maintained skills are grouped in [skills/](skills/README.md); shared guidance is grouped in [docs/](docs/README.md).

## Start here

| Need | Document or folder |
| --- | --- |
| Browse all five maintained skills | [Skill index](skills/README.md) |
| Browse shared documentation | [Documentation index](docs/README.md) |
| Understand ownership, freshness, versions and handoffs | [[03_Agents/docs/LEARNING_ARCHITECTURE|Learning architecture]] |
| Find course notes, materials and records | [[03_Agents/VAULT_MAP|Vault map]] |
| Name a new note, hub or course folder | [[03_Agents/docs/NAMING_CONVENTIONS|Naming conventions]] |
| Inspect processed source scopes | [[03_Agents/runtime/ingest/ingestion_log|Ingestion index]] and linked pass records |
| Find runtime records and engineering handoffs | [Runtime guide](runtime/README.md) |
| Run maintenance and record checks | [Utility guide](scripts/README.md) |
| Understand generated files and release status | [Package guide](plugins/README.md) |
| Find previous audits and superseded releases | [History index](history/README.md) |

## Five skills

| Skill | Responsibility | Owned outputs |
| --- | --- | --- |
| [ingest](skills/ingest/SKILL.md) | Verify raw materials; create complete notes and visuals; independently check sources and coverage. | `01_Notes/` content; runtime ingestion index/passes; course `ingestion_state.json`. |
| [plan](skills/plan/SKILL.md) | Prepare executable lessons from finished notes, with independent curriculum review and version reconciliation. | Course plan, manifest, lessons and immutable curriculum history. |
| [teach](skills/teach/SKILL.md) | Deliver prepared lessons, assess actual answers and commit observed evidence/session state. | Course `learning_log.md`. |
| [recall](skills/recall/SKILL.md) | Derive due reviews from committed evidence; synchronize positively owned Todoist tasks. | Course `recall_state.json`; verified shared project map. |
| [html-course](skills/html-course/SKILL.md) | Optionally convert checked notes and ready lessons into English offline HTML with LaTeX, week navigation and interactions. | Versioned `02_Resources/HTML_Courses/<course_id>/` exports. |

`html-course` is the fifth skill, added in 0.6.0, alongside the four core study stages. Request it explicitly with `$uni-teach:html-course Build <full course identity>, <scope>`, or ask to ingest and build an HTML course. It requires checked notes and ready lessons; ordinary ingestion does not trigger it.

Use `$ingest` with an exact source folder or explicitly named existing-note repair passages; `$uni-teach:plan` with a full course identity and bounded scope; `$teach` or `$uni-teach:teach` with a topic and study budget; and `$uni-teach:recall` for committed course reviews. Ingestion normally hands off to planning; teach/recall require the matching committed readiness/version gates. Completing a reminder never creates learner evidence.

## Files and authority

Paths in this table are relative to `03_Agents/`.

| Location | Meaning |
| --- | --- |
| `skills/<skill>/` | Sole maintained skill bodies, templates, references and skill utilities. |
| `<year>/<semester>/<course>/` | Course identity matching materials/notes. Ingestion, curriculum, evidence and scheduling files have separate owners. |
| `agents/` | Maintained `uni_*` role TOMLs. `.codex/agents/` and packaged profiles are generated copies. |
| `docs/` | Architecture, naming, shared methodology/lesson/routing contracts and the plugin README source. |
| `scripts/` | Owner-enforcing record transactions, package synchronization and maintenance tests. |
| `runtime/` | Ingestion index/passes, recall project map and engineering sessions. |
| `plugins/` | Generated distribution, prepared package and receipt for the last confirmed publication. |
| `validation/` | Fictional curricula and contract rehearsals; never real learner evidence. |
| `history/`, `.backups/` | Preserved reviews, migration evidence, snapshots and superseded packages. |

[LEARNING_METHODS.md](docs/LEARNING_METHODS.md) explains the evidence and limits behind study defaults. [LESSON_CONTENT.md](docs/LESSON_CONTENT.md) defines complete-note reuse, self-contained lessons, verified supplements and bounded teaching additions. [MODEL_ROUTING.md](docs/MODEL_ROUTING.md) defines owner/helper/reviewer profiles and escalation. Canonical role defaults remain unchanged; the host selects actual agents/models and cannot be assumed to reload a new package automatically.

Standalone ingest/teach registration names remain `~/.agents/skills/ingest` and `~/.agents/skills/teach`; their targets must follow `03_Agents/skills/<name>/` after the primary checkout is synchronized. See the [migration notes](docs/README.md#standalone-registration-migration). Plan/recall/html-course use plugin registration. The selected checkout is the workflow root; installed caches and legacy vault paths are not maintenance destinations.

## Checks and current limitations

Run the [maintenance commands](scripts/README.md) before and after scoped changes. Preserve `.transactions/` journals and staged bytes: they establish committed record integrity and support recovery. Record verification is distinct from a Git commit and from independent academic review.

The [repository audit](history/2026-10-17-repository-audit/REPORT.md) preserves the cleanup baseline. All six note-reference findings were subsequently [repaired and independently source checked](history/2026-10-17-repository-audit/NOTE_REFERENCE_REPAIRS.md). The two Statistics correction states certify only their listed passages, not whole-note/course adoption. Fresh worktrees may still lack empty course mirrors. See actual ingestion passes and course bundles for coverage; neither a successful structural check nor a sample validation curriculum certifies readiness or learning.

Recall runs on request or after a qualifying committed teach handoff when available. It uses the separate Todoist connector and verified existing projects; this repository installs no watcher or periodic notification service.

The [workflow consistency audit](history/2026-10-18-workflow-consistency-audit/REPORT.md) records the current evidence-gate, append-only record, bounded-coverage and package-snapshot contracts.

The [workspace organization audit](history/2026-10-18-agents-folder-audit/REPORT.md) records the grouped skills/docs layout, navigation updates and primary-registration migration limits.
