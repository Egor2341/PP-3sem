import enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.database import Base, intpk





class User(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(String(45))
    surname: Mapped[str] = mapped_column(String(45))
    email: Mapped[String] = mapped_column(String(256), unique=True)
    password: Mapped[String] = mapped_column(String(128))
    role: Mapped[String] = mapped_column(String(10))
    booking: Mapped[list["Booking"]] = relationship(back_populates="user", cascade="all, delete")
    review: Mapped[list["Review"]] = relationship(back_populates="user", cascade="all, delete")

from db.bookings import Booking
from db.reviews import Review
