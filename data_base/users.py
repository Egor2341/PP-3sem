import enum
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from data_base.database import Base


class Role(enum.Enum):
    client = "client"
    admin = "admin"


class Users(Base):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(45))
    surname: Mapped[str] = mapped_column(String(45))
    email: Mapped[String] = mapped_column(String(256), unique=True)
    password: Mapped[String] = mapped_column(String(32))
    role: Mapped[Role]
    booking: Mapped[list["Bookings"]] = relationship("Bookings", back_populates="user", cascade="all, delete")
    review: Mapped[list["Reviews"]] = relationship("Reviews", back_populates="user", cascade="all, delete")
