from db.database import session_factory
from db.tours import Tour
from _decimal import Decimal


def get_tour_by_title(title: str):
    with session_factory() as session:
        return session.query(Tour).filter_by(title=title).first()


def get_tours():
    with session_factory() as session:
        return session.query(Tour).all()


def get_tour_review(title: str):
    with session_factory() as session:
        return session.query(Tour).filter_by(title=title).first().review


def update_tour(title: str, update_data: dict):
    with session_factory() as session:
        session.query(Tour).filter_by(title=title).update(update_data)
        session.commit()


def delete_tour(title: str):
    with session_factory() as session:
        tour = session.query(Tour).filter_by(title=title).one()
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
