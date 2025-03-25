import datetime
from typing import Annotated

from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped, Session
from sqlalchemy import create_engine, text
from app.config import get_db_url

engine = create_engine(
    url=get_db_url(),
    pool_pre_ping=True,
    echo=False,
)

def session_factory():
    return Session(engine)

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.now(datetime.UTC))]


class Base(DeclarativeBase):
    __abstract__ = True

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
