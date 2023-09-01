from datetime import datetime
import csv, os
import pandas as pd


from common.tables import Match, Tournament, Player, Country, Surface, Round, Currency, TimeDimension
from extract import NEW_CSVS_PATH
from common.base import session
from sqlalchemy import text

from tools.transform_functions import *


def truncate_table():
    """
    Ensure that all tables are always in empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("""
            TRUNCATE TABLE fact_matches; ALTER SEQUENCE fact_matches RESTART;
            TRUNCATE TABLE dim_rounds; ALTER SEQUENCE dim_rounds RESTART;
            TRUNCATE TABLE dim_tournaments; ALTER SEQUENCE dim_tournaments RESTART;
            TRUNCATE TABLE dim_surfaces; ALTER SEQUENCE dim_surfaces RESTART;
            TRUNCATE TABLE dim_currencies; ALTER SEQUENCE dim_currencies RESTART;
            TRUNCATE TABLE dim_players; ALTER SEQUENCE dim_players RESTART;
            TRUNCATE TABLE dim_countries; ALTER SEQUENCE dim_countries RESTART;
            TRUNCATE TABLE dim_date; ALTER SEQUENCE dim_date RESTART;
             """)
    )
    session.commit()

def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """

#  T O U R N A M E N T S  D I M _ T A B L E    
    with open(f"{NEW_CSVS_PATH}/tournaments.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our tournament objects
        tournaments = []
        for row in reader:
            # Apply transformations and save as tournament object
            tournaments.append(
                Tournament(
                    name = regex_striper(row['tournament']),
                    category = int(row['masters']),
                    location_id = replace_country_codes_with_names(row['location']),
                    surface_id = regex_striper(row['court_surface']),
                    winning_prize = int(row['prize_money'])
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(tournaments)

#  P L A Y E R S  D I M _ T A B L E
    with open(f"{NEW_CSVS_PATH}/players.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        players = []
        for row in reader:
            # Apply transformations and save as players object
            players.append(
                Player(
                    name = regex_striper(row['player_id']),
                    nationality_id = replace_country_codes_with_names(row['country'])
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(players)
    
    with open(f"{NEW_CSVS_PATH}/countries.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        countries = []
        for row in reader:
            # Apply transformations and save as players object
            players.append(
                Country(
                    name = regex_striper(row['name']),
                    code = regex_striper(row['code']),
                    region = regex_striper(row['region']),
                    sub_region = regex_striper(row['sub_region'])
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(countries)
 
 #  M A T C H E S  F A C T  T A B L E    
    with open(f"{NEW_CSVS_PATH}/matches.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        matches = []
        for row in reader:
            # Apply transformations and save as players object
            players.append(
                Match(
                    start_date = date_transformation(row['start_date'])['date'],
                    end_date = date_transformation(row['start_date'])['date'],
                    location = replace_country_codes_with_names(row['location']),
                    surface = regex_striper(row['court_surface']),
                    prize_money = int(row['prize_money']),
                    currency = regex_striper(row['currency']),
                    year = date_transformation(row['year'])['year'],
                    player_id = regex_striper(row['player_id']),
                    opponent_id = regex_striper(row['opponent_id']),
                    tournament_id = regex_striper(row['tournament']),
                    t_round = regex_striper(row['round']),
                    num_sets = int(row['num_sets']),
                    sets_won = int(row['sets_won']),
                    games_won = int(row['game_won']),
                    games_against = int(row['games_against']),
                    tiebreaks_won = int(row['tiebreaks_won']),
                    tiebreaks_total = int(row['tiebreaks_total']),
                    serve_rating = int(row['serve_rating']),
                    aces = int(row['aces']),
                    double_faults = int(row['double_faults']),
                    first_serve_made = int(row['first_serve_made']),
                    first_serve_attempted = int(row['first_serve_attempted']),
                    first_serve_points_made = int(row['first_serve_points_made']),
                    first_serve_points_attempted = int(row['first_serve_points_attempted']),
                    second_serve_points_made = int(row['second_serve_points_made']),
                    second_serve_points_attempted = int(row['second_serve_points_attempted']),
                    break_points_saved = int(row['break_points_saved']),
                    break_points_against = int(row['break_points_against']),
                    service_games_won = int(row['service_games_won']),
                    return_rating = int(row['return_rating']),
                    first_serve_return_points_made = int(row['first_serve_return_points_made']),
                    first_serve_return_points_attempted = int(row['first_serve_return_points_attempted']),
                    second_serve_return_points_made = int(row['second_serve_return_points_made']),
                    second_serve_return_points_attempted = int(row['second_serve_return_points_attempted']),
                    break_points_made = int(row['break_points_made']),
                    break_points_attempted = int(row['break_points_attempted']),
                    return_games_played = int(row['return_games_played']),
                    service_points_won = int(row['service_points_won']),
                    service_points_attempted = int(row['service_points_attempted']),
                    return_points_won = int(row['return_points_won']),
                    return_points_attempted = int(row['return_points_attempted']),
                    total_points_won = int(row['total_points_won']),
                    total_points = int(row['total_points']),
                    duration = regex_striper(row['duration']),
                    player_victory = regex_striper(row['player_victory']),
                    retirement = regex_striper(row['retirement']),
                    seed = regex_striper(row['seed']),
                    won_first_set = regex_striper(row['won_first_set']),
                    doubles = regex_striper(row['doubles']),
                    masters = int(row['masters']),
                    round_num = int(row['round_num']),
                    nation = replace_country_codes_with_names(row['nation']),
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(matches)  
                    
#  R O U N D S  D I M _ T A B L E
    with open(f"{NEW_CSVS_PATH}/rounds.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        rondas = []
        for row in reader:
            # Apply transformations and save as players object
            rondas.append(
                Round(
                    ronda = regex_striper(row['name'])
                )
            )
        # Save all new processed objects and commit
        session.add_all(rondas)
   
#  C U R R E N C I E S  D I M _ T A B L E
    with open(f"{NEW_CSVS_PATH}/currencies.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        currencies = []
        for row in reader:
            # Apply transformations and save as players object
            currencies.append(
                Currency(
                    name = regex_striper(row['name'])
                )
            )
        # Save all new processed objects and commit
        session.add_all(currencies)

#  S U R F A C E S  D I M _ T A B L E
    with open(f"{NEW_CSVS_PATH}/surfaces.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        surfaces = []
        for row in reader:
            # Apply transformations and save as players object
            surfaces.append(
                Surface(
                    name = regex_striper(row['name'])
                )
            )
        # Save all new processed objects and commit
        session.add_all(surfaces)

#  D A T E S  D I M _ T A B L E
    with open(f"{NEW_CSVS_PATH}/dates.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our players objects
        dates_dim = []
        for row in reader:
            # Apply transformations and save as players object
            dates_dim.append(
                TimeDimension(
                        date = date_transformation(row['star_date'])['date'],
                        year = date_transformation(row['star_date'])['year'],
                        month = date_transformation(row['star_date'])['month'],
                        day = date_transformation(row['star_date'])['day'],
                        day_of_week = date_transformation(row['star_date'])['day_of_week'],
                        quarter = date_transformation(row['star_date'])['quarter'],
                        is_weekend = date_transformation(row['star_date'])['is_weekend']
                    )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(dates_dim)
        
        
    session.commit()


def main():
    print("[Transform] Start")
    print("[Transform] Remove any old data from ppr_raw_all table")
    # truncate_table()
    print("[Transform] Transform new data available in ppr_raw_all table")
    transform_new_data()
    print("[Transform] End")
    
main()

