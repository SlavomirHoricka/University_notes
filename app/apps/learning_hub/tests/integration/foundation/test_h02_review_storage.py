import json
import sqlite3
from pathlib import Path

import pytest
from learning_hub.adapters.storage.database import connect_database
from learning_hub.adapters.storage.jobs import SQLiteRequestedJobs
from learning_hub.adapters.storage.migration import migrate

from .test_h02_migrations import HASH, KEY, STAMP, insert, job_request, seed_command, seed_course


def proposal(db: sqlite3.Connection, name: str) -> None:
    insert(
        db,
        "approval_proposals",
        proposal_id=name,
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


def decision(db: sqlite3.Connection, name: str, proposal_id: str, command_id: str) -> None:
    insert(
        db,
        "approval_decisions",
        decision_id=name,
        proposal_id=proposal_id,
        command_id=command_id,
        principal="human",
        decision="approve",
        proposal_digest=HASH,
        expected_job_revision=1,
        decided_at=STAMP,
    )


@pytest.mark.parametrize("version", [4, 5])
def test_review_r1_human_command_is_bound_to_exactly_one_proposal(
    tmp_path: Path, version: int
) -> None:
    with connect_database(tmp_path / "approval.sqlite3") as db:
        migrate(db, target=version)
        seed_course(db)
        SQLiteRequestedJobs(db).request(job_request())
        proposal(db, "first")
        proposal(db, "second")
        seed_command(db, "unrelated", kind="approval_decision", aggregate_id="different-object")
        seed_command(db, "first-command", kind="approval_decision", aggregate_id="first")
        seed_command(db, "second-command", kind="approval_decision", aggregate_id="second")
        for command in ("unrelated", "first-command"):
            with pytest.raises(sqlite3.IntegrityError, match="digest_bound_human"):
                decision(db, "bad", "second", command)
        decision(db, "accepted-first", "first", "first-command")
        with pytest.raises(sqlite3.IntegrityError):
            decision(db, "reused", "second", "first-command")
        decision(db, "accepted-second", "second", "second-command")
        rows = db.execute(
            "SELECT proposal_id,command_id FROM approval_decisions ORDER BY proposal_id"
        ).fetchall()
        assert [tuple(row) for row in rows] == [
            ("first", "first-command"),
            ("second", "second-command"),
        ]
        # Even bypassing the immutable-reference trigger cannot repurpose a recorded command.
        db.execute("DROP TRIGGER commands_fixed_refs")
        db.execute("UPDATE commands SET aggregate_id='second' WHERE command_id='first-command'")
        db.execute("DELETE FROM commands WHERE command_id='unrelated'")
        proposal(db, "third")
        db.execute("UPDATE commands SET aggregate_id='third' WHERE command_id='first-command'")
        with pytest.raises(sqlite3.IntegrityError, match="UNIQUE.*command_id"):
            decision(db, "duplicate-command", "third", "first-command")


@pytest.mark.parametrize("version", [1, 4, 5])
def test_review_r4_extraction_status_advances_without_mutating_original_bytes(
    tmp_path: Path, version: int
) -> None:
    with connect_database(tmp_path / "source.sqlite3") as db:
        migrate(db, target=version)
        seed_course(db)
        insert(
            db,
            "source_files",
            source_id="source",
            course_key=KEY,
            original_name="fixture.pdf",
            managed_relpath="fixture/source.pdf",
            week_ref=json.dumps({"id": "W001", "revision": 1}),
            created_at=STAMP,
            archived_at=None,
        )
        insert(
            db,
            "source_revisions",
            source_revision_id="revision",
            source_id="source",
            revision=1,
            sha256=HASH,
            byte_size=100,
            media_type="application/pdf",
            storage_ref="fixture/immutable-original.pdf",
            extraction_state="pending",
            created_at=STAMP,
        )
        before = dict(db.execute("SELECT * FROM source_revisions").fetchone())
        db.execute(
            "UPDATE source_revisions SET extraction_state='complete' "
            "WHERE source_revision_id='revision'"
        )
        after = dict(db.execute("SELECT * FROM source_revisions").fetchone())
        assert {key: value for key, value in after.items() if key != "extraction_state"} == {
            key: value for key, value in before.items() if key != "extraction_state"
        }
        assert after["extraction_state"] == "complete"
        changes = {
            "source_revision_id": "replacement",
            "source_id": "different",
            "revision": 2,
            "sha256": "b" * 64,
            "byte_size": 101,
            "media_type": "text/plain",
            "storage_ref": "fixture/replaced.pdf",
            "created_at": "2026-10-12T10:00:00Z",
        }
        for column, value in changes.items():
            with pytest.raises(sqlite3.IntegrityError, match="immutable_source_revisions"):
                db.execute(
                    f"UPDATE source_revisions SET {column}=? WHERE source_revision_id='revision'",
                    (value,),
                )
        with pytest.raises(sqlite3.IntegrityError):
            db.execute("UPDATE source_revisions SET extraction_state='invented'")
        with pytest.raises(sqlite3.IntegrityError, match="immutable_source_revisions"):
            db.execute("DELETE FROM source_revisions")
