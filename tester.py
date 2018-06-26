import StockFilters
import GetChart
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# df = StockFilters.cross_200_sma('TSLA')
#
# sma_col_noshift = df[0]
# close_noshift = GetChart.get_chart('TSLA', '6m', 0)['close']
#
# combined_df = sma_col_noshift.join(close_noshift)
# close_shift = combined_df['close'].shift(1)
# sma_shift = combined_df['SMA'].shift(1)
#
#
# diff = combined_df['close'] < combined_df['SMA']
# diff_forward = diff.shift(1)
# crossover = np.where(abs(diff - diff_forward) == 1)[0]
# print(crossover)
#
#
# # crossover = (((combined_df['SMA'] <= combined_df['close']) & (sma_shift >= close_shift)) |
# #              ((combined_df['SMA'] >= combined_df['close']) & (sma_shift <= close_shift)))
#
# # crossover = (((combined_df['close'] < combined_df['SMA']) & (close_shift >= sma_shift))
# #             | ((combined_df['close'] > combined_df['SMA']) & (close_shift <= sma_shift)))
# #
# #
# # print(combined_df)
# #
# #
# crossing_dates = combined_df.iloc[crossover]
# #
# print(crossing_dates)
# i = len(crossing_dates['SMA']) - 1
# while i > 0:
#     if crossing_dates['close'][i] == crossing_dates['SMA'][i] > crossing_dates['close'][i - 1]:
#                 print('Bullish Cross at ' + str(crossing_dates['close'][i]) + ' date: ' + str(crossing_dates.index[i]))
#     i -= 1
#
#
# combined_df.plot()
# crossing_dates.plot()
#
# plt.show()

# StockFilters.sma_200_close_crosses('TSLA')



StockFilters.gap_up('NDQTickers.csv')



