from db.bookings import Booking
from db.database import session_factory
from db.users import User
from db.tours import Tour


def add_booking(data: dict):
    with session_factory() as session:
        tour = session.query(Tour).get(data["tour_id"])
        tour.availability -= data["number_of_people"]
        session.add(tour)
        session.add(Booking(**data))
        session.commit()


def get_user_bookings(id: int):
    with session_factory() as session:
        return session.query(User).get(id).booking


def confirmation_booking(id: int, status: str):
    with session_factory() as session:
        booking = session.query(Booking).get(id)
        booking.status = status
        session.add(booking)
        session.commit()


def update_booking(id: int, data: dict):
    with session_factory() as session:
        tour = session.query(Tour).get(data["tour_id"])
        tour.availability += data["number_of_people"]
        session.query(Booking).filter_by(id=id).update(data)
        tour.availability -= data["number_of_people"]
        session.add(tour)
        session.commit()


def delete_booking(id: int):
    with session_factory() as session:
        booking = session.query(Booking).get(id)
        tour = session.query(Tour).get(booking.tour_id)
        tour.availability += booking.number_of_people
        session.add(tour)
        session.delete(booking)
        session.commit()
