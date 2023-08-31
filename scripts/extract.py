import requests, io, csv, os
from zipfile import ZipFile
from datetime import date


BASE_PATH = os.path.abspath('')
SOURCE_PATH = f"{BASE_PATH}/data/source/tennis_csvs.zip"
RAW_PATH = f"{BASE_PATH}/data/raw/"



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
        
        
def main():
    print("[Extract] Start")
    print(f"[Extract] Extracting data from '{SOURCE_PATH}' to '{RAW_PATH}'")
    save_raw_data()
    print(f"[Extract] End")