import datetime

from base_model import BaseModel
from database import str_64
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric
from decimal import Decimal
from bookings import Bookings
from reviews import Reviews


class Tours(BaseModel):
    __tablename__ = "tours"

    title: Mapped[str_64]
    description: Mapped[str]
    price: Mapped[Decimal] = mapped_column(Numeric(7, 2))
    duration: Mapped[int]
    start: Mapped[datetime.datetime]
    end: Mapped[datetime.datetime]
    destination: Mapped[str_64]
    availability: Mapped[int]
    booking: Mapped[Bookings] = relationship("Bookings", uselist=False, back_populates="tour")
    review: Mapped[Reviews] = relationship("Reviews", uselist=False, back_populates="tour")
