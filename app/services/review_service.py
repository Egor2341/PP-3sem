from db.database import session_factory
from db.reviews import Review
from db.users import User
from db.tours import Tour


def new_review(data: dict):
    with session_factory() as session:
        session.add(Review(**data))
        session.commit()


def get_user_reviews(id: int):
    with session_factory() as session:
        return session.query(User).get(id).review


def update_review(old_comment: str, data: dict):
    with session_factory() as session:
        session.query(Review).filter_by(comment=old_comment).update(data)
        session.commit()


def delete_review(id: int):
    with session_factory() as session:
        review = session.query(Review).get(id)
        session.delete(review)
        session.commit()
