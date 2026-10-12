import json
from typing import Any

import pytest
from learning_hub.domain.models.api import (
    AssessmentDraftV1,
    FinalizeAssessmentV1,
    FinalizeDraftSnapshotV1,
    LessonProgressV1,
    ReceiptV1,
    SaveDraftV1,
    SubmitResponseV1,
    validate_draft_freeze,
)
from learning_hub.domain.models.base import contract_digest
from learning_hub.domain.models.bundles import BundleManifestV1, public_bundle
from learning_hub.domain.models.identity import (
    CourseIdentity,
    DefinitionRef,
    ItemRef,
    assert_distinct_courses,
)
from learning_hub.domain.models.questions import (
    Response,
    ShortTextResponse,
    public_prompt,
    validate_response,
)
from learning_hub.domain.models.services import (
    ApprovalDecisionV1,
    ApprovalProposalBodyV1,
    ApprovalProposalV1,
)
from pydantic import RootModel, ValidationError

from .fixtures import (
    COURSE,
    HASH,
    KEY,
    STAMP,
    UUID,
    bundle_ref,
    conditions,
    definition,
    item,
    manifest,
)


def mutate(model: Any, **updates: Any) -> str:
    data = model.model_dump(mode="json")
    data.update(updates)
    return json.dumps(data)


@pytest.mark.parametrize(
    "field,value",
    [
        ("ingestion_revision", None),
        ("objective_revision", True),
        ("plan_version", "*"),
        ("criterion_version", "O001-Cgarbage"),
        ("source_version", "V*"),
        ("course_id", "../../outside"),
    ],
)
def test_h02_a1_invalid_definition_tuple(field: str, value: Any) -> None:
    with pytest.raises(ValidationError):
        DefinitionRef.model_validate_json(mutate(definition(), **{field: value}))


@pytest.mark.parametrize(
    "variant", ["var_" + "-" * 36, "var_12345678-1234-1123-8123-123456789abc", "att_" + UUID]
)
def test_uuid_shape_version_and_prefix(variant: str) -> None:
    with pytest.raises(ValidationError):
        ItemRef.model_validate_json(mutate(item().item_ref, variant_id=variant))


def test_course_local_ids_and_unicode_collision() -> None:
    other = DefinitionRef.model_validate_json(
        mutate(definition(), course_id="fixture/Winter_Semester/Other")
    )
    assert other != definition()
    identities = tuple(
        CourseIdentity(
            course_id="fixture/Winter_Semester/" + name,
            academic_year="fixture",
            semester="Winter_Semester",
            course_folder=name,
            course_code=None,
        )
        for name in ("Café", "Cafe\u0301")
    )
    with pytest.raises(ValueError, match="Unicode"):
        assert_distinct_courses(identities)


@pytest.mark.parametrize(
    "where", ["checkpoint", "component", "definition", "blueprint", "activity", "cycle"]
)
def test_h02_a1_dangling_bundle_references(where: str) -> None:
    data = manifest().model_dump(mode="json")
    if where == "checkpoint":
        data["lessons"][0]["sections"][0]["checkpoint_refs"] = ["absent"]
    elif where == "component":
        data["coverage"][0]["assessment_component_refs"] = ["absent/value"]
    elif where == "definition":
        data["private_items"][0]["item_ref"]["ingestion_revision"] = 2
    elif where == "blueprint":
        data["blueprints"][0]["items"][0]["item_id"] = "absent"
    elif where == "activity":
        data["routes"][0]["correction_activity_refs"] = ["absent"]
    else:
        data["objectives"][0]["dependencies"] = [definition().model_dump(mode="json")]
    with pytest.raises(ValidationError):
        BundleManifestV1.model_validate_json(json.dumps(data))


def test_h02_a2_public_projection_contains_no_bank_keys_feedback_or_retention() -> None:
    private = manifest()
    data = public_bundle(private).model_dump_json()
    for forbidden in (
        "PRIVATE_BANK_SENTINEL",
        "UNRELEASED_PROMPT_SENTINEL",
        "91234.56789",
        '"key"',
        '"target"',
        '"private_items"',
        '"feedback"',
        '"rubric"',
    ):
        assert forbidden not in data
    prompt = public_prompt(item(), "del_" + UUID, bundle_ref()).model_dump_json()
    assert "PRIVATE_BANK_SENTINEL" not in prompt and '"key"' not in prompt
    with pytest.raises(ValueError, match="Retention"):
        public_prompt(item(retention=True), "del_" + UUID, bundle_ref())


def test_strict_commands_unknown_fields_and_response_discriminator() -> None:
    command = SubmitResponseV1(
        session_id="ses_" + UUID,
        item_ref=item().item_ref,
        delivery_id="del_" + UUID,
        response=ShortTextResponse(kind="short_text", text="actual response"),
        conditions=conditions(),
        reported_answered_at=None,
        expected_revision=1,
    )
    with pytest.raises(ValidationError):
        SubmitResponseV1.model_validate_json(mutate(command, score=100))
    with pytest.raises(ValidationError):
        RootModel[Response].model_validate_json(
            '{"kind":"numeric","value":"1+1","unit":"percent","representation":"percentage_points"}'
        )
    with pytest.raises(ValidationError):
        RootModel[Response].model_validate_json('{"kind":"unknown","text":"yes"}')
    with pytest.raises(ValidationError):
        ShortTextResponse(kind="short_text", text="😀" * 5001)
    response = RootModel[Response].model_validate_json(
        '{"kind":"single_choice","option_id":"absent"}'
    )
    with pytest.raises(ValueError):
        validate_response(item().response_spec, response.root)


@pytest.mark.parametrize(
    "kind", ["assessment_draft", "approval_decision", "provider_action", "job_action", "upload"]
)
def test_exact_operational_receipt_kinds_not_evidence(kind: str) -> None:
    data = {
        "receipt_id": "rec_" + UUID,
        "command_id": "cmd_" + UUID,
        "kind": kind,
        "command_kind": kind,
        "aggregate_id": "att_" + UUID,
        "canonical_commit_state": "not_applicable",
        "processing_state": "received",
        "received_at": STAMP,
        "aggregate_revision": 1,
        "canonical_event_ids": [],
        "status_url": "/api/v1/receipts/rec_" + UUID,
    }
    ReceiptV1.model_validate_json(json.dumps(data))
    data["canonical_commit_state"] = "committed"
    with pytest.raises(ValidationError):
        ReceiptV1.model_validate_json(json.dumps(data))
    data["kind"] = "unsupported"
    with pytest.raises(ValidationError):
        ReceiptV1.model_validate_json(json.dumps(data))


def test_bookmark_nonacademic_and_pending_grade_unknown() -> None:
    receipt = ReceiptV1(
        receipt_id="rec_" + UUID,
        command_id="cmd_" + UUID,
        kind="session",
        command_kind="bookmark",
        aggregate_id="ses_" + UUID,
        canonical_commit_state="not_applicable",
        processing_state="bookmark_saved",
        received_at=STAMP,
        aggregate_revision=1,
        canonical_event_ids=(),
        status_url="/api/v1/receipts/rec_" + UUID,
    )
    assert receipt.canonical_event_ids == ()
    with pytest.raises(ValidationError):
        ReceiptV1.model_validate_json(mutate(receipt, canonical_commit_state="committed"))
    pending = LessonProgressV1(
        instruction_state="finished",
        assessment_submission_state="submitted",
        assessment_grading_state="pending",
        completed=True,
        passed=None,
        needs_attention=None,
        evidence_state="current",
        canonical_commit_state="verified",
    )
    with pytest.raises(ValidationError):
        LessonProgressV1.model_validate_json(mutate(pending, passed=True))


def test_atomic_draft_snapshot_contract_conflicts_and_complete_coverage() -> None:
    draft = AssessmentDraftV1(
        assessment_id="asm_" + UUID,
        item_id="O001-I01",
        attempt_id="att_" + UUID,
        draft_revision=1,
        response=ShortTextResponse(kind="short_text", text="actual"),
        explicit_blank=False,
        received_at=STAMP,
        reported_conditions=None,
    )
    command = FinalizeDraftSnapshotV1(
        mode="draft_snapshot",
        expected_revision=2,
        draft_revision_manifest={draft.item_id: 1},
        blank_item_ids=("O001-I02",),
        conditions=conditions(),
    )
    validate_draft_freeze(command, selected=("O001-I01", "O001-I02"), revision=2, drafts=(draft,))
    with pytest.raises(ValueError):
        validate_draft_freeze(
            command, selected=("O001-I01", "O001-I02"), revision=3, drafts=(draft,)
        )
    with pytest.raises(ValueError):
        validate_draft_freeze(
            command, selected=("O001-I01", "O001-I02", "O001-I03"), revision=2, drafts=(draft,)
        )
    with pytest.raises(ValidationError):
        RootModel[FinalizeAssessmentV1].model_validate_json(
            mutate(command, response_receipt_ids=[])
        )
    with pytest.raises(ValidationError):
        SaveDraftV1(
            response=draft.response,
            explicit_blank=True,
            expected_revision=2,
            expected_draft_revision=1,
            conditions=None,
        )


def test_approval_digest_binds_scope_expected_bytes_and_preview() -> None:
    body = ApprovalProposalBodyV1.model_validate_json(
        json.dumps(
            {
                "job_id": "job_" + UUID,
                "course_key": KEY,
                "kind": "source_selection",
                "source_snapshot_id": "src_" + UUID,
                "expected_hashes": {"00_Materials/fixture.txt": HASH},
                "scope": {
                    "course_id": COURSE,
                    "paths": ["00_Materials/fixture.txt"],
                    "action": "source_selection",
                },
                "preserved_version_refs": [],
                "safe_preview": {
                    "summary": "Synthetic selection",
                    "diff_digest": HASH,
                    "exposed_regions": [],
                },
            }
        )
    )
    proposal = ApprovalProposalV1(
        proposal_id="pro_" + UUID,
        proposal_digest=contract_digest(body),
        body=body,
        created_at=STAMP,
        status="awaiting_decision",
    )
    changed = proposal.model_dump(mode="json")
    changed["body"]["safe_preview"]["summary"] = "changed"
    with pytest.raises(ValidationError):
        ApprovalProposalV1.model_validate_json(json.dumps(changed))
    with pytest.raises(ValidationError):
        ApprovalDecisionV1.model_validate_json(
            '{"decision":"retry","proposal_digest":"' + HASH + '","expected_job_revision":1}'
        )


def test_public_payload_matches_reviewable_snapshot() -> None:
    from pathlib import Path

    actual = public_bundle(manifest()).model_dump(mode="json")
    snapshot = json.loads((Path(__file__).parent / "public_bundle.snapshot.json").read_text())
    assert actual == snapshot


def test_exported_contracts_cover_downstream_interfaces_without_private_models() -> None:
    from learning_hub.application.core.bootstrap import create_app

    schema = create_app().openapi()
    names = schema["components"]["schemas"]
    for name in (
        "StartSessionCommand",
        "SubmitResponseV1",
        "SaveDraftV1",
        "ReceiptV1",
        "FinalizeDraftSnapshotV1",
        "ApprovalDecisionV1",
        "ProviderAuthStartV1",
        "RequestedJobV1",
        "JobViewV1",
        "OperationalEventV1",
        "PublicPromptV1",
    ):
        assert name in names
        assert names[name]["additionalProperties"] is False
    assert not set(names) & {
        "PrivateItemV1",
        "NumericKey",
        "ChoiceKey",
        "WrittenKey",
        "CredentialMaterial",
        "EvidenceIntentV1",
    }
    assert schema["x-hub-schema-version"] == 1
    assert schema["x-hub-canonical-writes-enabled"] is False
    assert set(schema["paths"]) == {"/api/v1/health"}

    # Every generated component reference resolves in this actual export.
    def references(value: Any) -> None:
        if isinstance(value, dict):
            if "$ref" in value:
                assert value["$ref"].startswith("#/components/schemas/")
                assert value["$ref"].rsplit("/", 1)[1] in names
            for nested in value.values():
                references(nested)
        elif isinstance(value, list):
            for nested in value:
                references(nested)

    references(schema)


def test_prepared_decimal_sums_and_weighting_preserve_fifty_digit_boundary() -> None:
    from decimal import Decimal

    from learning_hub.domain.models.base import decimal_sum, decimal_weight_between

    assert decimal_sum(("0.12345678901234567890123456789012345678901234567890", "0.1")) == Decimal(
        "0.22345678901234567890123456789012345678901234567890"
    )
    assert not decimal_weight_between(
        Decimal("0.55000000000000000000000000000000000000000000000001"),
        Decimal("1"),
        "0.45",
        "0.55",
    )
