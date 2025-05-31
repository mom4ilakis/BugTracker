from enum import StrEnum

from sqlmodel import SQLModel, Field
from datetime import datetime
from sqlalchemy import Column, DateTime, func, Enum as SQLEnum
import uuid as _uuid

class Status(StrEnum):
    NEW = "NEW"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"
    WONT_DO = "WONT_DO"
    CLOSED = "CLOSED"
    REOPENED = "REOPENED"

class Priority(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Severity(StrEnum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Bug(SQLModel, table=True):
    id: int = Field(primary_key=True)
    uuid:_uuid.UUID = Field(default_factory=_uuid.uuid4, unique=True, index=True)
    title: str = Field(max_length=255)
    description: str = Field()
    steps: str = Field()
    expected: str = Field()
    actual: str = Field()
    status: Status = Field(sa_column=Column(SQLEnum(Status), server_default=Status.NEW.value, nullable=False))
    priority: Priority = Field(sa_column=Column(SQLEnum(Priority), default=Priority.MEDIUM, server_default=Priority.MEDIUM.value, nullable=False))
    severity: Severity = Field(sa_column=Column(SQLEnum(Severity), default=Severity.MEDIUM, server_default=Severity.MEDIUM.value, nullable=False))
    reported_by: int | None = Field(default=None, foreign_key="user.id")
    assigned_to: int | None = Field(default=None, foreign_key="user.id")
    created_at: datetime = Field(sa_column=Column(DateTime(), server_default=func.now(), nullable=False))
    updated_at: datetime = Field(sa_column=Column(DateTime(), server_default=func.now(), onupdate=func.now(), nullable=False))

