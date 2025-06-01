from typing import Annotated
from uuid import UUID

from fastapi import Depends
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from security import hash_password
from constants import UserExistsException
from db import get_session
from models import User


class UserService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def find_by_uuid(self, uuid: UUID):
        query = select(User).where(User.uuid == uuid)
        return self.session.exec(query).one()

    def find_by_email(self, email):
        query = select(User).where(User.email == email)
        return self.session.exec(query).one()

    def create_new_user(self, username: str, password: str, email: str):
        try:
            hashed_password = hash_password(password)
            user = User(username=username, password=hashed_password, email=email, is_active=True, is_superuser=False,
                        is_verified=False)
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
            return user
        except IntegrityError as e:
            self.session.rollback()
            raise UserExistsException("User already exists") from e
        except Exception as e:
            self.session.rollback()
            raise e


UserServiceDep = Annotated[UserService, Depends()]
