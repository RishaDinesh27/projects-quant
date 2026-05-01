# Clean Energy vs Market Analysis 

## What this project does
Compares the daily and cumulative returns of ICLN (iShares Global
Clean Energy ETF) against SPY (S&P 500 ETF) from 2020 to present.

## Why I built it
I've been passionate and interested about clean energy since I was young, I became more interested about it through projects, notably my start-up FLTR.
I wanted to understand how clean energy stocks have performed relative to the broader market, specific in terms of their volatility, and their returns.

## What I found
- ICLN has 55% higher daily volatility than SPY (2.0% vs 1.3%)

- Despite higher risk, ICLN delivered lower average daily returns (0.060% vs 0.064% per day) — clean energy investors were not compensated for the additional risk over this period

- Both were heavily impacted by the COVID crash in March 2020

- SPY outperformed ICLN over the full period despite ICLN briefly peaking near 2.8x during the 2020-2021 clean energy boom

- Rising interest rates likely drove ICLN's crash through 2022-2023:
  - clean energy companies carry heavy debt loads making them
    sensitive to rate increases

- ICLN nearly returned to breakeven in 2025 despite a 5 year
  holding period — wiping out years of gains

- SPY's lower volatility led to steadier compounding — high
  volatility stocks require good days to offset the bad ones

- Slow recovery post-2023, possible drivers include stabilizing rates and renewed clean energy investment such as the interest in EV's and carbon capture,
  though further  analysis would be needed to confirm causation

## Still building
- Sharpe ratio calculation
- Moving averages and trading signals

## How to run
1. Install dependencies: `pip install yfinance pandas matplotlib`
2. Run `main.py`

