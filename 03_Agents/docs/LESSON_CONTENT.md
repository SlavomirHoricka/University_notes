# Lesson content and teaching flexibility

## Contents

| Section | GitHub | Obsidian |
|---|---|---|
| **1. Purpose and boundaries** | [Jump](#1-purpose-and-boundaries) | [Jump](#1.%20Purpose%20and%20boundaries) |
| **2. Ownership and content reuse** | [Jump](#2-ownership-and-content-reuse) | [Jump](#2.%20Ownership%20and%20content%20reuse) |
| Content ownership and reuse | [Jump](#content-ownership-and-reuse) | [Jump](#Content%20ownership%20and%20reuse) |
| **3. Preparation and freshness** | [Jump](#3-preparation-and-freshness) | [Jump](#3.%20Preparation%20and%20freshness) |
| Preparation, freshness and review | [Jump](#preparation-freshness-and-review) | [Jump](#Preparation%2C%20freshness%20and%20review) |
| **4. Teaching adaptations** | [Jump](#4-teaching-adaptations) | [Jump](#4.%20Teaching%20adaptations) |
| Teach adaptation and questions | [Jump](#teach-adaptation-and-questions) | [Jump](#Teach%20adaptation%20and%20questions) |
| **5. Generated exercises and assessment** | [Jump](#5-generated-exercises-and-assessment) | [Jump](#5.%20Generated%20exercises%20and%20assessment) |
| Additional exercises during teaching | [Jump](#additional-exercises-during-teaching) | [Jump](#Additional%20exercises%20during%20teaching) |
| **6. Persistence and compatibility** | [Jump](#6-persistence-and-compatibility) | [Jump](#6.%20Persistence%20and%20compatibility) |
| Persistence and recall compatibility | [Jump](#persistence-and-recall-compatibility) | [Jump](#Persistence%20and%20recall%20compatibility) |

## 1. Purpose and boundaries

Contract `self-contained-lessons-v1`, agreed 2026-10-17. Read this with plan when preparing/reconciling lessons, and with teach when adapting a lesson, generating an item or assessing an alternative method. It changes content preparation and bounded teaching flexibility, not artifact ownership or evidence standards.

## 2. Ownership and content reuse

### Content ownership and reuse

#### Ingest-owned notes

Ingest produces high-quality source-grounded notes, explanations, derivations, visuals and source exercises. It does not prepare a second executable curriculum or a bespoke assessment bank. Its existing source verification and full-scope review remain mandatory.

#### Plan-owned full-content reuse

Plan arranges that content into self-contained lessons. Embed the complete relevant explanation, derivation and worked example from the notes; a locator or short excerpt cannot replace reasoning needed to teach the objective. Record exact note origin and fingerprint in the manifest. Reuse good content rather than independently rewriting it. Select coherent passages instead of copying unrelated chapters.

#### Language, notation and assets

Preserve language and notation by default. Plan may split steps, insert checkpoints, explain intermediate steps and map inconsistent notation explicitly, preserving the argument, assumptions and limits. Figures must be embedded and usable with necessary captions/interpretation; verify their asset paths. A lesson must be deliverable without opening its original notes.

Necessary prerequisites may route to another complete prepared lesson rather than repeating all foundations.

#### Main exercise preparation

Plan designs the main exercise progression and complete checked solutions, including diagnostics, completion tasks, independent and delayed checks. It may reuse a source exercise or hide steps in an existing worked example to make a completion task; identify the origin and retain a full key. Merely pointing at a source exercise is not preparation.

#### Verified plan additions

Plan may create missing intuition, explanations, derivations and examples within the requested scope. Mark each substantive block as reused, adapted or plan-created with its basis. Derivations/consequences established from checked notes need their reasoning; additional academic claims need actually consulted authoritative sources and precise citations. Consult those sources without routine permission, subject to host access restrictions.

Record bibliographic identity, URL/section, relevant claim/assumptions and a sufficient verified passage summary in the lesson/manifest. If verification is unavailable, qualify or block that addition; do not invent support. Supplementary explanation does not silently expand assessed course scope; only necessary prerequisites or explicitly requested broader learning may extend it.

#### Academic issues and teaching bridges

Actual note contradictions, erroneous claims, unreadable content or missing ingestion provenance return to ingest and block affected content only. A missing teaching bridge is plan's work, not automatically an ingestion failure. Plan never repairs notes, audits original course materials or imports additions into notes automatically. New explanations remain in lessons initially.

#### Misconceptions and feedback

Plan defines expected error signs, criteria and correction routes to included explanations or prepared prerequisite lessons. Teach phrases responsive hints/feedback from that content; plan need not script every feedback sentence.

## 3. Preparation and freshness

### Preparation, freshness and review

Prepare the complete requested bounded topic/week before teaching. For a whole course, establish the complete coverage/dependency route and prepare bounded units progressively; label unprepared units blocked and the plan partial. Never call the entire course ready from a ready first unit.

After successful committed ingestion, invoke plan reconciliation for affected notes in the same authorized workflow unless the user limits scope. This is a sequential handoff, not a watcher. Inspect semantic changes and update copied passages, keys and affected dependencies. Formatting or unrelated additions do not require academic rewriting, but metadata/transaction freshness must still match before use.

Preserve immutable prior definitions and actual learner evidence; no automatic regrading or mastery. Existing curricula remain intact until their next substantive revision; valid older schema-3 bundles retain their existing gates. An ingestion change still requires normal freshness reconciliation. On substantive revision adopt this contract; do not mass-migrate courses or rewrite logs.

The independent curriculum checker verifies complete reused content against notes, adaptations and all added reasoning/cited authoritative support, self-contained delivery including assets, every prepared assessment route, generation boundaries, compatibility and history. It may consult the cited authoritative sources to verify additions; it does not audit original course materials or write files. Missing review/material findings block affected readiness.

## 4. Teaching adaptations

### Teach adaptation and questions

Teach presents full explanations within the conversation, rather than sending the learner to read a note. It may rephrase, split steps, adjust pace, skip justified support, revisit prerequisites, select tasks and reorder independent topics while preserving dependencies, coverage and standards. Record the route/stopping point and any deferred scope.

Answer unexpected questions and follow short relevant tangents, then return to the route. Establish answers from the lesson/notes; verify additional academic claims with authoritative sources and record their basis as actual instruction/exposure. If verification fails, state uncertainty and defer the unsupported claim. Consequential lesson gaps return to plan, actual note errors to ingest.

Teach does not edit either artifact or expand assessed objectives.

## 5. Generated exercises and assessment

### Additional exercises during teaching

#### Permitted scope

Teach may create a further example, completion task or practice/check item for an existing objective and established method. New objectives/methods or substantial prerequisite design return to plan. Prefer prepared items; exhaustion alone need not stop an otherwise supported lesson.

#### Verification and frozen contract

Before displaying a generated prompt, solve and check it, establish its essential components, acceptable reasoning, critical errors and outcome rules against the existing criterion. For difficult or uncertain solutions request the read-only assessor and wait; if unresolved, do not present it as a scored check.

Persist an immutable `item_contract` within the teach-owned `attempt_started` event, with `item_origin: teach_generated`, stable item ID/version, exact prompt, complete solution, rubric, component IDs, item role, task relation, source basis and verification. This is a session item snapshot, not a new plan definition or file. Do not send its key/rubric to the learner before their answer. Release locks while waiting.

Reusing its identity requires identical contract content.

#### Eligibility for evidence

Generated checks may count toward acquisition or delayed evidence only if they cover the existing role/components and satisfy the unchanged rule and all independence, freshness and timing conditions. Record that mapping before the answer; do not count a narrow corrective item as a full check.

Existing rules naming exact item IDs or a reassessment requirement remain binding: a generated item cannot substitute unless the published rule expressly permits it. Legacy bundles without such permission keep their rules. No new learner result is created merely by generating/verifying a question.

#### Alternative methods and fixed criteria

Assess against the committed pre-answer contract. An alternative valid solution may receive credit when it meets the existing essential criteria, even if absent from the listed methods. Establish equivalence and record an `assessment_basis`; use the stronger assessor for difficult/uncertain reasoning. Do not change the pre-answer criteria to fit a response.

Missing/ambiguous criteria or an alternative requiring a different standard is unscorable and returns to plan. Preserve the actual answer and uncertainty; reasoning discussion remains possible as separately recorded feedback/exposure.

## 6. Persistence and compatibility

### Persistence and recall compatibility

Use existing schema-3 events and owner-scoped transactions. Optional `item_origin`, `item_contract` and `assessment_basis` fields are additive; no event type or scheduling algorithm changes. Results carry the same attempt/item/version tuple and reference their frozen start event. Recall consumes committed outcomes and plan-defined rules without grading generated keys. Generated items cannot bypass named reassessment gates.

Never rewrite earlier attempts or criteria; scoring corrections remain append-only.
