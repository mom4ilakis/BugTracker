import os
from datetime import datetime, timedelta, timezone

import jwt
from dotenv import load_dotenv

from models import User

load_dotenv()

ACCESS_TOKEN_EX = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EX = int(os.environ.get("REFRESH_TOKEN_EXPIRE_MINUTES"))
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")
JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM")


def encode_jwt(to_encode: dict):
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)


def create_access_token(user: User, expires_delta: int | None = ACCESS_TOKEN_EX):
    to_encode = {
        "sub": str(user.uuid),
        "scopes": ["bugs:write", "me:write"],
        "issuer": "bugtracker",
        "audiences": "bugtracker-api",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    }
    return encode_jwt(to_encode)


def create_refresh_token(user: User, expires_delta: int | None = REFRESH_TOKEN_EX):
    to_encode = {
        "sub": str(user.uuid),
        "issuer": "bugtracker",
        "audiences": "bugtracker-api",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    }
    return encode_jwt(to_encode)


def create_token_pair(user: User):
    access_token = create_access_token(user)
    refresh_token = create_refresh_token(user)
    return access_token, refresh_token


def decode_jwt(token: str):
    payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    return payload
