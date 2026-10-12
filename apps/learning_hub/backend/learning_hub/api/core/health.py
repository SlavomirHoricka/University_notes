from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict


class HealthResponse(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")

    schema_version: Literal[1] = 1
    service: Literal["learning-hub"] = "learning-hub"
    status: Literal["ok"] = "ok"
    ready: Literal[False] = False
    reason: Literal["scaffold_only"] = "scaffold_only"


router = APIRouter()


@router.get("/health", response_model=HealthResponse, operation_id="getHealth")
def health() -> HealthResponse:
    """Liveness only; H00 cannot certify provider, worker or academic readiness."""
    return HealthResponse()
