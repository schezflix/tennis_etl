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


def main():
    print("[Extract] Start")
    print(f"[Extract] Extracting data from '{SOURCE_PATH}' to '{RAW_PATH}' and adding a clean version into '{NEW_CSVS_PATH}'")
    save_raw_data()
    save_new_csv_data()
    print(f"[Extract] End")
    
