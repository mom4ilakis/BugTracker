from typing import Annotated

from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer, SecurityScopes
from sqlmodel import Session

from db import get_session
from dto import CurrentUser
from security import decode_jwt

SessionDep = Annotated[Session, Depends(get_session)]
PasswordRequestFormDep = Annotated[OAuth2PasswordRequestForm, Depends()]

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login",
    scopes={"me": "Read information about the current user.",
            "bugs:read": "Read bug data.",
            "bugs:write": "Create and update bug data."
            }
)


def get_current_user(scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    not_enough_permissions_exception = HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Forbidden, not enough permissions",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decode_jwt(token)
        if not payload:
            raise credentials_exception
        user = CurrentUser(uuid=payload["sub"], id=payload["id"], scopes=payload["scopes"])

        for scope in scopes.scopes:
            if scope not in user.scopes:
                raise not_enough_permissions_exception

        return user

    except (InvalidTokenError, ExpiredSignatureError):
        raise credentials_exception
