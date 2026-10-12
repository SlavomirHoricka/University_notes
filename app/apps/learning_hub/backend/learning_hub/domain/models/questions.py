from decimal import Decimal
from typing import Annotated, Literal, Self

from pydantic import AfterValidator, Field, model_validator

from learning_hub.domain.models.base import (
    Contract,
    DecimalString,
    DeliveryId,
    NonEmpty,
    NonNegativeInt,
    Points,
    PositiveInt,
    decimal_string,
    decimal_sum,
)
from learning_hub.domain.models.identity import BundleRef, DefinitionRef, ItemRef, NoteLocator

Unit = Literal["percent", "basis_points", "ratio", "currency", "years", "days", "count", "unitless"]
Representation = Literal["number", "decimal_fraction", "percentage_points", "basis_points"]


class TextNode(Contract):
    kind: Literal["text"]
    text: str


class MathNode(Contract):
    kind: Literal["math"]
    tex: NonEmpty
    display: bool


PromptNode = Annotated[TextNode | MathNode, Field(discriminator="kind")]


class Conditions(Contract):
    assistance: Literal[
        "none", "cue", "strategy_hint", "partial_worked", "full_solution", "unknown"
    ]
    note_access: Literal["closed", "open", "unknown"]
    tools: tuple[NonEmpty, ...]
    solution_exposure: Literal["none", "prior_same_session", "during_attempt", "unknown"]
    intervening_exposure: Literal["none", "reported", "unknown"]


class Choice(Contract):
    option_id: NonEmpty
    label: str


class ChoiceSpec(Contract):
    choices: tuple[Choice, ...] = Field(min_length=2)

    @model_validator(mode="after")
    def unique_options(self) -> Self:
        if len({choice.option_id for choice in self.choices}) != len(self.choices):
            raise ValueError("Duplicate options")
        return self


class SingleChoiceSpec(ChoiceSpec):
    kind: Literal["single_choice"]


class MultipleChoiceSpec(ChoiceSpec):
    kind: Literal["multiple_choice"]


class MatchLabel(Contract):
    id: NonEmpty
    label: str


class MatchingSpec(Contract):
    kind: Literal["matching"]
    left: tuple[MatchLabel, ...] = Field(min_length=1)
    right: tuple[MatchLabel, ...] = Field(min_length=1)
    right_reuse: bool

    @model_validator(mode="after")
    def unique_labels(self) -> Self:
        for side in (self.left, self.right):
            if len({label.id for label in side}) != len(side):
                raise ValueError("Duplicate matching labels")
        return self


class NumericSpec(Contract):
    kind: Literal["numeric"]
    unit: Unit
    representation: Representation
    rounding: NonEmpty


class ShortTextSpec(Contract):
    kind: Literal["short_text"]
    max_utf8_bytes: Literal[20000] = 20000


ResponseSpec = Annotated[
    SingleChoiceSpec | MultipleChoiceSpec | MatchingSpec | NumericSpec | ShortTextSpec,
    Field(discriminator="kind"),
]


class SingleChoiceResponse(Contract):
    kind: Literal["single_choice"]
    option_id: NonEmpty


class MultipleChoiceResponse(Contract):
    kind: Literal["multiple_choice"]
    option_ids: tuple[NonEmpty, ...]

    @model_validator(mode="after")
    def unique_options(self) -> Self:
        if len(self.option_ids) != len(set(self.option_ids)):
            raise ValueError("Duplicate response options")
        return self


class Pair(Contract):
    left_id: NonEmpty
    right_id: NonEmpty


class MatchingResponse(Contract):
    kind: Literal["matching"]
    pairs: tuple[Pair, ...]

    @model_validator(mode="after")
    def unique_left(self) -> Self:
        if len(self.pairs) != len({pair.left_id for pair in self.pairs}):
            raise ValueError("Duplicate left pairing")
        return self


def numeric_input(value: str) -> str:
    return decimal_string(value) if value != "" else value


class NumericResponse(Contract):
    kind: Literal["numeric"]
    value: Annotated[str, AfterValidator(numeric_input)]
    representation: Representation
    unit: Unit


def short_text(value: str) -> str:
    if len(value.encode("utf-8")) > 20000:
        raise ValueError("Response exceeds UTF-8 byte limit")
    return value


class ShortTextResponse(Contract):
    kind: Literal["short_text"]
    text: Annotated[str, AfterValidator(short_text)]


Response = Annotated[
    SingleChoiceResponse
    | MultipleChoiceResponse
    | MatchingResponse
    | NumericResponse
    | ShortTextResponse,
    Field(discriminator="kind"),
]


class ChoiceKey(Contract):
    kind: Literal["single_choice", "multiple_choice"]
    option_ids: tuple[NonEmpty, ...] = Field(min_length=1)


class MatchingKey(Contract):
    kind: Literal["matching"]
    pairs: tuple[Pair, ...] = Field(min_length=1)


class NumericKey(Contract):
    kind: Literal["numeric"]
    target: DecimalString
    absolute_tolerance: Points
    relative_tolerance: Points
    accepted_representations: tuple[Representation, ...]


class RubricComponent(Contract):
    component_id: NonEmpty
    definition: DefinitionRef
    max_points: Points
    essential: bool
    required_claims: tuple[NonEmpty, ...]
    acceptable_alternatives: tuple[NonEmpty, ...]
    critical_errors: tuple[NonEmpty, ...]
    source_notes: tuple[NoteLocator, ...] = Field(min_length=1)
    outcome_rule: NonEmpty


class WrittenKey(Contract):
    kind: Literal["short_text"]
    components: tuple[RubricComponent, ...] = Field(min_length=1)


PrivateKey = Annotated[
    ChoiceKey | MatchingKey | NumericKey | WrittenKey, Field(discriminator="kind")
]


class PreparedFeedback(Contract):
    selector: NonEmpty
    explanation: NonEmpty
    correction_route: NonEmpty


class ScoringComponent(Contract):
    component_id: NonEmpty
    definition: DefinitionRef
    max_points: Points
    essential: bool
    outcome_rule: NonEmpty


class PrivateItemV1(Contract):
    schema_version: Literal[1] = 1
    item_ref: ItemRef
    exposure_equivalence_id: NonEmpty
    family_id: NonEmpty
    purpose: Literal[
        "checkpoint", "lesson_quiz", "weekly_test", "immediate_repair", "retention", "reassessment"
    ]
    task_relation: Literal["same_item_retry", "parallel_variant", "new_application", "diagnostic"]
    prompt: tuple[PromptNode, ...] = Field(min_length=1)
    response_spec: ResponseSpec
    key: PrivateKey
    components: tuple[ScoringComponent, ...] = Field(min_length=1)
    max_points: Points
    feedback: tuple[PreparedFeedback, ...] = Field(min_length=1)
    allowed_conditions: Conditions
    source_notes: tuple[NoteLocator, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def key_and_points(self) -> Self:
        if self.response_spec.kind != self.key.kind:
            raise ValueError("Response spec/key kind mismatch")
        if decimal_sum(c.max_points for c in self.components) != Decimal(self.max_points):
            raise ValueError("Component point sum mismatch")
        if Decimal(self.max_points) <= 0:
            raise ValueError("Item needs positive prepared denominator")
        if len({f.selector for f in self.feedback}) != len(self.feedback):
            raise ValueError("Duplicate prepared feedback selector")
        if len({c.component_id for c in self.components}) != len(self.components):
            raise ValueError("Duplicate scoring components")
        if any(c.definition.course_id != self.item_ref.course_id for c in self.components):
            raise ValueError("Cross-course scoring component")
        if isinstance(self.response_spec, (SingleChoiceSpec, MultipleChoiceSpec)):
            options = {c.option_id for c in self.response_spec.choices}
            if not isinstance(self.key, ChoiceKey) or not set(self.key.option_ids) <= options:
                raise ValueError("Unknown key option")
            if self.key.kind == "single_choice" and len(self.key.option_ids) != 1:
                raise ValueError("Single-choice key requires one answer")
            if {f.selector for f in self.feedback} != options:
                raise ValueError("Every option needs prepared feedback")
        if isinstance(self.key, ChoiceKey) and len(set(self.key.option_ids)) != len(
            self.key.option_ids
        ):
            raise ValueError("Duplicate key option")
        if isinstance(self.response_spec, MatchingSpec) and isinstance(self.key, MatchingKey):
            left = {x.id for x in self.response_spec.left}
            right = {x.id for x in self.response_spec.right}
            if (
                len(self.key.pairs) != len(left)
                or (
                    not self.response_spec.right_reuse
                    and len({p.right_id for p in self.key.pairs}) != len(self.key.pairs)
                )
                or {p.left_id for p in self.key.pairs} != left
                or any(p.right_id not in right for p in self.key.pairs)
            ):
                raise ValueError("Matching key does not cover labels")
        if isinstance(self.key, WrittenKey):
            prepared = {
                (c.component_id, c.max_points, c.definition, c.essential) for c in self.components
            }
            rubric = {
                (c.component_id, c.max_points, c.definition, c.essential)
                for c in self.key.components
            }
            if prepared != rubric:
                raise ValueError("Rubric/component mismatch")
        return self


class PublicPromptV1(Contract):
    delivery_id: DeliveryId
    item_ref: ItemRef
    bundle_ref: BundleRef
    prompt: tuple[PromptNode, ...]
    response_spec: ResponseSpec
    allowed_conditions: Conditions
    estimated_minutes: PositiveInt | None = None


def public_prompt(item: PrivateItemV1, delivery_id: str, bundle: BundleRef) -> PublicPromptV1:
    if item.purpose == "retention":
        raise ValueError("Retention prompt requires explicit selected-delivery authorization")
    if (
        item.item_ref.course_id,
        item.item_ref.plan_version,
        item.item_ref.source_version,
        item.item_ref.ingestion_revision,
    ) != (bundle.course_id, bundle.plan_version, bundle.source_version, bundle.ingestion_revision):
        raise ValueError("Item/bundle tuple mismatch")
    return PublicPromptV1(
        delivery_id=delivery_id,
        item_ref=item.item_ref,
        bundle_ref=bundle,
        prompt=item.prompt,
        response_spec=item.response_spec,
        allowed_conditions=item.allowed_conditions,
    )


def validate_response(spec: ResponseSpec, response: Response) -> None:
    if spec.kind != response.kind:
        raise ValueError("Wrong response kind")
    if isinstance(spec, (SingleChoiceSpec, MultipleChoiceSpec)):
        options = {choice.option_id for choice in spec.choices}
        chosen = (
            (response.option_id,)
            if isinstance(response, SingleChoiceResponse)
            else response.option_ids
            if isinstance(response, MultipleChoiceResponse)
            else ()
        )
        if not set(chosen) <= options:
            raise ValueError("Unknown response option")
    if isinstance(spec, MatchingSpec) and isinstance(response, MatchingResponse):
        if (
            any(
                p.left_id not in {x.id for x in spec.left}
                or p.right_id not in {x.id for x in spec.right}
                for p in response.pairs
            )
            or not spec.right_reuse
            and len({p.right_id for p in response.pairs}) != len(response.pairs)
        ):
            raise ValueError("Invalid matching response")


class ResponseSpan(Contract):
    start: NonNegativeInt
    end: PositiveInt
    text: str

    @model_validator(mode="after")
    def ordered(self) -> Self:
        if self.start >= self.end:
            raise ValueError("Invalid response span")
        return self


class ComponentDecision(Contract):
    component_id: NonEmpty
    outcome: Literal["met", "partial", "unmet", "unscorable"]
    earned_points: Points | None
    spans: tuple[ResponseSpan, ...]
    blank_reason: NonEmpty | None
    prepared_rule: NonEmpty
    observed_errors: tuple[NonEmpty, ...]
    feedback: NonEmpty


class AssessmentDecisionV1(Contract):
    item_ref: ItemRef
    components: tuple[ComponentDecision, ...] = Field(min_length=1)
    earned_points: Points | None
    max_points: Points
    grading_state: Literal["scored", "unscorable"]


def validate_decision(
    item: PrivateItemV1, response: ShortTextResponse, decision: AssessmentDecisionV1
) -> None:
    if item.item_ref != decision.item_ref or item.max_points != decision.max_points:
        raise ValueError("Decision definition mismatch")
    prepared = {c.component_id: c for c in item.components}
    if set(prepared) != {c.component_id for c in decision.components} or len(prepared) != len(
        decision.components
    ):
        raise ValueError("Decision components mismatch")
    for c in decision.components:
        source = prepared[c.component_id]
        if c.prepared_rule != source.outcome_rule:
            raise ValueError("Invented rubric rule")
        if c.earned_points is not None and Decimal(c.earned_points) > Decimal(source.max_points):
            raise ValueError("Component exceeds prepared points")
        if not c.spans and not (response.text == "" and c.blank_reason):
            raise ValueError("Decision lacks actual response support")
        if any(
            response.text[s.start : s.end] != s.text or s.end > len(response.text) for s in c.spans
        ):
            raise ValueError("Unsupported response span")
    if decision.grading_state == "unscorable":
        if decision.earned_points is not None:
            raise ValueError("Unscorable decision cannot have total")
    elif any(c.earned_points is None or c.outcome == "unscorable" for c in decision.components):
        raise ValueError("Scored decision has unknown component")
    elif decimal_sum(c.earned_points or "0" for c in decision.components) != Decimal(
        decision.earned_points or "-1"
    ):
        raise ValueError("Decision total mismatch")
