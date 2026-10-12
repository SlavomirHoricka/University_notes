CREATE TABLE schema_migrations (
  version INTEGER PRIMARY KEY CHECK(version>0),
  name TEXT NOT NULL,
  checksum TEXT NOT NULL CHECK(length(checksum)=64 AND checksum NOT GLOB '*[^0-9a-f]*'),
  applied_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER schema_migrations_no_update BEFORE UPDATE ON schema_migrations BEGIN SELECT RAISE(ABORT,'immutable_schema_migrations'); END;
CREATE TRIGGER schema_migrations_no_delete BEFORE DELETE ON schema_migrations BEGIN SELECT RAISE(ABORT,'immutable_schema_migrations'); END;
CREATE TABLE courses (
  course_key TEXT PRIMARY KEY NOT NULL,
  course_id TEXT NOT NULL UNIQUE,
  academic_year TEXT NOT NULL,
  semester TEXT NOT NULL CHECK(semester IN ('Winter_Semester','Summer_Semester')),
  course_folder TEXT NOT NULL,
  course_code TEXT,
  display_name TEXT NOT NULL,
  CHECK(course_id=academic_year||'/'||semester||'/'||course_folder)
) STRICT;
CREATE UNIQUE INDEX courses_nfc_identity ON courses(nfc(course_id));
CREATE TRIGGER courses_fixed_refs BEFORE UPDATE ON courses WHEN NEW.course_key IS NOT OLD.course_key OR NEW.course_id IS NOT OLD.course_id OR NEW.academic_year IS NOT OLD.academic_year OR NEW.semester IS NOT OLD.semester OR NEW.course_folder IS NOT OLD.course_folder BEGIN SELECT RAISE(ABORT,'immutable_reference_courses'); END;
CREATE TABLE source_files (
  source_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  original_name TEXT NOT NULL,
  managed_relpath TEXT NOT NULL,
  week_ref TEXT NOT NULL CHECK(json_valid(week_ref)),
  created_at TEXT NOT NULL,
  archived_at TEXT
) STRICT;
CREATE UNIQUE INDEX source_live_path ON source_files(course_key,managed_relpath) WHERE archived_at IS NULL;
CREATE TRIGGER source_files_fixed_refs BEFORE UPDATE ON source_files WHEN NEW.source_id IS NOT OLD.source_id OR NEW.course_key IS NOT OLD.course_key BEGIN SELECT RAISE(ABORT,'immutable_reference_source_files'); END;
CREATE TABLE source_revisions (
  source_revision_id TEXT PRIMARY KEY NOT NULL,
  source_id TEXT NOT NULL REFERENCES source_files(source_id),
  revision INTEGER NOT NULL CHECK(revision>0),
  sha256 TEXT NOT NULL CHECK(length(sha256)=64 AND sha256 NOT GLOB '*[^0-9a-f]*'),
  byte_size INTEGER NOT NULL CHECK(byte_size>=0),
  media_type TEXT NOT NULL,
  storage_ref TEXT NOT NULL,
  extraction_state TEXT NOT NULL CHECK(extraction_state IN ('pending','complete','partial','blocked')),
  created_at TEXT NOT NULL,
  UNIQUE(source_id,revision)
) STRICT;
CREATE TRIGGER source_revisions_no_update BEFORE UPDATE ON source_revisions WHEN NEW.source_revision_id IS NOT OLD.source_revision_id OR NEW.source_id IS NOT OLD.source_id OR NEW.revision IS NOT OLD.revision OR NEW.sha256 IS NOT OLD.sha256 OR NEW.byte_size IS NOT OLD.byte_size OR NEW.media_type IS NOT OLD.media_type OR NEW.storage_ref IS NOT OLD.storage_ref OR NEW.created_at IS NOT OLD.created_at BEGIN SELECT RAISE(ABORT,'immutable_source_revisions'); END;
CREATE TRIGGER source_revisions_no_delete BEFORE DELETE ON source_revisions BEGIN SELECT RAISE(ABORT,'immutable_source_revisions'); END;
CREATE TABLE source_snapshots (
  snapshot_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  generation INTEGER NOT NULL CHECK(generation>0),
  snapshot_digest TEXT NOT NULL CHECK(length(snapshot_digest)=64 AND snapshot_digest NOT GLOB '*[^0-9a-f]*'),
  entries TEXT NOT NULL CHECK(json_valid(entries)),
  created_at TEXT NOT NULL,
  UNIQUE(course_key,generation)
) STRICT;
CREATE TRIGGER source_snapshots_no_update BEFORE UPDATE ON source_snapshots BEGIN SELECT RAISE(ABORT,'immutable_source_snapshots'); END;
CREATE TRIGGER source_snapshots_no_delete BEFORE DELETE ON source_snapshots BEGIN SELECT RAISE(ABORT,'immutable_source_snapshots'); END;
CREATE TABLE bundles (
  bundle_id TEXT PRIMARY KEY NOT NULL,
  course_key TEXT NOT NULL REFERENCES courses(course_key),
  snapshot_id TEXT NOT NULL REFERENCES source_snapshots(snapshot_id),
  schema_version INTEGER NOT NULL CHECK(schema_version=1),
  plan_version TEXT NOT NULL,
  source_version TEXT NOT NULL,
  ingestion_revision INTEGER NOT NULL CHECK(ingestion_revision>0),
  manifest TEXT NOT NULL CHECK(json_valid(manifest)),
  public_digest TEXT NOT NULL CHECK(length(public_digest)=64 AND public_digest NOT GLOB '*[^0-9a-f]*'),
  private_digest TEXT NOT NULL CHECK(length(private_digest)=64 AND private_digest NOT GLOB '*[^0-9a-f]*'),
  storage_ref TEXT NOT NULL,
  validation_state TEXT NOT NULL CHECK(validation_state IN ('staged','validated','blocked')),
  integrated_commit TEXT,
  created_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER bundles_bundle_snapshot_course_mismatch_insert BEFORE INSERT ON bundles WHEN NOT EXISTS(SELECT 1 FROM source_snapshots WHERE snapshot_id=NEW.snapshot_id AND course_key=NEW.course_key) BEGIN SELECT RAISE(ABORT,'bundle_snapshot_course_mismatch'); END;
CREATE TRIGGER bundles_bundle_snapshot_course_mismatch_update BEFORE UPDATE ON bundles WHEN NOT EXISTS(SELECT 1 FROM source_snapshots WHERE snapshot_id=NEW.snapshot_id AND course_key=NEW.course_key) BEGIN SELECT RAISE(ABORT,'bundle_snapshot_course_mismatch'); END;
CREATE TRIGGER bundles_no_update BEFORE UPDATE ON bundles BEGIN SELECT RAISE(ABORT,'immutable_bundles'); END;
CREATE TRIGGER bundles_no_delete BEFORE DELETE ON bundles BEGIN SELECT RAISE(ABORT,'immutable_bundles'); END;
CREATE TABLE publication_pointers (
  course_key TEXT PRIMARY KEY NOT NULL REFERENCES courses(course_key),
  bundle_id TEXT NOT NULL REFERENCES bundles(bundle_id),
  generation INTEGER NOT NULL CHECK(generation>0),
  changed_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER publication_pointers_unvalidated_publication_insert BEFORE INSERT ON publication_pointers WHEN NOT EXISTS(SELECT 1 FROM bundles WHERE bundle_id=NEW.bundle_id AND course_key=NEW.course_key AND validation_state='validated' AND integrated_commit IS NOT NULL) BEGIN SELECT RAISE(ABORT,'unvalidated_publication'); END;
CREATE TRIGGER publication_pointers_unvalidated_publication_update BEFORE UPDATE ON publication_pointers WHEN NOT EXISTS(SELECT 1 FROM bundles WHERE bundle_id=NEW.bundle_id AND course_key=NEW.course_key AND validation_state='validated' AND integrated_commit IS NOT NULL) BEGIN SELECT RAISE(ABORT,'unvalidated_publication'); END;
CREATE TRIGGER publication_generation BEFORE UPDATE ON publication_pointers WHEN NEW.generation != OLD.generation+1 OR NEW.course_key != OLD.course_key BEGIN SELECT RAISE(ABORT,'publication_generation_conflict'); END;
CREATE TABLE bundle_validity (
  validity_id TEXT PRIMARY KEY NOT NULL,
  bundle_id TEXT NOT NULL REFERENCES bundles(bundle_id),
  affected_definitions TEXT NOT NULL CHECK(json_valid(affected_definitions)),
  kind TEXT NOT NULL CHECK(kind IN ('validity_hold','cleared')),
  reason TEXT NOT NULL,
  owner_references TEXT NOT NULL CHECK(json_valid(owner_references)),
  recorded_at TEXT NOT NULL
) STRICT;
CREATE TRIGGER bundle_validity_no_update BEFORE UPDATE ON bundle_validity BEGIN SELECT RAISE(ABORT,'immutable_bundle_validity'); END;
CREATE TRIGGER bundle_validity_no_delete BEFORE DELETE ON bundle_validity BEGIN SELECT RAISE(ABORT,'immutable_bundle_validity'); END;
