import datetime as dt
import matplotlib.pyplot as plt
import matplotlib as style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader as web
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import pickle


ts = TimeSeries(key='XG6N7A6K1EL9Y2KR', output_format='csv')

df = ts.get_daily_adjusted(symbol='TSLA', outputsize='compact')

plt.style.use('ggplot')

start = dt.datetime(2014, 1, 1)
end = dt.datetime(2017, 12, 31)

# df = web.DataReader('TSLA', 'iex', start, end)

df = pd.read_csv(df, parse_dates=True, index_col=0)

print(df.head())
# print(df[['open', 'high']].head())
# df[['close', 'open']].plot()
# plt.show()

# moving averages:
# df['200ma'] = df['close'].rolling(window=200, min_periods=0).mean()
# df['50ma'] = df['close'].rolling(window=50, min_periods=0).mean()

# print(df.head())

df_olhc = df['close'].resample('10D').ohlc()
df_volume = df['volume'].resample('10D').sum()

df_olhc.reset_index(inplace=True)

df_olhc['date'] = df_olhc['date'].map(mdates.date2num)

print(df_olhc['date'])

#print(df_olhc.head())

# this is a subplot or another graph, god knows why it's called an axis?:
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax1.xaxis_date()
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)  # sharex just makes it so they zoom together

candlestick_ohlc(ax1, df_olhc.values, width=2, colorup='g')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

# plot SMAs, price, and volume:
# ax1.plot(df.index, df['close'])
# ax1.plot(df.index, df['200ma'])
# ax1.plot(df.index, df['50ma'])
# ax2.plot(df.index, df['volume'])

plt.show()
