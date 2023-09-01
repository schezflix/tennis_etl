from base import Base, engine
from tables import Player, Match, Tournament, Country, Surface, TimeDimension, Round, Currency


if __name__ == "__main__":
    Base.metadata.create_all(engine, tables =[Player.__tablename__,
                                               Match.__tablename__,
                                               Tournament.__tablename__,
                                               Country.__tablename__,
                                               Surface.__tablename__,
                                               TimeDimension.__tablename__,
                                               Round.__tablename__,
                                               Currency.__tablename__])