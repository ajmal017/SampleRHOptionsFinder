"""
Module for any API calls to robin_stocks.
"""
import os
import sys

import pandas as pd
import robin_stocks.options as opts
from robin_stocks.helper import set_output

def get_profitable(symbols, date, profit_type='short', min_percent=0.0, max_percent=1.0):
    """
    Parameters
    ----------
    symbols: list or str
        An individual or list of symbols
    date: str
        Expiration date formatted as YYYY-MM-DD
    profit_type: str, optional
        either 'short' or 'long', defaults to 'short'
    min_percent: float, optional
        between 0 and 1; defaults to 0
    max_percent: float, optional
        between 0 and 1; defaults to 1
    """
    if not isinstance(symbols, (str, list)):
        raise ValueError("symbols should be either a string or a list; got %s"%(type(symbols)))
    
    if profit_type not in ('short', 'long'):
        raise ValueError("profit_type should be either 'short' or 'long'; got %s"%profit_type)
    
    if min_percent < 0 or min_percent > 1:
        raise ValueError("min_percent should be between 0 and 1; got %s"%min_percent)
    
    if max_percent < 0 or max_percent > 1:
        raise ValueError("max_percent should be between 0 and 1; got %s"%max_percent)
        
    if min_percent > max_percent:
        raise ValueError("min_percent should be less than the max_percent!")
    
    p_type = 'chance_of_profit_short' if profit_type == 'short' else 'chance_of_profit_long'
    
    with open(os.devnull, 'w') as devNull:
        og = sys.stdout
        sys.stdout = devNull
        set_output(devNull)
    
        resp = opts.find_options_by_specific_profitability(symbols, expirationDate=date, typeProfit=p_type, profitFloor=min_percent, profitCeiling=max_percent)
        
        sys.stdout = og
        set_output(og)
    return pd.DataFrame.from_dict(resp)