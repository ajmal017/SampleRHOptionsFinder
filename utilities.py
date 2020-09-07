"""
Module for helper functions.
"""
import os
from datetime import timedelta

import yaml
import pandas as pd

PARENT_PATH = os.path.dirname(os.path.abspath(__file__))

def get_symbols():
    """
    Get a series of listed symbols.

    Returns
    -------
    pandas.Series
    """
    return pd.read_csv(os.path.join(PARENT_PATH, 'data/symbols.csv'), sep='|')['Symbol']

def get_listings():
    """
    Get a dataframe of listed symbols and security names

    Returns
    -------
    pandas.DataFrame
    """
    return pd.read_csv(os.path.join(PARENT_PATH, 'data/symbols.csv'), sep='|')[['Symbol', 'Security Name']]

def robinhood_login():
    """
    Log into robinhood via robin_stocks and the credentials file.
    """
    import robin_stocks
    credentials = read_login_file()
    robin_stocks.login(credentials['username'], credentials['password'])

def read_login_file():
    """
    Parse the credentials file into username and password.

    Returns
    -------
    dict
    """
    with open('.robinhood_login', 'r') as login_file:
        credentials = yaml.safe_load(login_file)
    return credentials

def query_date_to_display(date):
    """
    date: str
    """
    yyyy, mm, dd = date.split('-')
    return '-'.join((mm, dd, yyyy))

def display_date_to_query(date):
    """
    date: str
    """
    mm, dd, yyyy = date.split('-')
    return '-'.join((yyyy, mm, dd))

def date_range(start_date, end_date):
    """
    Parameters
    ----------
    start_date: datetime.date
    end_date: datetime.date
    """
    for n in range(int((end_date - start_date).days)):
        yield (start_date + timedelta(n)).strftime('%Y-%m-%d')