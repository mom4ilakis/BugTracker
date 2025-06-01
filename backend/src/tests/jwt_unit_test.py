import os
import uuid

import pytest

from models import User
from security import jwt


def assert_access_token_valid(token: str, sub: str):
    assert isinstance(token, str)
    decoded_token = jwt.decode_jwt(token)

    assert decoded_token["sub"] == sub
    assert decoded_token["scopes"] == ["bugs:write", "bugs:read", "me"]
    assert decoded_token["issuer"] == "bugtracker"
    assert decoded_token["audiences"] == "bugtracker-api"
    assert isinstance(decoded_token["exp"], int)


def assert_refresh_token_valid(token: str, sub: str):
    assert isinstance(token, str)
    decoded_token = jwt.decode_jwt(token)

    assert decoded_token["sub"] == sub
    assert decoded_token["issuer"] == "bugtracker"
    assert decoded_token["audiences"] == "bugtracker-api"
    assert isinstance(decoded_token["exp"], int)


@pytest.fixture()
def test_user():
    return User(uuid=uuid.uuid4(), username="testuser", email="testmail@mail.test", password="testpassword")


@pytest.fixture(autouse=True)
def setup_env():
    os.environ["JWT_SECRET_KEY"] = "testsecretkey"
    os.environ["JWT_ALGORITHM"] = "HS256"
    os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"] = "15"
    os.environ["REFRESH_TOKEN_EXPIRE_MINUTES"] = "60"


def test_create_access_token_return(test_user):
    token = jwt.create_access_token(test_user)
    assert_access_token_valid(token, str(test_user.uuid))


def test_create_refresh_token_return(test_user):
    token = jwt.create_refresh_token(test_user)
    assert_refresh_token_valid(token, str(test_user.uuid))


def test_create_token_pair_return(test_user):
    access_token, refresh_token = jwt.create_token_pair(test_user)
    assert_access_token_valid(access_token, str(test_user.uuid))
    assert_refresh_token_valid(refresh_token, str(test_user.uuid))


