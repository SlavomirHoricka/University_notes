"""Proposed union-reader fixtures only: never a production records writer or recall adapter."""

import json
import re
from dataclasses import dataclass
from pathlib import Path

import pytest
from learning_hub.domain.models.evidence import (
    CanonicalCompatibilityGate,
    EvidenceIntentV1,
    ProposedAttemptResultV4,
    ProposedEvidenceEventV4,
    ProposedLogMetadataV4,
    ProposedSiteEnvelopeV1,
    evidence_payload_digest,
)
from pydantic import RootModel, ValidationError

from .fixtures import COURSE, HASH, STAMP, UUID, conditions, definition

FIXTURES = Path(__file__).parent / "history_fixtures"
BOUNDARY = b"## Schema 4 boundary\n"


def fence(value: str) -> bytes:
    return ("```json\n" + value + "\n```\n").encode("utf-8")


@dataclass(frozen=True)
class HistoricalRecord:
    raw_fence: bytes
    # The proposed union retains original data without asserting modern evidence validity.


@dataclass(frozen=True)
class FixtureUnion:
    original_prefix: bytes
    history: tuple[HistoricalRecord, ...]
    metadata: ProposedLogMetadataV4
    appended: tuple[ProposedEvidenceEventV4, ...]


def proposed_union_reader(data: bytes) -> FixtureUnion:
    """Bounded test reader; metadata is resolved after latest explicit v4 boundary."""
    if BOUNDARY in data:
        prefix, extension = data.rsplit(BOUNDARY, 1)
    elif data.startswith(b"<!-- uni-teach-log:4 -->\n"):
        prefix, extension = b"", data.removeprefix(b"<!-- uni-teach-log:4 -->\n")
    else:
        raise ValueError("Missing explicit proposed schema-4 metadata boundary")
    old = tuple(
        HistoricalRecord(match.group(0))
        for match in re.finditer(rb"```json\r?\n.*?\r?\n```", prefix, re.S)
    )
    blocks = re.findall(rb"```json\n(.*?)\n```", extension, re.S)
    if not blocks:
        raise ValueError("Metadata missing")
    metadata = ProposedLogMetadataV4.model_validate_json(blocks[0])
    appended = tuple(
        RootModel[ProposedEvidenceEventV4].model_validate_json(block).root for block in blocks[1:]
    )
    if any(
        event.course_id != metadata.course_id or event.transaction_id != metadata.transaction_id
        for event in appended
    ):
        raise ValueError("Event metadata/course/transaction mismatch")
    if len({event.event_id for event in appended}) != len(appended):
        raise ValueError("Conflicting or duplicate event IDs")
    return FixtureUnion(prefix, old, metadata, appended)


def response_event() -> ProposedSiteEnvelopeV1:
    values = {name: None for name in type(definition()).model_fields if name != "course_id"}
    return ProposedSiteEnvelopeV1.model_validate_json(
        json.dumps(
            {
                **values,
                "schema_version": 4,
                "site_extension_version": 1,
                "writer": "teach",
                "event_id": "fixture-response",
                "event_type": "session_route",
                "committed": False,
                "transaction_id": "fixture-transaction",
                "course_id": COURSE,
                "occurred_at": None,
                "recorded_at": STAMP,
                "timezone": "Europe/Prague",
                "session_id": "ses_" + UUID,
                "site": {
                    "phase": "response_received",
                    "receipt_id": "rec_" + UUID,
                    "attempt_id": "att_" + UUID,
                    "bundle_id": "pub_" + UUID,
                    "response": {"kind": "short_text", "text": "Synthetic actual-response fixture"},
                    "received_at": STAMP,
                    "reported_answered_at": None,
                },
            }
        )
    )


def result_event() -> ProposedAttemptResultV4:
    return ProposedAttemptResultV4.model_validate_json(
        json.dumps(
            {
                **definition().model_dump(mode="json"),
                "schema_version": 4,
                "site_extension_version": 1,
                "writer": "teach",
                "event_id": "fixture-result-O001",
                "event_type": "attempt_result",
                "committed": False,
                "transaction_id": "fixture-transaction",
                "occurred_at": None,
                "recorded_at": STAMP,
                "timezone": "Europe/Prague",
                "session_id": "ses_" + UUID,
                "attempt_id": "att_" + UUID,
                "item_id": "O001-I01",
                "item_version": 1,
                "item_text": "Synthetic prepared prompt",
                "task_relation": "parallel_variant",
                "review_kind": "immediate",
                "review_id": None,
                "response_evidence": "Synthetic actual response",
                "component_outcomes": {"value": "partial"},
                "outcome": "partial",
                "independent": False,
                "assistance": {"level": "unknown", "count": None, "content": None},
                "note_access": "unknown",
                "tools": [],
                "solution_exposure": "unknown",
                "previous_attempt_id": None,
                "last_relevant_exposure_at": None,
                "elapsed_hours_since_exposure": None,
                "intervening_exposure": "unknown",
                "intervening_exposure_details": None,
                "observed_errors": [],
                "feedback_event_id": None,
                "site": {
                    "phase": "component_result",
                    "bundle_id": "pub_" + UUID,
                    "receipt_id": "rec_" + UUID,
                    "attempt_id": "att_" + UUID,
                    "result_id": "res_" + UUID,
                    "item_id": "O001-I01",
                    "item_version": 1,
                    "variant_id": "var_" + UUID,
                    "variant_version": 1,
                    "component_id": "value",
                    "points_awarded": "0.5",
                    "max_points": "1",
                    "outcome_rule": "fixture-rule",
                    "response": {"kind": "short_text", "text": "Synthetic actual response"},
                    "conditions": conditions().model_dump(mode="json"),
                },
            }
        )
    )


def extension() -> bytes:
    metadata = ProposedLogMetadataV4(
        schema_version=4,
        owner="teach",
        course_id=COURSE,
        timezone="Europe/Prague",
        record_revision=2,
        transaction_id="fixture-transaction",
    )
    return fence(metadata.model_dump_json()) + fence(response_event().model_dump_json())


@pytest.mark.parametrize("name", ["legacy.md", "schema3.md"])
def test_h02_a3_legacy_schema3_bytes_and_event_meaning_preserved(name: str) -> None:
    original = (FIXTURES / name).read_bytes()
    proposed = original + b"\n" + BOUNDARY + extension()
    union = proposed_union_reader(proposed)
    assert proposed[: len(original)] == original
    assert union.original_prefix == original + b"\n"
    old_fences = tuple(
        match.group(0) for match in re.finditer(rb"```json\r?\n.*?\r?\n```", original, re.S)
    )
    assert tuple(record.raw_fence for record in union.history) == old_fences
    assert b'"historical_status": "mystery"' in original
    assert union.appended == (response_event(),)
    assert union.metadata.schema_version == 4
    assert not CanonicalCompatibilityGate().live_writes_enabled
    # Historical records remain historical raw data, never newly qualified results.
    assert all(isinstance(record, HistoricalRecord) for record in union.history)


def test_h02_a3_new_marker_latest_boundary_and_invalid_metadata() -> None:
    assert proposed_union_reader(b"<!-- uni-teach-log:4 -->\n" + extension()).original_prefix == b""
    older = (FIXTURES / "schema3.md").read_bytes() + b"\n" + BOUNDARY + extension()
    latest = proposed_union_reader(older + BOUNDARY + extension())
    assert latest.original_prefix == older
    with pytest.raises(ValueError):
        proposed_union_reader(extension())
    with pytest.raises(ValidationError):
        proposed_union_reader(
            b"<!-- uni-teach-log:4 -->\n"
            + extension().replace(b'"schema_version":4', b'"schema_version":5')
        )


@pytest.mark.parametrize(
    "change", ["unknown", "incomplete_tuple", "excess_points", "independence", "missing_receipt"]
)
def test_proposed_result_rejects_malformed_components_and_conditions(change: str) -> None:
    data = result_event().model_dump(mode="json")
    if change == "unknown":
        data["site"]["mastery"] = True
    elif change == "incomplete_tuple":
        data["criterion_version"] = None
    elif change == "excess_points":
        data["site"]["points_awarded"] = "2"
    elif change == "independence":
        data["independent"] = True
    else:
        del data["site"]["receipt_id"]
    with pytest.raises(ValidationError):
        ProposedAttemptResultV4.model_validate_json(json.dumps(data))


def test_intent_binds_actual_events_digest_and_no_live_support() -> None:
    event = response_event()
    intent = EvidenceIntentV1(
        intent_id="int_" + UUID,
        receipt_id="rec_" + UUID,
        course_id=COURSE,
        owner="teach",
        transaction_id="fixture-transaction",
        event_ids=(event.event_id,),
        payload_digest=evidence_payload_digest((event,)),
        events=(event,),
        canonical_state="pending",
    )
    changed = intent.model_dump(mode="json")
    changed["events"][0]["site"]["response"]["text"] = "tampered"
    with pytest.raises(ValidationError):
        EvidenceIntentV1.model_validate_json(json.dumps(changed))
    changed["payload_digest"] = HASH
    changed["canonical_state"] = "not_applicable"
    with pytest.raises(ValidationError):
        EvidenceIntentV1.model_validate_json(json.dumps(changed))
    with pytest.raises(ValidationError):
        CanonicalCompatibilityGate.model_validate_json('{"live_writes_enabled":true}')
