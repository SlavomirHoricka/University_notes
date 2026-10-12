-- Additive H01 private operational state; accepted 0001-0005 bytes stay unchanged.
CREATE TABLE provider_accounts (
  subject TEXT NOT NULL,
  client_id TEXT NOT NULL,
  account_revision INTEGER NOT NULL CHECK(account_revision>0),
  scopes TEXT NOT NULL CHECK(json_valid(scopes) AND json_type(scopes)='array'),
  active INTEGER NOT NULL CHECK(active IN (0,1)),
  inference_verified INTEGER NOT NULL CHECK(inference_verified IN (0,1)),
  verified_settings TEXT CHECK(verified_settings IS NULL OR json_valid(verified_settings)),
  PRIMARY KEY(subject,client_id,account_revision),
  CHECK((inference_verified=1)=(verified_settings IS NOT NULL))
) STRICT;
CREATE UNIQUE INDEX one_active_provider_account ON provider_accounts(active) WHERE active=1;
CREATE TRIGGER provider_accounts_immutable_registration BEFORE UPDATE ON provider_accounts WHEN NEW.subject IS NOT OLD.subject OR NEW.client_id IS NOT OLD.client_id OR NEW.account_revision IS NOT OLD.account_revision OR NEW.scopes IS NOT OLD.scopes OR NEW.inference_verified IS NOT OLD.inference_verified OR NEW.verified_settings IS NOT OLD.verified_settings OR NEW.active!=0 OR OLD.active!=1 BEGIN SELECT RAISE(ABORT,'provider_registration_immutable'); END;
CREATE TRIGGER provider_accounts_no_delete BEFORE DELETE ON provider_accounts BEGIN SELECT RAISE(ABORT,'provider_registration_immutable'); END;
CREATE TABLE provider_account_state (
  singleton INTEGER PRIMARY KEY CHECK(singleton=1),
  revision INTEGER NOT NULL CHECK(revision>0),
  subject TEXT,
  client_id TEXT,
  account_revision INTEGER,
  FOREIGN KEY(subject,client_id,account_revision) REFERENCES provider_accounts(subject,client_id,account_revision),
  CHECK((subject IS NULL AND client_id IS NULL AND account_revision IS NULL) OR (subject IS NOT NULL AND client_id IS NOT NULL AND account_revision=revision))
) STRICT;
INSERT INTO provider_account_state(singleton,revision) VALUES(1,1);
CREATE TRIGGER provider_account_state_cas BEFORE UPDATE ON provider_account_state WHEN NEW.singleton!=OLD.singleton OR NEW.revision!=OLD.revision+1 OR (NEW.subject IS NOT NULL AND NOT EXISTS(SELECT 1 FROM provider_accounts WHERE subject=NEW.subject AND client_id=NEW.client_id AND account_revision=NEW.account_revision AND active=1)) BEGIN SELECT RAISE(ABORT,'provider_account_revision_conflict'); END;
CREATE TRIGGER provider_account_state_no_delete BEFORE DELETE ON provider_account_state BEGIN SELECT RAISE(ABORT,'provider_account_state_retained'); END;
ALTER TABLE provider_auth_flows ADD COLUMN revision INTEGER NOT NULL DEFAULT 1 CHECK(revision>0);
ALTER TABLE provider_auth_flows ADD COLUMN error_code TEXT;
CREATE UNIQUE INDEX provider_auth_state_unique ON provider_auth_flows(state_digest);
CREATE TRIGGER provider_flow_revision BEFORE UPDATE ON provider_auth_flows WHEN NEW.revision!=OLD.revision+1 BEGIN SELECT RAISE(ABORT,'provider_flow_revision_conflict'); END;
CREATE TRIGGER provider_flow_transition BEFORE UPDATE ON provider_auth_flows WHEN NOT (
  (OLD.state='pending' AND NEW.state IN ('awaiting_callback','failed','expired','cancelled')) OR
  (OLD.state='awaiting_callback' AND NEW.state IN ('validating','failed','expired','cancelled')) OR
  (OLD.state='validating' AND NEW.state IN ('completed','failed','expired','cancelled'))
) BEGIN SELECT RAISE(ABORT,'provider_flow_transition_conflict'); END;
CREATE TABLE provider_runs (
  run_id TEXT PRIMARY KEY NOT NULL,
  logical_task_id TEXT NOT NULL UNIQUE,
  request_digest TEXT NOT NULL CHECK(length(request_digest)=64 AND request_digest NOT GLOB '*[^0-9a-f]*'),
  subject TEXT NOT NULL,
  client_id TEXT NOT NULL,
  account_revision INTEGER NOT NULL,
  requested_settings TEXT NOT NULL CHECK(json_valid(requested_settings)),
  required_scopes TEXT NOT NULL CHECK(json_valid(required_scopes) AND json_type(required_scopes)='array' AND json_array_length(required_scopes)>0),
  actual_settings TEXT CHECK(actual_settings IS NULL OR json_valid(actual_settings)),
  thread_id TEXT,
  turn_id TEXT,
  state TEXT NOT NULL CHECK(state IN ('prepared','submitted','running','completed','failed','interrupted','unknown')),
  terminal_output TEXT CHECK(terminal_output IS NULL OR length(terminal_output)<=200000),
  error_code TEXT,
  revision INTEGER NOT NULL CHECK(revision>0),
  created_at TEXT NOT NULL,
  FOREIGN KEY(subject,client_id,account_revision) REFERENCES provider_accounts(subject,client_id,account_revision),
  CHECK(turn_id IS NULL OR thread_id IS NOT NULL),
  CHECK(state!='prepared' OR (thread_id IS NULL AND turn_id IS NULL AND actual_settings IS NULL AND terminal_output IS NULL AND error_code IS NULL)),
  CHECK(terminal_output IS NULL OR state IN ('completed','failed','interrupted')),
  CHECK(state!='running' OR turn_id IS NOT NULL)
) STRICT;
CREATE TRIGGER provider_runs_fixed_refs BEFORE UPDATE ON provider_runs WHEN NEW.run_id IS NOT OLD.run_id OR NEW.logical_task_id IS NOT OLD.logical_task_id OR NEW.request_digest IS NOT OLD.request_digest OR NEW.subject IS NOT OLD.subject OR NEW.client_id IS NOT OLD.client_id OR NEW.account_revision IS NOT OLD.account_revision OR NEW.requested_settings IS NOT OLD.requested_settings OR NEW.required_scopes IS NOT OLD.required_scopes OR NEW.created_at IS NOT OLD.created_at OR (OLD.thread_id IS NOT NULL AND NEW.thread_id IS NOT OLD.thread_id) OR (OLD.turn_id IS NOT NULL AND NEW.turn_id IS NOT OLD.turn_id) OR (OLD.actual_settings IS NOT NULL AND NEW.actual_settings IS NOT OLD.actual_settings) BEGIN SELECT RAISE(ABORT,'provider_run_identity_conflict'); END;
CREATE TRIGGER provider_runs_cas BEFORE UPDATE ON provider_runs WHEN NEW.revision!=OLD.revision+1 BEGIN SELECT RAISE(ABORT,'provider_run_revision_conflict'); END;
CREATE TRIGGER provider_runs_transition BEFORE UPDATE ON provider_runs WHEN NOT (
  (OLD.state='prepared' AND NEW.state IN ('submitted','failed','interrupted')) OR
  (OLD.state='submitted' AND NEW.state IN ('running','completed','failed','interrupted','unknown')) OR
  (OLD.state='running' AND NEW.state IN ('running','completed','failed','interrupted','unknown')) OR
  (OLD.state='unknown' AND OLD.turn_id IS NOT NULL AND NEW.state IN ('completed','failed','interrupted'))
) BEGIN SELECT RAISE(ABORT,'provider_run_transition_conflict'); END;
CREATE TRIGGER provider_runs_no_delete BEFORE DELETE ON provider_runs BEGIN SELECT RAISE(ABORT,'provider_run_retained'); END;

CREATE TRIGGER provider_accounts_verified_requires_terminal_run BEFORE INSERT ON provider_accounts WHEN NEW.inference_verified=1 AND NOT EXISTS(SELECT 1 FROM provider_runs r WHERE r.subject=NEW.subject AND r.client_id=NEW.client_id AND r.account_revision=NEW.account_revision-1 AND r.state='completed' AND r.turn_id IS NOT NULL AND r.actual_settings=NEW.verified_settings AND r.requested_settings=NEW.verified_settings) BEGIN SELECT RAISE(ABORT,'provider_verification_requires_terminal_run'); END;
