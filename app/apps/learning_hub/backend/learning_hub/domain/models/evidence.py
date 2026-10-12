from typing import Annotated, Literal, Self

from pydantic import Field, SerializerFunctionWrapHandler, model_serializer, model_validator

from learning_hub.domain.models.api import CanonicalCommitState
from learning_hub.domain.models.base import (
    AttemptId,
    BundleId,
    Contract,
    Digest,
    NonEmpty,
    OperationalId,
    Points,
    PositiveInt,
    ReceiptId,
    RelativePath,
    ReportedTime,
    SessionId,
    UTCTime,
)
from learning_hub.domain.models.identity import CourseId, DefinitionRef, ItemRef
from learning_hub.domain.models.questions import Conditions, Response


class SiteResponseReceivedV1(Contract):
    phase: Literal["response_received"]
    receipt_id: ReceiptId
    attempt_id: AttemptId
    bundle_id: BundleId
    response: Response
    received_at: UTCTime
    reported_answered_at: ReportedTime | None


class SiteActivityV1(Contract):
    phase: Literal["activity", "assessment_submitted", "exposure_reported"]
    receipt_id: ReceiptId
    bundle_id: BundleId
    reference_ids: tuple[NonEmpty, ...]
    content_digest: Digest


class ProposedLogMetadataV4(Contract):
    schema_version: Literal[4]
    owner: Literal["teach"]
    course_id: CourseId
    timezone: Literal["Europe/Prague"]
    record_revision: PositiveInt
    transaction_id: NonEmpty


class ProposedCommonEventV4(Contract):
    """Proposed common fields; H09 must validate against committed owner journals."""

    schema_version: Literal[4]
    site_extension_version: Literal[1]
    writer: Literal["teach"]
    event_id: NonEmpty
    committed: bool
    transaction_id: NonEmpty
    course_id: CourseId
    occurred_at: ReportedTime | None
    recorded_at: ReportedTime
    timezone: Literal["Europe/Prague"]
    session_id: SessionId | None
    objective_id: str | None
    objective_revision: PositiveInt | None
    criterion_version: str | None
    plan_version: str | None
    source_version: str | None
    ingestion_revision: PositiveInt | None

    @model_validator(mode="after")
    def complete_definition(self) -> Self:
        fields = {name: getattr(self, name) for name in DefinitionRef.model_fields}
        if any(value is not None for name, value in fields.items() if name != "course_id"):
            DefinitionRef.model_validate(fields)
        return self


class ProposedSiteEnvelopeV1(ProposedCommonEventV4):
    """Response/activity facts cannot declare an assessed outcome."""

    event_type: Literal["session_route", "exposure_reported", "instruction_or_feedback"]
    site: SiteResponseReceivedV1 | SiteActivityV1

    @model_validator(mode="after")
    def existing_event_mapping(self) -> Self:
        if isinstance(self.site, SiteResponseReceivedV1) and self.event_type != "session_route":
            raise ValueError("Received response uses teach session_route, not an inferred result")
        if isinstance(self.site, SiteActivityV1) and (
            (self.site.phase == "assessment_submitted" and self.event_type != "session_route")
            or (self.site.phase == "exposure_reported" and self.event_type != "exposure_reported")
        ):
            raise ValueError("Site phase must match existing teach event semantics")
        return self


class SiteComponentResultV1(Contract):
    phase: Literal["component_result"]
    bundle_id: BundleId
    receipt_id: ReceiptId
    attempt_id: AttemptId
    result_id: OperationalId
    item_id: NonEmpty
    item_version: PositiveInt
    variant_id: NonEmpty
    variant_version: PositiveInt
    component_id: NonEmpty
    points_awarded: Points
    max_points: Points
    outcome_rule: NonEmpty
    response: Response
    conditions: Conditions

    @model_validator(mode="after")
    def prepared_scale(self) -> Self:
        from decimal import Decimal

        if Decimal(self.max_points) <= 0 or Decimal(self.points_awarded) > Decimal(self.max_points):
            raise ValueError("Component points outside prepared scale")
        return self


class AssistanceV3(Contract):
    level: Literal["none", "cue", "strategy_hint", "partial_worked", "full_solution", "unknown"]
    count: int | None = Field(ge=0)
    content: str | None


Outcome = Literal["pass", "partial", "fail", "incomplete", "unscorable"]


class ProposedAttemptResultV4(ProposedCommonEventV4):
    event_type: Literal["attempt_result"]
    attempt_id: AttemptId
    item_id: NonEmpty
    item_version: PositiveInt
    item_text: NonEmpty
    task_relation: Literal["same_item_retry", "parallel_variant", "new_application", "diagnostic"]
    review_kind: Literal["diagnostic", "immediate", "delayed", "reassessment"]
    review_id: NonEmpty | None
    response_evidence: str
    component_outcomes: dict[NonEmpty, Outcome]
    outcome: Outcome
    independent: bool
    assistance: AssistanceV3
    note_access: Literal["closed", "open", "unknown"]
    tools: tuple[NonEmpty, ...]
    solution_exposure: Literal["none", "prior_same_session", "during_attempt", "unknown"]
    previous_attempt_id: AttemptId | None
    last_relevant_exposure_at: ReportedTime | None
    elapsed_hours_since_exposure: Points | None
    intervening_exposure: Literal["none", "reported", "unknown"]
    intervening_exposure_details: str | None
    observed_errors: tuple[NonEmpty, ...]
    feedback_event_id: NonEmpty | None
    site: SiteComponentResultV1

    @model_validator(mode="after")
    def actual_component(self) -> Self:
        if self.objective_id is None or self.session_id is None:
            raise ValueError("Result requires full objective/session tuple")
        if (self.attempt_id, self.item_id, self.item_version) != (
            self.site.attempt_id,
            self.site.item_id,
            self.site.item_version,
        ):
            raise ValueError("Result/actual attempt mismatch")
        conditions = self.site.conditions
        if (
            self.assistance.level,
            self.note_access,
            self.tools,
            self.solution_exposure,
            self.intervening_exposure,
        ) != (
            conditions.assistance,
            conditions.note_access,
            conditions.tools,
            conditions.solution_exposure,
            conditions.intervening_exposure,
        ):
            raise ValueError("Result conditions differ from actual response")
        if self.independent and (
            self.assistance.level != "none"
            or self.note_access == "unknown"
            or self.solution_exposure != "none"
        ):
            raise ValueError("Unknown/assisted conditions cannot declare independence")
        return self


class SiteSessionFactV1(Contract):
    phase: Literal[
        "session_started",
        "session_paused",
        "session_closed",
        "attempt_started",
        "attempt_abandoned",
        "plan_issue",
        "note_issue",
    ]
    bundle_id: BundleId
    receipt_id: ReceiptId
    reference_ids: tuple[NonEmpty, ...]
    item_ref: ItemRef | None
    conditions: Conditions | None
    detail: str | None


class ProposedSessionFactV4(ProposedCommonEventV4):
    event_type: Literal[
        "session_started",
        "session_paused",
        "session_closed",
        "attempt_started",
        "attempt_abandoned",
        "plan_issue",
        "note_issue",
    ]
    site: SiteSessionFactV1

    @model_validator(mode="after")
    def actual_fact(self) -> Self:
        if self.event_type != self.site.phase:
            raise ValueError("Session fact/event mapping mismatch")
        if self.event_type == "attempt_started" and (
            self.site.item_ref is None or self.site.conditions is None
        ):
            raise ValueError("Attempt start needs prepared item and observed conditions")
        return self


class SiteQualificationV1(Contract):
    phase: Literal["qualification"]
    bundle_id: BundleId
    receipt_id: ReceiptId
    actual_attempt_ids: tuple[AttemptId, ...] = Field(min_length=1)


class ProposedQualificationV4(ProposedCommonEventV4):
    event_type: Literal["acquisition_met", "reassessment_met"]
    evidence_event_ids: tuple[NonEmpty, ...] = Field(min_length=1)
    acquisition_rule: NonEmpty | None
    requirement_id: NonEmpty | None
    rule: NonEmpty
    site: SiteQualificationV1

    @model_validator(mode="after")
    def actual_qualification(self) -> Self:
        if self.objective_id is None or len(set(self.evidence_event_ids)) != len(
            self.evidence_event_ids
        ):
            raise ValueError("Qualification needs full definition and distinct supporting events")
        if len(set(self.site.actual_attempt_ids)) != len(self.site.actual_attempt_ids):
            raise ValueError("Components cannot duplicate qualifying attempts")
        if self.event_type == "acquisition_met" and self.acquisition_rule is None:
            raise ValueError("Acquisition requires the prepared rule")
        if self.event_type == "reassessment_met" and self.requirement_id is None:
            raise ValueError("Reassessment requires the named requirement")
        return self


class CorrectedFieldsV4(Contract):
    outcome: Outcome | None = None
    component_outcomes: dict[NonEmpty, Outcome] | None = None
    independent: bool | None = None
    assistance: AssistanceV3 | None = None
    response_evidence: str | None = None
    note_access: Literal["closed", "open", "unknown"] | None = None
    tools: tuple[NonEmpty, ...] | None = None
    solution_exposure: Literal["none", "prior_same_session", "during_attempt", "unknown"] | None = (
        None
    )
    intervening_exposure: Literal["none", "reported", "unknown"] | None = None
    intervening_exposure_details: str | None = None
    observed_errors: tuple[NonEmpty, ...] | None = None
    last_relevant_exposure_at: ReportedTime | None = None
    elapsed_hours_since_exposure: Points | None = None
    # The sole proposed extension to the old correction allowlist is a new typed component decision.
    component_result: SiteComponentResultV1 | None = None

    @model_serializer(mode="wrap")
    def sparse_fields(self, handler: SerializerFunctionWrapHandler) -> dict[str, object]:
        # Canonical corrections apply exactly the supplied keys. Keep explicit nulls,
        # but never manufacture null replacements for omitted optional fields.
        values = handler(self)
        if not isinstance(values, dict):
            raise ValueError("Correction serializer requires field mapping")
        return {name: value for name, value in values.items() if name in self.model_fields_set}

    @model_validator(mode="after")
    def nonempty_changes(self) -> Self:
        if not self.model_fields_set:
            raise ValueError("Correction has no explicit corrected fields")
        return self


class ProposedCorrectionV4(ProposedCommonEventV4):
    event_type: Literal["correction"]
    supersedes_event_id: NonEmpty
    reason: NonEmpty
    corrected_fields: CorrectedFieldsV4
    site: SiteComponentResultV1

    @model_validator(mode="after")
    def preserves_original_id(self) -> Self:
        if self.event_id == self.supersedes_event_id:
            raise ValueError("Correction cannot supersede itself")
        if self.corrected_fields.component_result is not None and (
            self.corrected_fields.component_result.attempt_id != self.site.attempt_id
            or self.corrected_fields.component_result.component_id != self.site.component_id
            or self.corrected_fields.component_result.response != self.site.response
        ):
            raise ValueError("Correction changes actual component identity")
        return self


ProposedEvidenceEventV4 = Annotated[
    ProposedSiteEnvelopeV1
    | ProposedAttemptResultV4
    | ProposedSessionFactV4
    | ProposedQualificationV4
    | ProposedCorrectionV4,
    Field(discriminator="event_type"),
]


def evidence_payload_digest(events: tuple[ProposedEvidenceEventV4, ...]) -> str:
    import hashlib
    import json

    payload = json.dumps(
        [event.model_dump(mode="json") for event in events],
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


class EvidenceIntentV1(Contract):
    intent_id: OperationalId
    receipt_id: ReceiptId
    course_id: CourseId
    owner: Literal["teach"]
    transaction_id: NonEmpty
    event_ids: tuple[NonEmpty, ...]
    payload_digest: Digest
    events: tuple[ProposedEvidenceEventV4, ...] = Field(min_length=1)
    canonical_state: CanonicalCommitState

    @model_validator(mode="after")
    def academic_only(self) -> Self:
        if (
            len(set(self.event_ids)) != len(self.event_ids)
            or self.event_ids != tuple(event.event_id for event in self.events)
            or any(
                event.site.receipt_id != self.receipt_id
                or event.course_id != self.course_id
                or event.transaction_id != self.transaction_id
                or event.committed
                for event in self.events
            )
        ):
            raise ValueError("Intent must bind exact uncommitted events/course/transaction")
        if self.payload_digest != evidence_payload_digest(self.events):
            raise ValueError("Intent digest does not bind exact event payload")
        if self.canonical_state == "not_applicable":
            raise ValueError("Operational receipt cannot enter evidence outbox")
        return self


class EvidenceCommitV1(Contract):
    intent_id: OperationalId
    transaction_id: NonEmpty
    canonical_path: RelativePath
    event_ids: tuple[NonEmpty, ...]
    event_digests: tuple[Digest, ...]
    committed_log_digest: Digest
    verified_at: UTCTime

    @model_validator(mode="after")
    def exact_events(self) -> Self:
        if (
            len(self.event_ids) != len(self.event_digests)
            or not self.event_ids
            or len(set(self.event_ids)) != len(self.event_ids)
        ):
            raise ValueError("Evidence proof requires unique event/hash pairs")
        return self


class CanonicalCompatibilityGate(Contract):
    maintained_schema4_supported: Literal[False] = False
    live_writes_enabled: Literal[False] = False
    pending_owner_task: Literal["H09"] = "H09"
