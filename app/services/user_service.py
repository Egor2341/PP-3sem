from db.database import session_factory
from db.users import User
from pydantic import EmailStr


def get_user_by_email(email: EmailStr):
    with session_factory() as session:
        return session.query(User).filter_by(email=email).first()


def get_users(user_id: int):
    with session_factory() as session:
        return session.query(User.name, User.surname, User.email).filter(User.id != user_id).all()


def delete_user(email: EmailStr):
    with session_factory() as session:
        user = session.query(User).filter_by(email=email).first()
        session.delete(user)
        session.commit()
