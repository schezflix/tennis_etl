import re
import pandas as pd
import boto3
import os
import datetime


def clean_currency(currency_input: str) -> str:
    currency_input = str(currency_input)
    if '€' in currency_input:
        return currency_input.replace('€', 'euro').strip()
    elif '$' in currency_input:
        return currency_input.replace('$', 'dollar').strip()
    elif '£' in currency_input:
        return currency_input.replace('£', 'pound').strip()
    elif 'A$' in currency_input:
        return currency_input.replace('A$', 'au_dollar').strip()
    else:
        return ''
    
    
def null_to_int(string: str) -> int:
    return int(string) if string else 0

def date_transformation(date_string: str) -> dict:
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    day_of_week = date_obj.weekday()
    quarter = (date_obj.month - 1) // 3 + 1
    is_weekend = day_of_week >= 5
    
    result = {
        "date": date_string,
        "year": year,
        "month": month,
        "day": day,
        "day_of_week": day_of_week,
        "quarter": quarter,
        "is_weekend": is_weekend
    }
    return result

def replace_country_codes_with_names(matches_df, countries_df):
    # Create a mapping dictionary from 'Countries' dataframe
    country_mapping = countries_df.set_index('code')['name'].to_dict()

    # Replace country codes with country names in 'Matches' dataframe
    matches_df['location'] = matches_df['location'].apply(lambda code: country_mapping.get(code, code))

    return matches_df


def regex_striper(string:str) -> str:
    string = re.sub('\r', '',string).strip()
    string = re.sub('\n', '',string).strip()
    string = re.sub('\t', '',string).strip()
    string = re.sub('-', ' ',string).strip()
    string = re.sub('_', ' ',string).strip()

    return string

def substring_challenger(string:str) -> str:
    string = re.sub('challenger', '', string, flags=re.I).strip()
    
    return string


def set_transformer(match):
    partido = []
    for set_t in match:
        if len(set_t) == 3:
            partido.append('-'.join(set_t[:2]))
            continue
        else:
            partido.append('-'.join(set_t))
    return partido


def csv_converter(data:dict, name:str) -> pd.DataFrame:
    return pd.DataFrame(data).to_csv(f"csv/{name}.csv", index=False)


def upload_to_s3(file) -> None:
    try:
        s3 = boto3.resource(
            service_name = "s3",
            region_name = "us-west-1",
            aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
        )
        s3.Bucket("schezflix-glue-etl").upload_file(Filename=file, Key=file)
        print('CSV file successfuly uploaded to S3.')

    except ConnectionError:
        raise ConnectionError('Something wrong happened with the connection to S3.')

def transform_case(input_string):
    """
    Lowercase string fields
    """
    # Return the string lowercase
    return input_string.lower()
  
def update_date_of_sale(date_input):
    """
    Update date format from DD/MM/YYYY to YYYY-MM-DD
    """
    # Create a datetime object
    current_format = datetime.strptime(date_input, "%d/%m/%Y")
    # Convert to the expected date format
    new_format = current_format.strftime("%Y-%m-%d")
    return new_format

def update_price(price_input):
    """
    Returns price as an integer by removing:
    - "€" and "," symbol
    - Converting to float first then to integer
    """
    # Replace € with an empty string
    price_input = price_input.replace("€", "")
    # Replace comma with an empty string
    price_input = price_input.replace(",", "")
    # Convert to float
    price_input = float(price_input)
    # Return price_input as integer
    return int(price_input)
  
def update_description(description_input):
    """
    Simplifies the description field for future analysis. Returns:
    - "new" if string contains "new" substring
    - "second-hand" if string contains "second-hand" substring
    """
    description_input = transform_case(description_input)
    # Check description and return "new" or "second-hand"
    if "new" in description_input:
        return "new"
    elif "second-hand" in description_input:
        return "second-hand"
    return description_input
