import pytest
from uuid import UUID, uuid4
from typing import Annotated
from sqlmodel import Session, SQLModel, create_engine
from services import UserService, UserServiceDep
from constants import UserExistsException
from security import verify_password

# Test database setup
@pytest.fixture(name="engine")
def engine_fixture():
    return create_engine("sqlite:///:memory:")

@pytest.fixture(name="session")
def session_fixture(engine):
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)

@pytest.fixture
def user_service(session):
    return UserService(session)

# Test data
TEST_USER = {
    "username": "testuser",
    "password": "securepassword",
    "email": "test@example.com"
}

class TestUserService:
    def test_create_new_user_success(self, user_service):
        user = user_service.create_new_user(**TEST_USER)

        assert user.uuid is not None
        assert isinstance(user.uuid, UUID)
        assert user.username == TEST_USER["username"]
        assert verify_password(TEST_USER["password"], user.password)
        assert user.email == TEST_USER["email"]
        assert user.is_active is True
        assert user.is_superuser is False
        assert user.is_verified is False

    def test_create_duplicate_user_raises_error(self, user_service):
        user_service.create_new_user(**TEST_USER)
        with pytest.raises(UserExistsException):
            user_service.create_new_user(**TEST_USER)

    def test_find_by_uuid_success(self, user_service):
        created_user = user_service.create_new_user(**TEST_USER)
        found_user = user_service.find_by_uuid(created_user.uuid)

        assert found_user == created_user

    def test_find_by_uuid_not_found(self, user_service):
        with pytest.raises(Exception):
            user_service.find_by_uuid(uuid4())

    def test_find_by_email_success(self, user_service):
        created_user = user_service.create_new_user(**TEST_USER)
        found_user = user_service.find_by_email(TEST_USER["email"])

        assert found_user == created_user

    def test_find_by_email_not_found(self, user_service):
        with pytest.raises(Exception):
            user_service.find_by_email("nonexistent@example.com")
