CREATE TABLE grading_results (
  result_id TEXT PRIMARY KEY NOT NULL,
  attempt_id TEXT NOT NULL REFERENCES attempts(attempt_id),
  decision_revision INTEGER NOT NULL CHECK(decision_revision>0),
  decision TEXT NOT NULL CHECK(json_valid(decision)),
  decision_digest TEXT NOT NULL CHECK(length(decision_digest)=64 AND decision_digest NOT GLOB '*[^0-9a-f]*'),
  supersedes_result_id TEXT REFERENCES grading_results(result_id),
  evidence_commit_id TEXT NOT NULL REFERENCES evidence_commits(commit_id),
  created_at TEXT NOT NULL,
  UNIQUE(attempt_id,decision_revision),
  CHECK(supersedes_result_id IS NULL OR supersedes_result_id!=result_id)
) STRICT;
CREATE TRIGGER grading_results_result_requires_response_verified_commit_insert BEFORE INSERT ON grading_results WHEN NOT EXISTS(SELECT 1 FROM responses WHERE attempt_id=NEW.attempt_id) OR NOT EXISTS(SELECT 1 FROM evidence_commits ec JOIN evidence_outbox eo ON eo.intent_id=ec.intent_id JOIN receipts r ON r.receipt_id=eo.receipt_id JOIN attempts a ON a.attempt_id=NEW.attempt_id WHERE ec.commit_id=NEW.evidence_commit_id AND eo.session_id=a.session_id AND (r.aggregate_id=a.attempt_id OR r.aggregate_id=a.assessment_id)) BEGIN SELECT RAISE(ABORT,'result_requires_response_verified_commit'); END;
CREATE TRIGGER grading_results_result_requires_response_verified_commit_update BEFORE UPDATE ON grading_results WHEN NOT EXISTS(SELECT 1 FROM responses WHERE attempt_id=NEW.attempt_id) OR NOT EXISTS(SELECT 1 FROM evidence_commits ec JOIN evidence_outbox eo ON eo.intent_id=ec.intent_id JOIN receipts r ON r.receipt_id=eo.receipt_id JOIN attempts a ON a.attempt_id=NEW.attempt_id WHERE ec.commit_id=NEW.evidence_commit_id AND eo.session_id=a.session_id AND (r.aggregate_id=a.attempt_id OR r.aggregate_id=a.assessment_id)) BEGIN SELECT RAISE(ABORT,'result_requires_response_verified_commit'); END;
CREATE TRIGGER grading_results_correction_attempt_mismatch_insert BEFORE INSERT ON grading_results WHEN NEW.supersedes_result_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM grading_results WHERE result_id=NEW.supersedes_result_id AND attempt_id=NEW.attempt_id AND decision_revision<NEW.decision_revision) BEGIN SELECT RAISE(ABORT,'correction_attempt_mismatch'); END;
CREATE TRIGGER grading_results_correction_attempt_mismatch_update BEFORE UPDATE ON grading_results WHEN NEW.supersedes_result_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM grading_results WHERE result_id=NEW.supersedes_result_id AND attempt_id=NEW.attempt_id AND decision_revision<NEW.decision_revision) BEGIN SELECT RAISE(ABORT,'correction_attempt_mismatch'); END;
CREATE TRIGGER grading_results_no_update BEFORE UPDATE ON grading_results BEGIN SELECT RAISE(ABORT,'immutable_grading_results'); END;
CREATE TRIGGER grading_results_no_delete BEFORE DELETE ON grading_results BEGIN SELECT RAISE(ABORT,'immutable_grading_results'); END;
DROP TRIGGER assessments_final_results_unavailable_until_v3_insert;
DROP TRIGGER assessments_final_results_unavailable_until_v3_update;
CREATE TRIGGER assessments_assessment_final_result_mismatch_insert BEFORE INSERT ON assessments WHEN NEW.final_result_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM grading_results g JOIN attempts a ON a.attempt_id=g.attempt_id JOIN evidence_commits e ON e.commit_id=g.evidence_commit_id WHERE g.result_id=NEW.final_result_id AND a.assessment_id=NEW.assessment_id AND a.session_id=NEW.session_id AND NEW.status='finalized') BEGIN SELECT RAISE(ABORT,'assessment_final_result_mismatch'); END;
CREATE TRIGGER assessments_assessment_final_result_mismatch_update BEFORE UPDATE ON assessments WHEN NEW.final_result_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM grading_results g JOIN attempts a ON a.attempt_id=g.attempt_id JOIN evidence_commits e ON e.commit_id=g.evidence_commit_id WHERE g.result_id=NEW.final_result_id AND a.assessment_id=NEW.assessment_id AND a.session_id=NEW.session_id AND NEW.status='finalized') BEGIN SELECT RAISE(ABORT,'assessment_final_result_mismatch'); END;
CREATE TABLE exposure_projection (
  projection_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  equivalence_id TEXT NOT NULL,
  objective_ref TEXT NOT NULL CHECK(json_valid(objective_ref)),
  canonical_event_id TEXT NOT NULL,
  time TEXT,
  timing_quality TEXT NOT NULL CHECK(timing_quality IN ('known','unknown','invalid_clock')),
  exposure_kind TEXT NOT NULL CHECK(exposure_kind IN ('prompt','worked_example','hint','solution','independent_study')),
  UNIQUE(course_key,canonical_event_id,equivalence_id)
) STRICT;
CREATE INDEX exposure_course_equivalence ON exposure_projection(course_key,equivalence_id);
CREATE TABLE variant_reservations (
  reservation_id TEXT PRIMARY KEY NOT NULL,
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  assessment_id TEXT REFERENCES assessments(assessment_id),
  equivalence_id TEXT NOT NULL,
  variant_ref TEXT NOT NULL CHECK(json_valid(variant_ref)),
  state TEXT NOT NULL CHECK(state IN ('reserved','offered','exposed','released')),
  created_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER variant_reservations_reservation_session_mismatch_insert BEFORE INSERT ON variant_reservations WHEN NEW.assessment_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM assessments WHERE assessment_id=NEW.assessment_id AND session_id=NEW.session_id) BEGIN SELECT RAISE(ABORT,'reservation_session_mismatch'); END;
CREATE TRIGGER variant_reservations_reservation_session_mismatch_update BEFORE UPDATE ON variant_reservations WHEN NEW.assessment_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM assessments WHERE assessment_id=NEW.assessment_id AND session_id=NEW.session_id) BEGIN SELECT RAISE(ABORT,'reservation_session_mismatch'); END;
CREATE UNIQUE INDEX one_live_variant ON variant_reservations(session_id,equivalence_id) WHERE state!='released';
CREATE TABLE review_projection (
  recommendation_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  canonical_cursor TEXT NOT NULL,
  recommendation TEXT NOT NULL CHECK(json_valid(recommendation)),
  rebuilt_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER review_projection_review_course_mismatch_insert BEFORE INSERT ON review_projection WHEN NOT EXISTS(SELECT 1 FROM courses WHERE course_key=NEW.course_key AND course_id=json_extract(NEW.recommendation,'$.course_id')) BEGIN SELECT RAISE(ABORT,'review_course_mismatch'); END;
CREATE TRIGGER review_projection_review_course_mismatch_update BEFORE UPDATE ON review_projection WHEN NOT EXISTS(SELECT 1 FROM courses WHERE course_key=NEW.course_key AND course_id=json_extract(NEW.recommendation,'$.course_id')) BEGIN SELECT RAISE(ABORT,'review_course_mismatch'); END;
CREATE TRIGGER exposure_projection_projection_course_mismatch_insert BEFORE INSERT ON exposure_projection WHEN NOT EXISTS(SELECT 1 FROM courses WHERE course_key=NEW.course_key AND course_id=json_extract(NEW.objective_ref,'$.course_id')) BEGIN SELECT RAISE(ABORT,'projection_course_mismatch'); END;
CREATE TRIGGER exposure_projection_projection_course_mismatch_update BEFORE UPDATE ON exposure_projection WHEN NOT EXISTS(SELECT 1 FROM courses WHERE course_key=NEW.course_key AND course_id=json_extract(NEW.objective_ref,'$.course_id')) BEGIN SELECT RAISE(ABORT,'projection_course_mismatch'); END;
CREATE TRIGGER variant_reservations_variant_course_mismatch_insert BEFORE INSERT ON variant_reservations WHEN NOT EXISTS(SELECT 1 FROM sessions s JOIN courses c USING(course_key) WHERE s.session_id=NEW.session_id AND c.course_id=json_extract(NEW.variant_ref,'$.course_id')) BEGIN SELECT RAISE(ABORT,'variant_course_mismatch'); END;
CREATE TRIGGER variant_reservations_variant_course_mismatch_update BEFORE UPDATE ON variant_reservations WHEN NOT EXISTS(SELECT 1 FROM sessions s JOIN courses c USING(course_key) WHERE s.session_id=NEW.session_id AND c.course_id=json_extract(NEW.variant_ref,'$.course_id')) BEGIN SELECT RAISE(ABORT,'variant_course_mismatch'); END;
