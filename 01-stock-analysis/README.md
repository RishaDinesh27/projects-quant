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

- SPY generated fewer signals than the ICLN due to SPY's steady upward trend while the ICLN stock had much more signals clustered together during times of high volatility.

- This showcases that the signals present in the SPY stock would be more trustworthy than those in the ICLN stock, as the volatility present in ICLN could suggest more frequent false signals. Since ICLN is a sector ETF, it is more sensitive to sector specific movements such as interest rate and policy changes.

- Conclusion: Moving average crossover signals are more reliable on low volatility broad ETFs, rather than sector ETFs.

- SPY's annualized Sharpe Ratio of 0.61 is higher than that of ICLN's 0.3. This showcases that the SPY provided better risk adjusted returns over the full period.

- Since both Sharpe ratios are below 1, this suggests that investors were not compensated for their risk. However it is important to interpret this in consideration of the time period. Due to the analysis being concentrated from 2020 through 2026, this reflects the high volatility environment primarily fueled by Covid, continuous rate hikes and growing inflation.

## How to run
1. Install dependencies: `pip install yfinance pandas matplotlib`
2. Run `main.py`

