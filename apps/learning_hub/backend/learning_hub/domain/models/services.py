from typing import Annotated, Literal, Self

from pydantic import AfterValidator, Field, SecretStr, model_validator

from learning_hub.domain.models.api import JobState, RoleEffort
from learning_hub.domain.models.base import (
    CommandId,
    Contract,
    Digest,
    JobId,
    NonEmpty,
    OperationalId,
    PositiveInt,
    RelativePath,
    UTCTime,
    contract_digest,
)
from learning_hub.domain.models.identity import AuthoringRef, CourseId, CourseKey, DefinitionRef


class ModelSettings(Contract):
    model: NonEmpty
    effort: RoleEffort
    speed: Literal["standard"] = "standard"


class RoleSettingsV1(Contract):
    role_key: NonEmpty
    requested: ModelSettings
    actual: ModelSettings | None
    revision: PositiveInt


class RoleSettingCommand(Contract):
    model: NonEmpty
    effort: RoleEffort
    expected_revision: PositiveInt


class ProviderAuthStartV1(Contract):
    action: Literal["sign_in", "grant"]
    expected_account_revision: PositiveInt | None = None


AuthFlowState = Literal[
    "pending", "awaiting_callback", "validating", "completed", "failed", "expired", "cancelled"
]


def authorization_url(value: str) -> str:
    from urllib.parse import urlsplit

    parsed = urlsplit(value)
    if (
        parsed.scheme != "https"
        or parsed.hostname not in ("auth.openai.com", "chatgpt.com")
        or parsed.username
        or parsed.password
        or parsed.fragment
    ):
        raise ValueError("Unsupported authorization URL")
    return value


class ProviderAuthFlowViewV1(Contract):
    flow_id: OperationalId
    status: AuthFlowState
    expires_at: UTCTime
    authorization_url: Annotated[str, AfterValidator(authorization_url)] | None = None
    error_code: NonEmpty | None = None


class ProviderSignOutV1(Contract):
    expected_account_revision: PositiveInt


class ReportedUsage(Contract):
    scope: NonEmpty
    used_percent: Annotated[int, Field(ge=0, le=100)] | None
    reset_at: UTCTime | None
    measured_at: UTCTime


class ProviderStatusV1(Contract):
    signed_in: bool
    eligibility: Literal["verified", "unverified", "denied", "missing_grant", "unknown"]
    inference_verified: bool
    account_revision: PositiveInt
    usage: ReportedUsage | None

    @model_validator(mode="after")
    def actual_proof(self) -> Self:
        if self.inference_verified and (not self.signed_in or self.eligibility != "verified"):
            raise ValueError("Inference proof requires verified account grant")
        return self


class ProviderModelChoice(Contract):
    model: NonEmpty
    supported_efforts: tuple[RoleEffort, ...]
    access: Literal["verified", "unverified", "denied", "unknown"]


class CapabilitiesV1(Contract):
    provider: ProviderStatusV1
    roles: tuple[RoleSettingsV1, ...]
    offline_features: tuple[Literal["published_rendering", "deterministic_practice"], ...]
    canonical_bridge: Literal["unavailable", "verified"]


class CredentialMaterial(Contract):
    """Private adapter-only material; deliberately absent from exported OpenAPI registry."""

    subject: NonEmpty
    client_id: NonEmpty
    access_token: SecretStr
    refresh_token: SecretStr | None
    id_token: SecretStr | None
    expires_at: UTCTime


class LocalPrincipal(Contract):
    principal: NonEmpty
    expires_at: UTCTime


class SourceRevisionV1(Contract):
    source_id: OperationalId
    source_revision_id: OperationalId
    revision: PositiveInt
    course_key: CourseKey
    sha256: Digest
    byte_size: Annotated[int, Field(ge=0)]
    media_type: NonEmpty
    managed_relpath: RelativePath
    week_ref: AuthoringRef
    extraction_state: Literal["pending", "complete", "partial", "blocked"]


class SourceSnapshotV1(Contract):
    snapshot_id: OperationalId
    course_key: CourseKey
    generation: PositiveInt
    snapshot_digest: Digest
    entries: tuple[SourceRevisionV1, ...]
    created_at: UTCTime

    @model_validator(mode="after")
    def one_course(self) -> Self:
        if any(entry.course_key != self.course_key for entry in self.entries) or len(
            {entry.source_id for entry in self.entries}
        ) != len(self.entries):
            raise ValueError("Snapshot course/selection conflict")
        return self


class UploadV1(Contract):
    week_id: NonEmpty
    replace_source_id: OperationalId | None
    expected_source_revision: PositiveInt | None

    @model_validator(mode="after")
    def replacement_tuple(self) -> Self:
        if (self.replace_source_id is None) != (self.expected_source_revision is None):
            raise ValueError("Replacement requires source ID and exact previous revision")
        return self


class JobInputV1(Contract):
    course_id: CourseId | None
    source_snapshot_id: OperationalId | None
    source_snapshot_digest: Digest | None
    scope: tuple[RelativePath, ...]
    requested_revision: PositiveInt

    @model_validator(mode="after")
    def snapshot_tuple(self) -> Self:
        if (self.source_snapshot_id is None) != (self.source_snapshot_digest is None):
            raise ValueError("Snapshot identity requires its exact digest")
        return self


class RequestedJobV1(Contract):
    job_id: JobId
    course_key: CourseKey | None
    kind: Literal[
        "ingest_prepare",
        "plan_prepare",
        "grade_written",
        "extend_bank",
        "publish",
        "source_inventory",
    ]
    dedupe_key: Digest
    input_ref: JobInputV1
    requested_settings: ModelSettings
    created_at: UTCTime

    @model_validator(mode="after")
    def course_tuple(self) -> Self:
        if (self.course_key is None) != (self.input_ref.course_id is None):
            raise ValueError("Job course key requires exact course identity")
        return self


class JobViewV1(Contract):
    request: RequestedJobV1
    state: JobState
    revision: PositiveInt
    actual_settings: ModelSettings | None
    next_eligible_at: UTCTime | None
    error_code: NonEmpty | None


class JobActionV1(Contract):
    expected_revision: PositiveInt


class ApprovalScope(Contract):
    course_id: CourseId
    paths: tuple[RelativePath, ...] = Field(min_length=1)
    action: Literal["preserved_replacement", "source_selection"]


class PreservedVersion(Contract):
    source_path: RelativePath
    preserved_ref: NonEmpty
    sha256: Digest


class SafeApprovalPreview(Contract):
    summary: NonEmpty
    diff_digest: Digest
    exposed_regions: tuple[NonEmpty, ...]


class ApprovalProposalBodyV1(Contract):
    job_id: JobId
    course_key: CourseKey
    kind: Literal["source_selection", "substantive_replacement"]
    source_snapshot_id: OperationalId
    expected_hashes: dict[RelativePath, Digest | None]
    scope: ApprovalScope
    preserved_version_refs: tuple[PreservedVersion, ...]
    safe_preview: SafeApprovalPreview

    @model_validator(mode="after")
    def exact_scope(self) -> Self:
        if set(self.scope.paths) != self.expected_hashes.keys():
            raise ValueError("Expected bytes must cover exact proposal scope")
        if self.kind == "substantive_replacement" and (
            self.scope.action != "preserved_replacement" or not self.preserved_version_refs
        ):
            raise ValueError("Replacement proposal must preserve prior versions")
        if self.kind == "source_selection" and self.scope.action != "source_selection":
            raise ValueError("Source selection has mismatched requested action")
        preserved = {version.source_path: version.sha256 for version in self.preserved_version_refs}
        if (
            len(preserved) != len(self.preserved_version_refs)
            or not preserved.keys() <= self.expected_hashes.keys()
        ):
            raise ValueError("Preserved versions must be unique and within exact scope")
        if self.kind == "substantive_replacement" and any(
            digest is not None and preserved.get(path) != digest
            for path, digest in self.expected_hashes.items()
        ):
            raise ValueError("Every replaced prior byte hash must have a preserved version")
        return self


class ApprovalProposalV1(Contract):
    proposal_id: OperationalId
    proposal_digest: Digest
    body: ApprovalProposalBodyV1
    created_at: UTCTime
    status: Literal["awaiting_decision", "approved", "rejected", "superseded"]

    @model_validator(mode="after")
    def bound_body(self) -> Self:
        if self.proposal_digest != contract_digest(self.body):
            raise ValueError("Proposal digest does not bind exact body")
        return self


class ApprovalDecisionV1(Contract):
    decision: Literal["approve", "reject"]
    proposal_digest: Digest
    expected_job_revision: PositiveInt


class StoredApprovalDecision(ApprovalDecisionV1):
    decision_id: OperationalId
    proposal_id: OperationalId
    command_id: CommandId
    principal: NonEmpty
    decided_at: UTCTime


class ReviewRecommendationV1(Contract):
    course_id: CourseId
    trigger_event_ids: tuple[NonEmpty, ...]
    definitions: tuple[DefinitionRef, ...]
    reason: NonEmpty
    route: Literal["corrective_refresh", "retention_check", "reassessment"]
    prepared_activity_refs: tuple[AuthoringRef, ...]
    estimated_minutes: PositiveInt
    recall_review_id: NonEmpty | None
    due_date: Annotated[str, Field(pattern=r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")] | None
    readiness: Literal["ready", "blocked", "unknown"]
    blockers: tuple[NonEmpty, ...]

    @model_validator(mode="after")
    def one_course(self) -> Self:
        if any(definition.course_id != self.course_id for definition in self.definitions):
            raise ValueError("Review cannot mix courses")
        return self
