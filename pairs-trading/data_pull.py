import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_prices(tickers, start_date):
    dataframe = yf.download(tickers, start = start_date)

    close_prices = dataframe['Close']
    close_prices = close_prices.dropna() #this will remove any rows whihc are misaligned or missing as for pairs reg you need same trading days

    return close_prices

