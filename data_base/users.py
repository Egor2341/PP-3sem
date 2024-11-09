import enum

from sqlalchemy import String
from base_model import BaseModel
from reviews import Reviews
from database import str_45
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bookings import Bookings


class Role(enum.Enum):
    client = "client"
    admin = "admin"


class Users(BaseModel):
    __tablename__ = "users"

    name: Mapped[str_45]
    surname: Mapped[str_45]
    email: Mapped[String] = mapped_column(String(256), unique=True)
    password: Mapped[String] = mapped_column(String(32))
    role: Mapped[Role]
    booking: Mapped[Bookings] = relationship("Bookings", back_populates="user", cascade="all, delete")
    review: Mapped[Reviews] = relationship("Reviews", back_populates="user", cascade="all, delete")
