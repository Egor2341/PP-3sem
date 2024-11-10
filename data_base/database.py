import datetime
from typing import Annotated

from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped
from sqlalchemy import create_engine, text, Integer
from app.config import get_db_url

engine = create_engine(
    url=get_db_url(),
    pool_pre_ping=True,
    echo=True,

)

session_factory = sessionmaker(engine)

created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"),
                                                        onupdate=datetime.datetime.utcnow)]


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime.datetime]
