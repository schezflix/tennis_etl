from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


username = 'postgres'
password = 'elunoalseis'
host = 'localhost'
port = '5432'
database = 'schezflix'

# initialize engine
engine = create_engine( f'postgresql://{username}:{password}@{host}:{port}/{database}')


# initialize the session

Session = sessionmaker(bind=engine)
session = Session()

# initialize the declarative base
Base = declarative_base()
