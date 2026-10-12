from pathlib import Path
from typing import Protocol

from learning_hub.domain.models.base import Contract, GitCommit, NonEmpty, PositiveInt
from learning_hub.domain.models.identity import CourseId


class CourseLease(Contract):
    course_id: CourseId
    holder_id: NonEmpty
    fence: PositiveInt
    selected_checkout: NonEmpty


class CourseReservation(Protocol):
    def acquire(self, course_id: str, checkout: Path) -> CourseLease: ...
    def assert_current(self, lease: CourseLease) -> None: ...
    def release(self, lease: CourseLease) -> None: ...


class IntegrationReceipt(Contract):
    commit: GitCommit
    merged_commit: GitCommit | None
    pull_request_url: NonEmpty | None
    verified: bool


class RepositoryIntegrator(Protocol):
    def inspect(self, checkout: Path, expected_commit: str) -> IntegrationReceipt: ...
