from data_base.database import Base, engine
from data_base.users import Users
from data_base.tours import Tours
from data_base.bookings import Bookings
from data_base.reviews import Reviews

def create_tables():
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

