from typing import Annotated

from fastapi import APIRouter, Query, HTTPException, status
from uuid import UUID

from fastapi.params import Security

from constants import UserNotFoundException
from constants.filters import FilterParams
from dependencies import get_current_user
from services import BugServiceDep
from dto import NewBug, Bug, CurrentUser, UpdatedBug

router = APIRouter(prefix="/bugs", tags=["bugs"])


@router.get("/")
async def get_bugs(bug_service: BugServiceDep, filter_query: Annotated[FilterParams, Query()],
                   current_user: Annotated[CurrentUser, Security(get_current_user, scopes=["bugs:read"])]) -> list[Bug]:
    return bug_service.find_all(filter_query)


@router.post("/")
async def create_bug(new_bug: NewBug, bug_service: BugServiceDep,
                     current_user: Annotated[CurrentUser, Security(get_current_user, scopes=["bugs:write"])]) -> Bug:
    title = new_bug.title
    assignee = new_bug.assigned_to

    rest = new_bug.model_dump(exclude={"title", "assigned_to"}, exclude_defaults=True)
    try:
        bug = bug_service.create_new_bug(title, current_user.uuid, assignee, rest)
        return bug
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assignee not found!")


@router.patch("/{bug_uuid}")
async def update_bug(bug_uuid: UUID, update: UpdatedBug, bug_service: BugServiceDep,
                     current_user: Annotated[CurrentUser, Security(get_current_user, scopes=["bugs:write"])]) -> Bug:
    try:
        return bug_service.update_bug(bug_uuid, update.model_dump(exclude_defaults=True))
    except UserNotFoundException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Assignee not found!")


@router.delete("/{bug_uuid}")
async def delete_bug(bug_uuid: UUID,
                     current_user: Annotated[CurrentUser, Security(get_current_user, scopes=["bugs:write"])]):
    return {"message": f"Delete bug {bug_uuid} successful"}
