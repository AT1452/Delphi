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

ts = TimeSeries(key='XG6N7A6K1EL9Y2KR', output_format='pandas')

df = ts.get_daily_adjusted(symbol='JNJ', outputsize='full')

df[0].to_csv('jnj.csv')
df = pd.read_csv('jnj.csv', parse_dates=True, index_col=0)

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax1.xaxis_date()
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex=ax1)  # sharex just makes it so they zoom together

ax1.plot(df.index, df['5. adjusted close'])
# ax1.plot(df.index, df['200ma'])
# ax1.plot(df.index, df['50ma'])
ax2.plot(df.index, df['6. volume'])

plt.show()
