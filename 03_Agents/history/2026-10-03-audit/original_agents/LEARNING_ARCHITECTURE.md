# Uni learning architecture

Diagram: [[Learning Workflow Architecture]]

## Ownership

| Skill | Trigger | Reads | Writes |
|---|---|---|---|
| **ingest** | New or changed course material; a request to repair notes | Raw material, existing notes, ingestion records | Finished source-grounded notes and ingestion records |
| **plan** | Create a course plan; ingest changed relevant notes; a tutor flags a plan gap | Finished notes, existing plan and log | Learning plan and note-version manifest |
| **teach** | Learn, practise, revise, or resume a topic | Relevant finished notes, learning plan, committed log | Actual learner events and current session state in the learning log |
| **recall** | Check due reviews, prepare reminders, reschedule after an observed review | Learning plan and committed log | Schedule proposals or updates in the log; reminders when enabled |

Ingest is the only skill that creates or corrects notes. Once an ingestion pass is complete, plan and teach treat its notes as the canonical course content. They do not re-audit raw material. A discovered contradiction is flagged for ingest to resolve; the other skills do not silently rewrite notes.

Plan is the only writer of learning_plan.md and source_manifest.md. It turns finished notes into stable objective IDs, a justified sequence, success criteria, worked-example references, short teaching steps, and fresh immediate and delayed prompts. It preserves prior objective and criterion versions when notes change. It may read learner evidence to identify a missing prerequisite or an unusable assessment, but it does not invent learner outcomes.

Teach is intended for a lighter, faster model. It uses the prepared route and only the note sections needed for the current step. It may adapt explanations, choose a fresh equivalent question, and record actual attempts, feedback, help, exposure, and stopping point. It does not create objectives, inspect raw source quality, rehash course files, or edit the plan. If the plan is absent, stale, or insufficient for a sound lesson, it records the issue and routes the request to plan.

Recall is a scheduler and reminder skill. It never grades an answer or marks a review complete. A due review remains pending until a teaching session records the learner's response. Reminders include the objective, reason it is due, and a direct prompt to begin a short review.

## Scheduling baseline

Use a simple SM-2-style baseline per objective. Schedule the first delayed review **1 day** after the objective reaches its recorded independent criterion; after the first successful delayed review, **6 days**; after later successful unaided reviews, approximately **2.5 ×** the previous interval, rounded to a whole day. These are starting defaults, not a claim about an optimal personal interval. Dates use Europe/Prague and the actual response date.

An incorrect, partial, or assisted delayed answer triggers corrective teaching and a fresh practice item, then a new review **1 day** later. An overdue review with no answer remains due and does not change learner status. A correct overdue answer advances from the observed answer date. Keep source-change gates and exam deadlines visible when selecting the next task. [Anki deck options](https://docs.ankiweb.net/deck-options) describe the 2.5 starting ease and one-day lapse default; [SM-2](https://www-beta.supermemo.com/archives1990-2015/english/ol/sm2) defines the one-day and six-day first intervals.

## Plugin and model use

The existing private uni-teach plugin packages four skills. Their descriptions let the host choose the relevant workflow for a user request. Skill selection does not itself change the model: run ingest and plan with a highly capable model, and select a lighter model for routine teach and recall sessions. This keeps expensive curriculum reasoning out of each tutoring turn.

No new database is required. Course records stay under 03_Agents/{year}/{semester}/{course}/: plan for curriculum, log for learner evidence and schedule proposals, manifest for note versions. Existing learner history remains intact. Legacy learner-status fields in old plans stay read-only; teach derives current status from committed log events, and the next plan revision omits those fields from new objective definitions.

All writers use the course's .learning-write.lock, reread the affected file and revision after acquiring it, and replace the file atomically. Event IDs are stable and log history is append-only. A writer encountering a held lock or unexpected revision preserves its pending change and retries or reports the conflict; it does not overwrite another writer's work.

## Rollout

1. [x] Publish the multi-skill plugin and use the new ownership contract for new courses.
2. [ ] On the next planning run for an existing course, reconcile its legacy plan against committed log events before revising objectives.
3. [ ] Turn on external reminders after choosing a delivery channel and cadence. The recall skill can compute a due queue without notifications.
