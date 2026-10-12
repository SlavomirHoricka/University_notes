from collections.abc import Sequence

from fastapi import APIRouter, FastAPI
from starlette.middleware.trustedhost import TrustedHostMiddleware

from learning_hub.api.core.health import router as health_router
from learning_hub.api.core.schema import ContractAPI


def create_app(*, routers: Sequence[APIRouter] = ()) -> FastAPI:
    """Compose owner-supplied routers; imports have no filesystem/provider side effects."""
    app = ContractAPI(title="Uni Learning Hub", version="1.0.0", openapi_url="/api/v1/openapi.json")
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost"])
    app.include_router(health_router, prefix="/api/v1")
    for router in routers:
        app.include_router(router, prefix="/api/v1")
    return app
