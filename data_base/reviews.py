from data_base.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric


class Reviews(Base):
    __tablename__ = "reviews"


    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped["Users"] = relationship("Users", back_populates="review")
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    tour: Mapped["Tours"] = relationship("Tours", back_populates="review")
    rating: Mapped[int]
    comment: Mapped[str]
