from datetime import datetime
import csv, os
import pandas as pd


from common.tables import Match, Tournament, Player, Country
from common.base import session
from sqlalchemy import text

from tools.transform_functions import *

BASE_PATH = os.path.abspath('')
SOURCE_PATH = f"{BASE_PATH}/data/source/tennis_csvs.zip"
RAW_PATH = f"{BASE_PATH}/data/raw/"

# def truncate_table():
#     """
#     Ensure that "ppr_raw_all" table is always in empty state before running any transformations.
#     And primary key (id) restarts from 1.
#     """
#     session.execute(
#         text("TRUNCATE TABLE ppr_raw_all;ALTER SEQUENCE ppr_raw_all_id_seq RESTART;")
#     )
#     session.commit()


def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    with open(f"{RAW_PATH}/all_tournaments.csv", mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list for our PprRawAll objects
        tournaments = []
        for row in reader:
            # Apply transformations and save as PprRawAll object
            tournaments.append(
                Tournament(
                    name = regex_striper(row['name']),
                    category = regex_striper(row['name']),
                    location = regex_striper(row['name']),
                    winning_price = regex_striper(row['name']),
                    date = regex_striper(row['name'])
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(tournaments)
        
        
        
        session.commit()


def main():
    print("[Transform] Start")
    print("[Transform] Remove any old data from ppr_raw_all table")
    # truncate_table()
    print("[Transform] Transform new data available in ppr_raw_all table")
    transform_new_data()
    print("[Transform] End")

