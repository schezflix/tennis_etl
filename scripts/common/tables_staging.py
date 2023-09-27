from sqlalchemy import Column, Integer, String, Date, Float, Boolean
from sqlalchemy.orm import relationship

from common.base import Base

class Match(Base):
    __tablename__ = 'matches'
    
    id = Column(Integer, primary_key=True, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    location = Column(String)
    court_surface = Column(String)
    prize_money = Column(Integer)
    currency = Column(Integer)
    year = Column(Integer)
    player_name = Column(String)
    opponent_name = Column(String)
    tournament = Column(String)
    tourney_round = Column(String)
    num_sets = Column(String)
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
    duration = Column(String)
    player_victory = Column(String)
    retirement = Column(String)
    seed = Column(Integer)
    won_first_set = Column(String)
    doubles = Column(String)
    masters = Column(Integer)
    round_num = Column(Integer)
    nation = Column(Integer)
    
    

class Round(Base): 
    __tablename__ = 'rounds'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    ronda = Column(String(55))    
    
    
class Tournament(Base): 
    __tablename__ = 'tournaments'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String)
    location = Column(Integer, nullable=True)
    surface = Column(Integer, nullable=True)
    winning_prize = Column(Integer, nullable=True)
    category = Column(String, nullable=True)


class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String)
    code = Column(String)
    region_ = Column(String)
    sub_region = Column(String)
  
    
class Surface(Base): # owner
    __tablename__ = 'surfaces'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(255))

    
class Currency(Base):
    __tablename__ = 'currencies'
    
    id = Column(Integer, primary_key=True, nullable=False)
    
    name = Column(String(55), nullable=True)

class Player(Base):
    __tablename__ = 'players'
    
    id = Column(Integer, primary_key=True)
    
    complete_name = Column(String)
    nationality = Column(String, nullable=True)
