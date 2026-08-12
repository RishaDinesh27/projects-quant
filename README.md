# Quant Projects — Risha Dinesh
*Northeastern University · CS & Finance · Class of 2029*

Quantitative finance projects built summer 2026

## Projects

### 01 — Clean Energy vs Market Analysis
Compares ICLN (clean energy ETF) vs SPY (S&P 500) across
volatility, daily returns, and cumulative performance.

**Key findings:**
- ICLN has 55% higher daily volatility than SPY (2.0% vs 1.3%)
- Despite higher risk, ICLN delivered lower average daily returns
(0.060% vs 0.064% per day): clean energy investors were not compensated
for the additional risk over this period
- Both were heavily impacted by the COVID crash in March 2020
- SPY outperformed ICLN over the full period despite ICLN briefly
peaking near 2.8x during the 2020-2021 clean energy boom



[View project →](01-stock-analysis/)

### 02 — Pairs Trading Strategy
Tests stock pairs for cointegration with a mean-reversion strategy

- 5 of 6 candidate pairs failed cointegration testing; GS/MS was the only
  workable pair, and only with a borderline pass
- Naive backtest looked mediocre but plausible (Sharpe 0.34, win rate 63%)
- Once corrected for look-ahead bias via walk-forward validation, Sharpe
  dropped to -0.10 and win rate to 44% — worse than a coin flip
- Both versions underperformed a simple buy-and-hold benchmark (Sharpe 0.93)
- Conclusion: This strategy would not be trustworthy with real capital

[View project →](pairs-trading/)

### 03 — Market Making Simulator
*Coming Soon*


## Skills demonstrated
- Python (pandas, numpy, matplotlib, yfinance)
- Financial data analysis
- Risk and return analysis
- Quantitative reasoning

## Background
Current sophomore at Northeastern University studying CS and Finance.

Targeting Quant Trading/Research and SWE co-ops for spring 2026.