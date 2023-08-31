from sqlalchemy import Column, Integer, String, DateTime, ForeignKey 
from sqlalchemy.orm import relationship
from base import Base


class Match(Base):
    __tablename__ = 'fact_matches'
    
    id = Column(Integer, primary_key=True, nullable=False)    
    tournament_id = Column(Integer, ForeignKey('dim_tournaments.id'))
    winner_id = Column(Integer, ForeignKey('dim_players.id'))
    looser_id = Column(Integer, ForeignKey('dim_players.id'))
    
    # relationships
    players = relationship("Player", backref="fact_matches")
    tournaments = relationship("Tournament", backref="fact_matches")
    time_dimension  = relationship("TimeDimension", back_populates="matches")

    
class Tournament(Base): # pets
    __tablename__ = 'dim_tournaments'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255))
    category = Column(String(255))
    location_id = Column(Integer, ForeignKey('dim_countries.id'))
    surface_id = Column(Integer, ForeignKey('dim_surfaces.id'))


    winning_prize = Column(Integer(), nullable=True)
    date = Column(DateTime(), nullable=False)
    
    
class Surface(Base): # owner
    __tablename__ = 'dim_surfaces'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255))
  
    # relationships
    tournaments = relationship('Tournament', backref='dim_tournaments')

    
class Player(Base):
    __tablename__ = 'dim_players'
    
    id = Column(Integer, primary_key=True)
    complete_name = Column(String(255))
    nationality_id = Column(Integer, ForeignKey('dim_countries.id'))
    
    
class Country(Base):
    __tablename__ = 'dim_countries'
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255))
    region = Column(String(255))
    sub_region = Column(String(255))

    # relationships
    players = relationship('Player', backref='dim_players')
    tournaments = relationship('Tournament', backref='dim_tournaments')
    
    
class TimeDimension(Base):
    __tablename__ = 'dim_date'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, unique=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    day_of_week = Column(Integer)
    quarter = Column(Integer)
    is_weekend = Column(Integer)
    
    # relationships
    matches = relationship("Matches", back_populates="time_dimension")

    
