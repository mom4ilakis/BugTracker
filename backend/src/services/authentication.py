from typing import Annotated

from fastapi import Depends
from sqlmodel import select, Session

from db import get_session
from models import User
from security import create_token_pair, verify_password
from constants import CredentialsException


class AuthenticationService:

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def authenticate_user(self, username: str, password: str):
        query = select(User).where(User.username == username)
        user = self.session.exec(query).one()

        if not user or not verify_password(password, user.password):
            raise CredentialsException("Invalid credentials")

        return create_token_pair(user)


AuthServiceDep = Annotated[AuthenticationService, Depends()]
