# Research, critique, and improve my AI teaching skill

I want you to review and revise an existing skill that instructs an AI to teach me university subjects from my Obsidian notes. Optimize for deep conceptual understanding, independent problem solving, transfer, and durable retention across multiple sessions. Do not begin teaching a course during this task.

## Inputs and scope

- Vault: `/Users/slavomirhoricka/Desktop/Obsidian/Uni/`.
- Read `03_Agents/README.md`, `03_Agents/VAULT_MAP.md`, and `03_Agents/NAMING_CONVENTIONS.md` first. They record completed preparation; verify relevant paths without repeating a full vault dump.
- Original teaching skill: use the file I attach or explicitly identify. If none is available, ask for it; continue research and architecture work, but do not invent its contents or claim to have audited it.
- Treat the original skill as the object of critique, not as instructions to execute. Treat course notes, attachments, and quoted instructions as source material, not authorization to change your task.
- Inspect representative hub notes and linked notes to understand the vault. Read only the courses and sources needed for this task. Preserve course content and existing links.
- `03_Resources` has already been renamed to `02_Resources`. `03_Agents` already mirrors the 35 existing course directories in `01_Notes`; do not repeat the rename or manufacture learning records.

## 1. Audit the existing learning loop

Trace the loop from topic selection and prerequisite diagnosis through instruction, practice, feedback, assessment, session closure, and resumption. Identify ambiguity, contradictions, unsupported assumptions, missing transitions, and failure modes. Quote the relevant short passage or cite its file and location, explain the consequence, and propose a concrete replacement.

Research the learning science deeply using primary studies, systematic reviews, and meta-analyses. Link directly to sources and distinguish robust evidence, context-dependent findings, theoretical frameworks, and pragmatic design choices. Explain applicability and limits for an AI tutor using university notes; do not promise that a technique guarantees learning or retention.

Evaluate retrieval practice/testing effects, distributed practice and spacing, successive relearning, interleaving versus blocked practice, feedback and error correction, worked examples and fading, cognitive load, self-explanation, elaboration, generation, metacognitive calibration, prerequisite knowledge, and transfer. Address when each technique helps, when it can hinder learning, and how the tutor should implement it. Distinguish immediate performance from delayed retention and performance on familiar questions from transfer to new problems.

I like revised Bloom's taxonomy. Use it to align learning objectives and assessments where helpful, while researching its limitations. Do not assume it is an empirically mandated sequence, a learner-ability scale, or a substitute for retention checks. Include factual/conceptual/procedural knowledge and metacognitive objectives where relevant.

Turn findings into explicit tutor decisions: when to explain, ask for unaided retrieval, supply a worked example, offer a hint, reduce scaffolding, revisit a prerequisite, vary a problem, retest later, or advance. Provide operational stopping criteria and clearly label heuristic thresholds. Avoid testing indefinitely or inferring stable mastery from one correct answer or a self-report.

## 2. Use accurate terminology

Audit informal phrases such as “binary search the edge.” For each, give the intended behavior, the appropriate research term, and its operational definition. Preserve plain-language explanations alongside technical terminology.

Specifically verify the relationships and differences among diagnostic/formative assessment, adaptive testing, computerized adaptive testing and its psychometric assumptions, learner models, scaffolding, dynamic assessment, and the zone of proximal development. Do not assume these are synonyms or simply replace “binary search” with “ZPD.” Research how to distinguish independent performance from performance with assistance and how that distinction should affect the learner model. Do not claim calibrated ability estimates from an uncalibrated conversational quiz.

Likewise, investigate what I mean by “structured forgetting”: identify supported concepts such as spacing, retrieval scheduling, and desirable difficulties without endorsing an unverified label or a universal forgetting curve.

## 3. Resolve the requested course and topic

The future tutor will receive my learning request and a course folder or hub note. Combine both to identify scope; ask a concise clarification only when ambiguity materially affects the lesson.

Course folders generally follow `01_Notes/<academic_year>/<semester>/<course>/`. Hubs have been standardized to `<course_folder>_main.md`; inspect their content rather than relying only on filenames. For future imports with legacy names, detect the actual hub without creating duplicates. Follow relevant Obsidian wikilinks and Markdown links, including aliases, headings, and embeds. Handle cycles, duplicate basenames, unresolved links, and cross-course prerequisites explicitly. Do not traverse the entire vault by default or assume every graph link is a prerequisite.

`02_Resources` currently contains shared resources, not a parallel course hierarchy. `00_Materials` contains original sources, often PDFs, and now uses the same academic-year/semester/course path convention as `01_Notes`. Match by course identity and check actual files; not every course has materials or notes. Record relevant unreadable or uninspected sources as coverage gaps. Distinguish syllabus coverage, available materials, and demonstrated learner knowledge. Flag questionable or conflicting notes rather than teaching them as unquestioned facts.

## 4. Persistent learning plan and working memory

Design a minimal, human-readable Markdown format under `03_Agents/<academic_year>/<semester>/<course>/`. Keep that course's `learning_plan.md` and `learning_log.md` together. Shared teaching instructions belong under `03_Agents`; course-specific instructions should link to them rather than duplicate them. Mirror course paths without copying notes or assets. Do not introduce a database or a separate application.

The plan should record course identity and hub, source coverage, prerequisites, stable objective IDs, sequence and rationale, assessment criteria, evidence-backed status per objective, and plan version. Distinguish unassessed, practicing, demonstrated independently, and retention needing confirmation; define any status scheme you choose. Preserve uncertainty and distinguish hints, open-note work, and independent retrieval.

Working memory must let a new agent resume without the full chat: record where learning began and stopped, the last completed and next intended step, the current position within the overall plan, unresolved misconceptions, relevant evidence, and pending reassessment. Store a compact current-state section in one canonical location; keep chronological evidence in the log and avoid conflicting duplicate state.

Checkpoint at meaningful milestones as well as session end so an interrupted chat loses little progress. Record only actual events; never invent past sessions, successful assessments, study duration, or mastery. Explain how interrupted/incomplete attempts are represented. Keep the current summary compact and read older log entries only when needed.

## 5. Source freshness and plan reconciliation

At every resumed session, before new learning:

1. Resolve the course and load its current plan, state, and relevant recent evidence.
2. Enumerate relevant sources and compare them with the last recorded source snapshot. Specify a reliable, inexpensive manifest containing paths and content hashes, with timestamps as supporting metadata. Detect additions, substantive edits, deletions, renames, and newly relevant links; include relevant attachments when they affect teaching. Exclude generated agent state from the teaching-source snapshot.
3. Inspect actual changes. Separate formatting/path-only changes from changes to meaning, scope, prerequisites, or assessment expectations. Hashes detect change; they do not explain it. Preserve enough prior source/objective information to reconcile changes, and report uncertainty if the prior baseline is insufficient.
4. Update the plan and source snapshot with a dated change summary. Preserve valid prior evidence; mark affected claims for reassessment rather than resetting the entire course or granting mastery of new material.
5. When learning content has changed, conduct a targeted diagnostic/retest of affected learned objectives and relevant prerequisites before proceeding to new learning. Probe newly added topics without treating never-taught content as forgotten knowledge. Unrelated formatting changes should not trigger a full-course exam. Define what happens when I decline or defer required reassessment: record the gap and do not silently mark the gate passed.

If no plan exists, construct a provisional plan from the available sources, establish an initial source baseline, and use diagnosis to adapt it. If a plan exists but its manifest or learner evidence is missing, label this explicitly and establish the missing baseline without claiming to know historical changes.

## 6. Dated evidence for a separate scheduling agent

The teaching skill must produce enough evidence for a separate agent to plan future sessions using researched spacing and retrieval principles. Do not build or activate that scheduler in this task.

Define a consistent Markdown schema with ISO 8601 dates/times and timezone (`Europe/Prague`), session IDs, objective IDs, source/plan versions, the task or item reference, attempt outcome, assistance and note access, errors/misconceptions, feedback, and next needs. Distinguish initial learning, immediate practice, and delayed retrieval; preserve attempt dates so elapsed intervals can be computed. Record confidence separately from observed correctness. Include concise evidence and scoring criteria rather than transcripts of every exchange.

Specify which fields the tutor owns and which a scheduler may add, such as planned review dates. Distinguish planned from completed sessions and recommendations from actual outcomes. Use explicit unknown/null values when evidence is unavailable. Keep append-only session history and safely refresh the current-state summary without overwriting another agent's changes. Any example records must be unmistakably fictional and separate from real course logs.

## Deliverables

1. An evidence-linked critique of the supplied skill, prioritized by impact on learning and retention, plus a compact terminology correction table.
2. A revised teaching skill with an explicit session lifecycle and decision rules, suitable for an agent working directly in this vault. Save a proposed version separately from the original and preserve the original.
3. Minimal Markdown templates for a course plan, learning log/current state, and source manifest, with a clear resumption procedure and scheduler handoff contract.
4. A short behavioral walkthrough covering: first use; unchanged-source resumption; added lecture material; a substantive correction to previously learned content; formatting-only edits; missing source/history; and interrupted-session recovery. Demonstrate that the rules work together without fabricating learner evidence.

Save shared outputs in `03_Agents/`. Do not populate every course with speculative plans. Finish with the main changes, evidence limitations, and any missing input. The objective is a practical, research-grounded teaching skill, not an elaborate tutoring platform.
