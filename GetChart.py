import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web


def get_chart(ticker, period, interval):

    start = 0
    end = 0

    if period == '1w':
        start = dt.datetime.now() - dt.timedelta(days=5)
        end = dt.datetime.now()
    elif period == '1m':
        start = dt.datetime.now() - dt.timedelta(30)
        end = dt.datetime.now()
    elif period == '6m':
        start = dt.datetime.now() - dt.timedelta(182)
        end = dt.datetime.now()
    elif period == '3m':
        start = dt.datetime.now() - dt.timedelta(90)
        end = dt.datetime.now()

    #add more periods

    df = web.DataReader(ticker, 'iex', start, end)

    df.to_csv(ticker + '.csv')
    df = pd.read_csv(ticker+'.csv', parse_dates=True, index_col=0)

    return df



