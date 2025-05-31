import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine
from sqlmodel import SQLModel, Session

load_dotenv()

ENGINE : Engine | None  = None

def setup_engine():
    global ENGINE
    user = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    db = os.environ.get("DB_NAME")

    if not user or not password or not db:
        raise RuntimeError("DB credentials were not provided!")

    connection_string = f"mysql+pymysql://{user}:{password}@localhost:3306/{db}"

    ENGINE = create_engine(connection_string, echo="DEBUG" in os.environ)

def create_tables():
    from models import User
    SQLModel.metadata.create_all(ENGINE)


def get_session():
    with Session(ENGINE) as session:
        yield session


if __name__ == '__main__':
    setup_engine()
    create_tables()
