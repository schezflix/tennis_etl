from datetime import datetime
import csv, os
import pandas as pd
import glob
import time


from common.tables_staging import Match, Tournament, Player, Country, Surface, Currency , Round
from common.base import session
from common.base import engine

from extract import NEW_CSVS_PATH
from sqlalchemy import text

from tools.transform_functions import *

def truncate_table():
    """
    Ensure that all tables are always in empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("""
            TRUNCATE TABLE matches; -- ALTER SEQUENCE matches RESTART;
            TRUNCATE TABLE rounds; -- ALTER SEQUENCE rounds RESTART;
            TRUNCATE TABLE tournaments; -- ALTER SEQUENCE tournaments RESTART;
            TRUNCATE TABLE surfaces; -- ALTER SEQUENCE surfaces RESTART;
            TRUNCATE TABLE currencies; -- ALTER SEQUENCE currencies RESTART;
            TRUNCATE TABLE players; -- ALTER SEQUENCE players RESTART;
            TRUNCATE TABLE countries; -- ALTER SEQUENCE countries RESTART;
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
                    matches.append(
                        Match(
                            start_date = date_transformation(row['start_date'])['date'],
                            end_date = date_transformation(row['start_date'])['date'],
                            location = regex_striper(row['location']),
                            court_surface = regex_striper(row['court_surface']),
                            prize_money = null_to_int(row['prize_money']),
                            currency = clean_currency(row['currency']),
                            year = null_to_int(row['year']),
                            player_name = regex_striper(row['player_id']),
                            opponent_name = regex_striper(row['opponent_id']),
                            tournament = regex_striper(row['tournament']),
                            tourney_round = regex_striper(row['round']),
                            num_sets = null_to_int(row['num_sets']),
                            sets_won = null_to_int(row['sets_won']),
                            games_won = regex_striper(row['games_won']),
                            games_against = null_to_int(row['games_against']),
                            tiebreaks_won = null_to_int(row['tiebreaks_won']),
                            tiebreaks_total = null_to_int(row['tiebreaks_total']),
                            serve_rating = regex_striper(row['serve_rating']),
                            aces = null_to_int(row['aces']),
                            double_faults = null_to_int(row['double_faults']),
                            first_serve_made = null_to_int(row['first_serve_made']),
                            first_serve_attempted = null_to_int(row['first_serve_attempted']),
                            first_serve_points_made = null_to_int(row['first_serve_points_made']),
                            first_serve_points_attempted = null_to_int(row['first_serve_points_attempted']),
                            second_serve_points_made = null_to_int(row['second_serve_points_made']),
                            second_serve_points_attempted = null_to_int(row['second_serve_points_attempted']),
                            break_points_saved = null_to_int(row['break_points_saved']),
                            break_points_against = null_to_int(row['break_points_against']),
                            service_games_won = null_to_int(row['service_games_won']),
                            return_rating = null_to_int(row['return_rating']),
                            first_serve_return_points_made = null_to_int(row['first_serve_return_points_made']),
                            first_serve_return_points_attempted = null_to_int(row['first_serve_return_points_attempted']),
                            second_serve_return_points_made = null_to_int(row['second_serve_return_points_made']),
                            second_serve_return_points_attempted = null_to_int(row['second_serve_return_points_attempted']),
                            break_points_made = null_to_int(row['break_points_made']),
                            break_points_attempted = null_to_int(row['break_points_attempted']),
                            return_games_played = null_to_int(row['return_games_played']),
                            service_points_won = null_to_int(row['service_points_won']),
                            service_points_attempted = null_to_int(row['service_points_attempted']),
                            return_points_won = null_to_int(row['return_points_won']),
                            return_points_attempted = null_to_int(row['return_points_attempted']),
                            total_points_won = null_to_int(row['total_points_won']),
                            total_points = null_to_int(row['total_points']),
                            duration = regex_striper(row['duration']),
                            player_victory = regex_striper(row['player_victory']),
                            retirement = regex_striper(row['retirement']),
                            seed = regex_striper(row['seed']),
                            won_first_set = regex_striper(row['won_first_set']),
                            doubles = regex_striper(row['doubles']),
                            masters = null_to_int(row['masters']),
                            round_num = null_to_int(row['round_num']),
                            nation = regex_striper(row['nation']),
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
                            category = null_to_int(row['masters']),
                            location = regex_striper(row['location']),
                            surface = regex_striper(row['court_surface']),
                            winning_prize = null_to_int(row['prize_money'])
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
                            nationality = regex_striper(row['country'])
                        )
                    )
                # Save all new processed objects and commit
                session.bulk_save_objects(players)  
        
        
#  C O U N T R I E S  D I M _ T A B L E                    
            if 'countries' in file_name:
                countries = []
                for row in reader:
                    # Apply transformations and save as players object
                    countries.append(
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
                            name = clean_currency(row['name'])
                        )
                    )
                # Save all new processed objects and commit
                session.add_all(currencies)
        
        session.flush()
        session.commit()
       

 
def staging_import_csv():
    
    csv_files = glob.glob(f'{NEW_CSVS_PATH}/*.csv')


    country_mapping = {}
    with open('data/csvs/countries.csv', 'r') as countries_file:
        for line in countries_file:
            if '"Taiwan' in line:
                country_name = line.strip().replace('"','').split(',')[0]
                country_code = line.strip().replace('"','').split(',')[2]
            else:
                country_name = line.strip().split(',')[0]
                country_code = line.strip().split(',')[1]
            
            country_mapping[country_name] = country_code


    with open('data/csvs/matches.csv', 'r') as matches_file, open('data/csvs/matches_nu.csv', 'w') as output_file:
        for line in matches_file:
            fields = line.strip().split(',')
            
            if len(fields) != 54:
                fields.pop(3)
                fields[2].replace('"', '')
                fields[2] = fields[2].replace('"', '')
                # output_file.write(','.join(fields) + '\n')            
            if fields[2] in country_mapping:
                fields[2] = country_mapping[fields[2]]
            
            output_file.write(','.join(fields) + '\n')
                
    

    for csv_file in csv_files:
        file_name = csv_file.split('/')[-1]
        
        if 'matches_nu' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=500000, low_memory=False):
                chunk.to_sql('matches_nu', engine, chunksize=500000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'matches_nu' table.")
                batch_no+=1
            print('matches_nu table just finished loading.\n')
            
            
        if 'tournaments' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=100000):
                chunk.to_sql('tournaments', engine, chunksize=100000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'tournaments' table.")
                batch_no+=1
            print('Tournaments table just finished loading.\n')
            
                
        if 'players' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=100000):
                chunk.to_sql('players', engine, chunksize=100000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'players' table.")
                batch_no+=1
            print('Players table just finished loading.\n')

        if 'countries' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=100000):
                chunk.to_sql('countries', engine, chunksize=100000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'countries' table.")
                batch_no+=1
            print('Countries table just finished loading.\n')


        if 'rounds' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=100000):
                chunk.to_sql('rounds', engine, chunksize=100000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'rounds' table.")
                batch_no+=1
            print('Rounds table just finished loading.\n')


        if 'surfaces' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=100000):
                chunk.to_sql('surfaces', engine, chunksize=100000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'surfaces' table.")
                batch_no+=1
            print('Surfaces table just finished loading.\n')
    
        if 'currencies' in file_name:
            batch_no = 1
            for chunk in pd.read_csv(csv_file, chunksize=100000):
                chunk.to_sql('currencies', engine, chunksize=100000, if_exists = 'append')
                print(f"Batch number: {batch_no} has been loaded to the staging 'currencies' table.")
                batch_no+=1
            print('Currencies table just finished loading.\n')


def main():
    print("[Transform] Start")
    start_time = time.time()

    print("[Transform] Removing any old data from all tables")
    # truncate_table()
    print("[Transform] Transforming and loading new data available in all tables")
    # transform_new_data() 
    staging_import_csv()   
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("[Transform] End\n")
    print(f"Transformation and load took: {round(elapsed_time/60,2)} minutes")
    
      

main()

