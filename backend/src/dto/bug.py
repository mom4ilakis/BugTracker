from uuid import UUID

from pydantic import BaseModel, Field

from constants import Status, Priority, Severity
from .user import User


class BaseBug(BaseModel):
    title: str
    description: str | None = Field(None, max_length=1000)
    steps: str | None = Field(None, max_length=255)
    expected: str | None = Field(None, max_length=255)
    actual: str | None = Field(None, max_length=255)
    status: Status | None = None
    priority: Priority | None = None
    severity: Severity | None = None


class NewBug(BaseBug):
    assigned_to: UUID | None = None


class UpdatedBug(BaseBug,):
    title: str | None = Field(None, max_length=255)
    assigned_to: UUID | None = None


class Bug(BaseBug):
    uuid: UUID
    reporter: User
    assignee: User | None = None


class Metadata(BaseModel):
    severity: list[str]
    priority: list[str]
    status: list[str]