from sqlalchemy import Column, Integer, String, Date, ForeignKey 
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

    
    
class Tournament(Base):
    __tablename__ = 'dim_tournaments'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(255))
    location = Column(Integer, ForeignKey('dim_countries.id'))
    surface = Column(Integer, ForeignKey('dim_surfaces.id'))


    winning_price = Column(Integer())
    date = Column(Date)
    
    
class Surface(Base):
    __tablename__ = 'dim_surfaces'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
  
    # relationships
    tournaments = relationship('Tournament', backref='dim_tournaments')

    
class Player(Base):
    __tablename__ = 'dim_players'
    
    id = Column(Integer, primary_key=True)
    complete_name = Column(String(255))
    nationality = Column(Integer, ForeignKey('dim_countries.id'))
    
    
class Country(Base):
    __tablename__ = 'dim_countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    # relationships
    players = relationship('Player', backref='dim_players')
    tournaments = relationship('Tournament', backref='dim_tournaments')
    
    
