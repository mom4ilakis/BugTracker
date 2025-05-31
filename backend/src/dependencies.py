from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from db import get_session
from services import UserService, AuthenticationService, BugService

SessionDep = Annotated[Session, Depends(get_session)]
PasswordRequestFormDep = Annotated[OAuth2PasswordRequestForm, Depends()]

UserServiceDep = Annotated[UserService, Depends()]
AuthServiceDep = Annotated[AuthenticationService, Depends()]
BugServiceDep = Annotated[BugService, Depends()]