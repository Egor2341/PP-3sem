from db.database import Base, intpk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric, String
from decimal import Decimal


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[intpk]
    number_of_people: Mapped[int]
    total_price: Mapped[Decimal] = mapped_column(Numeric(9, 2))
    status: Mapped[String] = mapped_column(String(9))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    user: Mapped["User"] = relationship(back_populates="booking")
    tour: Mapped["Tour"] = relationship(back_populates="booking")


from db.tours import Tour
from db.users import User
