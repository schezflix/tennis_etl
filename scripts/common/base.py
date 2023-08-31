from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base


# initialize engine
engine = create_engine('postgresql://localhost/schezflix')


# initialize the session
session = Session(engine)


# initialize the declarative base
Base = declarative_base()