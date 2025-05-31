from pydantic import BaseModel


class RegisterInfo(BaseModel):
    email: str
    username: str
    password: str