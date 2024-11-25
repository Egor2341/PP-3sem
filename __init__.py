from db.users import User
from db.tours import Tour
from db.bookings import Booking
from db.reviews import Review

from db.database import Base, engine
def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)