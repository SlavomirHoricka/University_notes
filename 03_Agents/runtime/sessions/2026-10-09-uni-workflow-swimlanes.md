# Editable Uni workflow swimlanes

- Status: in_progress
- Objective: visualize the current University Assistant architecture for brainstorming in an editable Excalidraw drawing; five swimlanes for learner, ingest, plan, teach and recall. Start with learner upload/add files, then request ingestion.
- Scope: new `Excalidraw/University_Assistant_Workflow_Swimlanes.excalidraw.md` and this task record. No course notes, curricula, learner evidence, scheduling records, skill behavior or plugin packaging changed. Existing drawings preserved.
- Branch: `codex/uni-workflow-swimlanes`
- Worktree: `/Users/slavomirhoricka/.codex/worktrees/9ab7/University_notes`
- Base: `9132663b49a26458b0edb0018a304db16bd5fd46`
- Authority: [[03_Agents/LEARNING_ARCHITECTURE]], the four canonical skill instructions, and root `AGENTS.md`. The existing `Excalidraw/Learning Workflow Architecture.md` is preserved as an earlier representation; current ownership contracts govern the new diagram.

## Decisions and validation

- Native rectangles, diamonds, ellipses, text and bound arrows remain individually editable. Shape legend distinguishes action, decision/gate, stored artifact and start/pause; arrow styles distinguish normal handoff, repair/retry and delayed-review/resume.
- Includes checked ingestion, independent source/curriculum review gates, freshness/version checks, learner responses, evidence commits, recall eligibility, synchronization holds, confirmed Todoist tasks and review return. Shared transaction and Git delivery contracts appear as supporting annotations.
- This is an architecture drawing, not an ingestion/planning run or a change to the learning workflow. No independent academic/curriculum reviewer or course records transaction is applicable.
- Parsed the Obsidian JSON drawing and portable scene; confirmed unique IDs, five lane backgrounds, valid element references and reciprocal text/arrow bindings, and contained node text.
- Restored and exported all 194 elements using the repository's bundled Obsidian Excalidraw 2.27.3 runtime in an isolated headless browser. No runtime errors. Visually inspected its native SVG/PNG output and corrected connector curvature and label placement.
- Baseline `python3 03_Agents/check_vault.py`: exit 1; four missing concept links, two missing heading anchors and eleven absent empty course mirrors. Final audit matches baseline issue identities and targets; the session record adds a valid checked architecture link. These are unrelated pre-existing findings; no placeholder course records created.
- `git diff --check`: passed. Source/package checks and academic transaction verification are inapplicable because their files are unchanged.
- Portable `.excalidraw` and native SVG/PNG previews are preserved outside the repository at `/Users/slavomirhoricka/.codex/visualizations/2026/10/09/01a121c7-b6a5-7300-b9c4-d1664d414b39/`; build/render helpers are temporary files, excluded from Git.

## Integration and handoff

Drawing validation is complete. Next: scoped staging/review, PR creation, record the known PR URL and ready state, merge after repository gates, verify remote merge, fast-forward primary checkout if clean, and clean up the task branch/worktree only when preserved artifacts permit it.
