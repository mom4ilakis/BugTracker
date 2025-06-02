from uuid import UUID

from pydantic import BaseModel

from constants import Status, Priority, Severity
from .user import User


class BaseBug(BaseModel):
    title: str
    description: str | None = None
    status: Status | None = None
    priority: Priority | None = None
    severity: Severity | None = None
    steps: str | None = None
    expected: str | None = None
    actual: str | None = None


class NewBug(BaseBug):
    assigned_to: UUID | None = None


class UpdatedBug(BaseBug,):
    title: str | None = None
    assigned_to: UUID | None = None


class Bug(BaseBug):
    uuid: UUID
    reporter: User
    assignee: User | None = None


class Metadata(BaseModel):
    severity: list[str]
    priority: list[str]
    status: list[str]