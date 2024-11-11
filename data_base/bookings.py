import enum

from data_base.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric
from decimal import Decimal

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from data_base.users import User
    from data_base.tours import Tour


class Status(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"


class Booking(Base):
    __tablename__ = "bookings"

    number_of_people: Mapped[int]
    total_price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    status: Mapped[Status]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    user: Mapped["User"] = relationship(back_populates="booking")
    tour: Mapped["Tour"] = relationship(back_populates="booking")

