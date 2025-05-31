from fastapi import APIRouter
from uuid import UUID

from dependencies import BugServiceDep
from dto import NewBug, Bug, BugUpdate

router = APIRouter(prefix="/bugs", tags=["bugs"])


@router.get("/")
async def get_bugs(bug_service: BugServiceDep) -> list[Bug]:
    return bug_service.find_all()

@router.post("/")
async def create_bug(new_bug: NewBug, bug_service: BugServiceDep) -> Bug:
    return bug_service.create_new_bug(**new_bug.model_dump())

@router.patch("/{bug_uuid}")
async def update_bug(bug_uuid: UUID, update: BugUpdate, bug_service: BugServiceDep) -> Bug:
    return bug_service.update_bug(bug_uuid, update.model_dump())

@router.delete("/{bug_uuid}")
async def delete_bug(bug_uuid: UUID):
    return {"message": f"Delete bug {bug_uuid} successful"}