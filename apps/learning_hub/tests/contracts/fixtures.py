from typing import Literal

from learning_hub.domain.models.bundles import (
    AssessmentBlueprintV1,
    BlueprintItem,
    BundleManifestV1,
    CoverageRow,
    EssentialRule,
    InstructionalRoute,
    LessonDefinition,
    ObjectiveIndex,
    PreparedActivityV1,
    PublicSectionV1,
    ReviewReference,
    WeekDefinition,
)
from learning_hub.domain.models.identity import (
    AuthoringRef,
    BundleRef,
    DefinitionRef,
    ItemRef,
    NoteLocator,
)
from learning_hub.domain.models.questions import (
    Choice,
    ChoiceKey,
    Conditions,
    NumericKey,
    NumericSpec,
    PreparedFeedback,
    PrivateItemV1,
    ScoringComponent,
    SingleChoiceSpec,
    TextNode,
)

COURSE = "fixture/Winter_Semester/Scaffold"
KEY = "crs_fixture01"
STAMP = "2026-10-11T10:00:00Z"
HASH = "a" * 64
UUID = "12345678-1234-4123-8123-123456789abc"


def definition() -> DefinitionRef:
    return DefinitionRef(
        course_id=COURSE,
        plan_version="P001",
        source_version="V001",
        ingestion_revision=1,
        objective_id="O001",
        objective_revision=1,
        criterion_version="O001-C1",
    )


def item_ref(item_id: str = "O001-I01") -> ItemRef:
    return ItemRef(
        **definition().model_dump(),
        item_id=item_id,
        item_version=1,
        variant_id="var_" + UUID,
        variant_version=1,
    )


def bundle_ref() -> BundleRef:
    return BundleRef(
        course_id=COURSE,
        plan_version="P001",
        source_version="V001",
        ingestion_revision=1,
        bundle_id="pub_" + UUID,
        public_digest=HASH,
        private_digest=HASH,
    )


def conditions() -> Conditions:
    return Conditions(
        assistance="unknown",
        note_access="unknown",
        tools=(),
        solution_exposure="unknown",
        intervening_exposure="unknown",
    )


def note() -> NoteLocator:
    return NoteLocator(
        path="01_Notes/fixture/Winter_Semester/Scaffold/test.md", heading="Synthetic"
    )


def item(*, retention: bool = False) -> PrivateItemV1:
    spec = (
        NumericSpec(
            kind="numeric",
            unit="percent",
            representation="percentage_points",
            rounding="2 decimals",
        )
        if retention
        else SingleChoiceSpec(
            kind="single_choice",
            choices=(
                Choice(option_id="o1", label="Synthetic A"),
                Choice(option_id="o2", label="Synthetic B"),
            ),
        )
    )
    key = (
        NumericKey(
            kind="numeric",
            target="91234.56789",
            absolute_tolerance="0.01",
            relative_tolerance="0",
            accepted_representations=(),
        )
        if retention
        else ChoiceKey(kind="single_choice", option_ids=("o2",))
    )
    feedback = (
        (
            PreparedFeedback(
                selector="general", explanation="PRIVATE_BANK_SENTINEL", correction_route="repair"
            ),
        )
        if retention
        else tuple(
            PreparedFeedback(
                selector=id, explanation="PRIVATE_BANK_SENTINEL", correction_route="repair"
            )
            for id in ("o1", "o2")
        )
    )
    return PrivateItemV1(
        item_ref=item_ref("O001-I02" if retention else "O001-I01"),
        exposure_equivalence_id="synthetic-lineage",
        family_id="fixture-family",
        purpose="retention" if retention else "checkpoint",
        task_relation="parallel_variant",
        prompt=(TextNode(kind="text", text="UNRELEASED_PROMPT_SENTINEL"),),
        response_spec=spec,
        key=key,
        components=(
            ScoringComponent(
                component_id="value",
                definition=definition(),
                max_points="2",
                essential=True,
                outcome_rule="fixture-rule",
            ),
        ),
        max_points="2",
        feedback=feedback,
        allowed_conditions=conditions(),
        source_notes=(note(),),
    )


def manifest() -> BundleManifestV1:
    reviewer_roles: tuple[Literal["uni_source_checker", "uni_curriculum_checker"], ...] = (
        "uni_source_checker",
        "uni_curriculum_checker",
    )
    quiz = AssessmentBlueprintV1(
        assessment_ref=AuthoringRef(id="A001", revision=1),
        kind="lesson_quiz",
        week_number=1,
        items=(
            BlueprintItem(
                item_id="O001-I01", role="current_week", points="2", studied_state="unknown"
            ),
        ),
        max_points="2",
        essential_rules=(
            EssentialRule(item_id="O001-I01", component_id="value", rule="fixture-rule"),
        ),
        allowed_notes="closed",
        allowed_tools=(),
        variant_families=("fixture-family",),
        feedback_policy="per_item",
        expected_minutes=5,
        retry_route="repair",
        unseen_bank_sufficient=True,
    )
    weekly = AssessmentBlueprintV1.model_validate_json(
        quiz.model_dump_json()
        .replace('"A001"', '"A002"')
        .replace('"lesson_quiz"', '"weekly_test"')
        .replace('"per_item"', '"after_final_submission"')
    )
    return BundleManifestV1(
        bundle_ref=bundle_ref(),
        source_snapshot_id="src_" + UUID,
        created_at=STAMP,
        public_files={"public/lessons/L001.json": HASH},
        private_files={"private/items.json": HASH},
        plan_transaction_id="fixture-plan",
        ingest_transaction_id="fixture-ingest",
        integrated_commit="b" * 40,
        reviews=tuple(
            ReviewReference(
                role=role,
                reviewer_id="fixture-reviewer",
                output_digest=HASH,
                transaction_id="fixture-review",
                final_result="no_material_findings",
            )
            for role in reviewer_roles
        ),
        required_scope=("synthetic",),
        optional_scope=(),
        blocked_scope=(),
        objectives=(
            ObjectiveIndex(
                definition=definition(),
                dependencies=(),
                ready=True,
                source_notes=(note(),),
                acquisition_rule="fixture-only",
                delayed_rule="fixture-only",
                compatibility=(),
                reassessment_requirement_ids=(),
            ),
        ),
        weeks=(
            WeekDefinition(
                week_ref=AuthoringRef(id="W001", revision=1),
                display_number=1,
                required=True,
                lesson_refs=("L001",),
                weekly_blueprint_ref="A002",
            ),
        ),
        lessons=(
            LessonDefinition(
                lesson_ref=AuthoringRef(id="L001", revision=1),
                title="Synthetic",
                required=True,
                teaching_minutes=25,
                quiz_minutes=5,
                sections=(
                    PublicSectionV1(
                        section_ref=AuthoringRef(id="L001-S001", revision=1),
                        heading="Synthetic",
                        content=(TextNode(kind="text", text="Synthetic teaching text"),),
                        checkpoint_refs=("O001-I01",),
                        visual_refs=(),
                    ),
                ),
                quiz_ref="A001",
            ),
        ),
        coverage=(
            CoverageRow(
                note_locator=note(),
                required_concept_id="synthetic",
                definition=definition(),
                section_ref="L001-S001",
                checkpoint_refs=("O001-I01",),
                assessment_component_refs=("O001-I01/value",),
                required=True,
                optional_reason=None,
                capability="value",
            ),
        ),
        routes=(
            InstructionalRoute(
                route_id="lesson",
                section_refs=("L001-S001",),
                checkpoint_refs=("O001-I01",),
                correction_activity_refs=("repair",),
            ),
        ),
        activities=(
            PreparedActivityV1(
                activity_ref=AuthoringRef(id="repair", revision=1),
                kind="immediate_repair",
                section_refs=("L001-S001",),
                item_refs=("O001-I01",),
                instructions=(TextNode(kind="text", text="Synthetic checked repair"),),
                source_notes=(note(),),
                estimated_minutes=5,
            ),
        ),
        blueprints=(quiz, weekly),
        visuals=(),
        private_items=(item(), item(retention=True)),
    )
