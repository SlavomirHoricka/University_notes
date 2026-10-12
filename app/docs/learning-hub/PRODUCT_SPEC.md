# Personal learning hub — implementation plan

Version: 1.0 · 10 October 2026 · Status: user-approved product specification; application not implemented. Detailed engineering execution is defined by the adjacent technical package, task graph and START_HERE entry point.

This plan incorporates the decisions made in this conversation, including all eleven response annotations. It proposes application development in three stages. It does not change the vault, installed plugin, curriculum, learner records, model configuration, or Git workflow. The existing HTML prototype is the visual starting point.

## 1. Product goal and boundaries

The learner opens a local web application, selects a course and week, uploads materials, and studies the checked lessons produced from those materials. The application handles extraction, ingestion, note preparation, curriculum preparation, independent checks, publication, assessment, evidence recording, and review scheduling. Normal operation does not require opening Obsidian, a terminal, or a separate LLM chat.

The first release serves one learner on the same computer through localhost. Internet is necessary for AI work, but already published content and deterministic interactions remain usable when internet or AI access is unavailable, provided the local service is running. Responsive layouts and a transport-independent backend prepare for later phone/tablet access; remote access, hosting, accounts, and synchronization are a subsequent project.

The learner manually launches the application. A background service survives closing the browser and continues queued work. It resumes jobs after limits reset while the computer is awake and the service is running. Closing the browser, stopping the service, sleep, and shutdown are distinct actions. The application does not start at login, wake the computer, or work while it is shut down. After restart and manual launch, it recovers pending work.

Existing Plus usage is the preferred AI funding route. No paid API or purchased-credit fallback is activated automatically. A successful account integration is an early feasibility gate, not an assumed entitlement.

## 2. Agreed learner experience

### Courses, weeks, and lessons

- Preserve the full course identity: academic year, semester, actual course folder, and code where known. A display title is not a stable identifier.
- Select course and week before uploading. The same week can receive several upload batches or replacements.
- Divide each week into as many coherent lessons as necessary. Target approximately 25 minutes for teaching and checkpoints, excluding the separate quiz. Estimates are informative, not timers or completion requirements.
- Split each lesson into short sections. Within a section, use ordinary scrolling; Previous/Next controls move between sections. Backtracking remains available. A separate next-lesson action moves between lessons.
- Show week and course navigation, estimated time, lesson section outline, checkpoint progress, assessment state, and resume position.
- All published weeks and lessons remain accessible regardless of previous scores. Explain recommended prerequisites without making assessment failures lock future material.
- Explicitly optional source material remains labelled optional. Ingestion records why it is optional. Every required concept in finished notes must map to teaching and appropriate assessment; there must be no silent required-content omission during lesson splitting.

### Lesson presentation

Use semantic headings, readable paragraphs, selective bullet lists, worked examples, source figures, and rendered inline/display maths. Use a sticky side outline generated from section headings. Highlight the active heading while scrolling; clicking a heading scrolls to it. Keep the active outline entry visible. Honor reduced-motion settings and avoid fighting the learner's manual scrolling. On narrow screens, collapse the outline into a drawer without changing content or progress semantics.

Build visual aids from a maintained component library: annotated diagrams, revealable derivation steps, linked charts/tables, parameter sliders, payoff scenarios, and other components justified by the notes. Potential market-instrument examples include bond-price/yield relationships, duration sensitivity, cash-flow timelines, and derivative payoff graphs when supported by the uploaded scope. Do not add these subjects merely because a visual component exists.

Each visual specification declares its source-supported equation or relationship, assumptions, units, parameter bounds, labels, accessible description, and known reference cases. Interaction is implemented in ordinary reviewed application code. AI supplies validated content/configuration; it does not inject executable JavaScript into published pages. Static illustrations remain available where interaction adds little.

### Checkpoints and feedback

Lesson checkpoints use multiple choice, matching, final numerical answers, or predefined interaction tasks. No AI call is required to assess these answers. Numerical questions define units, rounding rules, absolute/relative tolerances, and acceptable representations before publication; do not silently interpret a percentage as a decimal.

Every option has prepared feedback. A correct answer explains why it is correct. An incorrect answer explains the relevant misconception and the correction. Distractors are plausible consequences of common mistakes, such as a sign error, confusing a gross/net return, using the wrong denominator, or confusing an adjacent concept. Avoid joke answers, obvious outliers, and superficial shuffling presented as a new exercise.

Commit the original attempt before displaying feedback. Allow correction and continued navigation; preserve the first result and assistance. After repeated ineffective attempts, show the prepared repair/example route rather than loop until a pass is manufactured. A corrected checkpoint can establish completion of the instructional process but does not establish an unaided pass or delayed retention.

### Quizzes and weekly tests

- Lesson quiz: approximately 5–10 minutes, separate from the 25-minute lesson. Feedback follows submitted answers. Include deterministic items and short written responses where appropriate.
- Weekly test: approximately 25–35 minutes, feedback after final submission. Approximately 50% of available points assess that week's material and 50% assess earlier weeks in the same course. Use points/objective coverage rather than blindly splitting question counts.
- Week 1 uses current-week material. If earlier checked material is insufficient, explicitly disclose and version the adjusted blueprint; never manufacture coverage. Accessible but unstudied earlier content remains identifiable as such.
- No enforced timer initially. Show an estimate and optional timer; recording elapsed time does not create a pass or completion event.
- All questions, expected answers, rubrics, feedback, and variants are prepared and checked before use. Source sample quizzes/exams inform format, difficulty, distractors, and assessed skills through ingestion-produced assessment-pattern metadata. Plan works from these checked notes/metadata rather than substituting direct raw-source work.
- Short written answers use AI at submission time against the prepared rubric. The assessor returns component decisions, supported score, and concise feedback. It must not invent new criteria, infer an answer, or reject a prepared valid alternative because of wording.
- Calculation input asks for the final value. Worked derivations can still be taught visually; a correct final number does not establish that the learner demonstrated a derivation. Use separate conceptual/interpretation questions for capabilities that a number alone cannot assess.
- Retries have no mandatory waiting period. Use prepared equivalent variants and preserve first-attempt, assisted, immediate-retry, and delayed results separately. Do not equate best-ever percentage with current retention.

### Completion, passing, and attention

Remove manual lesson/week completion controls from the UI and mutation interface.

Maintain distinct states:

| State | Meaning |
|---|---|
| Not started / in progress | Required instructional or assessment activity is outstanding |
| Instruction finished | Required sections/checkpoints and any prepared correction route were completed |
| Assessment pending | A submitted answer/test still requires processing; no pass/fail inferred |
| Completed | Required instructional process and assessment submission are finished; grading may still be pending |
| Passed | Finalized assessment is at least 80% overall and every essential objective meets its prepared criterion |
| Needs attention | A relevant finalized assessment is below 90%, an essential criterion is unmet, or a later review identifies weakness |
| Evidence stale / reassessment needed | A substantive content/criterion change requires new evidence under the published compatibility mapping |

Completion and passing can coexist with Needs attention. For example, 85% with essential criteria met means completed and passed, with attention needed. A high overall percentage cannot override an unmet essential criterion. Essential criteria are question/component-level prepared rules, not an automatic 90% rule for every essential objective. Existing objective acquisition and retention rules remain independently applicable; a site percentage does not silently override them.

A week is completed when its required lessons' processes and quizzes, plus its weekly test submission, are finished. Show grading pending separately. Optional material does not hold required completion open. Display course progress as completed required activities in the available published scope, with explicit coverage; do not suggest that a partial uploaded semester is a completed entire course.

### Review and retention

Reviews are always course-specific. The dashboard can show several course review cards, but one review session never mixes courses. Present prominent Needs attention cards, estimated duration, weak-topic reasons, and Start recommended review. Reviews never block new lessons. Recommend the duration justified by the topics; do not impose a 15/25-minute cap.

Use two explicit routes:

1. Corrective refresh: prepared targeted explanation/example → fresh immediate quiz → update the repair recommendation. This demonstrates learning after support, not delayed retention.
2. Retention check: fresh unseen retrieval/application questions before refresher content or hints → assessment → targeted refresh for identified weaknesses → separately classified follow-up practice.

Delayed retention questions must be unseen question variants, not previously exposed prompts with rearranged choices. They test the same objective with changed inputs/context/discrimination where appropriate. Preserve an exposure ledger including shown prompts, worked examples, hints, and solutions. A scheduled date alone does not establish a delay; use actual elapsed time and known conditions. The existing minimum-delay and independent-evidence rules apply. Unlimited practice is allowed, but exhausted unseen variants trigger background preparation and checking of additional variants; do not recycle exposed items as fresh retention evidence.

Performance adaptation changes the learner's recommended sequence and review routes. It does not silently rewrite canonical curricular requirements or historical evidence. If new instructional or assessment content is necessary, plan prepares a checked revision before use.

### Updates and notifications

Freeze an active lesson/assessment to its exact published bundle. Finish/resume it without silently swapping questions, keys, or criteria. New publication updates the catalogue and future sessions. Queue informational content-update notifications until the active lesson is finished; show them on the course dashboard if no lesson is active. Do not interrupt reading with routine toasts.

Preserve attempt events and previous definitions. Unchanged/explicitly compatible capabilities retain justified status. Changed objectives receive a prepared delta lesson or reassessment route. Do not automatically regrade past answers. If a substantive source error invalidates teaching, pause publication/new affected sessions and retain the active snapshot with a clearly recorded validity issue; do not award unsupported evidence merely to avoid an interruption.

## 3. Proposed technical architecture

Use a modular local application, not a single expanded HTML script and not a distributed microservice system.

| Layer | Proposed choice | Responsibility |
|---|---|---|
| Frontend | React + TypeScript + Vite | Course UI, section player, outline, questions, review queues, Agents tab |
| Maths | KaTeX with controlled supported syntax | Native-looking inline/display rendering; invalid formula is a publication error |
| Visual components | React + SVG; a plotting library only where useful | Maintained accessible interactive components driven by validated specifications |
| Backend | Python + FastAPI + Pydantic | Typed HTTP contracts, deterministic grading, owner adapters, publication, events |
| Local storage | SQLite with migrations | Jobs, pending intents, receipts, preferences, projections, and operational indexes |
| Academic storage | Existing vault files and owner transactions | Originals, checked notes, curricula, immutable history, learner evidence and recall authority |
| AI runtime | Locally managed Codex app-server adapter using supported ChatGPT plan sign-in | Role dispatch, streamed job events, model selection, authentication and recovery |
| Job worker | Separate supervised local process | Durable workflows, scheduling, retries, scans, and quota recovery after browser close |

Python aligns with existing records/extraction/scheduling utilities. TypeScript gives explicit frontend contracts. Generate frontend types from versioned backend schemas so the two languages do not maintain conflicting definitions. Pin dependencies and lockfiles after checking supported versions during implementation. These choices remain proposals until a small feasibility spike validates installation, authentication, and transport on this computer.

The browser talks to the application backend; it never receives OAuth secrets or writes vault files directly. Bind the initial service only to loopback. Restrict accepted origins and require a local session/CSRF boundary for mutations. Resolve uploaded paths within approved roots, reject traversal/symlink escape, inspect actual file types, and impose documented limits. Render sanitized content and approved components. Course source text and learner answers are untrusted data, never executable instructions or permission to run unrelated tools.

### Ownership and persistence

Keep the current authoritative ownership:

- Ingest: notes/assets, ingestion coverage and freshness.
- Plan: curricula, prepared lessons/keys/rubrics, compatibility and history.
- Teach: actual responses, assessment outcomes, assistance/exposure and session state.
- Recall: schedules and review state.
- Application: job state, UI preferences, operational receipts, and derived views.

SQLite does not become a second writable authority for mastery or curriculum. A pending answer outbox can durably store the received response before the teach transaction succeeds; it remains pending until the canonical write is verified. Projection tables are rebuildable from committed canonical records. Do not claim saved learning evidence from an SQLite job row alone.

Existing contracts do not yet define all site concepts, including week containers, deterministic service grading, rubric point scores, and presentation receipts. Define versioned extensions in canonical maintained contracts with explicit migration tests and backward compatibility before using them. Never stuff unsupported fields/events into current records or bypass the owner utilities. Deterministic grading executes in the teach-owned application service without an LLM call; teach retains logical ownership.

### Core entities and identifiers

| Entity | Essential fields/relationships |
|---|---|
| Course / week | Full stable identity, display metadata, week number, source associations and coverage |
| Source revision | Stable file identity, content hash, original name, course/week, revision, extraction status, page/slide locators |
| Published bundle | Schema version, ingestion/plan/source versions, exact objective/criterion versions, private and learner-facing artifacts, verified references |
| Lesson / section | Stable IDs, objectives, order, required status, estimate, note anchors, component specifications, required checkpoints |
| Question / variant | ID/version, role, family, prompt, response type, allowed conditions, objective mapping, points, private key/rubric and feedback |
| Attempt / exposure | Actual response, exact question/bundle, receipt time, outcome/components, assistance and displayed-content receipts |
| Session | Course, frozen bundle, active lesson/section/item, resume pointer, status |
| Review recommendation | Course, triggering evidence, objective/version, review route, estimated duration, due/gate status |
| Job / step | Stable ID, scope, dependency graph, checkpoint, requested/actual model and effort, attempts, next eligible run time, result/error |

Use opaque stable IDs for items and attempts, plus full version tuples. Do not infer identity from titles or item positions. Use offset-aware timestamps and Europe/Prague calendar handling. Persistence, publication, and Git commits are separate recorded boundaries.

### Submission and publication contracts

Expose versioned commands and reads such as course/week catalogue, frozen lesson session, checkpoint submission, quiz/test submission, current evidence view, per-course review queue, upload/replacement, job status, role settings, and job pause/retry. Every mutation has an idempotency key and expected version/session identity. The backend validates transitions rather than trusting a client-supplied completion flag or score.

Prompt delivery → response receipt → assessment result → feedback delivery are distinct facts. Persist before acknowledging durable acceptance. Lost acknowledgement or browser refresh must not duplicate an attempt. A malformed, interrupted, ambiguous, or quota-limited AI result stays pending/unscorable as appropriate; it never becomes an inferred failure or pass. Unknown alternative answers route to curriculum repair under the prepared assessment contract.

Public lesson/question payloads exclude unearned answer keys, rubrics that disclose solutions, and unseen retention questions. Return feedback only at the appropriate submission boundary. Local software cannot provide exam-grade protection against a determined device owner; this split avoids accidentally exposing solutions in normal use.

Stage a complete course bundle, validate it, then atomically change the publication pointer. A reader sees one verified bundle, never a mixture of old/new files. Preserve the last valid bundle and all evidence on failure. Explicitly mark stale affected objectives and prevent new unsupported assessment; unaffected verified content can continue. Validate links, assets, formulas, visual reference cases, question coverage, feedback completeness, unseen-variant availability, and exact workflow transactions before publication.

## 4. Upload-to-publication workflow

1. Persist the upload to controlled staging; validate file type, safe name/path, size, course/week assignment, and content hash. Keep originals and record provenance. Reuploads with identical bytes are no-ops.
2. On upload and application startup, scan the selected course's managed uploads and existing materials, including all previous weeks. Additional debounced filesystem watching while the service runs catches local changes without repeated full AI ingestion. Source-byte hashing belongs to the inventory/ingest adapter, not teach.
3. Detect additions, replacements, renames, and deletions. Use stable identity plus hashes; avoid unnecessary re-ingestion for metadata-only renames. Treat deletion as missing/archived source information requiring reconciliation, never authorization to delete notes/evidence.
4. Coalesce nearby uploads into a source snapshot and serialize authoritative writes per course across workers and worktrees. A later source change creates a newer run; a stale run cannot publish over it. Reconcile shared ingestion indexes on integration.
5. Extract native text and render pages/slides locally. Use local OCR/conversion where needed; record page/slide coverage and extraction failures. Extraction is not academic verification. Preserve figures, tables, maths, source ambiguities, and optional designations.
6. Ingest checks the entire changed authorized scope and dependencies, prepares finished notes/assets, and records blocked freshness before modifications. Separate reviewers inspect originals, coverage, and final notes. Repair findings and recheck final content.
7. Only verified completed ingestion is handed to plan. Plan builds the required-note → objective → lesson → checkpoint → quiz/test coverage matrix, 25-minute lesson groupings, keys/rubrics, visual specifications, corrective routes, and unseen retention variants.
8. An independent curriculum checker reviews finished-note support and executes every changed route, including essential criteria, distractors, numerical tolerances, visual cases, weekly blueprint and compatibility. Academic gaps return to ingest for repair and renewed source review.
9. Validate owner transactions and repository requirements; integrate task-owned academic work through the repository's branch/PR/check/merge gates. Automated operation does not bypass unavailable reviews, CI/protection, or unfinished transactions. Record integration-blocked status honestly.
10. Publish the checked integrated bundle atomically, reconcile projections and course-specific review routes, preserve active sessions/history, and queue a quiet post-lesson update notice.

Check earlier weeks by source difference and dependency impact. Do not regenerate every prior week after every upload. Re-review all materially changed outputs and dependent context; unchanged content retains its established provenance. Current complete records establish readiness, not a folder name or an old session summary.

## 5. Agent roles and subscription-aware execution

Initial defaults mirror the existing Uni routing policy. They are operational starting choices, not claims of benchmarked optimality. Verify account/model/effort access and a completed request before production use. Record requested and actual settings separately.

| Task | Default model and effort | Boundary / escalation |
|---|---|---|
| Inventory, hashing, native extraction, numeric scoring, date arithmetic | No LLM | Ordinary deterministic code and tests |
| Ingestion owner/synthesis | GPT-6.1 Sol, high | Single writer; bounded Astra high consultation for difficult derivations/conflicts |
| Bounded straightforward drafting | GPT-6 Luna, medium | Read-only drafts; owner integrates; increase only for a concrete difficult task |
| Independent source review | GPT-6 Astra, high | Fresh separate reviewer, original-source coverage; extra high only for specified difficult discrepancies |
| Curriculum preparation | GPT-6.1 Sol, high | Checked notes only; Astra high for mathematically demanding revisions |
| Independent curriculum review | GPT-6 Astra, high | Fresh reviewer; final routes/support/version review; extra high only when justified |
| Routine short-answer assessment | GPT-6 Luna, medium | Prepared rubric only; Sol high adjudication of a concrete difficult/ambiguous case |
| Recall coordination | GPT-6 Luna, low where needed | Pure replay/date arithmetic remains code; medium only for operational complexity |

Model/effort controls are available from the Agents tab and settings. Apply changes to future runs, not mid-attempt. Validate supported combinations, disclose changes from recommended defaults, and keep role separation and publication gates mandatory. Changing a model cannot change an academic rubric or authorize broader writes. Avoid automatic Max/Ultra/Fast/Ultrafast and uncontrolled spawning. The published default reviewer can wait for quota rather than silently downgrade quality.

Standard speed is the default. Reuse extraction and checked artifacts, bound context to relevant sources/records, batch coherent work, avoid reprocessing identical content, and reserve interactive capacity where possible. Prioritize received-answer grading over optional drafting at safe job boundaries. A locally chosen headroom threshold is advisory; do not invent a fixed tokens-per-week capacity.

Official estimates currently differ substantially across Astra, Sol, and Luna; real consumption depends on task/context and shared limits. These are not a guaranteed count of ingestion jobs. [Current usage guidance](https://learn.chatgpt.com/docs/pricing). Default routing is consistent with the official distinction between focused repeatable work, sustained synthesis, and difficult reasoning, but needs representative-course validation. [Model guidance](https://learn.chatgpt.com/docs/models).

### Durable jobs and reset recovery

Job states: queued, running, waiting for usage, waiting for sign-in, waiting for dependency/review, retry scheduled, blocked, paused, succeeded, cancelled. Persist completed steps, exact inputs/revisions, outputs, transaction IDs, errors, and next eligible time. Report stage/file/page counts only when measured; do not invent a percentage or ETA for reasoning.

- Handle provider quota errors by pausing eligible inference, preserving work, and releasing course locks. Revalidate state before resumption.
- Use an actual reported reset/retry time when available. An HTTP 429 alone does not establish a five-hour reset or whether an app-level, weekly, or account limit applies.
- When no usable reset time is exposed, use bounded low-frequency availability checks with increasing backoff; do not repeatedly submit the full expensive job. Distinguish quota, temporary availability, revoked permissions, unsupported requests, and permanent eligibility failures.
- At eligible time, verify authorization/availability and resume from the last valid checkpoint. Interrupted inference is not a completed step; recover any actual journaled writes before rerunning it.
- Limit repair retries per output revision. Material unresolved findings remain blocked; never loop indefinitely to force Ready.
- Allow pause/cancel/retry. Cancelling a job stops further work safely and preserves existing artifacts/evidence; it does not delete a course.
- If the computer sleeps through a reset, resume when it wakes and the service is available. If stopped, resume on next manual launch.
- Never automatically buy credits, consume paid fallback, or bypass subscription controls.

The subscription-sharing documentation explicitly warns that a usage-limit error can be app-specific and does not provide a reset time by itself. [Error/recovery contract](https://developers.openai.com/siwc/token-sharing-open-source/errors-and-recovery).

## 6. Agents tab

Provide a plain-language default view and expandable technical detail:

- Course/week, operation, current stage, active role/model/effort, source revision, start time, progress facts and dependencies.
- Queued, active, waiting-for-limit, blocked, failed, and finished work, with a history of meaningful state transitions.
- Last completed checkpoint, next eligible retry/reset time when known, and the reason for waiting when unknown.
- Independent review status, material findings, repair/recheck outcome, and publication/version changes.
- Which notes/lessons changed, coverage boundaries, and whether curriculum/evidence is current.
- Account usage data when actually available, with unavailable values displayed as unknown; do not infer monetary cost from a Plus percentage.
- Controls for queued-work pause/resume, safe cancellation, retry, inspecting changes and role-specific model/effort settings.

Use actual operational events and concise action summaries. Do not display private chain-of-thought or present generated narration as a verified tool result. Redact credentials and sensitive infrastructure data from logs. Routine progress remains in this tab instead of interrupting lessons.

## 7. Development stages and acceptance criteria

### Stage 1 — local learning interface and trustworthy progress

Deliver a maintainable application shell based on the prototype, course/week catalogue, structured section player, maths, outline, visual-component foundation, deterministic checkpoints, separate prepared quiz UI, evidence/receipt adapter, resume behavior, and local launcher/service boundary.

Begin with a thin feasibility slice: local launch → supported ChatGPT sign-in → one successful authorized model request → streamed status → safe shutdown/restart. This gates the chosen subscription adapter early without building the whole pipeline first. Do not require AI for rendering or deterministic checkpoints.

Import only currently checked ready curriculum through a validated adapter. Existing Markdown objective blocks are not assumed already to be complete 25-minute web lessons. Prepare and independently check any substantive adaptation to site-ready bundles using plan. Academic omissions return to ingest. Fictional test data stays isolated from real course/evidence records.

Acceptance:

1. Course/week/lesson IDs and required coverage are explicit; unavailable/partial/stale material is honestly labelled.
2. A learner can navigate lesson sections, render equations/visuals, complete a deterministic checkpoint, receive prepared option-specific feedback, and resume after reload.
3. Manual completion controls and endpoints do not exist. Completion is rebuilt from authoritative activity, not localStorage counters.
4. Original attempts survive correction; repeated submissions/reloads do not duplicate evidence. Grading-pending and missing answers are not inferred outcomes.
5. A content refresh preserves active session versions and all progress.
6. Keyboard navigation, reduced motion, outline behavior, sensible typography, maths overflow, and responsive layout are visually verified.
7. Browser close leaves the local service available; explicit stop and restart recover durable state.

### Stage 2 — upload-driven ingestion and publication

Deliver durable upload storage/replacement, same-course previous-week scans, local extraction, workflow adapters, per-course serialization, independent source/curriculum reviews, generated teaching/assessment bundles, atomic publication, version changes, Agents tab, quota waiting/resumption, and repository integration status.

Acceptance:

1. Uploading a representative week produces checked notes and site lessons with source/notes/objective coverage traceability.
2. An identical upload produces no unnecessary AI run. An earlier-week source modification triggers affected reconciliation and a post-lesson notice.
3. A stale job cannot publish over a newer source snapshot. Overlapping writers across workers/checkouts cannot mutate the same course simultaneously.
4. Unreadable files, failed academic checks, pending transactions, absent review, exhausted variants and Git integration blockers cannot publish Ready.
5. A simulated crash at each step recovers without losing originals, corrupting journals, duplicating jobs, or replacing valid publication with a partial bundle.
6. Quota exhaustion preserves work, releases locks, and resumes at verified eligibility/bounded retry without paid fallback. Browser closure does not prevent recovery.
7. Published visuals/answers/rubrics/distractors are checked, keys are excluded from normal learner payloads, and external source text cannot issue agent instructions.

### Stage 3 — assessments and adaptive course-specific review

Deliver AI short-answer assessment, prepared lesson quizzes, mixed weekly test blueprints, essential-component rules, separate completion/pass/attention views, unseen retention banks/exposure tracking, targeted repair routes, course-specific recall queues, and adaptive recommendations.

Acceptance:

1. Deterministic lesson responses have immediate prepared explanations for correct and incorrect choices without AI.
2. Written answers are durably received and scored against their exact prepared rubric; slow/quota-limited assessment stays pending while the learner continues.
3. Weekly tests preserve approximately 50/50 point weighting where coverage allows, and disclose exceptions; all future lessons remain accessible.
4. 85% with essential criteria met yields Completed/Passed/Needs attention. A missing essential component is not overridden by 95% overall.
5. First attempts, assistance, corrections, retries and delayed results remain distinguishable and versioned.
6. Retention tests select unseen items before refresher content. An exposed item cannot qualify as fresh merely by changing choice order.
7. Reviews never mix courses, show reasons/estimates prominently, impose no arbitrary duration cap, and do not block new study.
8. Subsequent recommendations follow committed results; a corrupted/incomplete result cannot change evidence or recall schedules.
9. Updates preserve earlier evidence and require prepared reassessment only where compatibility warrants it.

## 8. Code structure, documentation, and quality standards

Proposed application location: a dedicated `apps/learning_hub/` area, with engineering documentation beside it and workflow-owned changes kept in their canonical locations. The implementation branch/worktree follows repository instructions. Runtime databases, credentials, locks, extraction scratch files and private submitted-answer backups are excluded from source control; preserved canonical transaction journals follow existing repository rules.

Suggested modules:

```text
apps/learning_hub/
  frontend/src/
    features/{courses,lessons,assessments,reviews,agents}/
    components/{math,outline,visuals,questions}/
    api/                       # Generated contracts and narrow client
  backend/learning_hub/
    domain/                    # Identity, state transitions, grading, selection
    application/               # Use cases, publication, workflow orchestration
    adapters/{vault,codex,extraction,storage}/
    api/                       # HTTP/event routes; no academic business logic
    worker/                    # Durable scheduling and process lifecycle
  tests/{unit,contracts,integration,e2e}/
  docs/{architecture,decisions,operations}/
```

Use clear responsibility boundaries, small cohesive modules, dependency injection at integration seams, explicit errors, validated schemas and named state machines. Keep provider-specific details behind the Codex adapter. Keep grading/publication/evidence decisions out of UI event handlers. Avoid a generic workflow framework or sprawling abstractions before actual requirements justify them.

Documentation includes setup/launch, architecture and owner matrix, endpoint/event contracts, schema versions/migrations, role configuration and escalation, publication lifecycle, question/visual authoring contracts, backup/restore, quota recovery, crash recovery, and later mobile constraints. Record important choices in short architecture decision records. Comments explain invariants and non-obvious reasoning; do not comment every line or create stale banners. Use descriptive names and docstrings for public interfaces.

Testing targets meaningful invariants: scoring tolerance and essential rules; valid state transitions; identity/exposure selection; duplicate submissions; interrupted persistence; stale publication; quota/auth recovery; job cancellation; source changes; question/key separation; permission boundaries; and progress preservation across revisions. Integration tests use temporary vaults and deterministic fake provider transports; no fabricated records enter the real vault. AI-quality checks use representative sources and human-reviewed answers plus the required independent academic reviewers. Passing software tests does not establish academic accuracy.

Automated checks: formatting, linting, type checking, unit/contract/integration tests, focused end-to-end user flows, migration checks, dependency/secret checks, and accessibility checks where appropriate. Inspect rendered lessons and interactive visuals in the browser. Run existing affected records verification, before/after vault checks with issue identity comparison, and plugin packaging checks only when canonical packaging inputs change. Use explicit staging, scoped diff review, `git diff --check`, protected PR integration, verified merge, and task-only cleanup.

Back up both canonical evidence/history and operational storage. Test restore into an isolated location; preserve version links and pending intent state. Never make a UI reset, source replacement, site rebuild, or database migration erase academic history or learner evidence.

## 9. Implementation readiness and remaining technical gates

Functional decisions are settled by this conversation. Implementation should resolve technical feasibility through bounded spikes rather than another broad questionnaire:

1. Confirm supported local ChatGPT plan registration, sign-in, account-specific model/effort access and a completed inference request. Keep the documented provider route; do not scrape ChatGPT or copy browser session cookies. [Subscription integration](https://developers.openai.com/siwc/token-sharing-open-source), [app-server adapter](https://developers.openai.com/siwc/token-sharing-open-source/codex-app-server).
2. Confirm which reset/usage metadata is exposed to this integration; retain bounded recovery if absent. Hosted Responses background jobs, file search and other unsupported facilities must not be assumed. [Preview limitations](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations).
3. Define and validate site-oriented curriculum/evidence contract extensions without changing immutable historical records. Establish one evidence authority.
4. Validate the chosen local extraction/OCR/conversion tools against actual file types and mathematical/visual content; identify unreadable inputs honestly.
5. Benchmark the proposed role routing on a bounded representative week and prepared assessment answers. Optimize repeated work and context first; preserve reviewers and academic gates rather than lowering quality to meet a quota.
6. Validate the local background process lifecycle, atomic publication, crash recovery and progress-preserving migrations before increasing automation.

The product specification is approved. The technical planning task commits engineering instructions and profiles separately; application code and academic records are not claimed implemented by this specification.
