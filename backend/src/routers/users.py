from uuid import UUID
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
async def get_users():
    return {"message": "Get ALL users successful"}


@router.post("/")
async def create_user():
    return {"message": "Create user successful"}


@router.patch("/{user_uuid}")
async def update_user(user_uuid: UUID):
    return {"message": f"Update user {user_uuid} successful"}


@router.delete("/{user_uuid}")
async def delete_user(user_uuid: UUID):
    return {"message": f"Delete user {user_uuid} successful"}
