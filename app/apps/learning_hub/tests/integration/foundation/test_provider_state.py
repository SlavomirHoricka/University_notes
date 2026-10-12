"""Additive H01 seam tests: operational fixtures only, never actual auth or learner facts."""

import sqlite3
from collections.abc import Iterator
from pathlib import Path
from uuid import uuid4

import pytest
from learning_hub.adapters.storage.database import connect_database
from learning_hub.adapters.storage.migration import load_migrations, migrate
from learning_hub.adapters.storage.provider import SQLiteProviderState
from learning_hub.domain.models.provider_state import (
    ProviderAccount,
    ProviderAction,
    ProviderFlowHost,
    ProviderFlowRegistration,
    ProviderFlowTransition,
    ProviderRunPreparation,
    ProviderRunTransition,
    StoredProviderFlow,
)
from learning_hub.domain.models.services import ModelSettings
from learning_hub.domain.ports.provider import ProviderStateConflict, ProviderStateRepository
from pydantic import ValidationError

STAMP = "2026-10-11T10:00:00Z"
SETTINGS = ModelSettings(model="fixture-model", effort="high")


def identifier(prefix: str) -> str:
    return f"{prefix}_{uuid4()}"


@pytest.fixture
def db(tmp_path: Path) -> Iterator[sqlite3.Connection]:
    connection = connect_database(tmp_path / "provider.sqlite3")
    migrate(connection)
    try:
        yield connection
    finally:
        connection.close()


def account(revision: int = 2, subject: str = "fixture-subject") -> ProviderAccount:
    return ProviderAccount(
        subject=subject,
        client_id="fixture-client",
        scopes=("inference",),
        active=True,
        account_revision=revision,
        inference_verified=False,
        verified_settings=None,
    )


def action(
    kind: str = "sign_in", revision: int = 1, aggregate: str | None = None
) -> ProviderAction:
    return ProviderAction.model_validate_json(
        __import__("json").dumps(
            {
                "command_id": identifier("cmd"),
                "receipt_id": identifier("rec"),
                "local_principal": "fixture-human",
                "kind": kind,
                "idempotency_key": str(uuid4()),
                "request_digest": "a" * 64,
                "aggregate_id": aggregate or identifier("aut"),
                "expected_account_revision": revision,
                "received_at": STAMP,
            }
        )
    )


def flow(command: ProviderAction, expected_subject: str | None = None) -> StoredProviderFlow:
    return StoredProviderFlow(
        flow_id=command.aggregate_id,
        requested_action="sign_in",
        state="pending",
        registration=ProviderFlowRegistration(
            client_id="fixture-client",
            redirect_uri="http://127.0.0.1:8765/callback",
            expected_account_revision=command.expected_account_revision,
            expected_subject=expected_subject,
        ),
        host=ProviderFlowHost(
            instance_id="fixture-instance", callback_origin="http://127.0.0.1:8765"
        ),
        state_digest="b" * 64,
        nonce_digest="c" * 64,
        expires_at="2026-10-11T10:05:00Z",
    )


def preparation(revision: int = 2) -> ProviderRunPreparation:
    return ProviderRunPreparation(
        logical_task_id="fixture-task",
        request_digest="d" * 64,
        run_id=identifier("run"),
        subject="fixture-subject",
        client_id="fixture-client",
        account_revision=revision,
        requested_settings=SETTINGS,
        required_scopes=("inference",),
        created_at=STAMP,
    )


def test_additive_upgrade_keeps_prior_checksums_rows_and_backup(tmp_path: Path) -> None:
    from .test_h02_migrations import seed_command

    with connect_database(tmp_path / "upgrade.sqlite3") as db:
        migrate(db, target=5)
        seed_command(db, "historical-command")
        before = tuple(db.execute("SELECT * FROM commands").fetchone())
        ledger = [tuple(row) for row in db.execute("SELECT * FROM schema_migrations")]
        backup = tmp_path / "backup.sqlite3"
        assert migrate(db, backup_path=backup) == 6
        assert tuple(db.execute("SELECT * FROM commands").fetchone()) == before
        assert [
            tuple(row) for row in db.execute("SELECT * FROM schema_migrations WHERE version<=5")
        ] == ledger
        assert migrate(db) == len(load_migrations()) == 6
        with connect_database(backup) as saved:
            assert saved.execute("SELECT max(version) FROM schema_migrations").fetchone()[0] == 5
            assert tuple(saved.execute("SELECT * FROM commands").fetchone()) == before


def test_account_singleton_cas_revoke_and_history(db: sqlite3.Connection) -> None:
    store: ProviderStateRepository = SQLiteProviderState(db)
    assert store.account_state().revision == 1
    assert store.account_state().account is None
    active = store.activate(account(), expected_revision=1)
    assert active.account == account()
    with pytest.raises(ProviderStateConflict):
        store.activate(account(3, "other-subject"), expected_revision=1)
    with pytest.raises(ProviderStateConflict):
        store.activate(account(2, "other-subject"), expected_revision=2)
    revoked = store.revoke(expected_revision=2)
    assert revoked.revision == 3 and revoked.account is None
    assert db.execute("SELECT count(*) FROM provider_accounts").fetchone()[0] == 1
    assert db.execute("SELECT active FROM provider_accounts").fetchone()[0] == 0
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("UPDATE provider_accounts SET subject='substitute'")
    with pytest.raises(sqlite3.IntegrityError):
        db.execute("DELETE FROM provider_accounts")
    assert store.activate(account(4, "other-subject"), expected_revision=3).revision == 4


def test_action_atomic_replay_precedes_stale_revision_and_body_conflict(
    db: sqlite3.Connection,
) -> None:
    store = SQLiteProviderState(db)
    command = action()
    original_flow = flow(command)
    result = store.create_flow(command, original_flow)
    assert result.flow_id == original_flow.flow_id
    assert result.receipt.canonical_commit_state == "not_applicable"
    store.activate(account(), expected_revision=1)
    replay = command.model_copy(
        update={"command_id": identifier("cmd"), "receipt_id": identifier("rec")}
    )
    assert store.create_flow(replay, original_flow) == result
    with pytest.raises(ProviderStateConflict, match="body mismatch"):
        store.create_flow(replay.model_copy(update={"request_digest": "e" * 64}), original_flow)
    assert db.execute("SELECT count(*) FROM receipts").fetchone()[0] == 1
    assert db.execute("SELECT count(*) FROM provider_auth_flows").fetchone()[0] == 1
    assert db.execute("SELECT count(*) FROM evidence_outbox").fetchone()[0] == 0
    assert store.get_flow_by_state_digest(original_flow.state_digest) == original_flow
    signout = action("sign_out", 2)
    signedout = store.revoke_action(signout)
    assert signedout.account_revision == 3
    assert store.revoke_action(signout) == signedout
    assert store.account_state().revision == 3


def test_flow_receipt_conflict_rolls_back_entire_creation(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    first = action()
    store.create_flow(first, flow(first))
    second = action()
    second = second.model_copy(update={"receipt_id": first.receipt_id})
    second_flow = flow(second).model_copy(update={"state_digest": "f" * 64})
    with pytest.raises(ProviderStateConflict):
        store.create_flow(second, second_flow)
    assert store.get_flow(second_flow.flow_id) is None
    assert db.execute("SELECT count(*) FROM commands").fetchone()[0] == 1


def validating(store: SQLiteProviderState, command: ProviderAction) -> StoredProviderFlow:
    original = flow(command)
    store.create_flow(command, original)
    store.transition_flow(
        original.flow_id, ProviderFlowTransition(expected_revision=1, state="awaiting_callback")
    )
    return store.transition_flow(
        original.flow_id, ProviderFlowTransition(expected_revision=2, state="validating")
    )


def test_flow_completion_atomic_activation_and_subject_revision_conflicts(
    db: sqlite3.Connection,
) -> None:
    store = SQLiteProviderState(db)
    command = action()
    original = validating(store, command)
    with pytest.raises(ProviderStateConflict):
        store.transition_flow(
            original.flow_id,
            ProviderFlowTransition(
                expected_revision=3,
                state="completed",
                subject_ref="fixture-subject",
                terminal_at=STAMP,
            ),
        )
    completed = store.complete_flow(
        original.flow_id, account(), expected_flow_revision=3, terminal_at=STAMP
    )
    assert completed.account == account()
    stored = store.get_flow(original.flow_id)
    assert stored is not None and stored.state == "completed" and stored.revision == 4
    with pytest.raises(ProviderStateConflict):
        store.transition_flow(
            original.flow_id,
            ProviderFlowTransition(expected_revision=4, state="failed", terminal_at=STAMP),
        )
    with pytest.raises(ProviderStateConflict):
        store.complete_flow(
            original.flow_id, account(3), expected_flow_revision=3, terminal_at=STAMP
        )


def test_pending_flow_cannot_overwrite_concurrently_changed_account(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    original = validating(store, action())
    store.activate(account(2, "concurrent-subject"), expected_revision=1)
    with pytest.raises(ProviderStateConflict):
        store.complete_flow(
            original.flow_id, account(), expected_flow_revision=3, terminal_at=STAMP
        )
    assert store.account_state().account == account(2, "concurrent-subject")
    assert store.get_flow(original.flow_id) == original


def test_run_claim_persisted_before_dispatch_recovery_no_redispatch(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    store.activate(account(), expected_revision=1)
    request = preparation()
    pending = store.prepare_run(request)
    assert pending.state == "prepared"
    claimed = store.claim_run(request.run_id, expected_revision=1)
    assert claimed.state == "submitted"
    # A replacement process uses only durable state. A missing turn stays uncertain.
    reopened = SQLiteProviderState(db)
    assert reopened.get_run_by_task(request.logical_task_id) == claimed
    uncertain = reopened.update_run(
        request.run_id,
        ProviderRunTransition(
            expected_revision=2, state="unknown", error_code="turn_identity_unknown"
        ),
    )
    assert uncertain.state == "unknown"
    for state in ("prepared", "submitted", "running"):
        with pytest.raises(ProviderStateConflict):
            reopened.update_run(
                request.run_id, ProviderRunTransition(expected_revision=3, state=state)
            )
    with pytest.raises(ProviderStateConflict):
        reopened.claim_run(request.run_id, expected_revision=3)
    retry = request.model_copy(update={"run_id": identifier("run")})
    assert reopened.prepare_run(retry) == uncertain
    with pytest.raises(ProviderStateConflict):
        reopened.prepare_run(retry.model_copy(update={"request_digest": "f" * 64}))
    assert db.execute("SELECT count(*) FROM provider_runs").fetchone()[0] == 1
    with pytest.raises(ProviderStateConflict, match="Unbound"):
        reopened.update_run(
            request.run_id,
            ProviderRunTransition(
                expected_revision=3, state="completed", thread_id="invented", turn_id="invented"
            ),
        )
    assert reopened.get_run(request.run_id) == uncertain


def test_bound_uncertain_run_can_recover_only_original_turn(db: sqlite3.Connection) -> None:
    reopened = SQLiteProviderState(db)
    reopened.activate(account(), expected_revision=1)
    request = preparation()
    reopened.prepare_run(request)
    reopened.claim_run(request.run_id, expected_revision=1)
    reopened.update_run(
        request.run_id,
        ProviderRunTransition(
            expected_revision=2,
            state="running",
            thread_id="actual-thread",
            turn_id="actual-turn",
            actual_settings=SETTINGS,
        ),
    )
    reopened.update_run(request.run_id, ProviderRunTransition(expected_revision=3, state="unknown"))
    with pytest.raises(ProviderStateConflict):
        reopened.update_run(
            request.run_id,
            ProviderRunTransition(
                expected_revision=4,
                state="completed",
                thread_id="actual-thread",
                turn_id="different-turn",
            ),
        )
    recovered = reopened.update_run(
        request.run_id,
        ProviderRunTransition(
            expected_revision=4,
            state="completed",
            thread_id="actual-thread",
            turn_id="actual-turn",
            actual_settings=SETTINGS,
            terminal_output="Actual fixture terminal text",
        ),
    )
    assert recovered.state == "completed" and recovered.revision == 5
    with pytest.raises(ProviderStateConflict):
        reopened.update_run(
            request.run_id, ProviderRunTransition(expected_revision=5, state="failed")
        )


def test_run_account_grant_and_bound_ids_cannot_change(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    store.activate(account(), expected_revision=1)
    request = preparation()
    with pytest.raises(ProviderStateConflict):
        store.prepare_run(request.model_copy(update={"required_scopes": ("missing-grant",)}))
    store.prepare_run(request)
    store.revoke(expected_revision=2)
    with pytest.raises(ProviderStateConflict):
        store.claim_run(request.run_id, expected_revision=1)
    store.activate(account(4), expected_revision=3)
    second = preparation(4).model_copy(update={"logical_task_id": "second-task"})
    store.prepare_run(second)
    store.claim_run(second.run_id, expected_revision=1)
    running = store.update_run(
        second.run_id,
        ProviderRunTransition(
            expected_revision=2,
            state="running",
            thread_id="thread",
            turn_id="turn",
            actual_settings=SETTINGS,
        ),
    )
    assert running.revision == 3
    with pytest.raises(ProviderStateConflict):
        store.update_run(
            second.run_id,
            ProviderRunTransition(
                expected_revision=3, state="completed", thread_id="other-thread", turn_id="turn"
            ),
        )
    assert store.get_run(second.run_id) == running


def test_verification_requires_actual_completed_bound_exact_settings(
    db: sqlite3.Connection,
) -> None:
    store = SQLiteProviderState(db)
    store.activate(account(), expected_revision=1)
    request = preparation()
    store.prepare_run(request)
    with pytest.raises(ProviderStateConflict):
        store.mark_verified(SETTINGS, expected_revision=2, run_id=request.run_id)
    store.claim_run(request.run_id, expected_revision=1)
    store.update_run(
        request.run_id,
        ProviderRunTransition(
            expected_revision=2,
            state="completed",
            thread_id="thread",
            turn_id="turn",
            actual_settings=SETTINGS,
            terminal_output="fixture",
        ),
    )
    with pytest.raises(ProviderStateConflict):
        store.mark_verified(
            ModelSettings(model="other", effort="high"), expected_revision=2, run_id=request.run_id
        )
    verified = store.mark_verified(SETTINGS, expected_revision=2, run_id=request.run_id)
    assert verified.revision == 3 and verified.account is not None
    assert verified.account.inference_verified and verified.account.verified_settings == SETTINGS
    assert store.get_run(request.run_id).preparation.account_revision == 2  # type: ignore[union-attr]
    assert db.execute("SELECT count(*) FROM provider_accounts").fetchone()[0] == 2


def test_private_unknown_secret_fields_and_invalid_scope_output_rejected() -> None:
    with pytest.raises(ValidationError):
        StoredProviderFlow.model_validate_json(
            flow(action()).model_dump_json()[:-1] + ',"verifier":"secret"}'
        )
    with pytest.raises(ValidationError):
        ProviderRunPreparation.model_validate_json(
            preparation().model_copy(update={"required_scopes": ()}).model_dump_json()
        )
    with pytest.raises(ValidationError):
        ProviderRunTransition(expected_revision=1, state="completed", terminal_output="x" * 200001)
    from learning_hub.application.core.bootstrap import create_app

    schema = create_app().openapi()["components"]["schemas"]
    for private in ("ProviderAccount", "StoredProviderFlow", "ProviderAction", "StoredProviderRun"):
        assert private not in schema


def test_expiry_and_verification_bypass_cannot_activate(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    with pytest.raises(ProviderStateConflict, match="terminal inference"):
        store.activate(
            account().model_copy(
                update={"inference_verified": True, "verified_settings": SETTINGS}
            ),
            expected_revision=1,
        )
    assert store.account_state().revision == 1
    command = action()
    expired = flow(command).model_copy(update={"expires_at": STAMP})
    with pytest.raises(ProviderStateConflict):
        store.create_flow(command, expired)
    assert store.get_flow(command.aggregate_id) is None
    original = validating(store, command)
    with pytest.raises(ProviderStateConflict, match="Expired"):
        store.complete_flow(
            original.flow_id, account(), expected_flow_revision=3, terminal_at=original.expires_at
        )
    assert store.get_flow(original.flow_id) == original
    assert store.account_state().revision == 1


def test_returning_flow_subject_bound_before_concurrent_switch(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    store.activate(account(), expected_revision=1)
    command = action(revision=2)
    original = flow(command, expected_subject="fixture-subject")
    store.create_flow(command, original)
    store.transition_flow(
        original.flow_id, ProviderFlowTransition(expected_revision=1, state="awaiting_callback")
    )
    store.transition_flow(
        original.flow_id, ProviderFlowTransition(expected_revision=2, state="validating")
    )
    with pytest.raises(ProviderStateConflict, match="subject/client"):
        store.complete_flow(
            original.flow_id,
            account(3, "different-subject"),
            expected_flow_revision=3,
            terminal_at=STAMP,
        )
    assert store.account_state().account == account()
    assert store.get_flow(original.flow_id).state == "validating"  # type: ignore[union-attr]


def test_initial_dynamic_registration_binds_validated_issued_client(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    command = action()
    original = flow(command).model_copy(
        update={
            "registration": flow(command).registration.model_copy(
                update={"client_id": "dynamic_agent_client"}
            )
        }
    )
    store.create_flow(command, original)
    store.transition_flow(
        original.flow_id, ProviderFlowTransition(expected_revision=1, state="awaiting_callback")
    )
    store.transition_flow(
        original.flow_id, ProviderFlowTransition(expected_revision=2, state="validating")
    )
    with pytest.raises(ProviderStateConflict, match="Issued"):
        store.complete_flow(
            original.flow_id,
            account().model_copy(update={"client_id": "dynamic_agent_client"}),
            expected_flow_revision=3,
            terminal_at=STAMP,
        )
    issued = account().model_copy(update={"client_id": "fixture-issued-client"})
    result = store.complete_flow(
        original.flow_id, issued, expected_flow_revision=3, terminal_at=STAMP
    )
    assert result.account == issued and not result.account.inference_verified
    with pytest.raises(ValidationError):
        ProviderAccount.model_validate_json(
            issued.model_copy(update={"client_id": ""}).model_dump_json()
        )


@pytest.mark.parametrize(
    "kind,active,expected_subject,client",
    [
        ("grant", False, None, "dynamic_agent_client"),
        ("grant", True, "fixture-subject", "dynamic_agent_client"),
        ("sign_in", True, "fixture-subject", "dynamic_agent_client"),
        ("sign_in", True, None, "dynamic_agent_client"),
        ("sign_in", True, "different-subject", "fixture-client"),
    ],
)
def test_dynamic_exception_rejects_mixed_returning_grant_cases(
    db: sqlite3.Connection, kind: str, active: bool, expected_subject: str | None, client: str
) -> None:
    store = SQLiteProviderState(db)
    if active:
        store.activate(account(), expected_revision=1)
    command = action(kind, 2 if active else 1)
    original = flow(command, expected_subject).model_copy(
        update={
            "requested_action": kind,
            "registration": flow(command, expected_subject).registration.model_copy(
                update={"client_id": client}
            ),
        }
    )
    with pytest.raises(ProviderStateConflict):
        store.create_flow(command, original)
    assert store.get_flow(command.aggregate_id) is None
    assert db.execute("SELECT count(*) FROM commands").fetchone()[0] == 0


def test_non_dynamic_initial_client_cannot_be_substituted(db: sqlite3.Connection) -> None:
    store = SQLiteProviderState(db)
    original = validating(store, action())
    with pytest.raises(ProviderStateConflict, match="client mismatch"):
        store.complete_flow(
            original.flow_id,
            account().model_copy(update={"client_id": "unrelated-issued-client"}),
            expected_flow_revision=3,
            terminal_at=STAMP,
        )
    assert store.account_state().account is None
