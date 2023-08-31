from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from base import Base


class Match(Base):
    __tablename__ = 'fact_matches'
    
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    prize_money = Column(Float)
    year = Column(Integer)
    tournament_id = Column(Integer, ForeignKey('dim_tournaments.id'))
    player_id = Column(Integer, ForeignKey('dim_players.id'))
    opponent_id = Column(Integer, ForeignKey('dim_players.id'))
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
    won_first_set = Column(Boolean)
    
    # relationships
    players = relationship("Player", backref="fact_matches")
    tournaments = relationship("Tournament", backref="fact_matches")
    time_dimension  = relationship("TimeDimension", back_populates="matches")

class Round(Base): 
    __tablename__ = 'dim_rounds'
    
    id = Column(Integer, primary_key=True, nullable=False)
    ronda = Column(String(55))

    
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

    
