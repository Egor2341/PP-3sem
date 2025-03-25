import sqlalchemy

from db.users import User
from db.tours import Tour
from db.bookings import Booking
from db.reviews import Review

from db.database import Base, engine

if not sqlalchemy.inspect(engine).get_table_names():
    Base.metadata.create_all(engine)