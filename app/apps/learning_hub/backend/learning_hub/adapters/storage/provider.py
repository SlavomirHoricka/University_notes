"""Transactional private provider metadata, without credentials or inferred RPC outcomes."""

import json
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import datetime

from learning_hub.domain.models.api import ReceiptV1
from learning_hub.domain.models.base import contract_digest
from learning_hub.domain.models.provider_state import (
    ProviderAccount,
    ProviderAccountState,
    ProviderAction,
    ProviderActionResult,
    ProviderFlowTransition,
    ProviderRunPreparation,
    ProviderRunTransition,
    StoredProviderFlow,
    StoredProviderRun,
)
from learning_hub.domain.models.services import ModelSettings
from learning_hub.domain.ports.provider import ProviderStateConflict


class SQLiteProviderState:
    """One connection per caller. Each mutation owns its short SQLite transaction."""

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection

    @contextmanager
    def _transaction(self) -> Iterator[None]:
        if self.connection.in_transaction:
            raise ProviderStateConflict("Provider mutation requires a quiescent connection")
        self.connection.execute("BEGIN IMMEDIATE")
        try:
            yield
            self.connection.commit()
        except sqlite3.IntegrityError as error:
            self.connection.rollback()
            raise ProviderStateConflict("Provider durable invariant conflict") from error
        except BaseException:
            self.connection.rollback()
            raise

    def account_state(self) -> ProviderAccountState:
        pointer = self.connection.execute("SELECT * FROM provider_account_state").fetchone()
        if pointer is None:
            raise ProviderStateConflict("Missing provider account state")
        account = None
        if pointer["subject"] is not None:
            row = self.connection.execute(
                "SELECT * FROM provider_accounts WHERE subject=? AND client_id=? "
                "AND account_revision=? AND active=1",
                (pointer["subject"], pointer["client_id"], pointer["account_revision"]),
            ).fetchone()
            if row is None:
                raise ProviderStateConflict("Account pointer has no active registration")
            account = ProviderAccount.model_validate_json(
                json.dumps(
                    {
                        "subject": row["subject"],
                        "client_id": row["client_id"],
                        "scopes": json.loads(row["scopes"]),
                        "active": bool(row["active"]),
                        "account_revision": row["account_revision"],
                        "inference_verified": bool(row["inference_verified"]),
                        "verified_settings": json.loads(row["verified_settings"])
                        if row["verified_settings"] is not None
                        else None,
                    }
                )
            )
        return ProviderAccountState(revision=pointer["revision"], account=account)

    def _expected_account(self, expected_revision: int) -> ProviderAccountState:
        state = self.account_state()
        if state.revision != expected_revision:
            raise ProviderStateConflict("Provider account revision changed")
        return state

    def _activate(
        self, account: ProviderAccount, expected_revision: int, *, verified_run: bool = False
    ) -> ProviderAccountState:
        self._expected_account(expected_revision)
        if account.inference_verified and not verified_run:
            raise ProviderStateConflict(
                "Only persisted terminal inference proof can verify account"
            )
        if account.client_id == "dynamic_agent_client":
            raise ProviderStateConflict("Issued registration client required")
        if not account.active or account.account_revision != expected_revision + 1:
            raise ProviderStateConflict("New account must use the next singleton revision")
        self.connection.execute("UPDATE provider_accounts SET active=0 WHERE active=1")
        self.connection.execute(
            "INSERT INTO provider_accounts(subject,client_id,account_revision,scopes,active,"
            "inference_verified,verified_settings) VALUES(?,?,?,?,1,?,?)",
            (
                account.subject,
                account.client_id,
                account.account_revision,
                json.dumps(account.scopes),
                int(account.inference_verified),
                account.verified_settings.model_dump_json() if account.verified_settings else None,
            ),
        )
        self.connection.execute(
            "UPDATE provider_account_state SET revision=?,subject=?,client_id=?,account_revision=? "
            "WHERE singleton=1 AND revision=?",
            (
                account.account_revision,
                account.subject,
                account.client_id,
                account.account_revision,
                expected_revision,
            ),
        )
        return self.account_state()

    def activate(self, account: ProviderAccount, *, expected_revision: int) -> ProviderAccountState:
        with self._transaction():
            return self._activate(account, expected_revision)

    def _revoke(self, expected_revision: int) -> ProviderAccountState:
        self._expected_account(expected_revision)
        self.connection.execute("UPDATE provider_accounts SET active=0 WHERE active=1")
        self.connection.execute(
            "UPDATE provider_account_state SET revision=revision+1,subject=NULL,client_id=NULL,"
            "account_revision=NULL WHERE singleton=1 AND revision=?",
            (expected_revision,),
        )
        return self.account_state()

    def revoke(self, *, expected_revision: int) -> ProviderAccountState:
        with self._transaction():
            return self._revoke(expected_revision)

    def mark_verified(
        self, settings: ModelSettings, *, expected_revision: int, run_id: str
    ) -> ProviderAccountState:
        with self._transaction():
            state = self._expected_account(expected_revision)
            if state.account is None:
                raise ProviderStateConflict("Cannot verify a signed-out account")
            run = self.get_run(run_id)
            if (
                run is None
                or run.state != "completed"
                or run.turn_id is None
                or (
                    run.actual_settings != settings
                    or run.preparation.requested_settings != settings
                    or run.preparation.account_revision != expected_revision
                    or run.preparation.subject != state.account.subject
                    or run.preparation.client_id != state.account.client_id
                )
            ):
                raise ProviderStateConflict("Inference proof requires exact completed bound run")
            # Create a new immutable registration revision, preserving the prior run binding.
            verified = ProviderAccount.model_validate_json(
                state.account.model_copy(
                    update={
                        "account_revision": expected_revision + 1,
                        "inference_verified": True,
                        "verified_settings": settings,
                    }
                ).model_dump_json()
            )
            return self._activate(verified, expected_revision, verified_run=True)

    def get_flow(self, flow_id: str) -> StoredProviderFlow | None:
        row = self.connection.execute(
            "SELECT * FROM provider_auth_flows WHERE flow_id=?", (flow_id,)
        ).fetchone()
        if row is None:
            return None
        return StoredProviderFlow.model_validate_json(
            json.dumps(
                {
                    "flow_id": row["flow_id"],
                    "requested_action": row["requested_action"],
                    "state": row["state"],
                    "registration": json.loads(row["registration_refs"]),
                    "host": json.loads(row["host_refs"]),
                    "state_digest": row["state_digest"],
                    "nonce_digest": row["nonce_digest"],
                    "expires_at": row["expires_at"],
                    "terminal_at": row["terminal_at"],
                    "subject_ref": row["subject_ref"],
                    "error_code": row["error_code"],
                    "revision": row["revision"],
                }
            )
        )

    def get_flow_by_state_digest(self, state_digest: str) -> StoredProviderFlow | None:
        row = self.connection.execute(
            "SELECT flow_id FROM provider_auth_flows WHERE state_digest=?", (state_digest,)
        ).fetchone()
        return self.get_flow(row["flow_id"]) if row else None

    def action_replay(self, action: ProviderAction) -> ProviderActionResult | None:
        row = self.connection.execute(
            "SELECT request_digest,replay_response FROM commands WHERE local_principal=? "
            "AND kind=? AND idempotency_key=?",
            (action.local_principal, action.command_kind, action.idempotency_key),
        ).fetchone()
        if row is None:
            return None
        if row["request_digest"] != action.request_digest:
            raise ProviderStateConflict("Provider action idempotency key body mismatch")
        return ProviderActionResult.model_validate_json(row["replay_response"])

    def _record_action(
        self, action: ProviderAction, revision: int, flow_id: str | None
    ) -> ProviderActionResult:
        receipt = ReceiptV1(
            receipt_id=action.receipt_id,
            command_id=action.command_id,
            kind="provider_action",
            command_kind=action.command_kind,
            aggregate_id=action.aggregate_id,
            canonical_commit_state="not_applicable",
            processing_state="completed",
            received_at=action.received_at,
            aggregate_revision=revision,
            canonical_event_ids=(),
            status_url=f"/api/v1/receipts/{action.receipt_id}",
        )
        result = ProviderActionResult(receipt=receipt, account_revision=revision, flow_id=flow_id)
        self.connection.execute(
            "INSERT INTO commands(command_id,local_principal,kind,idempotency_key,request_digest,"
            "aggregate_id,status,response_status,replay_response,created_at) "
            "VALUES(?,?,?,?,?,?,'completed',202,?,?)",
            (
                action.command_id,
                action.local_principal,
                action.command_kind,
                action.idempotency_key,
                action.request_digest,
                action.aggregate_id,
                result.model_dump_json(),
                action.received_at,
            ),
        )
        self.connection.execute(
            "INSERT INTO receipts(receipt_id,command_id,kind,aggregate_id,payload,payload_digest,"
            "received_at) VALUES(?,?,'provider_action',?,?,?,?)",
            (
                action.receipt_id,
                action.command_id,
                action.aggregate_id,
                receipt.model_dump_json(),
                contract_digest(receipt),
                action.received_at,
            ),
        )
        return result

    def create_flow(self, action: ProviderAction, flow: StoredProviderFlow) -> ProviderActionResult:
        with self._transaction():
            replay = self.action_replay(action)
            if replay is not None:
                return replay  # Before checking stale account revision or newly generated IDs.
            state = self._expected_account(action.expected_account_revision)
            if (
                action.kind == "sign_out"
                or action.kind != flow.requested_action
                or action.aggregate_id != flow.flow_id
                or flow.state != "pending"
                or flow.revision != 1
                or datetime.fromisoformat(flow.expires_at)
                <= datetime.fromisoformat(action.received_at)
                or flow.registration.expected_account_revision != state.revision
                or (action.kind == "grant" and state.account is None)
                or (
                    state.account is not None
                    and flow.registration.client_id != state.account.client_id
                )
                or flow.registration.expected_subject
                != (state.account.subject if state.account is not None else None)
            ):
                raise ProviderStateConflict("Provider flow does not bind original action/account")
            self.connection.execute(
                "INSERT INTO provider_auth_flows(flow_id,requested_action,state,registration_refs,"
                "host_refs,state_digest,nonce_digest,expires_at,terminal_at,subject_ref,revision,"
                "error_code) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (
                    flow.flow_id,
                    flow.requested_action,
                    flow.state,
                    flow.registration.model_dump_json(),
                    flow.host.model_dump_json(),
                    flow.state_digest,
                    flow.nonce_digest,
                    flow.expires_at,
                    flow.terminal_at,
                    flow.subject_ref,
                    flow.revision,
                    flow.error_code,
                ),
            )
            return self._record_action(action, state.revision, flow.flow_id)

    def revoke_action(self, action: ProviderAction) -> ProviderActionResult:
        with self._transaction():
            replay = self.action_replay(action)
            if replay is not None:
                return replay
            if action.kind != "sign_out":
                raise ProviderStateConflict("Sign-out action required")
            state = self._revoke(action.expected_account_revision)
            return self._record_action(action, state.revision, None)

    def _transition_flow(
        self, flow_id: str, transition: ProviderFlowTransition
    ) -> StoredProviderFlow:
        flow = self.get_flow(flow_id)
        if flow is None or flow.revision != transition.expected_revision:
            raise ProviderStateConflict("Provider flow revision changed")
        updated = StoredProviderFlow.model_validate_json(
            flow.model_copy(
                update={
                    "state": transition.state,
                    "terminal_at": transition.terminal_at,
                    "subject_ref": transition.subject_ref,
                    "error_code": transition.error_code,
                    "revision": flow.revision + 1,
                }
            ).model_dump_json()
        )
        self.connection.execute(
            "UPDATE provider_auth_flows SET state=?,terminal_at=?,subject_ref=?,error_code=?,"
            "revision=? WHERE flow_id=? AND revision=?",
            (
                updated.state,
                updated.terminal_at,
                updated.subject_ref,
                updated.error_code,
                updated.revision,
                flow_id,
                flow.revision,
            ),
        )
        return updated

    def transition_flow(
        self, flow_id: str, transition: ProviderFlowTransition
    ) -> StoredProviderFlow:
        if transition.state == "completed":
            raise ProviderStateConflict("Completion must atomically activate the verified account")
        with self._transaction():
            return self._transition_flow(flow_id, transition)

    def complete_flow(
        self,
        flow_id: str,
        account: ProviderAccount,
        *,
        expected_flow_revision: int,
        terminal_at: str,
    ) -> ProviderAccountState:
        with self._transaction():
            flow = self.get_flow(flow_id)
            if (
                flow is None
                or flow.revision != expected_flow_revision
                or flow.state != "validating"
            ):
                raise ProviderStateConflict("Provider flow is not at the expected validating step")
            initial_dynamic = (
                flow.requested_action == "sign_in"
                and flow.registration.client_id == "dynamic_agent_client"
                and flow.registration.expected_subject is None
            )
            if (not initial_dynamic and account.client_id != flow.registration.client_id) or (
                flow.registration.expected_subject is not None
                and flow.registration.expected_subject != account.subject
            ):
                raise ProviderStateConflict("Returning registration subject/client mismatch")
            if datetime.fromisoformat(terminal_at) >= datetime.fromisoformat(flow.expires_at):
                raise ProviderStateConflict("Expired flow cannot activate an account")
            state = self._activate(account, flow.registration.expected_account_revision)
            self._transition_flow(
                flow_id,
                ProviderFlowTransition(
                    expected_revision=flow.revision,
                    state="completed",
                    terminal_at=terminal_at,
                    subject_ref=account.subject,
                ),
            )
            return state

    def get_run(self, run_id: str) -> StoredProviderRun | None:
        row = self.connection.execute(
            "SELECT * FROM provider_runs WHERE run_id=?", (run_id,)
        ).fetchone()
        if row is None:
            return None
        return StoredProviderRun.model_validate_json(
            json.dumps(
                {
                    "preparation": {
                        "logical_task_id": row["logical_task_id"],
                        "request_digest": row["request_digest"],
                        "run_id": row["run_id"],
                        "subject": row["subject"],
                        "client_id": row["client_id"],
                        "account_revision": row["account_revision"],
                        "requested_settings": json.loads(row["requested_settings"]),
                        "required_scopes": json.loads(row["required_scopes"]),
                        "created_at": row["created_at"],
                    },
                    "state": row["state"],
                    "thread_id": row["thread_id"],
                    "turn_id": row["turn_id"],
                    "actual_settings": json.loads(row["actual_settings"])
                    if row["actual_settings"]
                    else None,
                    "terminal_output": row["terminal_output"],
                    "error_code": row["error_code"],
                    "revision": row["revision"],
                }
            )
        )

    def get_run_by_task(self, logical_task_id: str) -> StoredProviderRun | None:
        row = self.connection.execute(
            "SELECT run_id FROM provider_runs WHERE logical_task_id=?", (logical_task_id,)
        ).fetchone()
        return self.get_run(row["run_id"]) if row else None

    def _run_account(self, preparation: ProviderRunPreparation) -> None:
        state = self._expected_account(preparation.account_revision)
        if state.account is None or (
            state.account.subject != preparation.subject
            or state.account.client_id != preparation.client_id
            or not set(preparation.required_scopes) <= set(state.account.scopes)
        ):
            raise ProviderStateConflict("Run account/grant no longer matches active registration")

    def prepare_run(self, preparation: ProviderRunPreparation) -> StoredProviderRun:
        with self._transaction():
            existing = self.get_run_by_task(preparation.logical_task_id)
            if existing is not None:
                # Newly allocated run IDs/timestamps are not new task semantics on a retry.
                original = existing.preparation.model_dump(exclude={"run_id", "created_at"})
                requested = preparation.model_dump(exclude={"run_id", "created_at"})
                if original != requested:
                    raise ProviderStateConflict("Logical provider task body/account mismatch")
                return existing
            self._run_account(preparation)
            self.connection.execute(
                "INSERT INTO provider_runs(run_id,logical_task_id,request_digest,subject,client_id,"
                "account_revision,requested_settings,required_scopes,state,revision,created_at) "
                "VALUES(?,?,?,?,?,?,?,?,'prepared',1,?)",
                (
                    preparation.run_id,
                    preparation.logical_task_id,
                    preparation.request_digest,
                    preparation.subject,
                    preparation.client_id,
                    preparation.account_revision,
                    preparation.requested_settings.model_dump_json(),
                    json.dumps(preparation.required_scopes),
                    preparation.created_at,
                ),
            )
            return StoredProviderRun(preparation=preparation, state="prepared", revision=1)

    def _update_run(self, run_id: str, transition: ProviderRunTransition) -> StoredProviderRun:
        run = self.get_run(run_id)
        if run is None or run.revision != transition.expected_revision:
            raise ProviderStateConflict("Provider run revision changed")
        allowed = {
            "prepared": {"submitted", "failed", "interrupted"},
            "submitted": {"running", "completed", "failed", "interrupted", "unknown"},
            "running": {"running", "completed", "failed", "interrupted", "unknown"},
            "unknown": {"completed", "failed", "interrupted"},
        }
        if transition.state not in allowed.get(run.state, set()):
            raise ProviderStateConflict("Illegal provider run transition")
        if run.state == "unknown" and run.turn_id is None:
            raise ProviderStateConflict("Unbound uncertain turn cannot be resolved or redispatched")
        if (
            run.actual_settings is not None
            and transition.actual_settings is not None
            and (run.actual_settings != transition.actual_settings)
        ):
            raise ProviderStateConflict("Observed provider settings cannot be substituted")
        updated = StoredProviderRun.model_validate_json(
            run.model_copy(
                update={
                    "state": transition.state,
                    "thread_id": transition.thread_id
                    if transition.thread_id is not None
                    else run.thread_id,
                    "turn_id": transition.turn_id
                    if transition.turn_id is not None
                    else run.turn_id,
                    "actual_settings": transition.actual_settings
                    if transition.actual_settings is not None
                    else run.actual_settings,
                    "terminal_output": transition.terminal_output,
                    "error_code": transition.error_code,
                    "revision": run.revision + 1,
                }
            ).model_dump_json()
        )
        self.connection.execute(
            "UPDATE provider_runs SET state=?,thread_id=?,turn_id=?,actual_settings=?,"
            "terminal_output=?,error_code=?,revision=? WHERE run_id=? AND revision=?",
            (
                updated.state,
                updated.thread_id,
                updated.turn_id,
                updated.actual_settings.model_dump_json() if updated.actual_settings else None,
                updated.terminal_output,
                updated.error_code,
                updated.revision,
                run_id,
                run.revision,
            ),
        )
        return updated

    def claim_run(self, run_id: str, *, expected_revision: int) -> StoredProviderRun:
        with self._transaction():
            run = self.get_run(run_id)
            if run is None or run.state != "prepared":
                raise ProviderStateConflict(
                    "Run already dispatched or uncertain; cannot redispatch"
                )
            self._run_account(run.preparation)
            return self._update_run(
                run_id,
                ProviderRunTransition(
                    expected_revision=expected_revision,
                    state="submitted",
                ),
            )

    def update_run(self, run_id: str, transition: ProviderRunTransition) -> StoredProviderRun:
        if transition.state in {"prepared", "submitted"}:
            raise ProviderStateConflict(
                "Only claim_run can make the durable pre-dispatch transition"
            )
        with self._transaction():
            return self._update_run(run_id, transition)
