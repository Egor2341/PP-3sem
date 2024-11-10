from data_base.database import Base, engine
import data_base.all_models

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

