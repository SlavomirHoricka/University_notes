# University Assistant

## Contents

| Section | GitHub | Obsidian |
|---|---|---|
| **1. Overview and skills** | [Jump](#1-overview-and-skills) | [Jump](#1.%20Overview%20and%20skills) |
| **2. Model routing** | [Jump](#2-model-routing) | [Jump](#2.%20Model%20routing) |
| **3. Invocation and integration limits** | [Jump](#3-invocation-and-integration-limits) | [Jump](#3.%20Invocation%20and%20integration%20limits) |
| **4. Storage and ownership** | [Jump](#4-storage-and-ownership) | [Jump](#4.%20Storage%20and%20ownership) |
| **5. Packaging and publication** | [Jump](#5-packaging-and-publication) | [Jump](#5.%20Packaging%20and%20publication) |
| **6. Readiness and legacy records** | [Jump](#6-readiness-and-legacy-records) | [Jump](#6.%20Readiness%20and%20legacy%20records) |
| **7. Self-contained lesson preparation** | [Jump](#7-self-contained-lesson-preparation) | [Jump](#7.%20Self-contained%20lesson%20preparation) |

## 1. Overview and skills

Private `uni-teach` plugin for the selected University Notes checkout. The primary vault is `/Users/slavomirhoricka/Desktop/University_notes`; isolated tasks use their actual worktree root for all workflow paths. Never redirect writes to the legacy vault or another checkout.

Four core skills: ingest verifies raw materials and creates finished notes; plan prepares versioned executable curriculum; teach conducts sessions and records actual learner evidence; recall derives dates and synchronizes review tasks through the separately installed **Todoist: To Do List & Calendar** harness.

The separate optional **html-course** skill turns checked notes and ready prepared lessons into English offline HTML with LaTeX, week-grouped contents and purposeful interaction. It runs only for an explicit HTML request and owns versioned exports in `02_Resources/HTML_Courses/<course_id>/`. It does not alter the four-stage workflow or write learner evidence.

## 2. Model routing

Follow `references/MODEL_ROUTING.md`: Sol High owns ingest/plan, Luna Medium drafts bounded sections and teaches prepared lessons, Luna Low runs recall, and independent Astra High agents review sources/curriculum. Skills dispatch owner agents when the host supports it; they cannot change the running chat model. Explicit user overrides take precedence. `agents/*.toml` contains supporting custom-agent configurations; packaging does not auto-install them.

Project copies are generated at `.codex/agents/` by the canonical synchronizer. If native profile selection is unavailable, use explicit spawn model/effort and profile instructions. Report capability limits honestly.

## 3. Invocation and integration limits

Ask to ingest an exact folder or repair explicitly named existing-note passages; plan a full course identity and bounded scope; teach/resume with a study budget; or synchronize committed reviews with Todoist. Missing/ambiguous project mappings require a unique existing project ID. No guessed course project, solution disclosure, task-completion mastery, or speculative learner records.

## 4. Storage and ownership

Storage/ownership and handoffs are in `LEARNING_ARCHITECTURE.md`; methodology evidence is in `references/LEARNING_METHODS.md`. Skill bodies contain ordinary execution rules. Runtime files belong in the local vault, never this installation: ingestion records in `03_Agents/runtime/ingest`; curriculum, learner log and recall state under `03_Agents/<year>/<semester>/<course>` with separate owners.

## 5. Packaging and publication

All five canonical skill folders live under `03_Agents/skills/{ingest,plan,teach,recall,html-course}/`. Shared source documentation lives in `03_Agents/docs/`; packaged shared references remain under `references/`, and the architecture remains at the package root. Package copies and the current versioned ZIP are generated and verified by `03_Agents/scripts/sync_plugin.py`. Changed snapshots require an unused version; explicit `--source-only` operations exclude ZIP generation/checking and preserve snapshots; account releases update the existing private plugin ID through Plugin Creator with a guarded release ID. Never edit versioned installation caches as durable source. Installation grants no vault access and starts no background execution.

Recall runs on explicit request or after a committed teach handoff when available. No additional push-notification system is required.

## 6. Readiness and legacy records

Legacy schema-1 history remains intact. New schema-3 readiness requires ingest completion/freshness state and reconciled prepared curriculum. Representative validation artifacts are not real learner evidence. Root portable manifest is authoritative packaging metadata; Codex compatibility manifest is generated with the same identity/interface/default prompts. Account update overlays preserve remote files: obsolete planning-template paths are explicit deprecation redirects, never a second maintained template.

## 7. Self-contained lesson preparation

Self-contained lesson preparation follows `references/LESSON_CONTENT.md`. Ingest supplies complete notes; plan reuses full explanations, orders instruction and designs the main exercises/solutions. Teach may answer questions, follow relevant tangents and add checked exercises within unchanged objectives and criteria. Existing curricula migrate on substantive revision; actual learner history remains intact.

## Student-facing HTML lessons

The optional HTML-course skill uses a numbered outline before the introduction, bullet learning objectives and definitions, readable complete explanations, structured practice with reasoning hints, and locally checked four-option quizzes. Lesson dropdowns, course switching and optional source disclosures keep the reading flow focused. The maintained presentation contract is in `skills/html-course/references/student_presentation.md`; notes, prepared assessment criteria and learner evidence retain their existing owners.
