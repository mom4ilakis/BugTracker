from uuid import UUID

from pydantic import BaseModel, Field

from constants import Status, Priority, Severity


class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}
    status: Status | None = Field(None, description="Filter bugs by status")
    priority: Priority | None = Field(None, description="Filter bugs by priority")
    severity: Severity | None = Field(None, description="Filter bugs by severity")
    assigned_to: UUID | None = Field(None, description="Filter bugs by assigned_to")
    reported_by: UUID | None = Field(None, description="Filter bugs by reported_by")
