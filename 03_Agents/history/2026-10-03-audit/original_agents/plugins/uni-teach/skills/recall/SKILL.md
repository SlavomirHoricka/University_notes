---
name: recall
description: Find due Uni course reviews, schedule the next spaced review, or prepare an actionable reminder from the learning plan and observed learning log. Do not teach, grade, or edit the plan.
---

# Recall

Read the course learning plan and committed learning log. Work per objective ID and criterion version. You may append schedule_proposal or schedule_update events to learning_log.md; never edit learning_plan.md, source_manifest.md, course notes, learner answers, or grades. A scheduled or missed review is not evidence of learning.

Follow the course lock and append-only write rules in 03_Agents/LEARNING_ARCHITECTURE.md when recording proposals.

## Review intervals

Use an SM-2-style baseline: after an objective first meets its independent criterion, schedule a delayed review in 1 day; after the first successful unaided delayed review, 6 days; after later successful unaided reviews, round the preceding interval × 2.5 days, increasing by at least one day. After an incorrect, partial, or assisted delayed response, request corrective teaching and a fresh practice item, then schedule a new review in 1 day. Use the actual Europe/Prague answer date. A review overdue with no answer stays due unchanged; after a correct overdue answer, calculate from that answer date. Use scripts/schedule.py for date arithmetic.

Only observed, committed attempt results can advance or reset an interval. A newly changed criterion or source gate calls for reassessment before extending a review interval. A topic not yet independently learned belongs in a continuation queue, not the delayed-recall schedule. Keep one active proposal per objective; if the latest proposal already cites the latest result event, do not create another. Supersede an old proposal after a new result rather than duplicating reminders.

## Due queue and reminders

List due and overdue objectives with course, objective title, due date, why each is due, and a short invitation to start a review session. Prioritize overdue prerequisites and weak objectives; keep the queue manageable. Use a prepared delayed prompt from the plan when the learner starts the review, then let the teach skill conduct and log the answer.

If the user asks to activate notifications, use an available host reminder or automation capability and the requested cadence. Do not claim that a schedule proposal alone sent a notification. Avoid repeating unchanged reminders. The reminder should name the objective and offer a direct start action; it must not reveal the answer.

Source for baseline: [Anki's deck options](https://docs.ankiweb.net/deck-options) document a 2.5 starting ease and one-day minimum lapse interval, while [SM-2](https://www-beta.supermemo.com/archives1990-2015/english/ol/sm2) specifies 1-day and 6-day first intervals. These are transparent defaults, not a personal optimum.
