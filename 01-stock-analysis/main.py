import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#Define the tickers and the time frame for the analysis
tickers = ["ICLN", "SPY"] # comparing against SPY to benchmark clean energy performance vs broad market

dataframe = yf.download(tickers, start = "2020-01-01") #till current data by default

#Calculate the daily returns for each stock
close_prices = dataframe['Close']
returns = close_prices.pct_change() # pct_change() calculates day-over-day return — first row will be NaN since there's no prior day

#use first 10 col
print(returns.head(10) * 100) #displayed as a percentage

#Calculate cumulative returns
cumulative_returns = (1+ returns).cumprod()

# daily returns chart
returns.plot(title="Daily Returns: ICLN vs SPY (2020–Present)")
plt.xlabel("Date")
plt.ylabel("Daily Return (%)")
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
plt.show()

# cumulative returns chart
cumulative_returns.plot(title="Cumulative Returns: ICLN vs SPY (2020–Present)")
plt.xlabel("Date")
plt.ylabel("Growth of $1 Invested")
plt.axhline(y=1, color='gray', linestyle='--', linewidth=0.8)
plt.show()

# calculate variance and standard deviation for each ticker
variance = returns.var()
std_dev = returns.std()

print("Variance:")
print(variance)
print("\nStandard Deviation (Volatility):")
print(std_dev)

avg_return = returns.mean()
print("\nAverage Daily Return:")
print(avg_return)