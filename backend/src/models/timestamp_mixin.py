from datetime import datetime

from sqlalchemy import DateTime, func
from sqlmodel import SQLModel, Field


class TimeStampMixin(SQLModel):
    created_at: datetime = Field(sa_type=DateTime(), sa_column_kwargs={"server_default": func.now(), "nullable": False})
    updated_at: datetime = Field(sa_type=DateTime(),
                                 sa_column_kwargs={
                                     "server_default": func.now(),
                                     "onupdate": func.now(),
                                     "nullable": False
                                 })
