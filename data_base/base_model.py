from database import Base, intpk, created_at, updated_at
from sqlalchemy.orm import Mapped


class BaseModel(Base):
    __abstract__ = True

    id: Mapped[intpk]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
