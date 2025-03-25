from db.database import session_factory
from db.bookings import Booking
from db.users import User
from db.tours import Tour
from db.reviews import Review


def get_by_id(model: [User | Tour | Booking | Review], id: int):
    with session_factory() as session:
        return session.get(User, id)


def add_new_row(model: [User | Tour], data: dict):
    with session_factory() as session:
        session.add(model(**data))
        session.commit()


def get_all(model: [Tour | User | Booking | Review]):
    with session_factory() as session:
        return session.query(model).all()
