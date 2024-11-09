from base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, Numeric
from users import Users
from tours import Tours

class Reviews(BaseModel):
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped[Users] = relationship("Users", back_populates="review")
    tour_id: Mapped[int] = mapped_column(Integer, ForeignKey("tours.id"))
    tour: Mapped[Tours] = relationship("Tours", back_populates="review")
    rating: Mapped[int]
    comment: Mapped[str]
