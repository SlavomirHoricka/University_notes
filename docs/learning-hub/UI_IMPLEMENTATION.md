# Frontend and interactive-content instructions

Owners: hub_frontend H04/H05/H13, hub_visuals H06. Question/rubric contracts are owned by foundation/assessment; do not duplicate authoritative grading in UI code. All production values come from typed backend reads. Reference prototype is the visual baseline for dashboard, course cards, planner, materials and Agents tab; remove its localStorage course counters and manual completion controls.

## Routes and state

Target routes: `/`, `/courses`, `/courses/:courseId/weeks/:weekId`, `/learn/:sessionId`, `/assess/:assessmentSessionId`, `/courses/:courseId/reviews`, `/materials`, `/agents`, `/settings`. Opaque IDs go in routes, never raw vault filesystem paths. Deep links recover the pinned session from the server, not a fresh guessed lesson.

Use one typed query client and narrow command helpers generated from OpenAPI. Query keys include entity and publication/version where appropriate. Server responses own eligibility/state; local component state owns an unsent answer or expanded panel only. Keep pending input on navigation interruption until accepted/persisted, without claiming it is canonical evidence. Mutation helpers supply an idempotency key, expected session/version and handle pending/conflict statuses explicitly.

Global state is limited to UI theme/navigation and local auth-session status. Do not place full curriculum, all answers or keys in a context/localStorage object. Focused hooks: `useLessonSession`, `useSubmitAttempt`, `useDeliveryReceipt`, `useOutline`, `useJobEvents`, `useCourseReviewQueue`. Keep network calls out of presentational components. Update data from confirmed server facts; optimistic success is forbidden for grades/completion.

## H04 shell, catalogue and materials view

Implement reusable `AppShell`, `SidebarNav`, `PageHeading`, `CourseCard`, `WeekList`, `ReadinessBadge`, `ProcessProgress`, `AttentionBadge`, `EmptyState`, `PendingState`, `ErrorState`. Preserve the prototype's general typography/spacing/colors using shared CSS variables; refine responsive layouts and states rather than retaining a single giant inline stylesheet.

Course cards distinguish checked coverage, instructional completion, assessment status and attention. Show truthful initial zeros/unknowns, not demonstration statistics. Week rows list lessons in order with teaching estimate and a separate quiz estimate, optional tags and latest applicable results. Optional content does not inflate required-completion denominators. Future weeks have recommendations, not score locks. Clicking Continue resumes an actual saved session or starts a server-selected prepared route.

Materials upload uses selected course/week, drag/drop and keyboard file picker. Show staged/saving/queued/processing/checked/published/failed states separately. An upload accepted into local storage is not already ingested. Show duplicate/replacement decisions and errors per file; let user inspect an affected source revision. Do not delete an earlier source's bytes on replace. H07 owns upload backend.

## H05 section player

Build `LessonPlayer` from `LessonHeader`, `SectionNavigation`, `SectionRenderer`, `LessonOutline`, `CheckpointPanel`, `FeedbackPanel`, `ResumeIndicator`, `NextAction`. The server selects a pinned session/bundle; a refreshed catalogue cannot replace that session's content.

`SectionRenderer` handles an exhaustive discriminated union: prose, list, equation, figure, worked-example steps, approved visual config and checkpoint. Unknown/invalid blocks produce a supported-content error and cannot be skipped as if complete. Sanitized Markdown is allowed for prose, no raw HTML scripts or iframe content. Disable remote tracking assets. All source assets resolve through controlled publication URLs.

Use KaTeX for compiled inline/display expressions with `trust: false`, bounded macro expansion, strict parse errors at publication and accessible MathML/HTML output. Do not silently show malformed formulas as passed validation. Long display equations scroll within their block rather than overflow the page. Renderer options and macro allowlist are versioned. [KaTeX options](https://katex.org/docs/options.html).

Use `IntersectionObserver` for heading activation with an offset matching the sticky header. Stable heading IDs come from content, not text-generated IDs that change on formatting edits. Highlight the nearest current heading; scroll the outline's active entry into its own viewport with `nearest`, without changing page scroll. Outline clicks use a single smooth scroll except `prefers-reduced-motion`, which uses instant scrolling. Preserve keyboard focus, browser back behavior and explicit heading anchors. Do not create continuous scroll-handler loops or treat intersection as learning evidence.

Previous/Next section buttons preserve free navigation. Checkpoints determine instructional process state through recorded attempts/correction routes; a section cannot gain verified completion by scroll position alone. When skipping an unanswered required checkpoint, navigate freely but show it outstanding. Resume records section/anchor and incomplete item; it is a bookmark, not a result. Navigation saving is debounced (500ms target), answer submission is never debounced or discarded.

## Checkpoint components

- `SingleChoiceQuestion`: accessible radio group, explicit submit; choices may be shuffled deterministically by attempt identity but stored response uses stable option ID.
- `MatchingQuestion`: keyboard-operable selects as baseline, optional drag/drop with the same accessible alternative; serialize stable left/right IDs. No color-only correctness cue.
- `NumericQuestion`: string input with declared units and rounding instructions, calculator permitted where rubric allows. Do not add an algebra entry editor. Backend parsing rejects ambiguous notation without consuming a wrong-answer result.
- `ScenarioQuestion`: approved component-generated structured response checked deterministically; required manipulation and submitted conclusion remain distinct. Merely touching a slider is not proof of understanding.

While submission is pending, prevent duplicate accidental submissions but allow retries with the same request key after transport failure. Show prepared feedback for correct and incorrect options. Score the original response before displaying explanation. Fresh corrective variants are selected by the server; avoid reusing the same exposed prompt as a new independent check. A correction can complete the process while the underlying attention badge remains justified.

## Assessment/review screens

Lesson quiz is separate from instruction, 5–10-minute estimate, one prepared item at a time with feedback after that item's immutable submission and verified grading; whole-quiz finalization records aggregate coverage. Weekly test has 25–35-minute estimate, question navigator and editable saved drafts through CONTRACTS draft GET/PATCH commands; withhold correctness until atomic final draft-snapshot submission. Display saved/pending draft state, preserve input on revision conflicts and permit revisiting/editing questions before final submit. Session bookmarks use the explicit non-evidence PATCH, independently from delivery acknowledgements. Open-ended short answers use a plain text area, typically a few sentences, with optional word guidance rather than a forced long essay.

Show submitted, grading pending, graded and unscorable states. AI delay does not prevent continuing to another lesson. Result view separates first result, corrections, latest applicable result and objective-level weaknesses. Do not imply that selecting a best attempt establishes retention. Unmet essential criteria are visible even when total score is high.

Review page is per course. Dashboard cards can aggregate counts across courses, but Start review chooses one course. Show topics, why each needs review, estimated duration and overdue/gate state. No arbitrary duration cap and no unlock gate for new lessons. For delayed reviews, hide recap/hints until the initial retrieval attempt; corrective route displays support intentionally and labels subsequent performance accordingly.

Content updates are queued until the active lesson is finished. Surface them on the next natural dashboard/end screen. Never pop a toast on each job event. Critical persistence failure is shown immediately because the learner must know an answer was not saved; routine publication does not distract them.

## H06 approved visual library

Implement generic components, with first representative fixtures only where note-supported: `CashFlowTimeline`, `RelationshipPlot`, `PayoffPlot`, `ScenarioTable`, `DerivationReveal`, `AnnotatedDiagram`. Start with SVG for inspectable geometry and static labels; use a plotting dependency only when requirements justify it. Provide a table/text alternative and keyboard controls.

Visual configs contain type/version, source/lesson references, parameters/defaults/bounds/step/units, equation ID from approved code registry, assumptions, explanatory labels and reference cases. Never evaluate arbitrary formula strings using `eval` or import generated script URLs. Runtime mathematics lives in tested registry functions, whose inputs/output domains are validated by both backend/publication and component.

For supported bond examples, test cash-flow price at a documented yield, monotonic price/yield direction under specified assumptions, zero/negative rate boundaries and invalid denominators. For payoff fixtures, test values below/at/above strike and distinguish payoff from profit when a premium is included. These are component tests on synthetic fixtures, not permission to invent material for a course. Academic reviewer verifies the actual source-backed instances.

Mark interaction prompts such as “Predict the direction, then move the slider” with separate response fields and reference outcomes. Estimate interaction time from authored steps; do not generate engagement statistics as understanding evidence.

## H13 Agents tab/settings

Use `JobList`, `JobDetails`, `StepTimeline`, `ReviewFindings`, `ChangedContent`, `UsageStatus`, `RoleSettings`, `JobControls`. Subscribe via resumable SSE and refresh authoritative queries after relevant events; duplicates are ignored by event ID. A cursor gap means resnapshot, not missing jobs counted Done. Avoid a websocket unless a later concrete requirement needs bidirectionality.

`ChangedContent` handles owner-required approval proposals with concrete scope, preserved-version/diff preview and explicit Approve/Reject bound to proposal digest/job revision; Retry is never approval. A changed proposal refreshes the decision screen. Already-authorized work proceeds automatically. Preview access is recorded as possible study exposure. Settings/Agents contains Connect/Grant/Sign out using typed provider lifecycle endpoints; open only the server-validated authorization URL and show pending/validated/failed flow status without secrets. Local offline session and AI subscription login are separate statuses; a connected badge alone cannot imply completed inference.

Default summary shows course/week, stage, role/model/effort and last actual checkpoint. Expand technical tool/check/commit details without credentials or private chain-of-thought. Percentages appear only for measured file/page/task counts. Unknown quota/reset is displayed as unknown, never 0 or an invented ETA.

Role settings offer only supported model/effort combinations and warn when overriding recommended role quality. Saved changes affect future jobs, never a running grade or rubric. Pause/cancel/retry controls use backend legal transitions and show preserved-progress consequences. Settings cannot grant raw-source instructions privileges, disable mandatory academic review or activate paid fallback.

## Verification

Component tests cover empty/partial/stale states, stable IDs, navigation without false completion, feedback timing, pending grading, essential criterion visibility, keyboard matching, math overflow, reduced motion and dynamic outline. Integration tests assert no manual-complete mutation and no hidden keys in learner responses. H15 browser tests cover refresh mid-question, lost ack, changing publication mid-session, pending grade while continuing, SSE reconnect, no disruptive notification and course-specific reviews.

Capture screenshots at desktop widths around 1440 and 1024, plus a narrow responsive preview around 390 for future readiness. Inspect long headings, long equations, multi-line feedback, empty courses, offline-provider status and many queued jobs. Use semantic landmarks, visible focus, adequate contrast and readable errors. Screenshot checks supplement behavior tests; neither proves academic accuracy.
