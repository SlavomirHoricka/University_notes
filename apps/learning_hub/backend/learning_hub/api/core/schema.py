from typing import Any

from fastapi import FastAPI
from pydantic.json_schema import models_json_schema

from learning_hub.domain.models import api, services
from learning_hub.domain.models.base import Contract
from learning_hub.domain.models.bundles import PublicBundleV1

PUBLIC_CONTRACTS: tuple[type[Contract], ...] = (
    PublicBundleV1,
    api.ReceiptV1,
    api.StartSessionCommand,
    api.BookmarkCommandV1,
    api.SessionActionCommand,
    api.RequestDeliveryCommand,
    api.AdvanceCommand,
    api.DisplayAckCommand,
    api.SubmitResponseV1,
    api.StartAssessmentV1,
    api.SaveDraftV1,
    api.AssessmentDraftV1,
    api.FinalizeDraftSnapshotV1,
    api.FinalizeExistingResponsesV1,
    api.LessonProgressV1,
    api.CourseCatalogueV1,
    api.WeekSummaryV1,
    api.SessionViewV1,
    api.DeliveryViewV1,
    api.AttemptViewV1,
    api.AssessmentViewV1,
    api.ProblemV1,
    api.OperationalEventV1,
    services.RoleSettingsV1,
    services.RoleSettingCommand,
    services.ProviderAuthStartV1,
    services.ProviderAuthFlowViewV1,
    services.ProviderSignOutV1,
    services.ProviderStatusV1,
    services.ProviderModelChoice,
    services.CapabilitiesV1,
    services.SourceRevisionV1,
    services.SourceSnapshotV1,
    services.UploadV1,
    services.RequestedJobV1,
    services.JobViewV1,
    services.JobActionV1,
    services.ApprovalProposalV1,
    services.ApprovalDecisionV1,
    services.ReviewRecommendationV1,
)


class ContractAPI(FastAPI):
    def openapi(self) -> dict[str, Any]:
        schema = super().openapi()
        _, contracts = models_json_schema(
            [(model, "validation") for model in PUBLIC_CONTRACTS],
            ref_template="#/components/schemas/{model}",
        )
        existing = schema.setdefault("components", {}).setdefault("schemas", {})
        for name, definition in contracts["$defs"].items():
            if name in existing and existing[name] != definition:
                raise ValueError("Conflicting contract schema name")
            existing[name] = definition
        schema["x-hub-schema-version"] = 1
        schema["x-hub-canonical-writes-enabled"] = False
        return schema
