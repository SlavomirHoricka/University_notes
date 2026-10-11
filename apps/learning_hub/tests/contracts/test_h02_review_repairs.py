"""Regression evidence for the independent H02 review findings."""

import json
from decimal import Decimal, localcontext
from typing import Any

import pytest
from learning_hub.application.core.bootstrap import create_app
from learning_hub.domain.models.api import (
    AssessmentViewV1,
    EvidenceViewV1,
    PreferenceCommand,
    PreferencesV1,
    StartReviewV1,
)
from learning_hub.domain.models.bundles import BundleManifestV1
from learning_hub.domain.models.evidence import (
    CorrectedFieldsV4,
    ProposedCorrectionV4,
    ProposedEvidenceEventV4,
    evidence_payload_digest,
)
from learning_hub.domain.models.services import JobSummaryV1, UploadReceiptV1
from pydantic import RootModel, ValidationError

from .fixtures import COURSE, HASH, KEY, STAMP, UUID, definition, manifest
from .test_h02_canonical_extension import result_event


@pytest.mark.parametrize(
    "change",
    [
        "unselected_essential",
        "weekly_as_quiz",
        "quiz_as_weekly",
        "duplicate_week",
        "duplicate_route",
    ],
)
def test_review_r2_blueprint_local_reachability_and_identity(change: str) -> None:
    data = manifest().model_dump(mode="json")
    if change == "unselected_essential":
        excluded = data["private_items"][1]
        assert excluded["purpose"] == "retention"
        assert excluded["item_ref"]["item_id"] not in {
            item["item_id"] for item in data["blueprints"][0]["items"]
        }
        data["blueprints"][0]["essential_rules"] = [
            {
                "item_id": excluded["item_ref"]["item_id"],
                "component_id": excluded["components"][0]["component_id"],
                "rule": "fixture-rule",
            }
        ]
    elif change == "weekly_as_quiz":
        data["lessons"][0]["quiz_ref"] = data["blueprints"][1]["assessment_ref"]["id"]
    elif change == "quiz_as_weekly":
        data["weeks"][0]["weekly_blueprint_ref"] = data["blueprints"][0]["assessment_ref"]["id"]
    elif change == "duplicate_week":
        data["weeks"].append(data["weeks"][0])
    else:
        data["routes"].append(data["routes"][0])
    with pytest.raises(ValidationError):
        BundleManifestV1.model_validate_json(json.dumps(data))


def assessment_data(*, final: bool = False) -> dict[str, Any]:
    return {
        "assessment_id": "asm_" + UUID,
        "session_id": "ses_" + UUID,
        "prepared_ref": {"id": "A001", "revision": 1},
        "status": "finalized" if final else "grading_pending",
        "revision": 3,
        "submitted_at": STAMP,
        "final_result_id": "res_" + UUID if final else None,
        "max_points": "100",
        "required_item_count": 2,
        "finalized_item_count": 2 if final else 1,
        "result": {
            "kind": "final",
            "earned_points": "85",
            "max_points": "100",
            "percentage": "85",
            "passed": True,
            "needs_attention": True,
            "active_committed_review_weakness": False,
        }
        if final
        else {
            "kind": "provisional",
            "earned_points": "45",
            "possible_points": "50",
            "label": "partial",
        },
        "essential_states": [
            {
                "item_id": "O001-I01",
                "component_id": "value",
                "prepared_rule": "fixture-rule",
                "state": "met" if final else "pending",
            }
        ],
        "canonical_commit_state": "verified" if final else "pending",
    }


@pytest.mark.parametrize(
    "change",
    [
        "final_while_pending",
        "pass_in_provisional",
        "unscorable_final",
        "missing_denominator",
        "changed_denominator",
        "partial_exceeds_denominator",
        "incomplete_required",
        "unknown_essential",
        "unverified_final",
        "wrong_percentage",
        "wrong_pass",
        "wrong_attention",
    ],
)
def test_review_r3_assessment_pending_and_final_truth_boundaries(change: str) -> None:
    final = change not in {
        "pass_in_provisional",
        "missing_denominator",
        "partial_exceeds_denominator",
    }
    data = assessment_data(final=final)
    if change == "final_while_pending":
        data["status"] = "grading_pending"
    elif change == "pass_in_provisional":
        data["result"]["passed"] = True
    elif change == "unscorable_final":
        data["status"] = "unscorable"
    elif change == "missing_denominator":
        data["max_points"] = None
    elif change == "changed_denominator":
        data["max_points"] = "120"
    elif change == "partial_exceeds_denominator":
        data["result"]["possible_points"] = "101"
    elif change == "incomplete_required":
        data["finalized_item_count"] = 1
    elif change == "unknown_essential":
        data["essential_states"][0]["state"] = "pending"
    elif change == "unverified_final":
        data["canonical_commit_state"] = "pending"
    elif change == "wrong_percentage":
        data["result"]["percentage"] = "86"
    elif change == "wrong_pass":
        data["result"]["passed"] = False
    else:
        data["result"]["needs_attention"] = False
    with pytest.raises(ValidationError):
        AssessmentViewV1.model_validate_json(json.dumps(data))


def test_review_r3_aggregate_thresholds_and_precision80_are_truthful() -> None:
    provisional = AssessmentViewV1.model_validate_json(json.dumps(assessment_data()))
    assert provisional.max_points == "100" and provisional.result is not None
    assert "passed" not in provisional.result.model_dump()
    for points, essential, passed, attention in (
        ("85", "met", True, True),
        ("95", "unmet", False, True),
        ("90", "met", True, False),
    ):
        data = assessment_data(final=True)
        data["result"].update(
            earned_points=points, percentage=points, passed=passed, needs_attention=attention
        )
        data["essential_states"][0]["state"] = essential
        AssessmentViewV1.model_validate_json(json.dumps(data))
    data = assessment_data(final=True)
    with localcontext() as context:
        context.prec = 80
        percentage = str(Decimal(100) / 3)
    data["max_points"] = "3"
    data["result"].update(
        earned_points="1", max_points="3", percentage=percentage, passed=False, needs_attention=True
    )
    assert AssessmentViewV1.model_validate_json(json.dumps(data)).max_points == "3"


def evidence_data() -> dict[str, Any]:
    return {
        "course_id": COURSE,
        "canonical_cursor": "fixture-cursor",
        "owner_verified": True,
        "git_sync_state": "pending",
        "definitions": [
            {
                "definition": definition().model_dump(mode="json"),
                "applicability": "current",
                "acquisition_state": "met",
                "acquisition_event_ids": ["fixture-acquisition"],
                "last_result_event_id": "fixture-result",
                "last_outcome": "pass",
                "delayed_result_event_ids": [],
            }
        ],
        "activity": [],
    }


def test_review_r3_evidence_owner_proof_is_independent_of_git_sync() -> None:
    data = evidence_data()
    assert EvidenceViewV1.model_validate_json(json.dumps(data)).git_sync_state == "pending"
    data["owner_verified"] = False
    with pytest.raises(ValidationError):
        EvidenceViewV1.model_validate_json(json.dumps(data))
    data = evidence_data()
    data["definitions"][0]["definition"]["course_id"] = "fixture/Winter_Semester/Other"
    with pytest.raises(ValidationError):
        EvidenceViewV1.model_validate_json(json.dumps(data))
    data = evidence_data()
    data["canonical_cursor"] = None
    with pytest.raises(ValidationError):
        EvidenceViewV1.model_validate_json(json.dumps(data))


def test_review_r3_preferences_and_review_start_are_strict_and_nonacademic() -> None:
    PreferencesV1.model_validate_json(
        '{"preferences":{"theme":"dark","text_size":"large","reduced_motion":true,"outline_visible":false},"revision":1}'
    )
    with pytest.raises(ValidationError):
        PreferenceCommand.model_validate_json(
            '{"preferences":{"theme":"dark","mastery":true},"expected_revision":1}'
        )
    with pytest.raises(ValidationError):
        PreferencesV1.model_validate_json('{"preferences":{"theme":"arbitrary-html"},"revision":1}')
    StartReviewV1(
        recommendation_id="rev_" + UUID,
        bundle_id="pub_" + UUID,
        expected_projection_cursor="fixture-cursor",
    )
    with pytest.raises(ValidationError):
        StartReviewV1.model_validate_json(
            '{"recommendation_id":"rev_' + UUID + '","bundle_id":"pub_' + UUID + '"}'
        )


def upload_data() -> dict[str, Any]:
    return {
        "receipt": {
            "receipt_id": "rec_" + UUID,
            "command_id": "cmd_" + UUID,
            "kind": "upload",
            "command_kind": "upload",
            "aggregate_id": "upl_" + UUID,
            "canonical_commit_state": "not_applicable",
            "processing_state": "received",
            "received_at": STAMP,
            "aggregate_revision": 1,
            "canonical_event_ids": [],
            "status_url": "/api/v1/receipts/rec_" + UUID,
        },
        "course_key": KEY,
        "sources": [
            {
                "source_id": "src_" + UUID,
                "source_revision_id": "srr_" + UUID,
                "revision": 1,
                "course_key": KEY,
                "sha256": HASH,
                "byte_size": 100,
                "media_type": "application/pdf",
                "managed_relpath": "fixture/source.pdf",
                "week_ref": {"id": "W001", "revision": 1},
                "extraction_state": "pending",
            }
        ],
        "duplicate_source_revision_ids": [],
    }


def test_review_r3_upload_receipt_preserves_original_hash_and_course() -> None:
    data = upload_data()
    accepted = UploadReceiptV1.model_validate_json(json.dumps(data))
    assert accepted.sources[0].sha256 == HASH and accepted.sources[0].extraction_state == "pending"
    data["sources"][0]["course_key"] = "crs_other123"
    with pytest.raises(ValidationError):
        UploadReceiptV1.model_validate_json(json.dumps(data))
    data = upload_data()
    del data["sources"][0]["sha256"]
    with pytest.raises(ValidationError):
        UploadReceiptV1.model_validate_json(json.dumps(data))
    data = upload_data()
    data["receipt"]["canonical_commit_state"] = "committed"
    with pytest.raises(ValidationError):
        UploadReceiptV1.model_validate_json(json.dumps(data))


def test_review_r3_job_summary_counts_and_actual_settings_remain_factual() -> None:
    data = {
        "job_id": "job_" + UUID,
        "course_key": KEY,
        "kind": "source_inventory",
        "state": "queued",
        "revision": 1,
        "created_at": STAMP,
        "current_step": None,
        "completed_step_count": 0,
        "total_step_count": None,
        "requested_settings": {"model": "gpt-6.1-sol", "effort": "high"},
        "actual_settings": None,
        "next_eligible_at": None,
        "error_code": None,
    }
    assert JobSummaryV1.model_validate_json(json.dumps(data)).actual_settings is None
    data.update(total_step_count=1, completed_step_count=2)
    with pytest.raises(ValidationError):
        JobSummaryV1.model_validate_json(json.dumps(data))


def test_review_r3_missing_normative_models_are_in_actual_public_export() -> None:
    schemas = create_app().openapi()["components"]["schemas"]
    for name in (
        "EvidenceViewV1",
        "StartReviewV1",
        "UploadReceiptV1",
        "JobSummaryV1",
        "PreferencesV1",
        "PreferenceCommand",
    ):
        assert schemas[name]["additionalProperties"] is False
    assessment = schemas["AssessmentViewV1"]["properties"]
    assert {
        "max_points",
        "required_item_count",
        "finalized_item_count",
        "result",
        "essential_states",
    } <= assessment.keys()
    assert not set(schemas) & {"PrivateItemV1", "WrittenKey", "NumericKey", "CredentialMaterial"}


def correction_event(changes: dict[str, Any]) -> ProposedCorrectionV4:
    data = result_event().model_dump(mode="json")
    common = {name: data[name] for name in ProposedCorrectionV4.model_fields if name in data}
    common.update(
        event_id="fixture-correction",
        event_type="correction",
        supersedes_event_id=data["event_id"],
        reason="Synthetic scoring correction",
        corrected_fields=changes,
    )
    return ProposedCorrectionV4.model_validate_json(json.dumps(common))


def test_review_r5_sparse_correction_dump_roundtrip_and_digest_preserve_semantics() -> None:
    sparse = CorrectedFieldsV4(outcome="pass")
    assert sparse.model_dump(mode="json") == {"outcome": "pass"}
    parsed = CorrectedFieldsV4.model_validate_json(sparse.model_dump_json())
    assert parsed.model_fields_set == {"outcome"}
    event = correction_event({"outcome": "pass"})
    serialized = event.model_dump(mode="json")
    assert serialized["corrected_fields"] == {"outcome": "pass"}
    reparsed = RootModel[ProposedEvidenceEventV4].model_validate_json(event.model_dump_json()).root
    assert isinstance(reparsed, ProposedCorrectionV4)
    assert reparsed.corrected_fields.model_fields_set == {"outcome"}
    assert evidence_payload_digest((event,)) == evidence_payload_digest((reparsed,))
    explicit_null = correction_event({"outcome": "pass", "intervening_exposure_details": None})
    assert explicit_null.model_dump(mode="json")["corrected_fields"] == {
        "outcome": "pass",
        "intervening_exposure_details": None,
    }
    assert evidence_payload_digest((explicit_null,)) != evidence_payload_digest((event,))
    null_reparsed = ProposedCorrectionV4.model_validate_json(explicit_null.model_dump_json())
    assert null_reparsed.corrected_fields.model_fields_set == {
        "outcome",
        "intervening_exposure_details",
    }
    original = {
        "outcome": "partial",
        "response_evidence": "Actual original response",
        "independent": False,
        "note_access": "unknown",
        "assistance": {"level": "unknown"},
    }
    effective = {**original, **serialized["corrected_fields"]}
    assert effective["outcome"] == "pass"
    for field in ("response_evidence", "independent", "note_access", "assistance"):
        assert effective[field] == original[field]


def test_unverified_activity_cannot_publish_grade_and_provisional_hold_requires_submission() -> (
    None
):
    data = evidence_data()
    data.update(
        owner_verified=False,
        canonical_cursor=None,
        definitions=[],
        activity=[
            {
                "session_id": "ses_" + UUID,
                "last_receipt_id": None,
                "canonical_activity_event_ids": [],
                "progress": {
                    "instruction_state": "in_progress",
                    "assessment_submission_state": "submitted",
                    "assessment_grading_state": "finalized",
                    "completed": False,
                    "passed": True,
                    "needs_attention": False,
                    "evidence_state": "unknown",
                    "canonical_commit_state": "unknown",
                },
            }
        ],
    )
    with pytest.raises(ValidationError):
        EvidenceViewV1.model_validate_json(json.dumps(data))
    assessment = assessment_data()
    assessment.update(status="validity_hold", submitted_at=None)
    with pytest.raises(ValidationError):
        AssessmentViewV1.model_validate_json(json.dumps(assessment))
