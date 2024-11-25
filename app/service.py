from pydantic import EmailStr

from db.database import session_factory
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


def get_tours():
    with session_factory() as session:
        return session.query(Tour).all()
