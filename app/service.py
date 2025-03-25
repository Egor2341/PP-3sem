from _decimal import Decimal
from pydantic import EmailStr

from db.bookings import Booking
from db.database import session_factory
from db.reviews import Review
from db.users import User
from db.tours import Tour




def get_user_by_id(id: int):
    with session_factory() as session:
        return session.query(User).get(id)


def get_user_by_email(email: EmailStr):
    with session_factory() as session:
        return session.query(User).filter_by(email=email).first()


def add_new_user(data: dict):
    with session_factory() as session:
        session.add(User(**data))
        session.commit()


def get_users(user_id: int):
    with session_factory() as session:
        return session.query(User.name, User.surname, User.email).filter(User.id != user_id).all()


def delete_user(email: EmailStr):
    with session_factory() as session:
        user = session.query(User).filter_by(email=email).first()
        session.delete(user)
        session.commit()


def get_tour_by_title(title: str):
    with session_factory() as session:
        return session.query(Tour).filter_by(title=title).first()


def add_new_tour(data: dict):
    with session_factory() as session:
        session.add(Tour(**data))
        session.commit()


def get_tour_by_id(id: int):
    with session_factory() as session:
        return session.query(Tour).get(id)


def get_tours():
    with session_factory() as session:
        return session.query(Tour).all()


def update_tour(title: str, update_data: dict):
    with session_factory() as session:
        session.query(Tour).filter_by(title=title).update(update_data)
        session.commit()


def delete_tour(title: str):
    with session_factory() as session:
        tour = session.query(Tour).filter_by(title=title).first()
        session.delete(tour)
        session.commit()


def get_filtered_tours(title: str, price: Decimal, duration: int, destination: str, number_of_peoples: int):
    with session_factory() as session:
        tours = session.query(Tour)
        if title is not None:
            tours = tours.filter(Tour.title.like(title.lower()))
        if price is not None:
            tours = tours.filter(Tour.price <= price)
        if duration is not None:
            tours = tours.filter_by(duration=duration)
        if destination is not None:
            tours = tours.filter_by(destination=destination.lower())
        if number_of_peoples is not None:
            tours = tours.filter(Tour.availability >= number_of_peoples)
        return tours.all()


def add_booking(data: dict):
    with session_factory() as session:
        tour = session.query(Tour).get(data["tour_id"])
        tour.availability -= data["number_of_people"]
        session.add(tour)
        session.add(Booking(**data))
        session.commit()


def get_all_bookings():
    with session_factory() as session:
        return session.query(Booking).all()


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


def new_review(data: dict):
    with session_factory() as session:
        session.add(Review(**data))
        session.commit()


def get_all_reviews():
    with session_factory() as session:
        return session.query(Review).all()


def get_user_reviews(id: int):
    with session_factory() as session:
        return session.query(User).get(id).review


def get_tour_review(title: str):
    with session_factory() as session:
        return session.query(Tour).filter_by(title=title).first().review


def update_review(old_comment: str, data: dict):
    with session_factory() as session:
        session.query(Review).filter_by(comment=old_comment).update(data)
        session.commit()


def delete_review(id: int):
    with session_factory() as session:
        review = session.query(Review).get(id)
        session.delete(review)
        session.commit()
