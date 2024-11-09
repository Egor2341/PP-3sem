import datetime

from data_base.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, Text, String
from decimal import Decimal


class Tours(Base):
    __tablename__ = "tours"

    title: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(7, 2))
    duration: Mapped[int]
    start: Mapped[datetime.datetime]
    end: Mapped[datetime.datetime]
    destination: Mapped[str] = mapped_column(String(64))
    availability: Mapped[int]
    booking: Mapped["Bookings"] = relationship("Bookings", uselist=False, back_populates="tour")
    review: Mapped["Reviews"] = relationship("Reviews", uselist=False, back_populates="tour")
