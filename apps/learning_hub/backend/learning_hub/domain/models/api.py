from typing import Annotated, Literal, Self

from pydantic import Field, model_validator

from learning_hub.domain.models.base import (
    AttemptId,
    BundleId,
    CommandId,
    Contract,
    DeliveryId,
    Digest,
    NonEmpty,
    NonNegativeInt,
    OperationalId,
    PositiveInt,
    ReceiptId,
    ReportedTime,
    SessionId,
    UTCTime,
)
from learning_hub.domain.models.bundles import PublicSectionV1
from learning_hub.domain.models.identity import (
    AuthoringRef,
    BundleRef,
    CourseIdentity,
    CourseKey,
    ItemRef,
)
from learning_hub.domain.models.questions import Conditions, PublicPromptV1, Response

ReceiptKind = Literal[
    "response",
    "delivery",
    "activity",
    "assessment_submission",
    "assessment_draft",
    "session",
    "job_action",
    "upload",
    "approval_decision",
    "provider_action",
]
CanonicalCommitState = Literal[
    "pending", "committing", "committed", "conflict", "blocked", "not_applicable"
]
SessionState = Literal["active", "paused", "closed", "validity_hold"]
AttemptState = Literal[
    "started",
    "response_received",
    "grading_pending",
    "assessed",
    "evidence_committed",
    "feedback_available",
    "abandoned",
    "unscorable",
    "validity_hold",
]
AssessmentState = Literal[
    "assembling",
    "active",
    "submitted",
    "grading_pending",
    "finalized",
    "unscorable",
    "validity_hold",
    "abandoned",
]
DeliveryState = Literal["prepared", "offered", "displayed", "display_unknown"]
JobState = Literal[
    "queued",
    "running",
    "waiting_usage",
    "waiting_sign_in",
    "waiting_dependency",
    "retry_scheduled",
    "blocked",
    "paused",
    "succeeded",
    "cancelled",
]
RoleEffort = Literal["low", "medium", "high", "xhigh", "max", "ultra"]
RouteKind = Literal[
    "lesson", "lesson_quiz", "weekly_test", "corrective_refresh", "retention_check", "reassessment"
]


class ReceiptV1(Contract):
    receipt_id: ReceiptId
    command_id: CommandId
    kind: ReceiptKind
    command_kind: NonEmpty
    aggregate_id: OperationalId
    durable_receipt: Literal[True] = True
    canonical_commit_state: CanonicalCommitState
    processing_state: Literal[
        "received", "pending", "grading_pending", "completed", "blocked", "bookmark_saved"
    ]
    received_at: UTCTime
    aggregate_revision: PositiveInt
    canonical_event_ids: tuple[NonEmpty, ...]
    status_url: str

    @model_validator(mode="after")
    def receipt_authority(self) -> Self:
        operational = (
            self.kind
            in {"assessment_draft", "approval_decision", "provider_action", "job_action", "upload"}
            or self.command_kind == "bookmark"
        )
        if operational != (self.canonical_commit_state == "not_applicable"):
            raise ValueError("Operational/canonical receipt state mismatch")
        if self.command_kind == "bookmark" and self.kind != "session":
            raise ValueError("Bookmark maps to session receipt")
        if self.canonical_commit_state != "committed" and self.canonical_event_ids:
            raise ValueError("Uncommitted/nonacademic receipt cannot cite committed evidence")
        if self.status_url != f"/api/v1/receipts/{self.receipt_id}":
            raise ValueError("Receipt status URL mismatch")
        return self


class StartSessionCommand(Contract):
    course_key: CourseKey
    bundle_id: BundleId
    route_kind: RouteKind
    route_ref: AuthoringRef
    expected_publication_generation: PositiveInt


class BookmarkCommandV1(Contract):
    section_ref: AuthoringRef
    anchor_id: NonEmpty | None = None
    expected_revision: PositiveInt


class SessionActionCommand(Contract):
    expected_revision: PositiveInt


class RequestDeliveryCommand(Contract):
    activity_ref: AuthoringRef
    expected_revision: PositiveInt


class AdvanceCommand(Contract):
    section_ref: AuthoringRef
    delivery_receipt_id: ReceiptId
    next_activity_ref: AuthoringRef
    expected_revision: PositiveInt


class DisplayAckCommand(Contract):
    digest: Digest
    reported_display_at: ReportedTime | None
    conditions: Conditions


class SubmitResponseV1(Contract):
    session_id: SessionId
    item_ref: ItemRef
    delivery_id: DeliveryId
    response: Response
    conditions: Conditions
    reported_answered_at: ReportedTime | None
    expected_revision: PositiveInt


class StartAssessmentV1(Contract):
    prepared_assessment_ref: AuthoringRef
    expected_revision: PositiveInt


class SaveDraftV1(Contract):
    response: Response | None
    explicit_blank: bool
    expected_revision: PositiveInt
    expected_draft_revision: NonNegativeInt
    conditions: Conditions | None

    @model_validator(mode="after")
    def exactly_one_answer(self) -> Self:
        if (self.response is None) != self.explicit_blank:
            raise ValueError("Draft requires response or explicit blank, not both")
        return self


class AssessmentDraftV1(Contract):
    assessment_id: OperationalId
    item_id: NonEmpty
    attempt_id: AttemptId
    draft_revision: PositiveInt
    response: Response | None
    explicit_blank: bool
    received_at: UTCTime
    reported_conditions: Conditions | None

    @model_validator(mode="after")
    def exactly_one_answer(self) -> Self:
        if (self.response is None) != self.explicit_blank:
            raise ValueError("Draft requires response or explicit blank")
        return self


class FinalizeDraftSnapshotV1(Contract):
    mode: Literal["draft_snapshot"]
    expected_revision: PositiveInt
    draft_revision_manifest: dict[NonEmpty, PositiveInt]
    blank_item_ids: tuple[NonEmpty, ...]
    conditions: Conditions

    @model_validator(mode="after")
    def unique_blanks(self) -> Self:
        if len(set(self.blank_item_ids)) != len(self.blank_item_ids):
            raise ValueError("Duplicate blank item declarations")
        return self


class FinalizeExistingResponsesV1(Contract):
    mode: Literal["existing_responses"]
    expected_revision: PositiveInt
    response_receipt_ids: tuple[ReceiptId, ...]
    blank_item_ids: tuple[NonEmpty, ...]
    conditions: Conditions

    @model_validator(mode="after")
    def unique_manifest(self) -> Self:
        if len(set(self.response_receipt_ids)) != len(self.response_receipt_ids) or len(
            set(self.blank_item_ids)
        ) != len(self.blank_item_ids):
            raise ValueError("Duplicate finalization refs")
        return self


FinalizeAssessmentV1 = Annotated[
    FinalizeDraftSnapshotV1 | FinalizeExistingResponsesV1, Field(discriminator="mode")
]


def validate_draft_freeze(
    command: FinalizeDraftSnapshotV1,
    *,
    selected: tuple[str, ...],
    revision: int,
    drafts: tuple[AssessmentDraftV1, ...],
) -> None:
    """Pure preflight contract; H11 performs this and the full freeze in one DB transaction."""
    if command.expected_revision != revision or len(set(selected)) != len(selected):
        raise ValueError("Assessment revision/selection conflict")
    current = {draft.item_id: draft for draft in drafts}
    if len(current) != len(drafts) or not current.keys() <= set(selected):
        raise ValueError("Draft is not selected")
    if command.draft_revision_manifest != {
        item: draft.draft_revision for item, draft in current.items()
    }:
        raise ValueError("Draft manifest conflict")
    blank = set(command.blank_item_ids)
    if not blank <= set(selected) or set(selected) != current.keys() | blank:
        raise ValueError("Incomplete finalization coverage")
    if any(draft.explicit_blank != (item in blank) for item, draft in current.items()):
        raise ValueError("Response/blank declaration conflict")


class LessonProgressV1(Contract):
    instruction_state: Literal["not_started", "in_progress", "finished"]
    assessment_submission_state: Literal["not_started", "in_progress", "submitted"]
    assessment_grading_state: Literal["absent", "pending", "finalized", "unscorable"]
    completed: bool
    passed: bool | None
    needs_attention: bool | None
    evidence_state: Literal["current", "stale", "reassessment_needed", "unknown"]
    canonical_commit_state: Literal["pending", "verified", "conflict", "unknown"]

    @model_validator(mode="after")
    def unknown_grades_not_outcomes(self) -> Self:
        if self.assessment_grading_state != "finalized" and (
            self.passed is not None or self.needs_attention is not None
        ):
            raise ValueError("Pending/absent grade cannot declare pass or attention")
        if self.completed and (
            self.instruction_state != "finished"
            or self.assessment_submission_state != "submitted"
            or self.canonical_commit_state != "verified"
        ):
            raise ValueError("Completion requires committed process/submission facts")
        return self


class CourseCatalogueV1(Contract):
    course_key: CourseKey
    identity: CourseIdentity
    display_name: NonEmpty
    readiness: Literal["ready", "partial", "stale", "blocked", "unavailable"]
    available_scope: tuple[NonEmpty, ...]
    blocked_scope: tuple[NonEmpty, ...]
    bundle_ref: BundleRef | None


class WeekSummaryV1(Contract):
    course_key: CourseKey
    week_ref: AuthoringRef
    lessons: tuple[AuthoringRef, ...]
    readiness: Literal["ready", "partial", "stale", "blocked", "unavailable"]
    progress: LessonProgressV1 | None


class SessionViewV1(Contract):
    session_id: SessionId
    course_key: CourseKey
    bundle_ref: BundleRef
    route_kind: RouteKind
    route_ref: AuthoringRef
    status: SessionState
    revision: PositiveInt
    bookmark: BookmarkCommandV1 | None
    progress: LessonProgressV1 | None
    pending_receipt_ids: tuple[ReceiptId, ...]


class ReleasedFeedbackV1(Contract):
    item_ref: ItemRef
    verified_result_id: OperationalId
    explanation: NonEmpty
    correction_route: NonEmpty | None


class DeliveryViewV1(Contract):
    delivery_id: DeliveryId
    state: DeliveryState
    payload: PublicPromptV1 | PublicSectionV1 | ReleasedFeedbackV1 | None

    @model_validator(mode="after")
    def release_state(self) -> Self:
        if self.state == "prepared" and self.payload is not None:
            raise ValueError("Unreleased payload")
        return self


class AttemptViewV1(Contract):
    attempt_id: AttemptId
    item_ref: ItemRef
    status: AttemptState
    revision: PositiveInt
    response_receipt_id: ReceiptId | None
    result_id: OperationalId | None
    feedback: ReleasedFeedbackV1 | None

    @model_validator(mode="after")
    def result_needs_response(self) -> Self:
        if self.result_id is not None and self.response_receipt_id is None:
            raise ValueError("Result without actual response")
        if self.feedback is not None and self.status != "feedback_available":
            raise ValueError("Feedback not released")
        return self


class AssessmentViewV1(Contract):
    assessment_id: OperationalId
    session_id: SessionId
    prepared_ref: AuthoringRef
    status: AssessmentState
    revision: PositiveInt
    submitted_at: UTCTime | None
    final_result_id: OperationalId | None


class SafeErrorContext(Contract):
    aggregate_id: OperationalId | None = None
    expected_revision: NonNegativeInt | None = None
    actual_revision: NonNegativeInt | None = None
    refresh_url: str | None = None


ErrorCode = Literal[
    "MALFORMED_JSON",
    "INVALID_CURSOR",
    "LOCAL_SESSION_REQUIRED",
    "LOCAL_SESSION_EXPIRED",
    "ORIGIN_FORBIDDEN",
    "CSRF_INVALID",
    "DELIVERY_NOT_RELEASED",
    "ASSET_FORBIDDEN",
    "COURSE_NOT_FOUND",
    "SESSION_NOT_FOUND",
    "ITEM_NOT_FOUND",
    "RECEIPT_NOT_FOUND",
    "IDEMPOTENCY_CONFLICT",
    "ATTEMPT_ALREADY_SUBMITTED",
    "INVALID_TRANSITION",
    "PINNED_VERSION_MISMATCH",
    "PUBLICATION_CONFLICT",
    "VARIANT_POOL_EXHAUSTED",
    "VALIDITY_HOLD",
    "CANONICAL_WRITE_CONFLICT",
    "EVENT_CURSOR_EXPIRED",
    "RETIRED_ROUTE",
    "REVISION_MISMATCH",
    "UPLOAD_TOO_LARGE",
    "RESPONSE_TOO_LARGE",
    "UNSUPPORTED_MEDIA_TYPE",
    "RESPONSE_SHAPE_INVALID",
    "NUMERIC_FORMAT_INVALID",
    "UNSUPPORTED_MODEL_EFFORT",
    "BLUEPRINT_INVALID",
    "EXPECTED_REVISION_REQUIRED",
    "IDEMPOTENCY_KEY_REQUIRED",
    "LOCAL_RATE_LIMIT",
    "STORAGE_BUSY",
    "OWNER_BRIDGE_UNAVAILABLE",
    "SERVICE_STOPPING",
]


class ProblemV1(Contract):
    type: Literal["about:blank"] = "about:blank"
    title: NonEmpty
    status: Annotated[int, Field(ge=400, le=599)]
    code: ErrorCode
    detail: NonEmpty
    request_id: NonEmpty
    retryable: bool
    context: SafeErrorContext
    retry_after_at: UTCTime | None = None


class SafeEventPayload(Contract):
    state: JobState | AttemptState | CanonicalCommitState | Literal["online", "offline"] | None = (
        None
    )
    reason_code: NonEmpty | None = None
    completed_count: NonNegativeInt | None = None
    total_count: NonNegativeInt | None = None
    reference_ids: tuple[OperationalId, ...] = ()
    requested_model: NonEmpty | None = None
    requested_effort: RoleEffort | None = None
    actual_model: NonEmpty | None = None
    actual_effort: RoleEffort | None = None


class OperationalEventV1(Contract):
    schema_version: Literal[1] = 1
    event_id: OperationalId
    seq: PositiveInt
    occurred_at: UTCTime
    aggregate_kind: Literal[
        "job", "receipt", "assessment", "publication", "projection", "provider", "service"
    ]
    aggregate_id: NonEmpty
    course_key: CourseKey | None
    event: Literal[
        "job_state_changed",
        "step_completed",
        "receipt_committed",
        "assessment_updated",
        "publication_changed",
        "projection_updated",
        "provider_state_changed",
        "service_state_changed",
    ]
    payload: SafeEventPayload
