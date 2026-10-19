# README HTML course link

- Status: ready_for_merge; user explicitly authorized public GitHub Pages publication and merging the README link on 2026-10-19.
- Objective: open the existing five-course HTML collection from a prominent link in the GitHub repository README. User clarified GitHub on their Mac; a local file link cannot provide that browser navigation.
- Branch: codex/html-course-pages.
- Worktree: /Users/slavomirhoricka/.codex/worktrees/readme-course-site/University_notes.
- Base: freshly fetched origin/main 9ccefbd.
- Prior delivery: [Weeks 1–3 session](2026-10-18-week3-ingest-html.md); reuse the durable launcher layout and existing reviewed exports without changing any course page or academic record.
- Scope: root README, shared HTML launcher, GitHub Pages deployment workflow and this session record. Deploy only 02_Resources/HTML_Courses; course content stays byte-identical. No raw-material or learner-record folders enter the deployed artifact.
- Target: https://SlavomirHoricka.github.io/University_notes/.
- Baseline: check_vault.py reports no broken links/anchors/metadata; the same nine absent empty course mirrors as the starting checkout. Pages API reports no existing Pages site; repository is already public.
- Required validation: compare vault issue identities before/after, verify launcher/course/lesson/asset targets with HTML base resolution, review scoped diff and diff-check. No ingestion/planning changes or corresponding academic-review gates apply.
- Next: merge PR #24 normally after verifying the final validated head, then verify deployment and live navigation; preserve primary-checkout changes during cleanup.

## Prepared validation

- All 4,742 local HTML href/src targets resolve with each page’s base URL; all 334 manifest-listed course files match their reviewed SHA-256 digests. Shared launcher uses the existing delivery’s visual identity and links to all five course indexes.
- Browser preview confirms hub → Behavioral Economics → first lesson navigation and visible content over HTTP.
- Final vault check: zero broken links/anchors/metadata issues, same nine pre-existing absent empty course mirrors; diff-check passes. No course, note, plan, learner or source files changed.
- GitHub Pages action versions and permissions match GitHub’s current official custom-workflow documentation. Deployment is main-only and uploads only the HTML_Courses directory.

- Reviewable PR: https://github.com/SlavomirHoricka/University_notes/pull/24. Initial validated commit: 313bde1. Hold merge and Pages activation until the user approves public hosting. Primary checkout remains dirty and behind; synchronization must be deferred. Preserve this worktree for continuation.

## Authorized publication

- User approval received: “Yes, publish the courses through GitHub Pages and merge the README link.” This supersedes the earlier publication hold.
- Pages API activation succeeded: public Actions-based site, HTTPS enforced, URL https://slavomirhoricka.github.io/University_notes/. No branch-source build is enabled.
- Fresh origin/main remains 9ccefbd; PR is clean/mergeable with no required CI or review requests reported. Final scoped diff-check passes; vault issue identities remain the same nine baseline empty mirrors only.
- PR https://github.com/SlavomirHoricka/University_notes/pull/24 is ready for normal merge, followed by actual deployment verification. No integration or deployment success is predicted in this record.
