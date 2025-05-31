from sqlmodel import Field
from sqlalchemy import Column, Enum as SQLEnum, String
import uuid as _uuid

from constants import Status, Priority, Severity
from .timestamp_mixin import TimeStampMixin

class Bug(TimeStampMixin, table=True):
    id: int = Field(primary_key=True)
    uuid:_uuid.UUID = Field(default_factory=_uuid.uuid4, unique=True, index=True)
    title: str = Field(max_length=255)
    description: str | None = Field(max_length=1000)
    steps: str | None = Field(nullable=True, max_length=255)
    expected: str | None = Field(nullable=True, max_length=255)
    actual: str | None = Field(nullable=True, max_length=255)
    status: Status = Field(sa_column=Column(SQLEnum(Status), server_default=Status.NEW.value, nullable=False))
    priority: Priority = Field(sa_column=Column(SQLEnum(Priority), default=Priority.MEDIUM, server_default=Priority.MEDIUM.value, nullable=False))
    severity: Severity = Field(sa_column=Column(SQLEnum(Severity), default=Severity.MEDIUM, server_default=Severity.MEDIUM.value, nullable=False))
    reported_by: int | None = Field(default=None, foreign_key="user.id")
    assigned_to: int | None = Field(default=None, foreign_key="user.id")
