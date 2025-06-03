from pydantic import BaseModel, EmailStr, Field


class RegisterInfo(BaseModel):
    email: EmailStr
    username: str = Field(max_length=255)
    password: str = Field(max_length=255)