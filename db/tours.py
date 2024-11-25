import datetime

from db.database import Base, intpk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Numeric, Text, String
from decimal import Decimal


class Tour(Base):
    __tablename__ = "tours"

    id: Mapped[intpk]
    title: Mapped[str] = mapped_column(String(64), unique=True)
    description: Mapped[str] = mapped_column(Text)
    price: Mapped[Decimal] = mapped_column(Numeric(8, 2))
    duration: Mapped[int]
    start: Mapped[datetime.datetime]
    end: Mapped[datetime.datetime]
    destination: Mapped[str] = mapped_column(String(64))
    availability: Mapped[int]
    booking: Mapped["Booking"] = relationship(uselist=False, back_populates="tour")
    review: Mapped["Review"] = relationship(uselist=False, back_populates="tour")

from db.bookings import Booking
from db.reviews import Review
