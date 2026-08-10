# Pairs Trading

## Overview
Testing candidate pairs for cointegration using the Engle-Granger method,
as a foundation for a mean-reversion pairs trading strategy.

## Method
1. Pull daily close prices for two tickers
2. Regress one on the other (OLS) to get alpha, beta, and residuals
3. Run ADF test on residuals to check for stationarity
4. p < 0.05 → reject null → residuals are stationary → pair is cointegrated

--------------------------------------------------------------------------------

## Results So Far

Pair: JPM/BAC
Alpha: 15.15
Beta: 0.12
ADF stat: -1.93
P-Value: 0.316
Cointegrated?: No

Pair: XOM/CVX
Alpha: 38.24
Beta: 1.02
ADF stat: -3.23
P-Value: 0.018
Cointegrated?: ~~Yes~~  No. Further testing concludes that these two stocks
are not cointegrated. Updated reasoning under ADF Bias Limitation

Trace statistics: [8.55218803e+00 6.81789653e-03]
Critical values: [[13.4294 15.4943 19.9349]
[2.7055  3.8415  6.6349]]
Estimated Half-Life: 71.19868789765397
Cointegration Test Statistic: -3.229971134220717, p-value: 0.06505701188231364

--------------------------------------------------------------------------------

## Pair for Week 2 Signal and Strategy Logic

Pair: GS/MS
Alpha: 21.352894511383894
Beta: 0.17585776053067717
ADF Test Statistic: -3.689992145826318
p-value: 0.004256146119111804

Are the two series cointegrated? Yes

Trace statistics: [15.19141894  1.35211977]
Critical values: [[13.4294 15.4943 19.9349]
 [2.7055  3.8415  6.6349]]

Estimated Half-Life: 25.766167200664857
Cointegration Test Statistic: -3.6916295631023948
p-value: 0.018784364494598402

- For this pair, I changed the date range to 2022-01-01 to remove the volatile
COVID period. The ADF test and the `coint()` test actually agree here, both
suggesting cointegration. The ADF p-value being 0.004 and the `coint()` p-value
being 0.019, both below the 0.05 significance level. Notably, `coint()` is meant
to correct for the ADF test's known limitation, so their agreement here is
surprising and different compared to how it disagreed on the XOM/CVX pair. The
Johansen test, however, showed a trace statistic of 15.19 — just short of the 95%
critical value of 15.49 — falling just outside the range needed to confirm
cointegration at that confidence level.

Tested other pairs, COP/EOG, WFC/USB, and MPC/VLO however none showed a close
agreement between `coint()` and Johansen

--------------------------------------------------------------------------------

## Notes
JPM/BAC: Weak beta 0.12. This suggests a looser relationship than what you'd
expect from two large banks; these banks are not cointegrated

XOM/CVX: Beta near 1 makes economic sense because these two companies are
similar sized and have similar exposure to commodities.

~~These companies are cointegrated at the 5% significance level.~~

Not cointegrated once corrected for generated-regressor bias.
See ADF Bias Limitation section.

## ADF Bias Limitation

At first, the plain Engle-Granger test (adfuller) suggested XOM/CVX was
cointegrated. But when we ran the Johansen test and the corrected
cointegration test, both failed to reject the null hypothesis, meaning
they did not find evidence of cointegration.

The reason for this disagreement comes down to a known weakness in the
plain adfuller test. It does not correct for the fact that the residuals
being tested come from an estimated regression, not raw observed data.
This causes it to systematically overstate significance in this exact
setup.

Since the Johansen test and the corrected cointegration test both catch
this edge case and agree with each other, they're the more trustworthy
result here, allowing me to come to the conclusion that XOM/CVX are actually
not cointegrated.


## Look-Ahead Bias

Currently present in my code is look-ahead bias, which I have audited
today and will fix on an upcoming date. The look-ahead bias is present in
the `run_regression()` function, as it runs the regression once and then
generates values used in other functions. The beta value generated uses
data from the entire dataset all at once, rather than just data available
up to that point in time. This can't be ideal for backtesting, because a
backtester can only use data that would be available at that time, so
using the whole dataset at once can inflate or deflate the beta values and
subsequent results.

Other functions such as `compute_zscore()`, `generate_signals()`, and
`generate_positions()` don't have this issue, because they are looking
at values that are used from the current day and previous days,
not ones that look forward.

--------------------------------------------------------------------------------

## Failure Modes and Limitations

The issue was that the beta was originally calculated using the entire dataset,
therefore giving the best fit relationship between GS and MS throughout the whole
period, not just the data that would've been available at the time. This means
that beta reflected information that wouldn't have been known during that period
making subsequent calculations unrealistic and affected by the look-ahead bias.
Walk-forward validation removes this with the use of a 126 day training period
and a 21 day testing period, the latter estimated with the pair's 28 day half life
in mind. This in turn re-estimates beta every training period with only past data
at each step revealing a Sharpe Ratio of -0.10 and a win rate of 44% unlike the
previous 0.35 and 63% respectively. The updated metrics from the walk-forward
validation further confirms the fact that the previous metrics were inflated due
to a beta influenced by look-ahead bias.

## Buy and Hold Benchmarking

The strategy being tested should be able to beat a simple buy and hold baseline;
otherwise, the added complexity, time and effort of the strategy is not justified
if better results can be achieved with a simpler, more passive approach.
The buy and hold performed significantly better than the pairs trading strategy,
since buy and hold is a strategy that benefits directly from the direction of the
market. Therefore the upward trend seen in GS and MS over this period is why this
strategy achieved a Sharpe of 0.94. In contrast, pairs trading relies on mean
reversion, going long on one stock and short on the other. This means that the
shared directional movement of the stocks largely cancels out between the long and
short legs, showcasing the relative directional difference in how each stock moved
rather than the overall market direction itself. In other words both strategies
answer different questions, one about market direction while the other about
relative mean reversion.

--------------------------------------------------------------------------------

## Conclusion

Honestly finding a cointegrated pair at the 95% confidence level was difficult,
5 out of 6 candidates failed and even the candidate chosen was one that satisfied
the `coint()` and ADF tests, with a trace value just short of the level
needed for the Johansen test. The backtest, when not tested for look-ahead
bias, was mediocre with a Sharpe of 0.35 and win rate of 63%. It seemed that
if I wanted to test it further, it would be a plausible option. However, once I
adjusted for the look-ahead bias in the walk-forward version, the Sharpe was
-0.10 and the win rate was 44%, worse than a coin flip. Both underperformed the buy
and hold benchmark's Sharpe of 0.94 signaling to me that the strategy
presented would not be one I would test with real capital.