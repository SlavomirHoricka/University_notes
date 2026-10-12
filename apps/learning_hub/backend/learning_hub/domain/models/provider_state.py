"""Private provider metadata. Tokens, PKCE material and prompts are never stored here."""

from typing import Annotated, Literal, Self
from urllib.parse import urlsplit

from pydantic import AfterValidator, Field, StringConstraints, model_validator

from learning_hub.domain.models.api import ReceiptV1
from learning_hub.domain.models.base import (
    UUID4_PATTERN,
    CommandId,
    Contract,
    Digest,
    NonEmpty,
    OperationalId,
    PositiveInt,
    ReceiptId,
    UTCTime,
)
from learning_hub.domain.models.services import AuthFlowState, ModelSettings

IdempotencyKey = Annotated[str, StringConstraints(pattern="^" + UUID4_PATTERN + "$")]


def loopback_http_url(value: str) -> str:
    url = urlsplit(value)
    if (
        url.scheme != "http"
        or url.hostname not in ("localhost", "127.0.0.1", "::1")
        or url.username
        or url.password
        or url.fragment
        or url.query
    ):
        raise ValueError("Explicit loopback HTTP URL required")
    _ = url.port  # Validate malformed ports.
    return value


LoopbackURL = Annotated[NonEmpty, AfterValidator(loopback_http_url)]


class ProviderAccount(Contract):
    subject: NonEmpty
    client_id: NonEmpty
    scopes: Annotated[tuple[NonEmpty, ...], Field(max_length=100)]
    active: bool
    account_revision: PositiveInt
    inference_verified: bool
    verified_settings: ModelSettings | None

    @model_validator(mode="after")
    def proof_and_scopes(self) -> Self:
        if len(set(self.scopes)) != len(self.scopes):
            raise ValueError("Duplicate account scopes")
        if self.inference_verified != (self.verified_settings is not None):
            raise ValueError("Inference verification requires exact observed settings")
        return self


class ProviderAccountState(Contract):
    revision: PositiveInt
    account: ProviderAccount | None

    @model_validator(mode="after")
    def active_registration(self) -> Self:
        if self.account is not None and (
            not self.account.active or self.account.account_revision != self.revision
        ):
            raise ValueError("Active registration must match singleton revision")
        return self


class ProviderFlowRegistration(Contract):
    client_id: NonEmpty
    redirect_uri: LoopbackURL
    expected_account_revision: PositiveInt
    expected_subject: NonEmpty | None = None


class ProviderFlowHost(Contract):
    instance_id: NonEmpty
    callback_origin: LoopbackURL


class StoredProviderFlow(Contract):
    flow_id: OperationalId
    requested_action: Literal["sign_in", "grant"]
    state: AuthFlowState
    registration: ProviderFlowRegistration
    host: ProviderFlowHost
    state_digest: Digest
    nonce_digest: Digest
    expires_at: UTCTime
    terminal_at: UTCTime | None = None
    subject_ref: NonEmpty | None = None
    error_code: NonEmpty | None = None
    revision: PositiveInt = 1

    @model_validator(mode="after")
    def terminal(self) -> Self:
        terminal = self.state in {"completed", "failed", "expired", "cancelled"}
        if terminal != (self.terminal_at is not None):
            raise ValueError("Terminal flow requires terminal instant")
        if self.state == "completed" and self.subject_ref is None:
            raise ValueError("Completed flow requires verified subject")
        return self


class ProviderFlowTransition(Contract):
    expected_revision: PositiveInt
    state: AuthFlowState
    terminal_at: UTCTime | None = None
    subject_ref: NonEmpty | None = None
    error_code: NonEmpty | None = None


class ProviderAction(Contract):
    command_id: CommandId
    receipt_id: ReceiptId
    local_principal: NonEmpty
    kind: Literal["sign_in", "grant", "sign_out"]
    idempotency_key: IdempotencyKey
    request_digest: Digest
    aggregate_id: OperationalId
    expected_account_revision: PositiveInt
    received_at: UTCTime

    @property
    def command_kind(self) -> str:
        return "provider_" + self.kind


class ProviderActionResult(Contract):
    receipt: ReceiptV1
    account_revision: PositiveInt
    flow_id: OperationalId | None


ProviderRunState = Literal[
    "prepared", "submitted", "running", "completed", "failed", "interrupted", "unknown"
]
TerminalOutput = Annotated[str, StringConstraints(max_length=200_000)]


class ProviderRunPreparation(Contract):
    logical_task_id: NonEmpty
    request_digest: Digest
    run_id: OperationalId
    subject: NonEmpty
    client_id: NonEmpty
    account_revision: PositiveInt
    requested_settings: ModelSettings
    required_scopes: Annotated[tuple[NonEmpty, ...], Field(min_length=1, max_length=100)]
    created_at: UTCTime


class StoredProviderRun(Contract):
    preparation: ProviderRunPreparation
    state: ProviderRunState
    thread_id: NonEmpty | None = None
    turn_id: NonEmpty | None = None
    actual_settings: ModelSettings | None = None
    terminal_output: TerminalOutput | None = None
    error_code: NonEmpty | None = None
    revision: PositiveInt

    @model_validator(mode="after")
    def lifecycle(self) -> Self:
        if self.turn_id is not None and self.thread_id is None:
            raise ValueError("Turn requires thread identity")
        if self.state == "prepared" and any(
            value is not None
            for value in (
                self.thread_id,
                self.turn_id,
                self.actual_settings,
                self.terminal_output,
                self.error_code,
            )
        ):
            raise ValueError("Prepared run has no dispatch/result facts")
        if self.terminal_output is not None and self.state not in {
            "completed",
            "failed",
            "interrupted",
        }:
            raise ValueError("Only confirmed terminal runs contain terminal output")
        if self.state == "running" and self.turn_id is None:
            raise ValueError("Running requires actual turn identity")
        return self


class ProviderRunTransition(Contract):
    expected_revision: PositiveInt
    state: ProviderRunState
    thread_id: NonEmpty | None = None
    turn_id: NonEmpty | None = None
    actual_settings: ModelSettings | None = None
    terminal_output: TerminalOutput | None = None
    error_code: NonEmpty | None = None
