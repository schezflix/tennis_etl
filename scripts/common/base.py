from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base


username = 'postgres'
password = 'elunoalseis'
host = 'localhost'
port = '5432'
database = 'schezflix'

# Construct the PostgreSQL URL
postgresql_url = f'postgresql://{username}:{password}@{host}:{port}/{database}'

# initialize engine
engine = create_engine(postgresql_url)


# initialize the session
session = Session(engine)


# initialize the declarative base
Base = declarative_base()