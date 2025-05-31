from uuid import UUID

from fastapi import Depends
from sqlmodel import Session, select

from db import get_session
from models import Bug
from dependencies import UserServiceDep


class BugService:
    def __init__(self, user_service: UserServiceDep, session: Session = Depends(get_session), ):
        self.session = session
        self.user_service = user_service

    def create_new_bug(self, title: str, reporter_uuid: UUID, assignee_uuid: UUID = None, optional_props: dict = None):
        if optional_props is None:
            optional_props = {}

        reporter = self.user_service.find_by_uuid(reporter_uuid)

        if assignee_uuid:
            assignee = self.user_service.find_by_uuid(assignee_uuid)
            if assignee:
                optional_props["assigned_to"] = assignee.id

        bug = Bug(title=title, reported_by=reporter.id, **optional_props)
        self.session.add(bug)
        self.session.commit()
        self.session.refresh(bug)
        return bug

    def update_bug(self, uuid: UUID, updates):
        bug_to_update = self.find_by_uuid(uuid)
        for key, value in updates.items():
            setattr(bug_to_update, key, value)
        self.session.add(bug_to_update)
        self.session.commit()
        self.session.refresh(bug_to_update)
        return bug_to_update

    def find_by_uuid(self, uuid: UUID):
        query = select(Bug).where(Bug.uuid == uuid)
        return self.session.exec(query).one()

    def find_all(self):
        query = select(Bug)
        return self.session.exec(query).all()

    def delete(self, uuid: UUID):
        try:
            bug_to_delete = self.find_by_uuid(uuid)
            self.session.delete(bug_to_delete)
            self.session.commit()
        except Exception as e:
            pass
