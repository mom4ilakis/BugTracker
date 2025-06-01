from unittest.mock import patch, Mock

import pytest
from sqlmodel import Session, SQLModel, create_engine

from models import User
from security import hash_password
from services import AuthenticationService


@pytest.fixture(name="session")
def session_fixture():
    return Mock(Session)


@pytest.fixture
def auth_service(session):
    return AuthenticationService(session)


class TestAuthenticationService:
    def test_authenticate_success(self, auth_service, session):
        session.exec.return_value.one.return_value = User(username="testuser", password=hash_password("testpassword"))
        access_token, refresh_token = auth_service.authenticate_user("testuser", "testpassword")
        assert isinstance(access_token, str)
        assert isinstance(refresh_token, str)
