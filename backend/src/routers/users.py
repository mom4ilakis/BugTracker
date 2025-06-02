from typing import Annotated
from fastapi import APIRouter, Security

from dependencies import get_current_user
from dto import CurrentUser, User
from services import UserServiceDep

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users(user_service: UserServiceDep) -> list[User]:
    return user_service.find_all()

@router.get("/me")
async def get_me( current_user: Annotated[CurrentUser, Security(get_current_user, scopes=["me"])]) -> CurrentUser:
    return current_user.model_dump()
