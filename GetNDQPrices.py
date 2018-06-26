import csv
from iexfinance import Stock


tickersInRange = []


def get_prices_in_range():
    with open('NDQTickers.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            #print(row[0])
            if len(row[0]) > 4:
                continue
            else:
                ticker = Stock(row[0])
                price = ticker.get_price()
                if 10 < price < 250:
                    tickersInRange.append(row[0])
                    #print(row[0] + " " + str(ticker.get_price()))
    return tickersInRange



