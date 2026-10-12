# Agent execution entry point

## Trigger

When the human asks to begin/resume implementation of this app plan, execute the package to a working app instead of producing another outline. Equivalent natural-language wording uses this entry point. Reading the package alone never starts work. Only ask for information required by a concrete gate, such as supported sign-in; continue unaffected tasks. Runtime background jobs belong to the finished app, not this document, and do not imply an agent chat keeps running after it ends.

Read root AGENTS.md and MIGRATION.md, package README, PRODUCT_SPEC, ARCHITECTURE, task graph and assigned task cards. Verify actual checkout, branch/status, remotes, worktrees, attached artifacts and overlapping tasks. Resume from actual commits/journals and the existing implementation session, never a verbal Done claim.

## Fixed engineering roles

| Profile | Model | Effort | Branch | Tasks |
|---|---|---|---|---|
| hub_coordinator | gpt-6.1-sol | high | codex/hub-integration | orchestration,H16 |
| hub_foundation | gpt-6.1-sol | high | codex/hub-foundation | H00,H02,H03 |
| hub_provider | gpt-6.1-sol | high | codex/hub-provider | H01 |
| hub_frontend | gpt-6.1-sol | high | codex/hub-frontend | H04,H05,H13 |
| hub_visuals | gpt-6.1-sol | high | codex/hub-visuals | H06 |
| hub_workflows | gpt-6.1-sol | high | codex/hub-workflows | H07,H08,H09,H10 |
| hub_assessment | gpt-6.1-sol | high | codex/hub-assessment | H11,H12 |
| hub_operations | gpt-6.1-sol | high | codex/hub-operations | H14 |
| hub_qa | gpt-6.1-sol | high | codex/hub-qa | H15 |
| hub_reviewer | gpt-6-astra | high | codex/hub-review | independent read-only review |

Engineering code is interdependent and persistence/security-sensitive; use Sol/high for bounded implementation and Astra/high for independent review. Reserve xhigh for an explicitly assigned difficult finding, not routine work. Runtime Uni owner/draft/checker/assessor settings remain distinct and are defined by canonical MODEL_ROUTING and WORKFLOWS. Deterministic operations use code. Do not downgrade a required reviewer or switch billing to evade quota.

Profiles do not prove host activation. Validate actual model/effort/capability access at dispatch. Prefer native role selection; otherwise spawn with BOTH model and effort, `fork_turns: none`, its full profile instructions and a bounded assignment. Record requested and host-confirmed settings separately. Never silently inherit a different parent model. If required routing is unavailable, report the exact blocker.

## Start/resume procedure

1. Fetch origin/main; run the plan validator. Inspect existing role branches, integration state and current journals. Preserve unrelated changes.
2. The user-facing root is relay, Git integrator and accountable completion owner. If its running settings differ, delegate one `hub_coordinator` at Sol/high to manage dependency/verification reasoning; root executes dispatch/Git from verified results. Never recursively create competing coordinators. A coordinator can request dispatch from root rather than create an uncontrolled nested tree.
3. Use a dedicated managed worktree for `codex/hub-integration`. Its provisioned branch contains the technical package. Merge newer main without rewriting published history; record absolute root/base. Never reuse another task's worktree.
4. Root owns one session at `docs/learning-hub/history/YYYY-MM-DD-hub-implementation.md`; resume it when interrupted. Record task state, role/settings, branch/worktree, input/output SHAs, checks, review, blocker and next step. Optional `docs/learning-hub/runs/` receipts are engineering state, never learner evidence.
5. Use one branch/worktree per role. Before dependent tasks, merge the accepted integration commit into the role branch. Record that SHA. Never copy files manually or cherry-pick only part of a dependency. Prerequisites must be present and accepted.
6. Dispatch only ready DAG tasks and nonoverlapping owned paths. This host has four slots total: root plus three children. A separate coordinator consumes one child slot, leaving two workers. Queue other roles; profile count is not concurrency. Avoid nested uncontrolled spawning.
7. Worker commits only assigned paths after checks/diff review, returns a completion receipt and stops. Worker does not push/merge/open PRs. Root validates and normally merges accepted commits into integration, preserving role history. Push validated refs through normal permissions; never force-push.
8. Run fresh read-only `hub_reviewer` against the exact integrated SHA at stage boundaries and final release. Reviewer reports concrete locations/reproduction, no fixes. Owners repair; reviewer rechecks final bytes and context. Root stores the review receipt. Advance the review branch with normal merges so inspected candidates remain recoverable.
9. Material prerequisite changes invalidate affected downstream acceptance/review receipts. Rerun affected tasks/checks; a previously passing count is not sufficient.
10. Publish through a protected PR to main. Record ready_for_merge/known PR, verify required checks and exact validated head, merge normally, verify actual remote-main evidence, fast-forward clean primary. Retain requested role branches; archive only merged task worktrees after preserving needed ignored/runtime artifacts.

The human's begin request authorizes required implementation and normal integration within this scope. External sign-in and unavailable host capabilities remain real gates. Do not ask routine permission for already-authorized reversible implementation steps. Do not silently start extra services at login, buy credits, expose the server remotely, or synchronize external Todoist tasks.

## Waves (JSON DAG remains definitive)

- H00 scaffold first, then H02 contracts; H01 subscription/API proof consumes the accepted H02 auth-flow migrations.
- After H02, H01 subscription proof runs alongside H03 durable evidence and H04 UI shell; H07 uploads on independent paths. H08 jobs also needs H01/H03.
- H05 player after H03/H04; H06 visuals after H05. H09 owner bridge after H02/H03/H08; H10 checked pipeline/publication after H07/H09.
- H11 assessments after H03/H05/H09; H12 reviews after H10/H11. H13 Agents UI after H04/H08/H10.
- H14 operations after H01/H03/H08; H15 full QA after all functional tickets; H16 reviewed real pilot and release after H15.

Raw-source ingestion is not scaffold work. H16 pilot uses actual owner skills plus distinct source/curriculum reviewers in an isolated course task; engineering review does not certify academics.

## Assignment and return contracts

Each assignment includes role/profile+model+effort; task IDs; absolute selected root and exact branch; verified input SHA/dependencies; package/task-card paths; owned/forbidden paths; checks/acceptance cases; relevant records; trust boundaries; commit/no-push authority; failure/escalation protocol. Tell workers they are not alone and must preserve other changes.

```json
{
  "task_id": "H03", "role": "hub_foundation",
  "requested_model": "gpt-6.1-sol", "requested_effort": "high",
  "actual_settings_evidence": "host receipt or explicit unknown",
  "input_integration_sha": "<verified SHA>", "branch": "codex/hub-foundation",
  "worktree": "<absolute root>", "commit": "<output SHA>",
  "changed_paths": [], "checks": [{"command": "...", "exit_code": 0}],
  "acceptance_cases": [], "blockers": [], "next_step": "..."
}
```

Blocked work preserves intent/artifacts with a concrete next step. A mock provider or fictional fixture is acceptable in tests, never as a substitute for successful real production integration. Workers may propose a narrow contract adjustment; root approves compatibility and review before dependencies consume it.

## Branch lifecycle

The plan task provisions every named branch locally/remotely from the integrated package. `branch_provisioning.json` specifies names/base policy; verify actual refs before use rather than trusting a document. If absent, recreate from current verified package-containing main. Never overwrite an existing different task branch. Resume attached worktrees when appropriate; if ownership/unrelated changes conflict, isolate a successor branch and record provenance. No automatic stash/reset/clean or published rebases.

Keep working through the graph until release passes or a precise external blocker prevents progress. Final delivery identifies launcher, release/app commit, test and academic pilot scope, remaining limitations, PR/merge/main-sync evidence and retained role branches. Committed instructions/configuration alone never mean the app is finished.
