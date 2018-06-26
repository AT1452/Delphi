import GetNDQPrices
from iexfinance import Stock
from datetime import datetime, timedelta
import GetChart
from alpha_vantage.techindicators import TechIndicators
import GetChart
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


ti = TechIndicators(key='XG6N7A6K1EL9Y2KR', output_format='pandas')

# allTickers = GetNDQPrices.get_prices_in_range()

gapUpList = []
gapDownList = []
testList = ['AAPL', 'TSLA', 'JNJ', 'AMD', 'IQ', 'ETSY']


def gap_up(ticker_list):

    for ticker in ticker_list:
        current_ticker = Stock(ticker)
        prev_high = current_ticker.get_previous()['high']
        print('prev high: ' + str(prev_high))
        current_open = current_ticker.get_ohlc()['open']['price']
        print('cur open: ' + str(current_open))

        if current_open - prev_high >= 4.0:
            gapUpList.append(ticker)

    print(gapUpList)


def gap_down(ticker_list):

    for ticker in ticker_list:
        current_ticker = Stock(ticker)
        prev_low = current_ticker.get_previous()['low']
        print('prev high: ' + str(prev_low))
        current_open = current_ticker.get_ohlc()['open']['price']
        print('cur open: ' + str(current_open))

        if prev_low - current_open <= 4.0:
            gapDownList.append(ticker)

    print(gapDownList)


def sma_200_close_crosses(ticker):
    df = cross_200_sma(ticker)

    sma_col_noshift = df[0]
    close_noshift = GetChart.get_chart('TSLA', '6m', 0)['close']

    combined_df = sma_col_noshift.join(close_noshift)
    close_shift = combined_df['close'].shift(1)
    sma_shift = combined_df['SMA'].shift(1)

    diff = combined_df['close'] < combined_df['SMA']
    diff_forward = diff.shift(1)
    crossover = np.where(abs(diff - diff_forward) == 1)[0]

    crossing_dates = combined_df.iloc[crossover]

    i = 0
    while i < len(crossing_dates['SMA']):
        if crossing_dates['SMA'][i] < crossing_dates['close'][i]:
            print('Bullish cross at ' + str(crossing_dates['SMA'][i]) + ' date: ' + str(crossing_dates.index[i]))
        i += 1

    # i = len(crossing_dates['SMA']) - 1
    # while i > 0:
    #     if crossing_dates['close'][i] == crossing_dates['SMA'][i] > crossing_dates['close'][i - 1]:
    #         print('Bullish Cross at ' + str(crossing_dates['close'][i]) + ' date: ' + str(crossing_dates.index[i]))
    #     i -= 1

    combined_df.plot()
    crossing_dates.plot()

    plt.show()


def cross_200_sma(ticker):
    df_chart = GetChart.get_chart(ticker, '1m', '1d')
    df_200sma = ti.get_sma(symbol=ticker, interval='daily', time_period=200, series_type='close')
    return df_200sma








