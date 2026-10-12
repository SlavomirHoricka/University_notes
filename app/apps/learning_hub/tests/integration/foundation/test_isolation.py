from pathlib import Path

from fastapi import APIRouter
from fastapi.testclient import TestClient
from learning_hub.application.core.bootstrap import create_app


def test_app_creation_and_reads_do_not_write_vault(temporary_vault: Path) -> None:
    # HTTP reads have no course filesystem authority.
    before = sorted(str(path.relative_to(temporary_vault)) for path in temporary_vault.rglob("*"))
    with TestClient(create_app(), base_url="http://127.0.0.1") as client:
        assert client.get("/api/v1/health").status_code == 200
        assert client.get("/api/v1/courses").status_code == 404
    after = sorted(str(path.relative_to(temporary_vault)) for path in temporary_vault.rglob("*"))
    assert before == after
    assert not any(path.is_file() for path in temporary_vault.rglob("*"))


def test_rebinding_host_rejected() -> None:
    with TestClient(create_app(), base_url="http://attacker.example") as client:
        assert client.get("/api/v1/health").status_code == 400


def test_owner_router_composition_is_per_instance() -> None:
    owner_router = APIRouter()

    @owner_router.get("/test-owner")
    def owner() -> dict[str, str]:
        return {"fixture": "test-only"}

    with TestClient(create_app(routers=[owner_router]), base_url="http://127.0.0.1") as extended:
        assert extended.get("/api/v1/test-owner").status_code == 200
    with TestClient(create_app(), base_url="http://127.0.0.1") as plain:
        assert plain.get("/api/v1/test-owner").status_code == 404
