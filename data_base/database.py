import datetime
from typing import Annotated

from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from sqlalchemy import create_engine, String, text, Integer, DateTime
from config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    pool_pre_ping=True
)

session_factory = sessionmaker(engine)

intpk = Annotated[int, mapped_column(primary_key=True)]
str_45 = Annotated[str, 45]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())",
                                                                            onupdate=datetime.datetime.utcnow))]
str_64 = Annotated[str, 64]



class Base(DeclarativeBase):
    type_annotation_map = {
        str_45: String(45),
        str_64: String(64),
        intpk: Integer,
        created_at: DateTime,
        updated_at: DateTime
    }
