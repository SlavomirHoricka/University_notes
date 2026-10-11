from collections.abc import Iterator
from pathlib import Path

import httpx
import pytest
from fastapi.testclient import TestClient
from learning_hub.application.core.bootstrap import create_app


@pytest.fixture
def client() -> Iterator[TestClient]:
    with TestClient(create_app(), base_url="http://127.0.0.1") as test_client:
        yield test_client


@pytest.fixture
def temporary_vault(tmp_path: Path) -> Path:
    root = tmp_path / "fictional-vault"
    for name in ("00_Materials", "01_Notes", "03_Agents"):
        (root / name / "fixture" / "Winter_Semester" / "Scaffold").mkdir(parents=True)
    return root


@pytest.fixture
def test_transport() -> httpx.MockTransport:
    """Bounded synthetic transport; unavailable to production composition."""

    def respond(request: httpx.Request) -> httpx.Response:
        if request.url != httpx.URL("https://fixture.invalid/status"):
            raise AssertionError("Unexpected test transport request")
        return httpx.Response(503, json={"fixture": "unavailable"})

    return httpx.MockTransport(respond)
