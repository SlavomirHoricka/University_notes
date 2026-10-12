from typing import get_args

import pytest
from learning_hub.application.core.bootstrap import create_app
from learning_hub.domain.models.api import ErrorCode, ProblemV1, SafeErrorContext
from pydantic import ValidationError

PROVIDER_CODES = (
    "PROVIDER_AUTH_REQUIRED",
    "PROVIDER_MISSING_GRANT",
    "PROVIDER_INELIGIBLE",
    "PROVIDER_USAGE_LIMIT",
    "PROVIDER_TRANSIENT",
    "PROVIDER_INVALID_INPUT",
    "PROVIDER_PROTOCOL_ERROR",
    "PROVIDER_UNKNOWN_OUTCOME",
    "PROVIDER_REVISION_CONFLICT",
    "PROVIDER_STORAGE_FAILURE",
    "PROVIDER_VERSION_UNSUPPORTED",
)


@pytest.mark.parametrize("code", PROVIDER_CODES)
def test_provider_lifecycle_errors_typed_and_exported(code: str) -> None:
    import json

    payload = json.dumps(
        {
            "title": "Provider action unavailable",
            "status": 503,
            "code": code,
            "detail": "Retry after inspecting the durable provider status.",
            "request_id": "fixture-request",
            "retryable": False,
            "context": {},
        }
    )
    problem = ProblemV1.model_validate_json(payload)
    assert problem.code in get_args(ErrorCode)
    exported = create_app().openapi()["components"]["schemas"]["ProblemV1"]["properties"]
    assert problem.code in exported["code"]["enum"]
    with pytest.raises(ValidationError):
        SafeErrorContext.model_validate_json('{"token":"must-not-leak"}')
