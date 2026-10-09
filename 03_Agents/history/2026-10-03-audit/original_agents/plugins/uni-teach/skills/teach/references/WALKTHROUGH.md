# Behavioral walkthrough — fictional scenarios only

> Historical examples for the prior tutor-owned plan protocol. The current plan, teach, and recall skills supersede its ownership assumptions.

These are desk-check cases for the skill, not sessions conducted with the learner. Objective IDs, results, dates, and events below are invented test inputs. Nothing here belongs in a real course log. No course plan was populated during this review.

## Folder-entry checks

**Fictional request:** “Teach me this week's content” with `Week_02/` containing a median lesson. The supplied week folder sets the scope, without needing a calendar mapping. Resolve its parent course, initialize that course's three records, and ask one prerequisite/application question. Do not ask the learner to configure the plan, select a teaching method, or confirm the week again. No answer has yet been observed.

**Fictional alternative:** the same request points at a course root with undated `Week_01/` and `Week_02/` lessons, and no schedule or history. Ask which week they mean, naming those two choices. Do not pick Week 2 because it sorts last or has a newer modification time. Once answered, do the setup automatically.

**Fictional dated case:** on 2026-10-02, course content dated 2026-09-30 belongs to the current Monday–Sunday week (2026-09-28 through 2026-10-04); content dated 2026-09-23 does not. A relevant course schedule may establish the week mapping; import timestamps cannot.

## 1. First use

**Hypothetical request:** “Teach me why OLS is BLUE,” with the Econometrics I folder.

Resolve the hub and Gauss–Markov note; inspect its source assumptions and only relevant prerequisites. Inventory the course's materials and linked prerequisites without treating every related concept as required. Create a provisional plan and source baseline in that course only. All objectives begin unassessed. Briefly state the plan; ask an unaided explanation or small application that discriminates the needed prerequisites. If the response shows no foothold, explain and use an example; if adequate, advance within the requested scope. Do not ask progressively harder questions until failure. The actual response is still awaited: this walkthrough supplies none.

**Result to verify:** no fabricated learner evidence, no unconditional “OLS is always best,” no duplicate hub, and source coverage distinct from learner state.

## 2. Resumption with unchanged sources

**Fictional starting state:** O001 has two qualifying independent checks from a prior session, retention pending; O002 is practicing. Hashes and paths match.

Read current state and events after its last commit, compare source inventory, and retain the plan. If a delayed O001 review is relevant/due, ask it before re-explaining. Record elapsed time from actual attempts and known exposures; unknown independent restudy qualifies the interpretation. Continue O002 from its saved step. Do not reset diagnosis for the whole course or require a new plan approval.

**Result to verify:** unchanged bytes require no content-change retest, but do not cancel an ordinary pending retention check. A correct delayed response would support only that observed interval; it is not supplied here.

## 3. Added lecture material

**Fictional input:** a new lecture PDF appears in the watched materials directory without a hub link.

Enumeration detects the addition. Hash and inspect relevant pages; if unreadable, record a coverage gap. Compare its content with existing objectives. New topic: add O003 unassessed, update plan/source versions and probe prerequisites or prior familiarity without calling new material “forgotten.” Extension of learned O001: preserve its old evidence but create a required reassessment gate for the changed scope and downstream prerequisites as justified. A lecture outside the selected topic can remain a documented deferred candidate.

**Result to verify:** additions need not be linked to be detected; inspection determines impact rather than the filename or hash.

## 4. Substantive correction to learned content

**Fictional input:** a previously taught unconditional claim is corrected to include an assumption; the old semantic digest and criterion establish what was taught.

Record the changed claim, old/new hash and criterion, acknowledge the previous error, and identify dependent objectives. Keep the old attempts under their old versions. Explain the correction, then assess the revised distinction with a fresh unassisted case; immediate success still leaves a delayed need. If the learner declines, the gate becomes deferred and dependent advancement remains blocked; offer unrelated work or clearly supported explanation. Do not silently mark the correction learned because it was displayed.

**Result to verify:** a local correction does not erase unrelated evidence or grant mastery of the revised claim.

## 5. Formatting-only edits or a rename

**Fictional input:** a note's heading style changes and its file moves.

Hashes/paths trigger inspection. For a pure move, identical bytes support identity if not duplicated elsewhere. A move plus edit needs matching content/metadata; uncertainty remains explicit. Compare formulas, conditions, links and criteria with the retained semantic baseline before classifying formatting-only. Refresh locators, source version and dated change event; retain criterion and evidence. No content exam. If the old digest omitted the changed passage, classify impact uncertain and inspect further instead of assuming harmlessness.

**Result to verify:** neither hash inequality nor a renamed filename is a learner error.

## 6. Missing source or history

**Fictional input A:** plan claims independence but log/manifest is missing. Establish today's baseline; label old change history unknown and old status unsupported. A short current diagnostic may support a new decision but cannot recreate old attempt dates or certify historical retention.

**Fictional input B:** a source PDF disappeared. Record a tombstone and distinguish intentional scope removal from missing authoritative material. Keep evidence and retire objectives only with a documented scope decision. If correctness cannot be verified, block affected claims and continue unaffected work. File read permission failure is an access gap, not proof of deletion.

**Result to verify:** unknown history stays unknown; missing notes do not imply absent learner knowledge.

## 7. Interrupted session and concurrent scheduling

**Fictional input:** the last saved event starts an assessment; no response is persisted. A scheduler later adds a proposed review date.

Acquire the shared course lock, reread fresh files, and preserve the scheduler's append. Rebuild state from committed events after the old summary pointer. Treat the assessment as incomplete, not wrong or passed. Resume it if unexposed, or choose a fresh variant if a solution was shown. Record recovery time; interruption time remains unknown. If a result exists in an uncommitted transaction, reconcile that transaction before using it. Preserve a committed result even if the summary is stale. Never infer an unsaved answer from a planned next step.

**Result to verify:** the tutor owns the summary, the scheduler owns its proposal events, and no replacement overwrites the other's work. A planned review never becomes a completed session automatically.

## Additional stopping and scoring cases

- A useful diagnostic answer establishes the next teaching step: stop diagnosis instead of asking more questions to find a failure.
- Two hints followed by success: record assisted success; use a fresh independent task before changing status.
- An answer includes a valid alternative method: judge the rubric's essential criteria, not similarity to the tutor's model answer.
- Three unsuccessful assessment attempts: stop repeated testing, teach or pause; record the unresolved objective.
- Concurrent user edit despite the cooperative lock: hash mismatch stops the replacement. Reconcile without discarding that edit.
- Unknown note access: retain the observed answer but do not certify it as unaided closed-note retrieval.

## Validation scope

These scenarios trace the written rules; they are not an empirical trial of the tutor or a test of long-term learner outcomes. Future evaluation should use actual teaching sessions and assess independent work, later retention and changed-context tasks, while tracking time burden and unnecessary questioning.
