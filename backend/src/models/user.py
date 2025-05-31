import uuid as _uuid

from sqlmodel import Field

from .timestamp_mixin import TimeStampMixin


class User(TimeStampMixin, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uuid: _uuid.UUID = Field(default_factory=_uuid.uuid4, unique=True, index=True)
    username: str = Field(unique=True)
    email: str = Field(unique=True, max_length=255)
    password: str = Field()
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)
