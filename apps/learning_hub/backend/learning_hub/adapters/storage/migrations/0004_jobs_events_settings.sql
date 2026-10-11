CREATE TABLE jobs (
  job_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT REFERENCES courses(course_key),
  kind TEXT NOT NULL CHECK(kind IN ('ingest_prepare','plan_prepare','grade_written','extend_bank','publish','source_inventory')),
  dedupe_key TEXT NOT NULL CHECK(length(dedupe_key)=64 AND dedupe_key NOT GLOB '*[^0-9a-f]*') UNIQUE,
  input_ref TEXT NOT NULL CHECK(json_valid(input_ref)),
  requested_settings TEXT NOT NULL CHECK(json_valid(requested_settings)),
  actual_settings TEXT CHECK(actual_settings IS NULL OR json_valid(actual_settings)),
  state TEXT NOT NULL CHECK(state IN ('queued','running','waiting_usage','waiting_sign_in','waiting_dependency','retry_scheduled','blocked','paused','succeeded','cancelled')),
  revision INTEGER NOT NULL CHECK(revision>0),
  created_at TEXT NOT NULL,
  next_eligible_at TEXT,
  error TEXT CHECK(error IS NULL OR json_valid(error))
) STRICT;
CREATE TRIGGER jobs_job_course_mismatch_insert BEFORE INSERT ON jobs WHEN NEW.course_key IS NOT NULL AND NOT EXISTS(SELECT 1 FROM courses WHERE course_key=NEW.course_key AND course_id=json_extract(NEW.input_ref,'$.course_id')) BEGIN SELECT RAISE(ABORT,'job_course_mismatch'); END;
CREATE TRIGGER jobs_job_course_mismatch_update BEFORE UPDATE ON jobs WHEN NEW.course_key IS NOT NULL AND NOT EXISTS(SELECT 1 FROM courses WHERE course_key=NEW.course_key AND course_id=json_extract(NEW.input_ref,'$.course_id')) BEGIN SELECT RAISE(ABORT,'job_course_mismatch'); END;
CREATE TRIGGER jobs_fixed_refs BEFORE UPDATE ON jobs WHEN NEW.job_id IS NOT OLD.job_id OR NEW.course_key IS NOT OLD.course_key OR NEW.kind IS NOT OLD.kind OR NEW.dedupe_key IS NOT OLD.dedupe_key OR NEW.input_ref IS NOT OLD.input_ref OR NEW.requested_settings IS NOT OLD.requested_settings OR NEW.created_at IS NOT OLD.created_at BEGIN SELECT RAISE(ABORT,'immutable_reference_jobs'); END;
CREATE TABLE job_steps (
  job_id TEXT NOT NULL REFERENCES jobs(job_id),
  step_key TEXT NOT NULL,
  ordinal INTEGER NOT NULL CHECK(ordinal>=0),
  input_digest TEXT NOT NULL CHECK(length(input_digest)=64 AND input_digest NOT GLOB '*[^0-9a-f]*'),
  state TEXT NOT NULL CHECK(state IN ('queued','running','waiting_usage','waiting_sign_in','waiting_dependency','retry_scheduled','blocked','paused','succeeded','cancelled','completed','invalidated')),
  output_ref TEXT CHECK(output_ref IS NULL OR json_valid(output_ref)),
  checkpoint TEXT CHECK(checkpoint IS NULL OR json_valid(checkpoint)),
  attempt_count INTEGER NOT NULL CHECK(attempt_count>=0),
  last_error TEXT CHECK(last_error IS NULL OR json_valid(last_error)),
  PRIMARY KEY(job_id,step_key)
) STRICT;
CREATE TRIGGER completed_step_frozen BEFORE UPDATE ON job_steps WHEN OLD.state='completed' AND (NEW.state!='invalidated' OR NEW.input_digest=OLD.input_digest) BEGIN SELECT RAISE(ABORT,'completed_step_immutable'); END;
CREATE TABLE course_leases (
  course_key TEXT PRIMARY KEY NOT NULL REFERENCES courses(course_key),
  holder_id TEXT NOT NULL,
  fence INTEGER NOT NULL CHECK(fence>0),
  owner_checkout TEXT NOT NULL,
  acquired_at TEXT NOT NULL,
  renewed_at TEXT NOT NULL,
  expires_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER lease_monotonic_fence BEFORE UPDATE ON course_leases WHEN NEW.fence<OLD.fence OR (NEW.holder_id IS NOT OLD.holder_id AND NEW.fence<=OLD.fence) BEGIN SELECT RAISE(ABORT,'lease_fence_conflict'); END;
CREATE TABLE events (
  seq INTEGER PRIMARY KEY AUTOINCREMENT,
  event_id TEXT NOT NULL UNIQUE,
  course_key TEXT REFERENCES courses(course_key),
  aggregate_kind TEXT NOT NULL CHECK(aggregate_kind IN ('job','receipt','assessment','publication','projection','provider','service')),
  aggregate_id TEXT NOT NULL,
  event_type TEXT NOT NULL CHECK(event_type IN ('job_state_changed','step_completed','receipt_committed','assessment_updated','publication_changed','projection_updated','provider_state_changed','service_state_changed')),
  safe_payload TEXT NOT NULL CHECK(json_valid(safe_payload)),
  occurred_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER events_no_update BEFORE UPDATE ON events BEGIN SELECT RAISE(ABORT,'immutable_events'); END;
CREATE TRIGGER events_no_delete BEFORE DELETE ON events BEGIN SELECT RAISE(ABORT,'immutable_events'); END;
CREATE INDEX event_replay ON events(seq);
CREATE TABLE role_settings (
  role_key TEXT PRIMARY KEY NOT NULL,
  requested_model TEXT NOT NULL,
  requested_effort TEXT NOT NULL CHECK(requested_effort IN ('low','medium','high','xhigh','max','ultra')),
  speed TEXT NOT NULL CHECK(speed='standard'),
  revision INTEGER NOT NULL CHECK(revision>0),
  updated_at TEXT NOT NULL
) STRICT;
CREATE TABLE local_auth_sessions (
  session_digest TEXT NOT NULL CHECK(length(session_digest)=64 AND session_digest NOT GLOB '*[^0-9a-f]*') PRIMARY KEY,
  local_principal TEXT NOT NULL,
  csrf_digest TEXT NOT NULL CHECK(length(csrf_digest)=64 AND csrf_digest NOT GLOB '*[^0-9a-f]*'),
  created_at TEXT NOT NULL,
  last_used_at TEXT NOT NULL,
  expires_at TEXT NOT NULL,
  revoked_at TEXT
) STRICT;
CREATE TABLE bootstrap_capabilities (
  capability_digest TEXT NOT NULL CHECK(length(capability_digest)=64 AND capability_digest NOT GLOB '*[^0-9a-f]*') PRIMARY KEY,
  expires_at TEXT NOT NULL,
  consumed_at TEXT
) STRICT;
CREATE TRIGGER bootstrap_one_use BEFORE UPDATE ON bootstrap_capabilities WHEN OLD.consumed_at IS NOT NULL OR NEW.capability_digest IS NOT OLD.capability_digest OR NEW.expires_at IS NOT OLD.expires_at BEGIN SELECT RAISE(ABORT,'bootstrap_already_consumed'); END;
CREATE TABLE preferences (
  local_principal TEXT PRIMARY KEY NOT NULL,
  schema_version INTEGER NOT NULL CHECK(schema_version=1),
  preferences TEXT NOT NULL CHECK(json_valid(preferences)),
  revision INTEGER NOT NULL CHECK(revision>0)
) STRICT;
CREATE TABLE provider_auth_flows (
  flow_id TEXT PRIMARY KEY NOT NULL,
  requested_action TEXT NOT NULL CHECK(requested_action IN ('sign_in','grant')),
  state TEXT NOT NULL CHECK(state IN ('pending','awaiting_callback','validating','completed','failed','expired','cancelled')),
  registration_refs TEXT NOT NULL CHECK(json_valid(registration_refs)),
  host_refs TEXT NOT NULL CHECK(json_valid(host_refs)),
  state_digest TEXT NOT NULL CHECK(length(state_digest)=64 AND state_digest NOT GLOB '*[^0-9a-f]*'),
  nonce_digest TEXT NOT NULL CHECK(length(nonce_digest)=64 AND nonce_digest NOT GLOB '*[^0-9a-f]*'),
  expires_at TEXT NOT NULL,
  terminal_at TEXT,
  subject_ref TEXT,
  CHECK((state IN ('completed','failed','expired','cancelled'))=(terminal_at IS NOT NULL)),
  CHECK(state!='completed' OR subject_ref IS NOT NULL)
) STRICT;
CREATE TRIGGER provider_auth_flows_fixed_refs BEFORE UPDATE ON provider_auth_flows WHEN NEW.flow_id IS NOT OLD.flow_id OR NEW.requested_action IS NOT OLD.requested_action OR NEW.registration_refs IS NOT OLD.registration_refs OR NEW.host_refs IS NOT OLD.host_refs OR NEW.state_digest IS NOT OLD.state_digest OR NEW.nonce_digest IS NOT OLD.nonce_digest OR NEW.expires_at IS NOT OLD.expires_at BEGIN SELECT RAISE(ABORT,'immutable_reference_provider_auth_flows'); END;
CREATE TRIGGER auth_terminal_immutable BEFORE UPDATE ON provider_auth_flows WHEN OLD.terminal_at IS NOT NULL BEGIN SELECT RAISE(ABORT,'auth_flow_terminal'); END;
CREATE TABLE approval_proposals (
  proposal_id TEXT PRIMARY KEY NOT NULL,
  job_id TEXT NOT NULL REFERENCES jobs(job_id),
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  kind TEXT NOT NULL CHECK(kind IN ('source_selection','substantive_replacement')),
  proposal_digest TEXT NOT NULL CHECK(length(proposal_digest)=64 AND proposal_digest NOT GLOB '*[^0-9a-f]*'),
  source_snapshot_id TEXT NOT NULL REFERENCES source_snapshots(snapshot_id),
  expected_hashes TEXT NOT NULL CHECK(json_valid(expected_hashes)),
  scope TEXT NOT NULL CHECK(json_valid(scope)),
  preserved_version_refs TEXT NOT NULL CHECK(json_valid(preserved_version_refs)),
  safe_preview TEXT NOT NULL CHECK(json_valid(safe_preview)),
  created_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER approval_proposals_proposal_course_snapshot_mismatch_insert BEFORE INSERT ON approval_proposals WHEN NOT EXISTS(SELECT 1 FROM jobs WHERE job_id=NEW.job_id AND course_key=NEW.course_key) OR NOT EXISTS(SELECT 1 FROM source_snapshots WHERE snapshot_id=NEW.source_snapshot_id AND course_key=NEW.course_key) BEGIN SELECT RAISE(ABORT,'proposal_course_snapshot_mismatch'); END;
CREATE TRIGGER approval_proposals_proposal_course_snapshot_mismatch_update BEFORE UPDATE ON approval_proposals WHEN NOT EXISTS(SELECT 1 FROM jobs WHERE job_id=NEW.job_id AND course_key=NEW.course_key) OR NOT EXISTS(SELECT 1 FROM source_snapshots WHERE snapshot_id=NEW.source_snapshot_id AND course_key=NEW.course_key) BEGIN SELECT RAISE(ABORT,'proposal_course_snapshot_mismatch'); END;
CREATE TRIGGER approval_proposals_no_update BEFORE UPDATE ON approval_proposals BEGIN SELECT RAISE(ABORT,'immutable_approval_proposals'); END;
CREATE TRIGGER approval_proposals_no_delete BEFORE DELETE ON approval_proposals BEGIN SELECT RAISE(ABORT,'immutable_approval_proposals'); END;
CREATE TABLE approval_decisions (
  decision_id TEXT PRIMARY KEY NOT NULL,
  proposal_id TEXT NOT NULL UNIQUE REFERENCES approval_proposals(proposal_id),
  command_id TEXT NOT NULL REFERENCES commands(command_id),
  principal TEXT NOT NULL,
  decision TEXT NOT NULL CHECK(decision IN ('approve','reject')),
  proposal_digest TEXT NOT NULL CHECK(length(proposal_digest)=64 AND proposal_digest NOT GLOB '*[^0-9a-f]*'),
  expected_job_revision INTEGER NOT NULL CHECK(expected_job_revision>0),
  decided_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER approval_decisions_approval_not_digest_bound_human_command_insert BEFORE INSERT ON approval_decisions WHEN NOT EXISTS(SELECT 1 FROM approval_proposals p JOIN jobs j ON j.job_id=p.job_id JOIN commands c ON c.command_id=NEW.command_id WHERE p.proposal_id=NEW.proposal_id AND p.proposal_digest=NEW.proposal_digest AND j.revision=NEW.expected_job_revision AND c.local_principal=NEW.principal AND c.kind='approval_decision') BEGIN SELECT RAISE(ABORT,'approval_not_digest_bound_human_command'); END;
CREATE TRIGGER approval_decisions_approval_not_digest_bound_human_command_update BEFORE UPDATE ON approval_decisions WHEN NOT EXISTS(SELECT 1 FROM approval_proposals p JOIN jobs j ON j.job_id=p.job_id JOIN commands c ON c.command_id=NEW.command_id WHERE p.proposal_id=NEW.proposal_id AND p.proposal_digest=NEW.proposal_digest AND j.revision=NEW.expected_job_revision AND c.local_principal=NEW.principal AND c.kind='approval_decision') BEGIN SELECT RAISE(ABORT,'approval_not_digest_bound_human_command'); END;
CREATE TRIGGER approval_decisions_no_update BEFORE UPDATE ON approval_decisions BEGIN SELECT RAISE(ABORT,'immutable_approval_decisions'); END;
CREATE TRIGGER approval_decisions_no_delete BEFORE DELETE ON approval_decisions BEGIN SELECT RAISE(ABORT,'immutable_approval_decisions'); END;
INSERT INTO role_settings(role_key,requested_model,requested_effort,speed,revision,updated_at) VALUES
  ('uni_curriculum_checker','gpt-6-astra','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_curriculum_checker_xhigh','gpt-6-astra','xhigh','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_ingest_draft','gpt-6-luna','medium','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_ingest_draft_high','gpt-6-luna','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_ingest_owner','gpt-6.1-sol','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_ingest_reasoning_astra','gpt-6-astra','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_plan_owner','gpt-6.1-sol','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_plan_owner_astra','gpt-6-astra','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_recall_owner','gpt-6-luna','low','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_recall_owner_medium','gpt-6-luna','medium','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_source_checker','gpt-6-astra','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_source_checker_xhigh','gpt-6-astra','xhigh','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_teach_assessor','gpt-6.1-sol','high','standard',1,'2026-10-11T00:00:00Z'),
  ('uni_teach_owner','gpt-6-luna','medium','standard',1,'2026-10-11T00:00:00Z');
CREATE TRIGGER completed_step_no_delete BEFORE DELETE ON job_steps WHEN OLD.state='completed' BEGIN SELECT RAISE(ABORT,'completed_step_immutable'); END;
CREATE TRIGGER course_leases_preserve_fence BEFORE DELETE ON course_leases BEGIN SELECT RAISE(ABORT,'lease_fence_must_be_retained'); END;
