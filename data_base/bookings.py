import enum

from data_base.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric
from decimal import Decimal


class Status(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"


class Bookings(Base):
    __tablename__ = "bookings"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["Users"] = relationship("Users", back_populates="booking")
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    tour: Mapped["Tours"] = relationship("Tours", back_populates="booking")
    number_of_people: Mapped[int]
    total_price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    status: Mapped[Status]

