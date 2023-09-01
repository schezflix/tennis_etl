import requests, io, csv, os
from zipfile import ZipFile
from datetime import date
import pandas as pd


BASE_PATH = os.path.abspath('')
SOURCE_PATH = f"{BASE_PATH}/data/source/tennis_csvs.zip"
RAW_PATH = f"{BASE_PATH}/data/raw/"
NEW_CSVS_PATH = f"{BASE_PATH}/data/csvs/"



def create_folder_if_not_exists(path:str):
    """
    Create a new folder if it doesn't exists
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    
def save_raw_data():
    """
    Save new raw data from the source
    """
    create_folder_if_not_exists(RAW_PATH)
    
    with ZipFile(SOURCE_PATH, mode= 'r') as f:
        f.extractall(path=RAW_PATH)
        
def save_new_csv_data():
    """
    Saves new csvs with only necessary columns
    """
    create_folder_if_not_exists(NEW_CSVS_PATH)
    
    # countries
    pd.read_csv('data/raw/countries.csv', usecols=['name', 'code', 'region', 'sub_region']
                , dtype={'name': str, 'region': str, 'sub_region': str})\
        .to_csv(f'{NEW_CSVS_PATH}countries.csv', index=False)

    # players
    pd.read_csv('data/raw/all_players.csv'
                , dtype={'player_id': str, 'country': str})\
        .to_csv(f'{NEW_CSVS_PATH}players.csv', index=False)
        
    # tournaments
    pd.read_csv('data/raw/all_tournaments.csv', usecols=['tournament', 'location', 'court_surface', 'prize_money', 'masters']
            , dtype={'tournament': str, 'location': str, 'court_surface': str, 'prize_money': str, 'masters': str})\
        .to_csv(f'{NEW_CSVS_PATH}tournaments.csv', index=False)
        
    # matches
    pd.read_csv('data/raw/all_matches.csv', dtype={
        'start_date': str, 'end_date': str, 'location': str, 'court_surface': str, 'prize_money': str, 'currency': str, 'year': int, 'player_id': str,
        'opponent_id': str, 'tournament': str, 'round': str, 'num_sets': str, 'sets_won': str, 'games_won': str,'games_against': str, 'tiebreaks_won': str,
        'tiebreaks_total': str, 'serve_rating': str, 'aces': str, 'double_faults': str, 'first_serve_made': str, 'first_serve_attempted': str, 'first_serve_points_made': str,
        'first_serve_points_attempted': str, 'second_serve_points_made': str, 'second_serve_points_attempted': str, 'break_points_saved': str, 'break_points_against': str,
        'service_games_won': str, 'return_rating': str, 'first_serve_return_points_made': str, 'first_serve_return_points_attempted': str,'second_serve_return_points_made': str,
        'second_serve_return_points_attempted': str, 'break_points_made': str, 'break_points_attempted': str, 'return_games_played': str, 'service_points_won': str,
        'service_points_attempted': str, 'return_points_won': str, 'return_points_attempted': str,'total_points_won': str, 'total_points': str, 'duration': str,
        'player_victory': str, 'retirement': str, 'seed': str, 'won_first_set': str, 'doubles': str, 'masters': str, 'round_num': str, 'nation': str
    }, usecols= ['start_date', 'end_date', 'location', 'court_surface', 'prize_money', 'currency', 'year', 'player_id', 'player_name', 'opponent_id','opponent_name',
                'tournament', 'round', 'num_sets', 'sets_won', 'games_won', 'games_against', 'tiebreaks_won', 'tiebreaks_total', 'serve_rating', 'aces', 'double_faults',
                'first_serve_made', 'first_serve_attempted', 'first_serve_points_made', 'first_serve_points_attempted', 'second_serve_points_made', 'second_serve_points_attempted',
                'break_points_saved', 'break_points_against', 'service_games_won', 'return_rating', 'first_serve_return_points_made', 'first_serve_return_points_attempted',
                'second_serve_return_points_made', 'second_serve_return_points_attempted', 'break_points_made','break_points_attempted', 'return_games_played', 'service_points_won',
                'service_points_attempted', 'return_points_won', 'return_points_attempted', 'total_points_won', 'total_points', 'duration', 'player_victory', 'retirement',
                'seed', 'won_first_set', 'doubles', 'masters', 'round_num', 'nation'])\
                    .to_csv(f'{NEW_CSVS_PATH}matches.csv', index=False)
    
    # surfaces
    pd.Series(pd.read_csv('data/raw/all_matches.csv', usecols=['court_surface']
            , dtype={'court_surface': str})['court_surface'].unique(), name='name')\
        .to_csv(f'{NEW_CSVS_PATH}surfaces.csv', index=False)  

    # currency
    pd.Series(pd.read_csv('data/raw/all_matches.csv', usecols=['currency']
            , dtype={'currency': str})['currency'].unique(), name='name')\
        .to_csv(f'{NEW_CSVS_PATH}currencies.csv', index=False)  

    # rounds
    pd.Series(pd.read_csv('data/raw/all_matches.csv', usecols=['round']
            , dtype={'round': str})['round'].unique(), name='name')\
        .to_csv(f'{NEW_CSVS_PATH}rounds.csv', index=False)  

    # dates
    pd.Series(pd.read_csv('data/raw/all_matches.csv', usecols=['start_date']
            , dtype={'start_date': str})['start_date'].unique(), name='dates')\
        .to_csv(f'{NEW_CSVS_PATH}dates.csv', index=False)   


def main():
    print("[Extract] Start")
    print(f"[Extract] Extracting data from '{SOURCE_PATH}' to '{RAW_PATH}' and adding a clean version into '{NEW_CSVS_PATH}'")
    save_raw_data()
    save_new_csv_data()
    print(f"[Extract] End")
        
