import backtrader as bt

import yfinance as yf
import pandas as pd

def fetch_data(symbol, start_date, end_date):
    df = yf.download(symbol, start=start_date, end=end_date)
    if df.empty:
        raise ValueError(f"No data found for {symbol} between {start_date} and {end_date}")
    return df

