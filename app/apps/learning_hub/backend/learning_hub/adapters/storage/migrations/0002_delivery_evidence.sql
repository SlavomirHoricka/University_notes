CREATE TABLE commands (
  command_id TEXT PRIMARY KEY NOT NULL,
  local_principal TEXT NOT NULL,
  kind TEXT NOT NULL,
  idempotency_key TEXT NOT NULL,
  request_digest TEXT NOT NULL CHECK(length(request_digest)=64 AND request_digest NOT GLOB '*[^0-9a-f]*'),
  aggregate_id TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('accepted','completed','blocked')),
  response_status INTEGER NOT NULL CHECK(response_status BETWEEN 100 AND 599),
  replay_response TEXT NOT NULL CHECK(json_valid(replay_response)),
  created_at TEXT NOT NULL,
  UNIQUE(local_principal,kind,idempotency_key)
) STRICT;
CREATE UNIQUE INDEX command_idempotency ON commands(local_principal,kind,idempotency_key);
CREATE TRIGGER commands_fixed_refs BEFORE UPDATE ON commands WHEN NEW.command_id IS NOT OLD.command_id OR NEW.local_principal IS NOT OLD.local_principal OR NEW.kind IS NOT OLD.kind OR NEW.idempotency_key IS NOT OLD.idempotency_key OR NEW.request_digest IS NOT OLD.request_digest OR NEW.aggregate_id IS NOT OLD.aggregate_id OR NEW.created_at IS NOT OLD.created_at BEGIN SELECT RAISE(ABORT,'immutable_reference_commands'); END;
CREATE TABLE sessions (
  session_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  bundle_id TEXT NOT NULL REFERENCES bundles(bundle_id),
  route_kind TEXT NOT NULL CHECK(route_kind IN ('lesson','lesson_quiz','weekly_test','corrective_refresh','retention_check','reassessment')),
  route_ref TEXT NOT NULL CHECK(json_valid(route_ref)),
  status TEXT NOT NULL CHECK(status IN ('active','paused','closed','validity_hold')),
  revision INTEGER NOT NULL CHECK(revision>0),
  bookmark TEXT NOT NULL CHECK(json_valid(bookmark)),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER sessions_session_bundle_course_mismatch_insert BEFORE INSERT ON sessions WHEN NOT EXISTS(SELECT 1 FROM bundles WHERE bundle_id=NEW.bundle_id AND course_key=NEW.course_key) BEGIN SELECT RAISE(ABORT,'session_bundle_course_mismatch'); END;
CREATE TRIGGER sessions_session_bundle_course_mismatch_update BEFORE UPDATE ON sessions WHEN NOT EXISTS(SELECT 1 FROM bundles WHERE bundle_id=NEW.bundle_id AND course_key=NEW.course_key) BEGIN SELECT RAISE(ABORT,'session_bundle_course_mismatch'); END;
CREATE TRIGGER sessions_fixed_refs BEFORE UPDATE ON sessions WHEN NEW.session_id IS NOT OLD.session_id OR NEW.course_key IS NOT OLD.course_key OR NEW.bundle_id IS NOT OLD.bundle_id OR NEW.route_kind IS NOT OLD.route_kind OR NEW.route_ref IS NOT OLD.route_ref OR NEW.created_at IS NOT OLD.created_at BEGIN SELECT RAISE(ABORT,'immutable_reference_sessions'); END;
CREATE TABLE assessments (
  assessment_id TEXT PRIMARY KEY NOT NULL,
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  prepared_ref TEXT NOT NULL CHECK(json_valid(prepared_ref)),
  blueprint_digest TEXT NOT NULL CHECK(length(blueprint_digest)=64 AND blueprint_digest NOT GLOB '*[^0-9a-f]*'),
  selected_items TEXT NOT NULL CHECK(json_valid(selected_items)),
  selection_seed TEXT NOT NULL,
  algorithm_version TEXT NOT NULL,
  status TEXT NOT NULL CHECK(status IN ('assembling','active','submitted','grading_pending','finalized','unscorable','validity_hold','abandoned')),
  revision INTEGER NOT NULL CHECK(revision>0),
  submitted_at TEXT,
  final_result_id TEXT
) STRICT;
CREATE TRIGGER assessments_final_results_unavailable_until_v3_insert BEFORE INSERT ON assessments WHEN NEW.final_result_id IS NOT NULL BEGIN SELECT RAISE(ABORT,'final_results_unavailable_until_v3'); END;
CREATE TRIGGER assessments_final_results_unavailable_until_v3_update BEFORE UPDATE ON assessments WHEN NEW.final_result_id IS NOT NULL BEGIN SELECT RAISE(ABORT,'final_results_unavailable_until_v3'); END;
CREATE TRIGGER assessments_fixed_refs BEFORE UPDATE ON assessments WHEN NEW.assessment_id IS NOT OLD.assessment_id OR NEW.session_id IS NOT OLD.session_id OR NEW.prepared_ref IS NOT OLD.prepared_ref OR NEW.blueprint_digest IS NOT OLD.blueprint_digest OR NEW.selection_seed IS NOT OLD.selection_seed OR NEW.algorithm_version IS NOT OLD.algorithm_version BEGIN SELECT RAISE(ABORT,'immutable_reference_assessments'); END;
CREATE TRIGGER assessment_selection_frozen BEFORE UPDATE ON assessments WHEN OLD.status!='assembling' AND NEW.selected_items IS NOT OLD.selected_items BEGIN SELECT RAISE(ABORT,'assessment_selection_frozen'); END;
CREATE TABLE attempts (
  attempt_id TEXT PRIMARY KEY NOT NULL,
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  assessment_id TEXT REFERENCES assessments(assessment_id),
  item_ref TEXT NOT NULL CHECK(json_valid(item_ref)),
  equivalence_id TEXT NOT NULL,
  previous_attempt_id TEXT REFERENCES attempts(attempt_id),
  status TEXT NOT NULL CHECK(status IN ('started','response_received','grading_pending','assessed','evidence_committed','feedback_available','abandoned','unscorable','validity_hold')),
  revision INTEGER NOT NULL CHECK(revision>0),
  created_at TEXT NOT NULL,
  CHECK(previous_attempt_id IS NULL OR previous_attempt_id!=attempt_id)
) STRICT;
CREATE TRIGGER attempts_attempt_assessment_session_mismatch_insert BEFORE INSERT ON attempts WHEN NEW.assessment_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM assessments WHERE assessment_id=NEW.assessment_id AND session_id=NEW.session_id) BEGIN SELECT RAISE(ABORT,'attempt_assessment_session_mismatch'); END;
CREATE TRIGGER attempts_attempt_assessment_session_mismatch_update BEFORE UPDATE ON attempts WHEN NEW.assessment_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM assessments WHERE assessment_id=NEW.assessment_id AND session_id=NEW.session_id) BEGIN SELECT RAISE(ABORT,'attempt_assessment_session_mismatch'); END;
CREATE TRIGGER attempts_retry_course_mismatch_insert BEFORE INSERT ON attempts WHEN NEW.previous_attempt_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM attempts p JOIN sessions s ON s.session_id=p.session_id JOIN sessions n ON n.session_id=NEW.session_id WHERE p.attempt_id=NEW.previous_attempt_id AND s.course_key=n.course_key) BEGIN SELECT RAISE(ABORT,'retry_course_mismatch'); END;
CREATE TRIGGER attempts_retry_course_mismatch_update BEFORE UPDATE ON attempts WHEN NEW.previous_attempt_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM attempts p JOIN sessions s ON s.session_id=p.session_id JOIN sessions n ON n.session_id=NEW.session_id WHERE p.attempt_id=NEW.previous_attempt_id AND s.course_key=n.course_key) BEGIN SELECT RAISE(ABORT,'retry_course_mismatch'); END;
CREATE TRIGGER attempts_attempt_pinned_tuple_mismatch_insert BEFORE INSERT ON attempts WHEN NOT EXISTS(SELECT 1 FROM sessions s JOIN courses c USING(course_key) JOIN bundles b ON b.bundle_id=s.bundle_id WHERE s.session_id=NEW.session_id AND json_extract(NEW.item_ref,'$.course_id')=c.course_id AND json_extract(NEW.item_ref,'$.plan_version')=b.plan_version AND json_extract(NEW.item_ref,'$.source_version')=b.source_version AND json_extract(NEW.item_ref,'$.ingestion_revision')=b.ingestion_revision) BEGIN SELECT RAISE(ABORT,'attempt_pinned_tuple_mismatch'); END;
CREATE TRIGGER attempts_attempt_pinned_tuple_mismatch_update BEFORE UPDATE ON attempts WHEN NOT EXISTS(SELECT 1 FROM sessions s JOIN courses c USING(course_key) JOIN bundles b ON b.bundle_id=s.bundle_id WHERE s.session_id=NEW.session_id AND json_extract(NEW.item_ref,'$.course_id')=c.course_id AND json_extract(NEW.item_ref,'$.plan_version')=b.plan_version AND json_extract(NEW.item_ref,'$.source_version')=b.source_version AND json_extract(NEW.item_ref,'$.ingestion_revision')=b.ingestion_revision) BEGIN SELECT RAISE(ABORT,'attempt_pinned_tuple_mismatch'); END;
CREATE TRIGGER attempts_fixed_refs BEFORE UPDATE ON attempts WHEN NEW.attempt_id IS NOT OLD.attempt_id OR NEW.session_id IS NOT OLD.session_id OR NEW.assessment_id IS NOT OLD.assessment_id OR NEW.item_ref IS NOT OLD.item_ref OR NEW.equivalence_id IS NOT OLD.equivalence_id OR NEW.previous_attempt_id IS NOT OLD.previous_attempt_id OR NEW.created_at IS NOT OLD.created_at BEGIN SELECT RAISE(ABORT,'immutable_reference_attempts'); END;
CREATE TABLE assessment_drafts (
  assessment_id TEXT NOT NULL REFERENCES assessments(assessment_id),
  item_id TEXT NOT NULL,
  attempt_id TEXT NOT NULL REFERENCES attempts(attempt_id),
  draft_revision INTEGER NOT NULL CHECK(draft_revision>0),
  response TEXT CHECK(response IS NULL OR json_valid(response)),
  explicit_blank INTEGER NOT NULL CHECK(explicit_blank IN (0,1)),
  reported_conditions TEXT CHECK(reported_conditions IS NULL OR json_valid(reported_conditions)),
  updated_at TEXT NOT NULL,
  PRIMARY KEY(assessment_id,item_id),
  CHECK((response IS NULL AND explicit_blank=1) OR (response IS NOT NULL AND explicit_blank=0))
) STRICT;
CREATE TRIGGER assessment_drafts_draft_not_active_selected_weekly_item_insert BEFORE INSERT ON assessment_drafts WHEN NOT EXISTS(SELECT 1 FROM assessments a JOIN attempts t ON t.assessment_id=a.assessment_id WHERE a.assessment_id=NEW.assessment_id AND a.status='active' AND json_extract(a.prepared_ref,'$.kind')='weekly_test' AND t.attempt_id=NEW.attempt_id AND json_extract(t.item_ref,'$.item_id')=NEW.item_id AND EXISTS(SELECT 1 FROM json_each(a.selected_items) i WHERE json_extract(i.value,'$.item_id')=NEW.item_id AND json_extract(i.value,'$.attempt_id')=NEW.attempt_id)) BEGIN SELECT RAISE(ABORT,'draft_not_active_selected_weekly_item'); END;
CREATE TRIGGER assessment_drafts_draft_not_active_selected_weekly_item_update BEFORE UPDATE ON assessment_drafts WHEN NOT EXISTS(SELECT 1 FROM assessments a JOIN attempts t ON t.assessment_id=a.assessment_id WHERE a.assessment_id=NEW.assessment_id AND a.status='active' AND json_extract(a.prepared_ref,'$.kind')='weekly_test' AND t.attempt_id=NEW.attempt_id AND json_extract(t.item_ref,'$.item_id')=NEW.item_id AND EXISTS(SELECT 1 FROM json_each(a.selected_items) i WHERE json_extract(i.value,'$.item_id')=NEW.item_id AND json_extract(i.value,'$.attempt_id')=NEW.attempt_id)) BEGIN SELECT RAISE(ABORT,'draft_not_active_selected_weekly_item'); END;
CREATE TRIGGER assessment_drafts_fixed_refs BEFORE UPDATE ON assessment_drafts WHEN NEW.assessment_id IS NOT OLD.assessment_id OR NEW.item_id IS NOT OLD.item_id OR NEW.attempt_id IS NOT OLD.attempt_id BEGIN SELECT RAISE(ABORT,'immutable_reference_assessment_drafts'); END;
CREATE TRIGGER draft_revision_increment BEFORE UPDATE ON assessment_drafts WHEN NEW.draft_revision!=OLD.draft_revision+1 BEGIN SELECT RAISE(ABORT,'draft_revision_conflict'); END;
CREATE TABLE receipts (
  receipt_id TEXT PRIMARY KEY NOT NULL,
  command_id TEXT NOT NULL REFERENCES commands(command_id),
  kind TEXT NOT NULL CHECK(kind IN ('response','delivery','activity','assessment_submission','assessment_draft','session','job_action','upload','approval_decision','provider_action')),
  aggregate_id TEXT NOT NULL,
  payload TEXT NOT NULL CHECK(json_valid(payload)),
  payload_digest TEXT NOT NULL CHECK(length(payload_digest)=64 AND payload_digest NOT GLOB '*[^0-9a-f]*'),
  received_at TEXT NOT NULL,
  UNIQUE(command_id,kind,aggregate_id)
) STRICT;
CREATE TRIGGER receipts_no_update BEFORE UPDATE ON receipts BEGIN SELECT RAISE(ABORT,'immutable_receipts'); END;
CREATE TRIGGER receipts_no_delete BEFORE DELETE ON receipts BEGIN SELECT RAISE(ABORT,'immutable_receipts'); END;
CREATE TABLE responses (
  receipt_id TEXT PRIMARY KEY NOT NULL REFERENCES receipts(receipt_id),
  attempt_id TEXT NOT NULL UNIQUE REFERENCES attempts(attempt_id),
  command_id TEXT NOT NULL REFERENCES commands(command_id),
  response TEXT NOT NULL CHECK(json_valid(response)),
  response_digest TEXT NOT NULL CHECK(length(response_digest)=64 AND response_digest NOT GLOB '*[^0-9a-f]*'),
  conditions TEXT NOT NULL CHECK(json_valid(conditions)),
  received_at TEXT NOT NULL,
  reported_answered_at TEXT
) STRICT;
CREATE UNIQUE INDEX one_response_per_attempt ON responses(attempt_id);
CREATE TRIGGER responses_response_receipt_command_mismatch_insert BEFORE INSERT ON responses WHEN NOT EXISTS(SELECT 1 FROM receipts r WHERE r.receipt_id=NEW.receipt_id AND r.command_id=NEW.command_id AND r.kind='response' AND r.aggregate_id=NEW.attempt_id) BEGIN SELECT RAISE(ABORT,'response_receipt_command_mismatch'); END;
CREATE TRIGGER responses_response_receipt_command_mismatch_update BEFORE UPDATE ON responses WHEN NOT EXISTS(SELECT 1 FROM receipts r WHERE r.receipt_id=NEW.receipt_id AND r.command_id=NEW.command_id AND r.kind='response' AND r.aggregate_id=NEW.attempt_id) BEGIN SELECT RAISE(ABORT,'response_receipt_command_mismatch'); END;
CREATE TRIGGER responses_no_update BEFORE UPDATE ON responses BEGIN SELECT RAISE(ABORT,'immutable_responses'); END;
CREATE TRIGGER responses_no_delete BEFORE DELETE ON responses BEGIN SELECT RAISE(ABORT,'immutable_responses'); END;
CREATE TABLE deliveries (
  delivery_id TEXT PRIMARY KEY NOT NULL,
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  attempt_id TEXT REFERENCES attempts(attempt_id),
  kind TEXT NOT NULL CHECK(kind IN ('prompt','section','feedback','hint','worked_example')),
  content_ref TEXT NOT NULL CHECK(json_valid(content_ref)),
  content_digest TEXT NOT NULL CHECK(length(content_digest)=64 AND content_digest NOT GLOB '*[^0-9a-f]*'),
  equivalence_refs TEXT NOT NULL CHECK(json_valid(equivalence_refs)),
  state TEXT NOT NULL CHECK(state IN ('prepared','offered','displayed','display_unknown')),
  offered_at TEXT
) STRICT;
CREATE TRIGGER deliveries_delivery_attempt_session_mismatch_insert BEFORE INSERT ON deliveries WHEN NEW.attempt_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM attempts WHERE attempt_id=NEW.attempt_id AND session_id=NEW.session_id) BEGIN SELECT RAISE(ABORT,'delivery_attempt_session_mismatch'); END;
CREATE TRIGGER deliveries_delivery_attempt_session_mismatch_update BEFORE UPDATE ON deliveries WHEN NEW.attempt_id IS NOT NULL AND NOT EXISTS(SELECT 1 FROM attempts WHERE attempt_id=NEW.attempt_id AND session_id=NEW.session_id) BEGIN SELECT RAISE(ABORT,'delivery_attempt_session_mismatch'); END;
CREATE TRIGGER deliveries_fixed_refs BEFORE UPDATE ON deliveries WHEN NEW.delivery_id IS NOT OLD.delivery_id OR NEW.session_id IS NOT OLD.session_id OR NEW.attempt_id IS NOT OLD.attempt_id OR NEW.kind IS NOT OLD.kind OR NEW.content_ref IS NOT OLD.content_ref OR NEW.content_digest IS NOT OLD.content_digest OR NEW.equivalence_refs IS NOT OLD.equivalence_refs BEGIN SELECT RAISE(ABORT,'immutable_reference_deliveries'); END;
CREATE TABLE delivery_receipts (
  receipt_id TEXT PRIMARY KEY NOT NULL REFERENCES receipts(receipt_id),
  delivery_id TEXT NOT NULL UNIQUE REFERENCES deliveries(delivery_id),
  command_id TEXT NOT NULL UNIQUE REFERENCES commands(command_id),
  reported_display_at TEXT,
  timing_quality TEXT NOT NULL CHECK(timing_quality IN ('known','unknown','invalid_clock')),
  observed_conditions TEXT NOT NULL CHECK(json_valid(observed_conditions)),
  received_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER delivery_receipts_delivery_receipt_command_mismatch_insert BEFORE INSERT ON delivery_receipts WHEN NOT EXISTS(SELECT 1 FROM receipts WHERE receipt_id=NEW.receipt_id AND command_id=NEW.command_id AND kind='delivery' AND aggregate_id=NEW.delivery_id) BEGIN SELECT RAISE(ABORT,'delivery_receipt_command_mismatch'); END;
CREATE TRIGGER delivery_receipts_delivery_receipt_command_mismatch_update BEFORE UPDATE ON delivery_receipts WHEN NOT EXISTS(SELECT 1 FROM receipts WHERE receipt_id=NEW.receipt_id AND command_id=NEW.command_id AND kind='delivery' AND aggregate_id=NEW.delivery_id) BEGIN SELECT RAISE(ABORT,'delivery_receipt_command_mismatch'); END;
CREATE TRIGGER delivery_receipts_no_update BEFORE UPDATE ON delivery_receipts BEGIN SELECT RAISE(ABORT,'immutable_delivery_receipts'); END;
CREATE TRIGGER delivery_receipts_no_delete BEFORE DELETE ON delivery_receipts BEGIN SELECT RAISE(ABORT,'immutable_delivery_receipts'); END;
CREATE TABLE evidence_outbox (
  intent_id TEXT PRIMARY KEY NOT NULL,
  receipt_id TEXT NOT NULL REFERENCES receipts(receipt_id),
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  session_id TEXT NOT NULL REFERENCES sessions(session_id),
  owner TEXT NOT NULL CHECK(owner='teach'),
  stable_event_ids TEXT NOT NULL CHECK(json_valid(stable_event_ids)),
  payload TEXT NOT NULL CHECK(json_valid(payload)),
  payload_digest TEXT NOT NULL CHECK(length(payload_digest)=64 AND payload_digest NOT GLOB '*[^0-9a-f]*'),
  transaction_id TEXT NOT NULL UNIQUE,
  state TEXT NOT NULL CHECK(state IN ('pending','committing','committed','conflict','blocked')),
  attempt_count INTEGER NOT NULL CHECK(attempt_count>=0),
  next_eligible_at TEXT,
  error_code TEXT,
  UNIQUE(course_key,intent_id)
) STRICT;
CREATE TRIGGER evidence_outbox_nonacademic_or_cross_course_outbox_insert BEFORE INSERT ON evidence_outbox WHEN NOT EXISTS(SELECT 1 FROM sessions WHERE session_id=NEW.session_id AND course_key=NEW.course_key) OR NOT EXISTS(SELECT 1 FROM receipts WHERE receipt_id=NEW.receipt_id AND kind IN ('response','delivery','activity','assessment_submission','session') AND json_extract(payload,'$.canonical_commit_state') IN ('pending','committing','committed','conflict','blocked')) BEGIN SELECT RAISE(ABORT,'nonacademic_or_cross_course_outbox'); END;
CREATE TRIGGER evidence_outbox_nonacademic_or_cross_course_outbox_update BEFORE UPDATE ON evidence_outbox WHEN NOT EXISTS(SELECT 1 FROM sessions WHERE session_id=NEW.session_id AND course_key=NEW.course_key) OR NOT EXISTS(SELECT 1 FROM receipts WHERE receipt_id=NEW.receipt_id AND kind IN ('response','delivery','activity','assessment_submission','session') AND json_extract(payload,'$.canonical_commit_state') IN ('pending','committing','committed','conflict','blocked')) BEGIN SELECT RAISE(ABORT,'nonacademic_or_cross_course_outbox'); END;
CREATE TRIGGER evidence_outbox_fixed_refs BEFORE UPDATE ON evidence_outbox WHEN NEW.intent_id IS NOT OLD.intent_id OR NEW.receipt_id IS NOT OLD.receipt_id OR NEW.course_key IS NOT OLD.course_key OR NEW.session_id IS NOT OLD.session_id OR NEW.owner IS NOT OLD.owner OR NEW.stable_event_ids IS NOT OLD.stable_event_ids OR NEW.payload IS NOT OLD.payload OR NEW.payload_digest IS NOT OLD.payload_digest OR NEW.transaction_id IS NOT OLD.transaction_id BEGIN SELECT RAISE(ABORT,'immutable_reference_evidence_outbox'); END;
CREATE INDEX outbox_ready ON evidence_outbox(state,next_eligible_at);
CREATE TABLE evidence_commits (
  commit_id TEXT PRIMARY KEY NOT NULL,
  intent_id TEXT NOT NULL UNIQUE REFERENCES evidence_outbox(intent_id),
  transaction_id TEXT NOT NULL UNIQUE,
  canonical_path TEXT NOT NULL,
  event_ids TEXT NOT NULL CHECK(json_valid(event_ids)),
  event_digests TEXT NOT NULL CHECK(json_valid(event_digests)),
  committed_log_digest TEXT NOT NULL CHECK(length(committed_log_digest)=64 AND committed_log_digest NOT GLOB '*[^0-9a-f]*'),
  verified_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER evidence_commits_commit_intent_mismatch_insert BEFORE INSERT ON evidence_commits WHEN NOT EXISTS(SELECT 1 FROM evidence_outbox WHERE intent_id=NEW.intent_id AND transaction_id=NEW.transaction_id) BEGIN SELECT RAISE(ABORT,'commit_intent_mismatch'); END;
CREATE TRIGGER evidence_commits_commit_intent_mismatch_update BEFORE UPDATE ON evidence_commits WHEN NOT EXISTS(SELECT 1 FROM evidence_outbox WHERE intent_id=NEW.intent_id AND transaction_id=NEW.transaction_id) BEGIN SELECT RAISE(ABORT,'commit_intent_mismatch'); END;
CREATE TRIGGER evidence_commits_no_update BEFORE UPDATE ON evidence_commits BEGIN SELECT RAISE(ABORT,'immutable_evidence_commits'); END;
CREATE TRIGGER evidence_commits_no_delete BEFORE DELETE ON evidence_commits BEGIN SELECT RAISE(ABORT,'immutable_evidence_commits'); END;
CREATE TABLE activity_projection (
  session_id TEXT PRIMARY KEY NOT NULL REFERENCES sessions(session_id),
  canonical_cursor TEXT NOT NULL,
  canonical_digest TEXT NOT NULL CHECK(length(canonical_digest)=64 AND canonical_digest NOT GLOB '*[^0-9a-f]*'),
  progress TEXT NOT NULL CHECK(json_valid(progress)),
  rebuilt_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER assessment_drafts_delete_only_active BEFORE DELETE ON assessment_drafts WHEN NOT EXISTS(SELECT 1 FROM assessments WHERE assessment_id=OLD.assessment_id AND status='active') BEGIN SELECT RAISE(ABORT,'draft_not_active_selected_weekly_item'); END;
