from uuid import UUID

from pydantic import BaseModel

from constants import Status, Priority, Severity
from .user import User

class NewBug(BaseModel):
    title: str
    description: str | None
    status: Status | None
    priority: Priority | None
    severity: Severity | None
    steps: str | None
    expected: str | None
    actual: str | None
    reported_by: User | None
    assigned_to: User | None

class Bug(NewBug):
    uuid: UUID


class BugUpdate(BaseModel):
    title: str
    description: str | None
    status: Status | None
    priority: Priority | None
    severity: Severity | None
    steps: str | None
    expected: str | None
    actual: str | None
    assigned_to: User | None
