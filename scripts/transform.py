from datetime import datetime
import csv, os
import pandas as pd
import glob


from common.tables import Match, Tournament, Player, Country, Surface, Round, Currency
# from common.tables import Owner, Pet
from common.base import session

from extract import NEW_CSVS_PATH
from sqlalchemy import text

from tools.transform_functions import *


# def add_owner_pets():
#     # Create two owners
#     owner1 = Owner(name='John Doe')
#     owner2 = Owner(name='Jane Smith')

#     # Create two pets and associate them with owners
#     pet1 = Pet(name='Fido', species='Dog', owner=owner1)
#     pet2 = Pet(name='Whiskers', species='Cat', owner=owner2)

#     # Add the objects to the session
#     session.add_all([owner1, owner2, pet1, pet2])

#     # Commit the changes to the database
#     session.commit()

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
    csv_files = glob.glob(f'{NEW_CSVS_PATH}/*.csv')
    
    for csv_file in csv_files:
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
    
            file_name = csv_file.split('/')[-1]  # Get the last part of the file path (the file name)

#  M A T C H E S  F A C T _ T A B L E      
        
            if 'matches' in file_name:
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


#  T O U R N A M E N T S  D I M _ T A B L E      
            if 'tournaments' in file_name:
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
            if 'players' in file_name:
                players = []
                for row in reader:
                    # Apply transformations and save as players object
                    players.append(
                        Player(
                            name = regex_striper(row['player_id']).title(),
                            nationality_id = replace_country_codes_with_names(row['country'])
                        )
                    )
                # Save all new processed objects and commit
                session.bulk_save_objects(players)  
        
        
#  C O U N T R I E S  D I M _ T A B L E                    
            if 'countries' in file_name:
                countries = []
                for row in reader:
                    # Apply transformations and save as players object
                    players.append(
                        Country(
                            name = regex_striper(row['name']),
                            code = regex_striper(row['code']),
                            region_ = regex_striper(row['region']),
                            sub_region = regex_striper(row['sub_region'])
                        )
                    )
                # Save all new processed objects and commit
                session.bulk_save_objects(countries)


#  R O U N D S  D I M _ T A B L E                            
            if 'rounds' in file_name:
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
        
        
#  S U R F A C E S  D I M _ T A B L E                                  
            if 'surfaces' in file_name:
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
            

#  C U R R E N C I E S  D I M _ T A B L E        
            if 'currencies' in file_name:
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
            
        
#  D A T E S  D I M _ T A B L E        
            # if 'dates' in file_name:
            #     dates_dim = []
            #     for row in reader:
            #         # Apply transformations and save as players object
            #         dates_dim.append(
            #             TimeDimension(
            #                     date = date_transformation(row['star_date'])['date'],
            #                     year = date_transformation(row['star_date'])['year'],
            #                     month = date_transformation(row['star_date'])['month'],
            #                     day = date_transformation(row['star_date'])['day'],
            #                     day_of_week = date_transformation(row['star_date'])['day_of_week'],
            #                     quarter = date_transformation(row['star_date'])['quarter'],
            #                     is_weekend = date_transformation(row['star_date'])['is_weekend']
            #                 )
            #         )
            #     # Save all new processed objects and commit
            #     session.bulk_save_objects(dates_dim)
        
        
        session.commit()


def main():
    print("[Transform] Start")
    # print("[Transform] Remove any old data from ppr_raw_all table")
    # truncate_table()
    
    # add_owner_pets()
    print("[Transform] Transform new data available in all tables")
    transform_new_data()
    print("[Transform] End")
      

main()

