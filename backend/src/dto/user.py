from pydantic import BaseModel
from uuid import UUID

class User(BaseModel):
    uuid: UUID
    username: str
    is_superuser: bool