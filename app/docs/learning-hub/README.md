# Learning hub implementation package

Status: implementation in progress; see [CURRENT_STATE.md](CURRENT_STATE.md) for the audited partial checkpoint. This package complements the existing learning architecture and does not replace academic skill ownership or certify course readiness.

In a new chat in this repository, say **“Begin the implementation of the app plan.”** The root agent follows [START_HERE.md](START_HERE.md), resumes verified work and dispatches fixed-role subagents on their separate branches/worktrees. No new feature questionnaire is required. This planning request does not itself start application coding; a later explicit begin/resume request activates execution.

## Reading order

1. [START_HERE.md](START_HERE.md): orchestration, branches, waves and resume protocol.
2. [PRODUCT_SPEC.md](PRODUCT_SPEC.md): approved learner behavior, including all annotations.
3. [ARCHITECTURE.md](ARCHITECTURE.md): modules, owner boundaries and local process topology.
4. [CONTRACTS.md](CONTRACTS.md): schemas, storage, HTTP/events, scoring and persistence.
5. [WORKFLOWS.md](WORKFLOWS.md): sign-in, sources, durable jobs and checked publication.
6. [UI_IMPLEMENTATION.md](UI_IMPLEMENTATION.md): components and interaction/visual acceptance.
7. [TASKS.md](TASKS.md): concrete implementation tickets and verification.
8. [task_graph.json](task_graph.json): definitive dependencies, roles, models, effort and branches.
9. [VALIDATION.md](VALIDATION.md): structural checks and finished-app release matrix.

Profiles under `.codex/agents/hub_*.toml` are maintained project-local engineering roles, separate from generated `uni_*` runtime academic roles. Do not edit installed caches/global configuration or regenerate Uni packaging merely because this package exists. The [reference prototype](reference/personal_learning_hub_v3.html) is design input, not trusted executable backend logic.

Run `python3.11 docs/learning-hub/validate_plan.py` before dispatch and after package changes (Python 3.11+ is required for TOML validation). This validates the plan, not model entitlement, app behavior or academic accuracy.

Stage 1 delivers the contracts/evidence foundation, local shell, section player, maths/visuals/checkpoints, resume and prepared quiz UI. Stage 2 adds uploads/prior-week deltas, subscription provider, durable jobs, reviewed preparation, publication and Agents tab. Stage 3 completes assessment, mixed weekly tests, course-specific adaptive reviews and local release/restore verification.

The app is finished only when H00–H16 and the release matrix pass on an integrated commit, required reviews apply to that commit, a bounded real course pilot passes, and a manual launcher works. Static screens, mocked production AI or a successful build alone do not satisfy delivery. Genuine external blockers remain explicit.

Root AGENTS.md and host policy take precedence. The product spec fixes functionality; this graph fixes engineering dispatch; current canonical Uni skills fix academic ownership. Resolve conflicts through narrow documented contract changes and review. Never silently weaken checks or reinterpret historical evidence.
