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
cumulative_returns = (1 + returns).cumprod()

# calculate the daily volatility (standard deviation) for each stock over 30-day rolling window
rolling_vol = returns.rolling(window = 30).std()


# Trading Strategy: Long and Short Run Moving Average Crossover: for ICLN
short_mavg = close_prices['ICLN'].rolling(window = 20).mean()
long_mavg = close_prices['ICLN'].rolling(window = 50).mean()

short_mavg_spy= close_prices['SPY'].rolling(window = 20).mean()
long_mavg_spy = close_prices['SPY'].rolling(window = 50).mean()


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

# 30- day rolling volatility chart

rolling_vol.plot(title="30-Day Rolling Volatility: ICLN vs SPY (2020–Present)")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.axhline(y=0, color='gray', linestyle='--', linewidth=0.8)
plt.show()

# moving average crossover chart with buy and sell signals on chart
buy_sig = (short_mavg > long_mavg) & (short_mavg.shift(1) <= long_mavg.shift(1))
sell_sig = (short_mavg < long_mavg) & (short_mavg.shift(1) >= long_mavg.shift(1))

buy_dates = buy_sig[buy_sig].index
sell_dates = sell_sig[sell_sig].index

close_prices['ICLN'].plot(label = "ICLN Prices")
long_mavg.plot(label = "50 Day Moving Average")
short_mavg.plot(label = "20 Day Moving Average")

plt.scatter(buy_dates, close_prices['ICLN'][buy_dates], marker = '^', color = 'green', s = 100,  label = 'Buy', zorder = 5)
plt.scatter(sell_dates, close_prices['ICLN'][sell_dates], marker = 'v', color = 'red', s = 100, label = 'Sell', zorder = 5)


plt.title("ICLN Price and Moving Average Crossovers (2020–Present)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# moving average crossover for SPY

buy_sig_spy = (short_mavg_spy > long_mavg_spy) & (short_mavg_spy.shift(1) <= long_mavg_spy.shift(1))
sell_sig_spy = (short_mavg_spy < long_mavg_spy) & (short_mavg_spy.shift(1) >= long_mavg_spy.shift(1))
 
buy_dates_spy = buy_sig_spy[buy_sig_spy].index
sell_dates_spy = sell_sig_spy[sell_sig_spy].index

close_prices['SPY'].plot(label = "SPY Prices")
long_mavg_spy .plot(label = "50 Day Moving Average")
short_mavg_spy.plot(label = "20 Day Moving Average")

plt.scatter(buy_dates_spy, close_prices['SPY'][buy_dates_spy], marker = '^', color = 'green', s = 100, label = 'Buy', zorder = 5)
plt.scatter(sell_dates_spy, close_prices['SPY'][sell_dates_spy], marker = 'v', color = 'red', s = 100, label = 'Sell', zorder = 5)

plt.title("SPY Price and Moving Average Crossovers (2020–Present)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
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

