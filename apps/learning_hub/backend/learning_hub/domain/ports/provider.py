from collections.abc import AsyncIterator
from typing import Literal, Protocol

from learning_hub.domain.models.base import Contract, NonEmpty
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


class LocalAuthorization(Protocol):
    """Injected trusted seam; H01 tests can supply it without waiting for H03's local auth."""

    def authenticate(self, cookie: str | None) -> LocalPrincipal: ...
    def validate_mutation(
        self, principal: LocalPrincipal, origin: str | None, csrf_token: str | None
    ) -> None: ...


class ProviderClient(Protocol):
    async def status(self) -> ProviderStatusV1: ...
    async def models(self) -> tuple[ProviderModelChoice, ...]: ...
    def run(self, request: ProviderRunRequest) -> AsyncIterator[ProviderRunEvent]: ...
    async def cancel(self, run_id: str) -> None: ...
