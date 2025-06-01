import pytest
from uuid import UUID, uuid4
from sqlmodel import Session, SQLModel, create_engine

from constants import Priority, Status, FilterParams
from services import BugService, UserService


# Fixtures
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


@pytest.fixture
def bug_service(user_service, session):
    return BugService(user_service, session)


# Test data
TEST_USER = {
    "username": "reporter",
    "password": "password123",
    "email": "reporter@example.com"
}

TEST_ASSIGNEE = {
    "username": "assignee",
    "password": "password456",
    "email": "assignee@example.com"
}


class TestBugService:
    def test_create_new_bug_with_assignee(self, bug_service, user_service):
        # Setup users
        reporter = user_service.create_new_user(**TEST_USER)
        assignee = user_service.create_new_user(**TEST_ASSIGNEE)

        # Create bug
        bug = bug_service.create_new_bug(
            title="Critical Bug",
            reporter_uuid=reporter.uuid,
            assignee_uuid=assignee.uuid,
            optional_props={"priority": Priority.HIGH}
        )

        assert isinstance(bug.uuid, UUID)
        assert bug.title == "Critical Bug"
        assert bug.priority == Priority.HIGH
        assert bug.reported_by == reporter.id
        assert bug.assigned_to == assignee.id

    def test_create_bug_without_assignee(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        bug = bug_service.create_new_bug(
            title="Minor Issue",
            reporter_uuid=reporter.uuid
        )

        assert bug.assigned_to is None
        assert bug.reported_by == reporter.id

    def test_update_bug_properties(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        assignee = user_service.create_new_user(**TEST_ASSIGNEE)
        bug = bug_service.create_new_bug("Initial Title", reporter.uuid)

        updated_bug = bug_service.update_bug(bug.uuid, {"title": "Updated Title", "status": Status.DONE, "assigned_to": assignee.uuid})

        assert updated_bug.title == "Updated Title"
        assert updated_bug.status == Status.DONE

    def test_find_by_uuid(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        created_bug = bug_service.create_new_bug("Findable Bug", reporter.uuid)

        found_bug = bug_service.find_by_uuid(created_bug.uuid)

        assert found_bug == created_bug

    def test_find_all_with_filters(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        bug1 = bug_service.create_new_bug("Bug 1", reporter.uuid, optional_props={"status": Status.NEW})
        bug_service.create_new_bug("Bug 2", reporter.uuid, optional_props={"status": Status.CLOSED})

        open_bugs = bug_service.find_all(filters=FilterParams(status=Status.NEW))
        assert len(open_bugs) == 1
        assert open_bugs[0].uuid == bug1.uuid

    def test_delete_bug(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        bug = bug_service.create_new_bug("To Delete", reporter.uuid)

        bug_service.delete(bug.uuid)

        with pytest.raises(Exception):
            bug_service.find_by_uuid(bug.uuid)

    def test_delete_wont_raise(self, bug_service):
        bug_service.delete(uuid4())


class TestErrorHandling:
    def test_invalid_reporter_uuid(self, bug_service):
        with pytest.raises(Exception):
            bug_service.create_new_bug("Test", uuid4())

    def test_invalid_assignee_uuid(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        with pytest.raises(Exception):
            bug_service.create_new_bug("Test", reporter.uuid, assignee_uuid=uuid4())

    def test_invalid_assignee_update(self, bug_service, user_service):
        reporter = user_service.create_new_user(**TEST_USER)
        bug = bug_service.create_new_bug("Test", reporter.uuid)
        with pytest.raises(Exception):
            bug_service.update_bug(bug.uuid, {"assigned_to": uuid4()})
