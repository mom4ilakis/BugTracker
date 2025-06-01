import os
import pytest
from unittest.mock import patch
from sqlalchemy import Engine
from sqlmodel import Session, create_engine

from db import setup_engine, get_session

# Mock environment variables for testing
@pytest.fixture
def mock_env_vars():
    with patch.dict(os.environ, {
        "DB_USER": "testuser",
        "DB_PASSWORD": "testpass",
        "DB_NAME": "testdb"
    }):
        yield

# Use an in-memory SQLite database for testing
@pytest.fixture
def test_engine(mock_env_vars):
    with patch('db.create_engine') as mock_create_engine:
        mock_engine = create_engine("sqlite:///:memory:", echo=False)
        mock_create_engine.return_value = mock_engine
        setup_engine()
        yield mock_engine

def test_setup_engine_success():
    with patch('db.create_engine') as mock_create_engine:
        mock_engine = create_engine("sqlite:///:memory:", echo=False)
        mock_create_engine.return_value = mock_engine
        engine = setup_engine()
        assert engine is not None
        assert isinstance(engine, Engine)

def test_setup_engine_missing_credentials():
    with patch.dict(os.environ, {}, clear=True):
        with pytest.raises(RuntimeError):
            setup_engine()

def test_get_session(test_engine):
    session_gen = get_session()
    session = next(session_gen)
    assert isinstance(session, Session)
    session.close()
