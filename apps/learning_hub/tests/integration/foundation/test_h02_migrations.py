import hashlib
import json
import sqlite3
from dataclasses import replace
from pathlib import Path
from typing import Any

import pytest
from learning_hub.adapters.storage.database import connect_database
from learning_hub.adapters.storage.jobs import JobConflict, SQLiteRequestedJobs
from learning_hub.adapters.storage.migration import (
    MigrationError,
    applied_versions,
    load_migrations,
    migrate,
    verify_integrity,
)
from learning_hub.domain.models.services import RequestedJobV1

STAMP = "2026-10-11T10:00:00Z"
HASH = "a" * 64
COURSE = "fixture/Winter_Semester/Scaffold"
KEY = "crs_fixture01"


def insert(db: sqlite3.Connection, table: str, **values: Any) -> None:
    # Identifiers are fixed test code, never external request values.
    columns = ",".join(values)
    placeholders = ",".join("?" for _ in values)
    db.execute(f"INSERT INTO {table}({columns}) VALUES({placeholders})", tuple(values.values()))


def seed_course(db: sqlite3.Connection, suffix: str = "") -> None:
    insert(
        db,
        "courses",
        course_key=KEY + suffix,
        course_id=COURSE + suffix,
        academic_year="fixture",
        semester="Winter_Semester",
        course_folder="Scaffold" + suffix,
        course_code=None,
        display_name="Fixture",
    )
    insert(
        db,
        "source_snapshots",
        snapshot_id="snapshot" + suffix,
        course_key=KEY + suffix,
        generation=1,
        snapshot_digest=HASH,
        entries="[]",
        created_at=STAMP,
    )
    seed_bundle(db, "bundle" + suffix, suffix)


def seed_bundle(db: sqlite3.Connection, bundle_id: str, suffix: str = "") -> None:
    insert(
        db,
        "bundles",
        bundle_id=bundle_id,
        course_key=KEY + suffix,
        snapshot_id="snapshot" + suffix,
        schema_version=1,
        plan_version="P001",
        source_version="V001",
        ingestion_revision=1,
        manifest="{}",
        public_digest=HASH,
        private_digest=HASH,
        storage_ref="fixture/bundle",
        validation_state="validated",
        integrated_commit="b" * 40,
        created_at=STAMP,
    )


def seed_session(db: sqlite3.Connection, suffix: str = "") -> None:
    insert(
        db,
        "sessions",
        session_id="session" + suffix,
        course_key=KEY + suffix,
        bundle_id="bundle" + suffix,
        route_kind="weekly_test",
        route_ref="{}",
        status="active",
        revision=1,
        bookmark="{}",
        created_at=STAMP,
        updated_at=STAMP,
    )


def seed_assessment(
    db: sqlite3.Connection,
    name: str = "assessment",
    suffix: str = "",
    status: str = "active",
    final_result: str | None = None,
) -> None:
    insert(
        db,
        "assessments",
        assessment_id=name,
        session_id="session" + suffix,
        prepared_ref='{"kind":"weekly_test"}',
        blueprint_digest=HASH,
        selected_items=json.dumps([{"item_id": "item", "attempt_id": "attempt" + suffix}]),
        selection_seed="seed",
        algorithm_version="1",
        status=status,
        revision=1,
        submitted_at=STAMP if status == "submitted" else None,
        final_result_id=final_result,
    )


def seed_attempt(db: sqlite3.Connection, suffix: str = "", assessment: str = "assessment") -> None:
    insert(
        db,
        "attempts",
        attempt_id="attempt" + suffix,
        session_id="session" + suffix,
        assessment_id=assessment,
        item_ref=json.dumps(
            {
                "course_id": COURSE + suffix,
                "plan_version": "P001",
                "source_version": "V001",
                "ingestion_revision": 1,
                "item_id": "item",
            }
        ),
        equivalence_id="eq",
        previous_attempt_id=None,
        status="started",
        revision=1,
        created_at=STAMP,
    )


def seed_command(
    db: sqlite3.Connection,
    name: str = "command",
    kind: str = "response",
    principal: str = "human",
    aggregate_id: str = "attempt",
) -> None:
    insert(
        db,
        "commands",
        command_id=name,
        local_principal=principal,
        kind=kind,
        idempotency_key=name,
        request_digest=HASH,
        aggregate_id=aggregate_id,
        status="accepted",
        response_status=202,
        replay_response="{}",
        created_at=STAMP,
    )


def seed_response(db: sqlite3.Connection, suffix: str = "") -> None:
    seed_command(db, "command" + suffix)
    insert(
        db,
        "receipts",
        receipt_id="receipt" + suffix,
        command_id="command" + suffix,
        kind="response",
        aggregate_id="attempt" + suffix,
        payload='{"canonical_commit_state":"pending"}',
        payload_digest=HASH,
        received_at=STAMP,
    )
    insert(
        db,
        "responses",
        receipt_id="receipt" + suffix,
        attempt_id="attempt" + suffix,
        command_id="command" + suffix,
        response='{"kind":"numeric","value":"5"}',
        response_digest=HASH,
        conditions="{}",
        received_at=STAMP,
        reported_answered_at=None,
    )


def seed_verified_result(db: sqlite3.Connection, suffix: str = "") -> None:
    seed_response(db, suffix)
    insert(
        db,
        "evidence_outbox",
        intent_id="intent" + suffix,
        receipt_id="receipt" + suffix,
        course_key=KEY + suffix,
        session_id="session" + suffix,
        owner="teach",
        stable_event_ids='["event"]',
        payload="{}",
        payload_digest=HASH,
        transaction_id="transaction" + suffix,
        state="committed",
        attempt_count=1,
        next_eligible_at=None,
        error_code=None,
    )
    insert(
        db,
        "evidence_commits",
        commit_id="commit" + suffix,
        intent_id="intent" + suffix,
        transaction_id="transaction" + suffix,
        canonical_path="fixture/log.md",
        event_ids='["event"]',
        event_digests=json.dumps([HASH]),
        committed_log_digest=HASH,
        verified_at=STAMP,
    )
    insert(
        db,
        "grading_results",
        result_id="result" + suffix,
        attempt_id="attempt" + suffix,
        decision_revision=1,
        decision="{}",
        decision_digest=HASH,
        supersedes_result_id=None,
        evidence_commit_id="commit" + suffix,
        created_at=STAMP,
    )


@pytest.mark.parametrize("prior", range(1, 6))
def test_each_prior_version_upgrades_with_exact_rows_and_restorable_wal_backup(
    tmp_path: Path, prior: int
) -> None:
    path = tmp_path / "live.sqlite3"
    with connect_database(path) as db:
        assert migrate(db, target=prior) == prior
        seed_course(db)
        if prior >= 2:
            seed_session(db)
            seed_assessment(db)
            seed_attempt(db)
            seed_response(db)
        before = tuple(tuple(row) for row in db.execute("SELECT * FROM bundles"))
        responses = (
            tuple(tuple(row) for row in db.execute("SELECT * FROM responses")) if prior >= 2 else ()
        )
        backup = tmp_path / "backups" / "before.sqlite3"
        assert migrate(db, target=5, backup_path=backup) == 5
        assert tuple(tuple(row) for row in db.execute("SELECT * FROM bundles")) == before
        if prior >= 2:
            assert tuple(tuple(row) for row in db.execute("SELECT * FROM responses")) == responses
        assert db.execute("SELECT count(*) FROM exposure_projection").fetchone()[0] == 0
        assert db.execute("SELECT count(*) FROM grading_results").fetchone()[0] == 0
        verify_integrity(db)
    if prior < 5:
        assert backup.stat().st_mode & 0o777 == 0o600
        with connect_database(backup) as restored:
            assert applied_versions(restored, load_migrations()) == prior
            assert tuple(tuple(row) for row in restored.execute("SELECT * FROM bundles")) == before
            if prior >= 2:
                assert (
                    tuple(tuple(row) for row in restored.execute("SELECT * FROM responses"))
                    == responses
                )
    else:
        assert not backup.exists()


def test_empty_database_versions_checksums_and_settings(tmp_path: Path) -> None:
    with connect_database(tmp_path / "empty.sqlite3") as db:
        assert migrate(db, target=5) == 5
        assert migrate(db, target=5) == 5
        assert db.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        assert db.execute("PRAGMA journal_mode").fetchone()[0] == "wal"
        assert db.execute("PRAGMA synchronous").fetchone()[0] == 2
        assert db.execute("PRAGMA busy_timeout").fetchone()[0] == 5000
        assert len(db.execute("SELECT * FROM schema_migrations").fetchall()) == 5
        with pytest.raises(sqlite3.IntegrityError, match="immutable_schema_migrations"):
            db.execute("UPDATE schema_migrations SET name='changed'")
        assert db.execute("SELECT count(*) FROM courses").fetchone()[0] == 0
        assert db.execute(
            "SELECT requested_model,requested_effort FROM role_settings "
            "WHERE role_key='uni_source_checker'"
        ).fetchone()[:] == ("gpt-6-astra", "high")


def test_checksum_unknown_schema_and_unversioned_database_fail_closed(tmp_path: Path) -> None:
    known = load_migrations()
    with connect_database(tmp_path / "ledger.sqlite3") as db:
        migrate(db)
        altered = (replace(known[0], checksum="b" * 64),) + known[1:]
        with pytest.raises(MigrationError, match="checksum"):
            migrate(db, migrations=altered)
        insert(
            db,
            "schema_migrations",
            version=len(known) + 1,
            name="future.sql",
            checksum=HASH,
            applied_at=STAMP,
        )
        with pytest.raises(MigrationError, match="Unknown newer"):
            migrate(db)
    with connect_database(tmp_path / "unversioned.sqlite3") as db:
        db.execute("CREATE TABLE unexpected(value TEXT)")
        with pytest.raises(MigrationError, match="Unversioned"):
            migrate(db)


def test_upgrade_requires_backup_and_rollback_preserves_prior_schema(tmp_path: Path) -> None:
    known = load_migrations()
    with connect_database(tmp_path / "crash.sqlite3") as db:
        migrate(db, target=4)
        seed_course(db)
        with pytest.raises(MigrationError, match="backup"):
            migrate(db)
        sql = "CREATE TABLE partial_write(value TEXT);\nSELECT missing_function();\n"
        broken = known[:4] + (
            replace(known[4], sql=sql, checksum=hashlib.sha256(sql.encode()).hexdigest()),
        )
        backup = tmp_path / "before.sqlite3"
        with pytest.raises(sqlite3.OperationalError, match="missing_function"):
            migrate(db, migrations=broken, backup_path=backup)
        assert applied_versions(db, known) == 4
        assert not db.execute(
            "SELECT name FROM sqlite_master WHERE name='partial_write'"
        ).fetchall()
        assert db.execute("SELECT count(*) FROM courses").fetchone()[0] == 1
        assert migrate(db, target=5, backup_path=tmp_path / "retry.sqlite3") == 5
        with pytest.raises(MigrationError, match="Downgrade"):
            migrate(db, target=4)


def test_v1_publication_course_guards_and_compare_and_swap(tmp_path: Path) -> None:
    with connect_database(tmp_path / "v1.sqlite3") as db:
        migrate(db, target=1)
        seed_course(db)
        seed_course(db, "other")
        seed_bundle(db, "next")
        insert(
            db,
            "publication_pointers",
            course_key=KEY,
            bundle_id="bundle",
            generation=1,
            changed_at=STAMP,
        )
        assert (
            db.execute(
                "UPDATE publication_pointers SET bundle_id=?,generation=generation+1 "
                "WHERE course_key=? AND generation=?",
                ("next", KEY, 1),
            ).rowcount
            == 1
        )
        assert (
            db.execute(
                "UPDATE publication_pointers SET bundle_id=?,generation=generation+1 "
                "WHERE course_key=? AND generation=?",
                ("bundle", KEY, 1),
            ).rowcount
            == 0
        )
        with pytest.raises(sqlite3.IntegrityError, match="unvalidated_publication"):
            db.execute("UPDATE publication_pointers SET bundle_id='bundleother',generation=3")
        with pytest.raises(sqlite3.IntegrityError, match="immutable_bundles"):
            db.execute("UPDATE bundles SET plan_version='P002'")
        with pytest.raises(sqlite3.IntegrityError):
            insert(
                db,
                "courses",
                course_key="crs_unicode01",
                course_id="fixture/Winter_Semester/Cafe\u0301",
                academic_year="fixture",
                semester="Winter_Semester",
                course_folder="Cafe\u0301",
                course_code=None,
                display_name="Fixture",
            )
            insert(
                db,
                "courses",
                course_key="crs_unicode02",
                course_id="fixture/Winter_Semester/Caf\u00e9",
                academic_year="fixture",
                semester="Winter_Semester",
                course_folder="Caf\u00e9",
                course_code=None,
                display_name="Fixture",
            )


def test_v2_forward_result_guards_and_v3_valid_verified_assignment(tmp_path: Path) -> None:
    with connect_database(tmp_path / "staged.sqlite3") as db:
        migrate(db, target=2)
        seed_course(db)
        seed_session(db)
        seed_assessment(db)
        seed_assessment(db, "submitted", status="submitted")
        seed_attempt(db)
        with pytest.raises(sqlite3.IntegrityError, match="unavailable_until_v3"):
            seed_assessment(db, "bad", final_result="not-yet-real")
        with pytest.raises(sqlite3.IntegrityError, match="unavailable_until_v3"):
            db.execute(
                "UPDATE assessments SET final_result_id='not-yet-real' WHERE "
                "assessment_id='assessment'"
            )
        migrate(db, target=3, backup_path=tmp_path / "v2.sqlite3")
        seed_verified_result(db)
        with pytest.raises(sqlite3.IntegrityError, match="assessment_final_result_mismatch"):
            db.execute(
                "UPDATE assessments SET status='finalized',final_result_id='missing' "
                "WHERE assessment_id='assessment'"
            )
        with pytest.raises(sqlite3.IntegrityError, match="assessment_final_result_mismatch"):
            db.execute(
                "UPDATE assessments SET status='finalized',final_result_id='result' "
                "WHERE assessment_id='submitted'"
            )
        db.execute(
            "UPDATE assessments SET status='finalized',final_result_id='result' "
            "WHERE assessment_id='assessment'"
        )
        assert (
            db.execute(
                "SELECT final_result_id FROM assessments WHERE assessment_id='assessment'"
            ).fetchone()[0]
            == "result"
        )
        assert (
            db.execute("SELECT status FROM assessments WHERE assessment_id='submitted'").fetchone()[
                0
            ]
            == "submitted"
        )
        with pytest.raises(sqlite3.IntegrityError, match="immutable_grading_results"):
            db.execute("DELETE FROM grading_results")


def test_v2_drafts_revision_selection_and_submission_freeze(tmp_path: Path) -> None:
    with connect_database(tmp_path / "draft.sqlite3") as db:
        migrate(db, target=2)
        seed_course(db)
        seed_session(db)
        seed_assessment(db)
        seed_attempt(db)
        insert(
            db,
            "assessment_drafts",
            assessment_id="assessment",
            item_id="item",
            attempt_id="attempt",
            draft_revision=1,
            response=None,
            explicit_blank=1,
            reported_conditions=None,
            updated_at=STAMP,
        )
        with pytest.raises(sqlite3.IntegrityError, match="draft_revision_conflict"):
            db.execute("UPDATE assessment_drafts SET explicit_blank=0,response='{}'")
        db.execute("UPDATE assessment_drafts SET explicit_blank=0,response='{}',draft_revision=2")
        with pytest.raises(sqlite3.IntegrityError, match="draft_not_active_selected"):
            insert(
                db,
                "assessment_drafts",
                assessment_id="assessment",
                item_id="unselected",
                attempt_id="attempt",
                draft_revision=1,
                response=None,
                explicit_blank=1,
                reported_conditions=None,
                updated_at=STAMP,
            )
        db.execute("UPDATE assessments SET status='submitted',revision=2")
        with pytest.raises(sqlite3.IntegrityError, match="draft_not_active_selected"):
            db.execute("UPDATE assessment_drafts SET draft_revision=3,response='{}'")
        with pytest.raises(sqlite3.IntegrityError, match="selection_frozen"):
            db.execute("UPDATE assessments SET selected_items='[]'")
        with pytest.raises(sqlite3.IntegrityError, match="draft_not_active_selected"):
            db.execute("DELETE FROM assessment_drafts")
        assert db.execute("SELECT count(*) FROM responses").fetchone()[0] == 0
        assert db.execute("SELECT count(*) FROM evidence_outbox").fetchone()[0] == 0


def test_v2_response_receipt_command_and_nonacademic_guards(tmp_path: Path) -> None:
    with connect_database(tmp_path / "receipts.sqlite3") as db:
        migrate(db, target=2)
        seed_course(db)
        seed_session(db)
        seed_assessment(db)
        seed_attempt(db)
        seed_response(db)
        seed_command(db, "different")
        with pytest.raises(sqlite3.IntegrityError, match="immutable_responses"):
            db.execute("UPDATE responses SET response='{}'")
        with pytest.raises(sqlite3.IntegrityError):
            insert(
                db,
                "responses",
                receipt_id="receipt",
                attempt_id="attempt",
                command_id="different",
                response="{}",
                response_digest=HASH,
                conditions="{}",
                received_at=STAMP,
                reported_answered_at=None,
            )
        insert(
            db,
            "receipts",
            receipt_id="bookmark",
            command_id="different",
            kind="session",
            aggregate_id="session",
            payload='{"canonical_commit_state":"not_applicable"}',
            payload_digest=HASH,
            received_at=STAMP,
        )
        with pytest.raises(sqlite3.IntegrityError, match="nonacademic"):
            insert(
                db,
                "evidence_outbox",
                intent_id="intent",
                receipt_id="bookmark",
                course_key=KEY,
                session_id="session",
                owner="teach",
                stable_event_ids='["event"]',
                payload="{}",
                payload_digest=HASH,
                transaction_id="tx",
                state="pending",
                attempt_count=0,
            )
        with pytest.raises(sqlite3.IntegrityError):
            seed_command(db)


def job_request() -> RequestedJobV1:
    return RequestedJobV1.model_validate_json(
        json.dumps(
            {
                "job_id": "job_12345678-1234-4123-8123-123456789abc",
                "course_key": KEY,
                "kind": "source_inventory",
                "dedupe_key": HASH,
                "input_ref": {
                    "course_id": COURSE,
                    "source_snapshot_id": None,
                    "source_snapshot_digest": None,
                    "scope": ["fixture/source.pdf"],
                    "requested_revision": 1,
                },
                "requested_settings": {
                    "model": "gpt-6.1-sol",
                    "effort": "high",
                    "speed": "standard",
                },
                "created_at": STAMP,
            }
        )
    )


def test_v4_requested_jobs_are_durable_idempotent_and_conflict_checked(tmp_path: Path) -> None:
    path = tmp_path / "jobs.sqlite3"
    request = job_request()
    with connect_database(path) as db:
        migrate(db, target=4)
        seed_course(db)
        repo = SQLiteRequestedJobs(db)
        first = repo.request(request)
        assert first.state == "queued" and first.revision == 1 and first.actual_settings is None
        replay = request.model_copy(update={"job_id": "job_22345678-1234-4123-8123-123456789abc"})
        assert repo.request(replay) == first
        different = request.model_copy(update={"kind": "ingest_prepare"})
        with pytest.raises(JobConflict):
            repo.request(different)
    with connect_database(path) as reopened:
        assert SQLiteRequestedJobs(reopened).get(request.job_id) == first
        assert reopened.execute("SELECT count(*) FROM jobs").fetchone()[0] == 1
        assert reopened.execute("SELECT count(*) FROM events").fetchone()[0] == 0


def test_v4_approval_digest_revision_and_human_command_guards(tmp_path: Path) -> None:
    with connect_database(tmp_path / "approval.sqlite3") as db:
        migrate(db, target=4)
        seed_course(db)
        SQLiteRequestedJobs(db).request(job_request())
        insert(
            db,
            "approval_proposals",
            proposal_id="proposal",
            job_id=job_request().job_id,
            course_key=KEY,
            kind="source_selection",
            proposal_digest=HASH,
            source_snapshot_id="snapshot",
            expected_hashes="{}",
            scope="{}",
            preserved_version_refs="[]",
            safe_preview="{}",
            created_at=STAMP,
        )
        seed_command(db, "decision", kind="approval_decision", aggregate_id="proposal")
        seed_command(db, "retry", kind="retry")
        for digest, revision, command, principal in (
            ("b" * 64, 1, "decision", "human"),
            (HASH, 2, "decision", "human"),
            (HASH, 1, "retry", "human"),
            (HASH, 1, "decision", "source-content"),
        ):
            with pytest.raises(sqlite3.IntegrityError, match="digest_bound_human"):
                insert(
                    db,
                    "approval_decisions",
                    decision_id="invalid",
                    proposal_id="proposal",
                    command_id=command,
                    principal=principal,
                    decision="approve",
                    proposal_digest=digest,
                    expected_job_revision=revision,
                    decided_at=STAMP,
                )
        insert(
            db,
            "approval_decisions",
            decision_id="decision",
            proposal_id="proposal",
            command_id="decision",
            principal="human",
            decision="reject",
            proposal_digest=HASH,
            expected_job_revision=1,
            decided_at=STAMP,
        )
        with pytest.raises(sqlite3.IntegrityError, match="immutable_approval_proposals"):
            db.execute("UPDATE approval_proposals SET safe_preview='{}'")
        with pytest.raises(sqlite3.IntegrityError, match="immutable_approval_decisions"):
            db.execute("DELETE FROM approval_decisions")
        with pytest.raises(sqlite3.IntegrityError):
            insert(
                db,
                "approval_decisions",
                decision_id="second",
                proposal_id="proposal",
                command_id="decision",
                principal="human",
                decision="approve",
                proposal_digest=HASH,
                expected_job_revision=1,
                decided_at=STAMP,
            )


def test_v4_auth_terminal_and_single_use_capability(tmp_path: Path) -> None:
    with connect_database(tmp_path / "auth.sqlite3") as db:
        migrate(db, target=4)
        insert(
            db,
            "provider_auth_flows",
            flow_id="flow",
            requested_action="sign_in",
            state="pending",
            registration_refs="{}",
            host_refs="{}",
            state_digest=HASH,
            nonce_digest=HASH,
            expires_at=STAMP,
            terminal_at=None,
            subject_ref=None,
        )
        with pytest.raises(sqlite3.IntegrityError):
            db.execute("UPDATE provider_auth_flows SET state='completed',terminal_at=?", (STAMP,))
        db.execute(
            "UPDATE provider_auth_flows SET "
            "state='completed',terminal_at=?,subject_ref='opaque-subject'",
            (STAMP,),
        )
        with pytest.raises(sqlite3.IntegrityError, match="auth_flow_terminal"):
            db.execute("UPDATE provider_auth_flows SET state='pending',terminal_at=NULL")
        insert(
            db, "bootstrap_capabilities", capability_digest=HASH, expires_at=STAMP, consumed_at=None
        )
        db.execute(
            "UPDATE bootstrap_capabilities SET consumed_at=? WHERE "
            "capability_digest=? AND consumed_at IS NULL",
            (STAMP, HASH),
        )
        with pytest.raises(sqlite3.IntegrityError, match="already_consumed"):
            db.execute("UPDATE bootstrap_capabilities SET consumed_at=NULL")
        columns = {row[1] for row in db.execute("PRAGMA table_info(provider_auth_flows)")}
        assert not columns & {
            "access_token",
            "refresh_token",
            "pkce_verifier",
            "authorization_code",
        }


@pytest.mark.parametrize("version", [3, 4, 5])
def test_derived_cross_course_guards_apply_when_tables_introduced(
    tmp_path: Path, version: int
) -> None:
    with connect_database(tmp_path / "cross-course.sqlite3") as db:
        migrate(db, target=version)
        seed_course(db)
        seed_course(db, "other")
        seed_session(db)
        seed_session(db, "other")
        seed_assessment(db)
        with pytest.raises(sqlite3.IntegrityError, match="session_bundle_course_mismatch"):
            insert(
                db,
                "sessions",
                session_id="bad-session",
                course_key=KEY,
                bundle_id="bundleother",
                route_kind="lesson",
                route_ref="{}",
                status="active",
                revision=1,
                bookmark="{}",
                created_at=STAMP,
                updated_at=STAMP,
            )
        with pytest.raises(sqlite3.IntegrityError, match="projection_course_mismatch"):
            insert(
                db,
                "exposure_projection",
                projection_id="bad",
                course_key=KEY,
                equivalence_id="eq",
                objective_ref=json.dumps({"course_id": COURSE + "other"}),
                canonical_event_id="event",
                time=None,
                timing_quality="unknown",
                exposure_kind="prompt",
            )
        with pytest.raises(sqlite3.IntegrityError, match="review_course_mismatch"):
            insert(
                db,
                "review_projection",
                recommendation_id="bad",
                course_key=KEY,
                canonical_cursor="cursor",
                recommendation=json.dumps({"course_id": COURSE + "other"}),
                rebuilt_at=STAMP,
            )
        with pytest.raises(sqlite3.IntegrityError, match="variant_course_mismatch"):
            insert(
                db,
                "variant_reservations",
                reservation_id="bad",
                session_id="session",
                assessment_id="assessment",
                equivalence_id="eq",
                variant_ref=json.dumps({"course_id": COURSE + "other"}),
                state="reserved",
                created_at=STAMP,
            )
        insert(
            db,
            "variant_reservations",
            reservation_id="valid",
            session_id="session",
            assessment_id="assessment",
            equivalence_id="eq",
            variant_ref=json.dumps({"course_id": COURSE}),
            state="reserved",
            created_at=STAMP,
        )
        with pytest.raises(sqlite3.IntegrityError):
            insert(
                db,
                "variant_reservations",
                reservation_id="duplicate",
                session_id="session",
                assessment_id="assessment",
                equivalence_id="eq",
                variant_ref=json.dumps({"course_id": COURSE}),
                state="offered",
                created_at=STAMP,
            )
        db.execute("UPDATE variant_reservations SET state='released'")
        insert(
            db,
            "variant_reservations",
            reservation_id="replacement",
            session_id="session",
            assessment_id="assessment",
            equivalence_id="eq",
            variant_ref=json.dumps({"course_id": COURSE}),
            state="reserved",
            created_at=STAMP,
        )


def test_v4_completed_checkpoint_and_lease_fences_survive_retries(tmp_path: Path) -> None:
    with connect_database(tmp_path / "lease.sqlite3") as db:
        migrate(db, target=4)
        seed_course(db)
        SQLiteRequestedJobs(db).request(job_request())
        insert(
            db,
            "job_steps",
            job_id=job_request().job_id,
            step_key="inventory",
            ordinal=0,
            input_digest=HASH,
            state="completed",
            output_ref="{}",
            checkpoint="{}",
            attempt_count=1,
            last_error=None,
        )
        with pytest.raises(sqlite3.IntegrityError, match="completed_step_immutable"):
            db.execute("UPDATE job_steps SET state='running'")
        with pytest.raises(sqlite3.IntegrityError, match="completed_step_immutable"):
            db.execute("DELETE FROM job_steps")
        db.execute("UPDATE job_steps SET state='invalidated',input_digest=?", ("b" * 64,))
        insert(
            db,
            "course_leases",
            course_key=KEY,
            holder_id="first",
            fence=1,
            owner_checkout="/fixture",
            acquired_at=STAMP,
            renewed_at=STAMP,
            expires_at=STAMP,
        )
        with pytest.raises(sqlite3.IntegrityError, match="lease_fence_conflict"):
            db.execute("UPDATE course_leases SET holder_id='second'")
        db.execute("UPDATE course_leases SET holder_id='second',fence=2")
        with pytest.raises(sqlite3.IntegrityError, match="fence_must_be_retained"):
            db.execute("DELETE FROM course_leases")
