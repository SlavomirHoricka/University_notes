import pytest
from fastapi.testclient import TestClient
from learning_hub.api.core.health import HealthResponse
from pydantic import ValidationError


def test_liveness_cannot_claim_readiness(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == HealthResponse().model_dump()
    with pytest.raises(ValidationError):
        HealthResponse.model_validate({"ready": True})
    with pytest.raises(ValidationError):
        HealthResponse.model_validate({"learner_score": 100})


def test_only_health_is_exposed(client: TestClient) -> None:
    schema = client.get("/api/v1/openapi.json").json()
    assert set(schema["paths"]) == {"/api/v1/health"}
    assert client.post("/api/v1/complete").status_code == 404
