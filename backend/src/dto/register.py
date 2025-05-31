from pydantic import BaseModel, EmailStr


class RegisterInfo(BaseModel):
    email: EmailStr
    username: str
    password: str