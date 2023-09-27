from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship

from common.base import Base
# from base import Base

# from .base import Base


class Match(Base):
    __tablename__ = 'fact_matches'

    id = Column(Integer, primary_key=True)
    
    _start_date = Column(Date)
    _end_date = Column(Date)
    
    # foreign keys
    location_id = Column(Integer, ForeignKey('dim_countries.id'))
    surface_id = Column(Integer, ForeignKey('dim_surfaces.id'))
    currency_id = Column(Integer, ForeignKey('dim_currencies.id'))
    player_id = Column(Integer, ForeignKey('dim_players.id'))
    opponent_id = Column(Integer, ForeignKey('dim_players.id'))
    tournament_id = Column(Integer, ForeignKey('dim_tournaments.id'))
    # rondas_id = Column(Integer, ForeignKey('dim_rounds.id'))
  
    prize_money = Column(Integer)
    year = Column(Integer)
    num_sets = Column(Integer)
    sets_won = Column(Integer)
    games_won = Column(Integer)
    games_against = Column(Integer)
    tiebreaks_won = Column(Integer)
    tiebreaks_total = Column(Integer)
    serve_rating = Column(Float)
    aces = Column(Integer)
    double_faults = Column(Integer)
    first_serve_made = Column(Integer)
    first_serve_attempted = Column(Integer)
    first_serve_points_made = Column(Integer)
    first_serve_points_attempted = Column(Integer)
    second_serve_points_made = Column(Integer)
    second_serve_points_attempted = Column(Integer)
    break_points_saved = Column(Integer)
    break_points_against = Column(Integer)
    service_games_won = Column(Integer)
    return_rating = Column(Float)
    first_serve_return_points_made = Column(Integer)
    first_serve_return_points_attempted = Column(Integer)
    second_serve_return_points_made = Column(Integer)
    second_serve_return_points_attempted = Column(Integer)
    break_points_made = Column(Integer)
    break_points_attempted = Column(Integer)
    return_games_played = Column(Integer)
    service_points_won = Column(Integer)
    service_points_attempted = Column(Integer)
    return_points_won = Column(Integer)
    return_points_attempted = Column(Integer)
    total_points_won = Column(Integer)
    total_points = Column(Integer)
    duration = Column(Integer)
    player_victory = Column(Boolean)
    retirement = Column(Boolean)
    seed = Column(Integer)
    won_first_set = Column(Boolean)
    doubles = Column(String)
    masters = Column(Integer, ForeignKey('dim_tournaments.id'))
    round_num = Column(Integer)
    nation = Column(Integer, ForeignKey('dim_countries.id'))
    
    
    # relationships
    # rondas = relationship('Round', back_populates='matches', primaryjoin='Match.rondas_id == Round.id')
    # tournament = relationship('Tournament', primaryjoin='Match.tournament_id == Tournament.id', back_populates='matches')
    tournament = relationship('Tournament', back_populates='matches')

    country = relationship('Country', back_populates='matches', primaryjoin='Match.location_id == Country.id')
    surface = relationship('Surface', back_populates='matches', primaryjoin='Match.surface_id == Surface.id')
    currency = relationship('Currency', back_populates='matches', primaryjoin='Match.currency_id == Currency.id')
    players = relationship('Player', back_populates='matches',primaryjoin='Match.player_id == Player.id', foreign_keys=[player_id])
    opponents = relationship('Player', foreign_keys=[opponent_id])


class Round(Base): 
    __tablename__ = 'dim_rounds'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    ronda = Column(String(55))    
    
    # relationships
    matches = relationship('Match', back_populates='round')

    
class Tournament(Base): # pets
    __tablename__ = 'dim_tournaments'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(255))
    category = Column(String(255))
    location_id = Column(Integer, ForeignKey('dim_countries.id'))
    surface_id = Column(Integer, ForeignKey('dim_surfaces.id'))
    winning_prize = Column(Integer, nullable=True)
    currency_id = Column(Integer, ForeignKey('dim_currencies.id'))
        
    # relationships
    countries = relationship('Country') # , back_populates='tournament')
    surfaces = relationship('Surface') #, back_populates='tournament')
    matches = relationship('Match') #, back_populates='tournament')  
    currency = relationship('Currency') #, back_populates='tournament')  


    # time_dimension  = relationship("TimeDimension", back_populates="dim_tournaments")

class Country(Base):
    __tablename__ = 'dim_countries'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(255))
    code = Column(String())
    region_ = Column(String(255))
    sub_region = Column(String(255))

    
    # relationships
    tournaments = relationship('Tournament', back_populates='country')  
    players = relationship('Player', back_populates='country')
    matches = relationship('Match', back_populates='country')  
    
    # matches = relationship('Match', backref='country')
  
    
class Surface(Base): # owner
    __tablename__ = 'dim_surfaces'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(255))
  
    # relationships
    tournaments = relationship('Tournament', back_populates='surface')  
    matches = relationship('Match', back_populates='surface')  

    
class Currency(Base):
    __tablename__ = 'dim_currencies'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(55), nullable=True)

    # relationships
    tournaments = relationship('Tournament', back_populates='currency')
    matches = relationship('Match', back_populates='currency')  


class Player(Base):
    __tablename__ = 'dim_players'
    
    id = Column(Integer, primary_key=True)
    
    complete_name = Column(String(255))
    nationality_id = Column(Integer, ForeignKey('dim_countries.id'))

    # relationships
    matches = relationship('Match', back_populates='player')  

    
    
    
# class TimeDimension(Base):
#     __tablename__ = 'dim_date'
    
#     id = Column(Integer, primary_key=True)
#     date = Column(DateTime, unique=True)
#     year = Column(Integer)
#     month = Column(Integer)
#     day = Column(Integer)
#     day_of_week = Column(Integer)
#     quarter = Column(Integer)
#     is_weekend = Column(Integer)
#     # duration_minutes = Column(Integer)
    
#     # relationships
#     matches = relationship('Matches', primaryjoin='TimeDimension.id == Match.time_dimension_id')

#     matches = relationship("Match", back_populates='dim_date')
    
    
    
 
    
