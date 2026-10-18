# Maintained skills

All five canonical skills live here. Each folder contains its `SKILL.md` and any owned templates, references, scripts or assets. Edit these sources, then use the [packaging guide](../plugins/README.md) to regenerate distribution copies.

| Skill | Purpose | Invocation |
| --- | --- | --- |
| [ingest](ingest/SKILL.md) | Verify an exact source scope and produce checked notes. | `$ingest <source folder>` |
| [plan](plan/SKILL.md) | Prepare executable lessons from checked notes. | `$uni-teach:plan <course identity>, <scope>` |
| [teach](teach/SKILL.md) | Teach prepared lessons and record actual responses. | `$teach <course identity>, <topic>, <budget>` |
| [recall](recall/SKILL.md) | Schedule committed evidence-based reviews and synchronize owned Todoist tasks. | `$uni-teach:recall <course identity>` |
| [html-course](html-course/SKILL.md) | Build English offline HTML from checked notes and ready lessons. | `$uni-teach:html-course Build <course identity>, <scope>` |

Ingest → plan → teach → recall are the four core stages. Added in 0.6.0, html-course is an optional fifth skill invoked explicitly; it owns only derived HTML exports and creates no learner evidence.

Shared contracts live in [docs/](../docs/README.md). Course state stays under `03_Agents/<year>/<semester>/<course>/`; runtime logs stay under `03_Agents/runtime/`. Generated packages and archived snapshots are separate from these maintained sources.
