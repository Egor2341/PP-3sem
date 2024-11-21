from db.database import Base, intpk
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer


class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[intpk]
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="review")
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    tour: Mapped["Tour"] = relationship(back_populates="review")
    rating: Mapped[int]
    comment: Mapped[str]


from db.users import User
from db.tours import Tour
