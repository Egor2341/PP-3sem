from data_base.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from all_models import User, Tour


class Review(Base):
    __tablename__ = "reviews"

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="review")
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    tour: Mapped["Tour"] = relationship(back_populates="review")
    rating: Mapped[int]
    comment: Mapped[str]
