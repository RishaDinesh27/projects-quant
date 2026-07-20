# Pairs Trading

## Overview
Testing candidate pairs for cointegration using the Engle-Granger method,
as a foundation for a mean-reversion pairs trading strategy.

## Method
1. Pull daily close prices for two tickers
2. Regress one on the other (OLS) to get alpha, beta, and residuals
3. Run ADF test on residuals to check for stationarity
4. p < 0.05 → reject null → residuals are stationary → pair is cointegrated

## Results So Far

Pair: JPM & BAC
Alpha: 15.15
Beta: 0.12
ADF stat: -1.93
P-Value: 0.316
Cointegration?: No

Pair: XOM & CVX
Alpha: 38.24
Beta: 1.02
ADF stat: -3.23
P-Value: 0.018
Cointegration?: Yes


## Notes
JPM/BAC: Weak beta 0.12. This suggests a looser relationship than what you'd expect from two large banks; These banks are not co-integrated
XOM/CVX: beta near 1 makes economic sense because these two companies are similar sized and have similar exposure to commodities. These companies are co-integrated at the 5% significance level