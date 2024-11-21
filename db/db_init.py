from db.database import Base, engine
import __init__
def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

