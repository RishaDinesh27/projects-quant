# Pairs Trading

## Overview
Testing candidate pairs for cointegration using the Engle-Granger method,
as a foundation for a mean-reversion pairs trading strategy.

## Method
1. Pull daily close prices for two tickers
2. Regress one on the other (OLS) to get alpha, beta, and residuals
3. Run ADF test on residuals to check for stationarity
4. p < 0.05 → reject null → residuals are stationary → pair is co-integrated

## Results So Far

Pair: JPM & BAC
Alpha: 15.15
Beta: 0.12
ADF stat: -1.93
P-Value: 0.316
Co-integration?: No

--------------------------------------------------------------------------------
Pair: XOM & CVX
Alpha: 38.24
Beta: 1.02
ADF stat: -3.23
P-Value: 0.018
Co-integration?: ~~Yes~~  No. Further testing concludes that these two stocks
are not co-integrated. Updated reasoning under ADF Bias - Limitation

Trace statistics: [8.55218803e+00 6.81789653e-03]
Critical values: [[13.4294 15.4943 19.9349]
 [2.7055  3.8415  6.6349]]
Estimated Half-Life: 71.19868789765397
Co-integration Test Statistic: -3.229971134220717, p-value: 0.06505701188231364


--------------------------------------------------------------------------------
## Pair for Week 2 Signal and Strategy Logic

Pair: GS & MS
Alpha: 21.352894511383894, Beta: 0.17585776053067717
ADF Test Statistic: -3.689992145826318, p-value: 0.004256146119111804
Are the two series cointegrated? Yes
Trace statistics: [15.19141894  1.35211977]
Critical values: [[13.4294 15.4943 19.9349]
 [2.7055  3.8415  6.6349]]
Estimated Half-Life: 25.766167200664857
Co-integration Test Statistic: -3.6916295631023948, p-value: 0.018784364494598402

- For this pair, I changed the date range to 2022-01-01 to remove the volatile
COVID period. The ADF test and the `coint()` test actually agree here, both
suggesting co-integration. The ADF p-value being 0.004 and the `coint()` p-value
being 0.019, both below the 0.05 significance level. Notably, `coint()` is meant
to correct for the ADF test's known limitation, so their agreement here is
surprising and different compared to how it disagreed on the XOM & CVX pair. The
Johansen test, however, showed a trace statistic of 15.19 — just short of the 95%
critical value of 15.49 — so it falls just outside the range needed to confirm
co-integration at that confidence level.

Tested other pairs, COP & EOG, WFC & USB and MPC & VLO however none showed a close
or any agreement between `coint` or Johansen

## Notes
JPM/BAC: Weak beta 0.12. This suggests a looser relationship than what you'd
expect from two large banks; These banks are not co-integrated

XOM/CVX: beta near 1 makes economic sense because these two companies are
similar sized and have similar exposure to commodities.

~~These companies are co-integrated at the 5% significance level.~~

Not co-integrated once corrected for generated-regressor bias.
See ADF Bias - Limitation section.

## ADF Bias - Limitation

At first, the plain Engle-Granger test (adfuller) suggested XOM/CVX was
co-integrated. But when we ran the Johansen test and the corrected
co-integration test, both failed to reject the null hypothesis. meaning
they did not find evidence of co-integration.

The reason for this disagreement comes down to a known weakness in the
plain adfuller test. It doesn't correct for the fact that the residuals
being tested come from an estimated regression, not raw observed data.
This causes it to systematically overstate significance in this exact
setup.

Since the Johansen test and the corrected co-integration test both catch
this edge case and agree with each other, they're the more trustworthy
result here, allowing me to come to the conclusion that XOM & CVX are actually
not co-integrated.