---
name: html-course
description: Build or refresh an optional English offline HTML course from checked Uni notes and ready prepared lessons, with week-grouped navigation, LaTeX and purposeful interactions. Use for explicit HTML-course requests, including after requested ingestion and planning; not for ordinary ingestion, tutoring, grading or curriculum changes.
---

# HTML course

## Contents

| Section | GitHub | Obsidian |
|---|---|---|
| **1. Purpose and when to use** | [Jump](#1-purpose-and-when-to-use) | [Jump](#1.%20Purpose%20and%20when%20to%20use) |
| 1.1. Optional course generation | [Jump](#11-optional-course-generation) | [Jump](#1.1.%20Optional%20course%20generation) |
| **2. Scope and ownership** | [Jump](#2-scope-and-ownership) | [Jump](#2.%20Scope%20and%20ownership) |
| 2.1. Artifact ownership at a glance | [Jump](#21-artifact-ownership-at-a-glance) | [Jump](#2.1.%20Artifact%20ownership%20at%20a%20glance) |
| **3. Inputs and prerequisites** | [Jump](#3-inputs-and-prerequisites) | [Jump](#3.%20Inputs%20and%20prerequisites) |
| 3.1. Checked input snapshot | [Jump](#31-checked-input-snapshot) | [Jump](#3.1.%20Checked%20input%20snapshot) |
| 3.2. Week and lesson mapping | [Jump](#32-week-and-lesson-mapping) | [Jump](#3.2.%20Week%20and%20lesson%20mapping) |
| **4. Roles and model routing** | [Jump](#4-roles-and-model-routing) | [Jump](#4.%20Roles%20and%20model%20routing) |
| 4.1. Owner and independent reviewer | [Jump](#41-owner-and-independent-reviewer) | [Jump](#4.1.%20Owner%20and%20independent%20reviewer) |
| **5. Workflow** | [Jump](#5-workflow) | [Jump](#5.%20Workflow) |
| 5.1. Prepare complete English lessons | [Jump](#51-prepare-complete-english-lessons) | [Jump](#5.1.%20Prepare%20complete%20English%20lessons) |
| 5.2. Preserve the approved visual identity | [Jump](#52-preserve-the-approved-visual-identity) | [Jump](#5.2.%20Preserve%20the%20approved%20visual%20identity) |
| 5.3. Mathematics and interaction | [Jump](#53-mathematics-and-interaction) | [Jump](#5.3.%20Mathematics%20and%20interaction) |
| 5.4. Build and refresh | [Jump](#54-build-and-refresh) | [Jump](#5.4.%20Build%20and%20refresh) |
| **6. Validation and completion** | [Jump](#6-validation-and-completion) | [Jump](#6.%20Validation%20and%20completion) |
| 6.1. Academic and browser checks | [Jump](#61-academic-and-browser-checks) | [Jump](#6.1.%20Academic%20and%20browser%20checks) |
| **7. Writes and recovery** | [Jump](#7-writes-and-recovery) | [Jump](#7.%20Writes%20and%20recovery) |
| 7.1. Versioned local publication | [Jump](#71-versioned-local-publication) | [Jump](#7.1.%20Versioned%20local%20publication) |
| **8. Handoffs and reporting** | [Jump](#8-handoffs-and-reporting) | [Jump](#8.%20Handoffs%20and%20reporting) |
| 8.1. User delivery and blocked inputs | [Jump](#81-user-delivery-and-blocked-inputs) | [Jump](#8.1.%20User%20delivery%20and%20blocked%20inputs) |

## 1. Purpose and when to use

### 1.1. Optional course generation

Produce an independently readable English HTML course from checked notes and ready prepared lessons. A learner opens `index.html`, chooses a week and lesson, reads the complete explanation, explores useful illustrations and practises. They may reference a lesson file and section in a separate tutor chat.

Run only when the user asks for HTML generation or refresh, such as “ingest and build the HTML course” or “build HTML from the existing Week 1 plan.” In a combined request, wait for successful checked ingestion and committed plan reconciliation. Plain ingestion does not invoke this skill. No watcher, app, server, installation, export button or tutor integration is part of the delivered course.

## 2. Scope and ownership

### 2.1. Artifact ownership at a glance

| Read | Own | Leave with its owner |
|---|---|---|
| Selected complete ingestion state/pass, matching plan/manifest, ready lessons, cited note sections and necessary assets | HTML course drafts, candidate files, coverage/build metadata, conversion reviews and versioned exports | Original materials and notes: ingest; curriculum: plan; actual evidence: teach; scheduling/Todoist: recall |

The default export is `02_Resources/HTML_Courses/<course_id>/` in the selected checkout. Keep full academic-year/semester/course identity and Unicode paths. Honor an explicitly requested separate output directory; never overwrite notes, records, another course or installation files. The helper confines publication to a dedicated export root and detects externally edited files.

Do not change existing skills or use this skill to repair notes, redefine objectives/criteria, grade actual learner responses or create review tasks. Local answer feedback, drafts and reading position are browser conveniences, never mastery or committed learner evidence. Do not read learner logs merely to render lessons.

## 3. Inputs and prerequisites

### 3.1. Checked input snapshot

Resolve the actual vault with `git rev-parse --show-toplevel`; the selected worktree is the vault root. The installed skill supplies templates/utilities, never a vault destination. Resolve `scripts/course.py` and `assets/` against this skill's own directory. Commands below use `SKILL_DIR` for that absolute directory, `VAULT` for the absolute checkout, and temporary draft paths outside authoritative records.

Read the selected complete ingestion state and its linked checked pass, including bounded coverage limits. Require the selected note headings to be checked; a whole-file hash alone never establishes whole-note coverage. Require matching schema-3 course/plan/source/ingestion tuples, ready indexed lessons, resolved prerequisites and committed owner journals. A partial overall plan may supply a genuinely ready bounded scope; show what is available without implying exam completeness.

Capture inputs without writing course records:

```sh
python3 "$SKILL_DIR/scripts/course.py" snapshot --vault "$VAULT" --course "$COURSE_ID" --objectives O002 --out /tmp/html-snapshot.json
```

The helper verifies transaction bytes through the checkout's `03_Agents/scripts/records.py`, note hashes/headings and prerequisite closure. Read the snapshot's actual source sections before composing. It records no learner outcomes and does not replace semantic provenance inspection. Unjournaled, stale, unreadable or pending inputs block generation; return them to their existing owner.

### 3.2. Week and lesson mapping

Group the contents page by source week, then coherent lessons. Use week identities established by the plan or checked note paths. Do not invent weekly assignments. Cross-week synthesis records all contributing weeks and appears once in the primary week, with a cross-reference from the others. A non-week source needs an explicitly meaningful grouping; clarify only when the source and user request cannot establish one.

Lessons may combine related objectives or split a long objective. Give each a stable readable ID and each section a stable anchor, keeping the objective/dependency mapping complete. Include requested prerequisites or route to already exported complete lessons; do not leave a prerequisite pointing to an unavailable page.

## 4. Roles and model routing

### 4.1. Owner and independent reviewer

The active capable agent owns conversion and export writes. Do not introduce a fifth core workflow owner, change the four existing model profiles or pretend a skill changes the chat model. A delegated assignment includes `helper_role: html_course_review`, the absolute vault/skill/candidate paths, selected scope and explicit read-only boundaries. The helper is a reviewer, not another writer.

Use a separate independent agent to compare the final candidate against its checked notes, prepared lessons, keys and coverage map. Give it the actual artifacts, not the desired conclusion. It checks English fidelity, academic substance, assumptions, derivations, examples, figures, questions, solutions, source/week mapping and preserved scope. It may verify cited lesson supplements against their cited support; it does not audit raw course sources, repair notes or edit curriculum. Fix findings as owner and obtain renewed confirmation on the final candidate digest. An unavailable reviewer leaves the candidate unapproved; never fabricate a passed report.

## 5. Workflow

### 5.1. Prepare complete English lessons

Use `templates/course.json` as the operational draft format; the helper's `--help` lists commands. Prepare the whole requested bounded scope. Reuse complete relevant explanations, derivations and worked examples from notes/lessons, preserving notation, definitions, units, assumptions, exceptions and interpretation. Translate teaching text into English while retaining original bibliographic titles and technical symbols where appropriate.

Reorganization, intermediate steps and interactive versions of existing examples are welcome when they preserve substance. A concise summary or a link back to the notes is not a replacement for the reasoning needed to study independently. New numerical illustrations stay within an established method, are identified as illustrative, and have checked solutions. Substantive missing academic content returns to plan; actual note errors return to ingest.

Account for every snapshot source section in the draft coverage map. Map included sections to concrete HTML anchors. Only tutor routing/scheduling, record-metadata and navigation sections may be omitted as operational-only, with a reason; academic explanation, conditions, practice, keys and misconceptions remain available. Preserve prepared item IDs when reusing them. All HTML exercises are self-study practice: freely revealing solutions or trying a question here cannot establish the plan's independence/freshness gates. Tell the user that viewing prepared assessment items may make those exact items unsuitable as fresh checks in chat; do not write exposure evidence automatically.

### 5.2. Preserve the approved visual identity

Build from the supplied assets, not a newly invented design. Paper & Ink uses warm paper `#fbf9f4`, forest green `#164e3e`, quiet rules, Source Serif 4, generous reading space and a compact desktop sidebar. Keep the week-grouped course contents, visible active lesson, breadcrumbs, previous/next links, unrestricted navigation, stable section labels, optional hints and freely revealable solutions.

Every lesson must open directly in a local browser; `index.html` is the full contents page. Bundle CSS, scripts, math fonts and figures with relative paths. No CDN, runtime fetch, module loader or server requirement. Preserve a usable compact layout and keyboard focus. Keep technical build metadata out of the reading flow; a small “Sources and scope” disclosure may explain meaningful academic limits.

### 5.3. Mathematics and interaction

Use actual LaTeX for all inline and display mathematics. Use `\(...\)` and `\[...\]` delimiters. Convert dollar-delimited source mathematics to these explicit delimiters; leave literal currency dollar signs as plain text. Check summation limits, hats, subscripts, matrices, aligned derivations, equation labels and overflow. Never substitute screenshots or raw TeX for readable equations. Math parse/font failures are visible build issues, not acceptable fallback typography.

Choose interaction to illuminate a concept. Built-in numerical questions, multiple choice, written reflection and adjustable residual plots are available. Static figures are preferable when manipulation adds nothing. Custom local assets/scripts may supply a genuinely needed component; keep them self-contained, solve/check their behavior, and include them in both reviews. Do not insert widgets to satisfy a quota.

Numerical and structured questions may give reliable immediate feedback. Written arguments use model solutions for self-assessment. Preserve conditions on formulas and visualizations; a slider's fixed intercept or illustrative sampling assumptions must be stated. Local storage is optional, version-qualified and allowed to fail gracefully; it never communicates with a tutor or external service.

### 5.4. Build and refresh

Write the English lesson draft beside its snapshot; build a candidate outside the live export:

```sh
python3 "$SKILL_DIR/scripts/course.py" build --vault "$VAULT" --snapshot /tmp/html-snapshot.json --draft /tmp/html-course.json --candidate /tmp/html-candidate
python3 "$SKILL_DIR/scripts/course.py" check --candidate /tmp/html-candidate
```

On refresh, read the existing export manifest and its saved draft. Retain unaffected lessons and their stable IDs; inspect changed source sections, copied passages, keys and downstream dependencies. Refresh the full already-exported scope plus requested additions, rather than silently replacing a course with only the latest week. The helper compares page/asset hashes and reports changed files. An explicit narrowed scope or plan retirement may remove live entries only with a recorded reason; earlier versions remain intact.

Recheck freshness before publication. No ordinary ingestion, elapsed time or background process refreshes HTML automatically: an explicit build request performs the change detection and refresh.

## 6. Validation and completion

### 6.1. Academic and browser checks

Completion requires independent conversion review on the final candidate, coverage of the selected supported scope, usable local assets/links and browser checks of the final bytes. The owner checks desktop and compact reading, all math rendering/fonts, figures, keyboard access, primary interactions, wrong/empty/correct feedback and solution reveals. Compare the reading identity with the supplied theme; tests alone do not establish academic fidelity.

Save separate academic and browser reports outside the candidate. Each names its actual reviewer, the candidate digest, scope/evidence, findings and final status. The academic report covers all objective IDs; a passed final report has no material findings. The browser report records checks for `links`, `math`, `interactions`, `desktop`, `compact` and `offline_dependencies`. Report unavailable direct-file browser testing precisely; a confined local preview may verify rendering when the host disallows file URLs, but the delivery must still have no server dependency.

Publish only after both final reports pass:

```sh
python3 "$SKILL_DIR/scripts/course.py" publish --vault "$VAULT" --candidate /tmp/html-candidate --review /tmp/html-academic-review.json --qa /tmp/html-browser-review.json
```

Exam completeness is not a gate. Accurate coverage of the selected prepared material is. Unsupported or unprepared material remains explicit, without certifying a whole syllabus from a bounded export.

## 7. Writes and recovery

### 7.1. Versioned local publication

The helper owns only its dedicated export. It checks input hashes again, serializes export writes with `.html-course.lock`, and never steals a lock by age. Export versions are immutable under `versions/b-<digest>/`; final review records and file hashes accompany them. The only activation write is an atomic replacement of the root `index.html`, which contains the complete contents page and points into a fully verified version. A crash before that replacement leaves the earlier version usable. An identical retry verifies and reuses the already completed version.

Never overwrite externally edited pages, metadata, root contents or unexpected export files. Preserve unfinished stages and lock records; inspect their intent and recorded host/process before explicit recovery. An inactive complete version is retained history, not disposable cache. A corrupt stage/version or an uncertain conflict stops affected publication. Do not use the four-owner records utility to write HTML, extend record schemas, or edit existing transaction journals.

## 8. Handoffs and reporting

### 8.1. User delivery and blocked inputs

Return the full contents path and representative lesson path, actual course/week scope, input plan/source/ingestion tuple, changed pages, reviewer identities/results and any limits. Explain that the folder opens locally and must stay together. Open a preview when supported; do not host publicly or create an app. A user can reference the HTML file and section in a tutor chat without this skill exporting or synchronizing context.

Send a blocked-input handoff to the responsible owner with exact course identity, file/heading or transaction, observed versions, affected objectives and the concrete issue. Do not quietly invoke ingest/plan or change their artifacts solely to complete an HTML build unless that repair is separately within the user's request. Keep candidates, earlier exports and their evidence available for resumption.
