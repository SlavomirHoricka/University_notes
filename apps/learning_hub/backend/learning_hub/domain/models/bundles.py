from decimal import Decimal
from typing import Literal, Self

from pydantic import Field, model_validator

from learning_hub.domain.models.base import (
    Contract,
    DecimalString,
    Digest,
    GitCommit,
    NonEmpty,
    Points,
    PositiveInt,
    RelativePath,
    UTCTime,
    decimal_sum,
    decimal_weight_between,
)
from learning_hub.domain.models.identity import (
    AuthoringRef,
    BundleRef,
    CompatibilityRow,
    DefinitionRef,
    NoteLocator,
)
from learning_hub.domain.models.questions import PrivateItemV1, PromptNode


class ReviewReference(Contract):
    role: Literal["uni_source_checker", "uni_curriculum_checker"]
    reviewer_id: NonEmpty
    output_digest: Digest
    transaction_id: NonEmpty
    final_result: Literal["no_material_findings"]


class ObjectiveIndex(Contract):
    definition: DefinitionRef
    dependencies: tuple[DefinitionRef, ...]
    ready: bool
    source_notes: tuple[NoteLocator, ...] = Field(min_length=1)
    acquisition_rule: NonEmpty
    delayed_rule: NonEmpty
    compatibility: tuple[CompatibilityRow, ...]
    reassessment_requirement_ids: tuple[NonEmpty, ...]


class PublicSectionV1(Contract):
    section_ref: AuthoringRef
    heading: NonEmpty
    content: tuple[PromptNode, ...]
    checkpoint_refs: tuple[NonEmpty, ...]
    visual_refs: tuple[NonEmpty, ...]


class LessonDefinition(Contract):
    lesson_ref: AuthoringRef
    title: NonEmpty
    required: bool
    teaching_minutes: PositiveInt
    quiz_minutes: PositiveInt
    sections: tuple[PublicSectionV1, ...] = Field(min_length=1)
    quiz_ref: NonEmpty


class WeekDefinition(Contract):
    week_ref: AuthoringRef
    display_number: PositiveInt
    required: bool
    lesson_refs: tuple[NonEmpty, ...]
    weekly_blueprint_ref: NonEmpty


class CoverageRow(Contract):
    note_locator: NoteLocator
    required_concept_id: NonEmpty
    definition: DefinitionRef
    section_ref: NonEmpty
    checkpoint_refs: tuple[NonEmpty, ...]
    assessment_component_refs: tuple[NonEmpty, ...]
    required: bool
    optional_reason: NonEmpty | None
    capability: Literal["value", "concept", "procedure", "interpretation"]

    @model_validator(mode="after")
    def complete_coverage(self) -> Self:
        if self.required and not self.assessment_component_refs:
            raise ValueError("Required concept lacks assessment coverage")
        if not self.required and self.optional_reason is None:
            raise ValueError("Optional concept requires provenance reason")
        return self


class InstructionalRoute(Contract):
    route_id: NonEmpty
    section_refs: tuple[NonEmpty, ...]
    checkpoint_refs: tuple[NonEmpty, ...]
    correction_activity_refs: tuple[NonEmpty, ...]


class PreparedActivityV1(Contract):
    activity_ref: AuthoringRef
    kind: Literal["immediate_repair", "corrective_refresh", "retention_check", "reassessment"]
    section_refs: tuple[NonEmpty, ...]
    item_refs: tuple[NonEmpty, ...] = Field(min_length=1)
    instructions: tuple[PromptNode, ...] = Field(min_length=1)
    source_notes: tuple[NoteLocator, ...] = Field(min_length=1)
    estimated_minutes: PositiveInt


class BlueprintItem(Contract):
    item_id: NonEmpty
    role: Literal["current_week", "earlier_week"]
    points: Points
    studied_state: Literal["studied", "unstudied", "unknown"]


class EssentialRule(Contract):
    item_id: NonEmpty
    component_id: NonEmpty
    rule: NonEmpty


class AssessmentBlueprintV1(Contract):
    assessment_ref: AuthoringRef
    kind: Literal["lesson_quiz", "weekly_test"]
    week_number: PositiveInt
    items: tuple[BlueprintItem, ...] = Field(min_length=1)
    max_points: Points
    essential_rules: tuple[EssentialRule, ...]
    allowed_notes: Literal["closed", "open"]
    allowed_tools: tuple[NonEmpty, ...]
    variant_families: tuple[NonEmpty, ...]
    feedback_policy: Literal["per_item", "after_final_submission"]
    expected_minutes: PositiveInt
    retry_route: NonEmpty
    unseen_bank_sufficient: bool
    exception_reason: NonEmpty | None = None

    @model_validator(mode="after")
    def correct_points_and_policy(self) -> Self:
        total = decimal_sum(item.points for item in self.items)
        if total <= 0 or total != Decimal(self.max_points):
            raise ValueError("Blueprint point total mismatch")
        if len({item.item_id for item in self.items}) != len(self.items):
            raise ValueError("Duplicate blueprint item")
        expected = "per_item" if self.kind == "lesson_quiz" else "after_final_submission"
        if self.feedback_policy != expected:
            raise ValueError("Invalid feedback policy")
        if self.kind == "weekly_test":
            current = decimal_sum(item.points for item in self.items if item.role == "current_week")
            if self.week_number == 1 and current != total:
                raise ValueError("Week 1 cannot borrow earlier scope")
            if (
                self.week_number > 1
                and not decimal_weight_between(current, total, "0.45", "0.55")
                and not self.exception_reason
            ):
                raise ValueError("Noncompliant weekly weighting needs checked exception")
        return self


class VisualParameter(Contract):
    name: NonEmpty
    unit: NonEmpty
    minimum: DecimalString
    maximum: DecimalString
    default: DecimalString

    @model_validator(mode="after")
    def bounded(self) -> Self:
        if not Decimal(self.minimum) <= Decimal(self.default) <= Decimal(self.maximum):
            raise ValueError("Visual default outside declared domain")
        return self


class VisualConfigV1(Contract):
    visual_id: NonEmpty
    component: Literal["line_chart", "payoff", "cash_flow", "derivation", "diagram"]
    formula_id: NonEmpty
    source_notes: tuple[NoteLocator, ...] = Field(min_length=1)
    assumptions: tuple[NonEmpty, ...] = Field(min_length=1)
    parameters: tuple[VisualParameter, ...]
    labels: tuple[NonEmpty, ...]
    accessible_description: NonEmpty
    reference_case_ids: tuple[NonEmpty, ...] = Field(min_length=1)
    static_fallback_asset: NonEmpty


class BundleManifestV1(Contract):
    bundle_ref: BundleRef
    source_snapshot_id: NonEmpty
    created_at: UTCTime
    public_files: dict[RelativePath, Digest]
    private_files: dict[RelativePath, Digest]
    plan_transaction_id: NonEmpty
    ingest_transaction_id: NonEmpty
    integrated_commit: GitCommit
    reviews: tuple[ReviewReference, ...] = Field(min_length=2)
    required_scope: tuple[NonEmpty, ...]
    optional_scope: tuple[NonEmpty, ...]
    blocked_scope: tuple[NonEmpty, ...]
    objectives: tuple[ObjectiveIndex, ...] = Field(min_length=1)
    weeks: tuple[WeekDefinition, ...] = Field(min_length=1)
    lessons: tuple[LessonDefinition, ...] = Field(min_length=1)
    coverage: tuple[CoverageRow, ...] = Field(min_length=1)
    routes: tuple[InstructionalRoute, ...] = Field(min_length=1)
    activities: tuple[PreparedActivityV1, ...] = Field(min_length=1)
    blueprints: tuple[AssessmentBlueprintV1, ...] = Field(min_length=1)
    visuals: tuple[VisualConfigV1, ...]
    private_items: tuple[PrivateItemV1, ...] = Field(min_length=1)

    @model_validator(mode="after")
    def references(self) -> Self:
        definitions = {objective.definition for objective in self.objectives}
        items = {item.item_ref.item_id: item for item in self.private_items}
        sections = {
            section.section_ref.id: section
            for lesson in self.lessons
            for section in lesson.sections
        }
        lessons = {lesson.lesson_ref.id for lesson in self.lessons}
        blueprints = {blueprint.assessment_ref.id for blueprint in self.blueprints}
        weeks = {week.week_ref.id for week in self.weeks}
        routes = {route.route_id for route in self.routes}
        if len(weeks) != len(self.weeks) or len(routes) != len(self.routes):
            raise ValueError("Duplicate week/route IDs")
        blueprints_by_id = {blueprint.assessment_ref.id: blueprint for blueprint in self.blueprints}
        visuals = {visual.visual_id for visual in self.visuals}
        activities = {activity.activity_ref.id for activity in self.activities}
        if len(activities) != len(self.activities) or len(visuals) != len(self.visuals):
            raise ValueError("Duplicate activity/visual IDs")
        if self.public_files.keys() & self.private_files.keys():
            raise ValueError("Public/private file maps overlap")
        if len(items) != len(self.private_items) or len(sections) != sum(
            len(lesson.sections) for lesson in self.lessons
        ):
            raise ValueError("Duplicate authoring IDs")
        if (
            len(definitions) != len(self.objectives)
            or len(lessons) != len(self.lessons)
            or len(blueprints) != len(self.blueprints)
        ):
            raise ValueError("Duplicate definitions/lessons/blueprints")
        if {r.role for r in self.reviews} != {"uni_source_checker", "uni_curriculum_checker"}:
            raise ValueError("Both independent review roles required")
        for definition in definitions:
            if (
                definition.course_id,
                definition.plan_version,
                definition.source_version,
                definition.ingestion_revision,
            ) != (
                self.bundle_ref.course_id,
                self.bundle_ref.plan_version,
                self.bundle_ref.source_version,
                self.bundle_ref.ingestion_revision,
            ):
                raise ValueError("Objective/bundle tuple mismatch")
        for objective in self.objectives:
            if not set(objective.dependencies) <= definitions:
                raise ValueError("Dangling objective dependency")

        def walk(definition: DefinitionRef, path: frozenset[DefinitionRef]) -> None:
            if definition in path:
                raise ValueError("Cyclic objective dependency")
            objective = next(o for o in self.objectives if o.definition == definition)
            for dependency in objective.dependencies:
                walk(dependency, path | {definition})

        for definition in definitions:
            walk(definition, frozenset())
        for item in items.values():
            if item.item_ref.model_dump(include=set(DefinitionRef.model_fields)) != next(
                (
                    d.model_dump()
                    for d in definitions
                    if d.objective_id == item.item_ref.objective_id
                ),
                None,
            ):
                raise ValueError("Unknown item definition")
            if not {c.definition for c in item.components} <= definitions:
                raise ValueError("Unknown component definition")
            if not {feedback.correction_route for feedback in item.feedback} <= activities:
                raise ValueError("Dangling feedback correction activity")
        for section in sections.values():
            if (
                not set(section.checkpoint_refs) <= items.keys()
                or not set(section.visual_refs) <= visuals
            ):
                raise ValueError("Dangling checkpoint/visual reference")
        for lesson in self.lessons:
            if lesson.quiz_ref not in blueprints:
                raise ValueError("Dangling quiz")
            if blueprints_by_id[lesson.quiz_ref].kind != "lesson_quiz":
                raise ValueError("Lesson quiz references non-quiz blueprint")
        for week in self.weeks:
            if not set(week.lesson_refs) <= lessons or week.weekly_blueprint_ref not in blueprints:
                raise ValueError("Dangling week lesson/blueprint")
            if blueprints_by_id[week.weekly_blueprint_ref].kind != "weekly_test":
                raise ValueError("Weekly assessment references non-weekly blueprint")
        for activity in self.activities:
            if (
                not set(activity.section_refs) <= sections.keys()
                or not set(activity.item_refs) <= items.keys()
            ):
                raise ValueError("Dangling prepared activity")
        for route in self.routes:
            if (
                not set(route.section_refs) <= sections.keys()
                or not set(route.checkpoint_refs) <= items.keys()
                or not set(route.correction_activity_refs) <= activities
            ):
                raise ValueError("Dangling instructional route")
        components = {
            f"{item_id}/{c.component_id}"
            for item_id, item in items.items()
            for c in item.components
        }
        for row in self.coverage:
            if (
                row.definition not in definitions
                or row.section_ref not in sections
                or not set(row.checkpoint_refs) <= items.keys()
                or not set(row.assessment_component_refs) <= components
            ):
                raise ValueError("Dangling coverage reference")
        if {row.definition for row in self.coverage if row.required} != {
            o.definition for o in self.objectives if o.ready
        }:
            raise ValueError("Ready objective lacks required concept coverage")
        for blueprint in self.blueprints:
            if blueprint.retry_route not in activities:
                raise ValueError("Dangling blueprint retry activity")
            if not {i.item_id for i in blueprint.items} <= items.keys():
                raise ValueError("Dangling blueprint item")
            if any(
                Decimal(i.points) != Decimal(items[i.item_id].max_points) for i in blueprint.items
            ):
                raise ValueError("Blueprint/item point mismatch")
            selected_components = {
                f"{entry.item_id}/{component.component_id}"
                for entry in blueprint.items
                for component in items[entry.item_id].components
            }
            if any(
                f"{e.item_id}/{e.component_id}" not in selected_components
                for e in blueprint.essential_rules
            ):
                raise ValueError("Dangling essential rule")
        return self


class PublicBundleV1(Contract):
    bundle_ref: BundleRef
    required_scope: tuple[NonEmpty, ...]
    optional_scope: tuple[NonEmpty, ...]
    blocked_scope: tuple[NonEmpty, ...]
    definitions: tuple[DefinitionRef, ...]
    weeks: tuple[WeekDefinition, ...]
    lessons: tuple[LessonDefinition, ...]


def public_bundle(manifest: BundleManifestV1) -> PublicBundleV1:
    """Explicit allowlist projection excludes the private bank from ordinary lessons."""
    return PublicBundleV1(
        bundle_ref=manifest.bundle_ref,
        required_scope=manifest.required_scope,
        optional_scope=manifest.optional_scope,
        blocked_scope=manifest.blocked_scope,
        definitions=tuple(o.definition for o in manifest.objectives),
        weeks=manifest.weeks,
        lessons=manifest.lessons,
    )
