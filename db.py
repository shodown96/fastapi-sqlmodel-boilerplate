from typing import Annotated

from config import settings
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine(settings.SQLITE_URL, connect_args=settings.CONNECT_ARGS)

def create_db_and_tables():
    print("Creating DB")
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
