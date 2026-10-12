from collections.abc import AsyncIterator
from typing import Literal, Protocol

from learning_hub.domain.models.base import Contract, NonEmpty
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
from learning_hub.domain.models.services import (
    CredentialMaterial,
    LocalPrincipal,
    ModelSettings,
    ProviderModelChoice,
    ProviderStatusV1,
)


class ProviderRunRequest(Contract):
    logical_task_id: NonEmpty
    thread_id: NonEmpty | None
    settings: ModelSettings
    prompt: str
    selected_checkout: NonEmpty


class ProviderRunEvent(Contract):
    run_id: NonEmpty
    thread_id: NonEmpty
    turn_id: NonEmpty
    state: Literal["running", "completed", "failed", "interrupted", "unknown"]
    actual_settings: ModelSettings | None
    output: str | None
    error_code: NonEmpty | None


class CredentialStore(Protocol):
    def get(self, subject: str, client_id: str) -> CredentialMaterial | None: ...
    def put(self, credentials: CredentialMaterial) -> None: ...
    def delete(self, subject: str, client_id: str) -> None: ...


LOCAL_SESSION_COOKIE_NAME = "hub_session"
LocalAuthorizationCode = Literal[
    "LOCAL_SESSION_REQUIRED", "LOCAL_SESSION_EXPIRED", "ORIGIN_FORBIDDEN", "CSRF_INVALID"
]


class LocalAuthorizationError(ValueError):
    """Local boundary failures have a typed code and constant redacted message."""

    def __init__(self, code: LocalAuthorizationCode) -> None:
        messages: dict[LocalAuthorizationCode, str] = {
            "LOCAL_SESSION_REQUIRED": "A local browser session is required.",
            "LOCAL_SESSION_EXPIRED": "The local browser session has expired.",
            "ORIGIN_FORBIDDEN": "The request origin is not authorized.",
            "CSRF_INVALID": "The local request verification failed.",
        }
        if code not in messages:
            raise ValueError("Unsupported local authorization error code")
        self.code = code
        super().__init__(messages[code])


class LocalAuthorization(Protocol):
    """Injected seam raising LocalAuthorizationError; H03 supplies actual local auth."""

    def authenticate(self, cookie: str | None) -> LocalPrincipal: ...
    def validate_mutation(
        self, principal: LocalPrincipal, origin: str | None, csrf_token: str | None
    ) -> None: ...


class ProviderClient(Protocol):
    async def status(self) -> ProviderStatusV1: ...
    async def models(self) -> tuple[ProviderModelChoice, ...]: ...
    def run(self, request: ProviderRunRequest) -> AsyncIterator[ProviderRunEvent]: ...
    async def cancel(self, run_id: str) -> None: ...


class ProviderStateConflict(ValueError):
    """CAS, immutable identity or idempotency conflict; no new external action is safe."""


class ProviderStateRepository(Protocol):
    def account_state(self) -> ProviderAccountState: ...
    def activate(
        self, account: ProviderAccount, *, expected_revision: int
    ) -> ProviderAccountState: ...
    def revoke(self, *, expected_revision: int) -> ProviderAccountState: ...
    def mark_verified(
        self, settings: ModelSettings, *, expected_revision: int, run_id: str
    ) -> ProviderAccountState: ...
    def complete_flow(
        self,
        flow_id: str,
        account: ProviderAccount,
        *,
        expected_flow_revision: int,
        terminal_at: str,
    ) -> ProviderAccountState: ...
    def get_flow(self, flow_id: str) -> StoredProviderFlow | None: ...
    def get_flow_by_state_digest(self, state_digest: str) -> StoredProviderFlow | None: ...
    def create_flow(
        self, action: ProviderAction, flow: StoredProviderFlow
    ) -> ProviderActionResult: ...
    def transition_flow(
        self, flow_id: str, transition: ProviderFlowTransition
    ) -> StoredProviderFlow: ...
    def action_replay(self, action: ProviderAction) -> ProviderActionResult | None: ...
    def revoke_action(self, action: ProviderAction) -> ProviderActionResult: ...
    def prepare_run(self, preparation: ProviderRunPreparation) -> StoredProviderRun: ...
    def claim_run(self, run_id: str, *, expected_revision: int) -> StoredProviderRun: ...
    def update_run(self, run_id: str, transition: ProviderRunTransition) -> StoredProviderRun: ...
    def get_run(self, run_id: str) -> StoredProviderRun | None: ...
    def get_run_by_task(self, logical_task_id: str) -> StoredProviderRun | None: ...
