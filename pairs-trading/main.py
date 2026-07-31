from data_pull import get_prices
from engle_granger import run_regression, run_adf_test, check_cointegration, run_coint_test
from johansen import run_johansen
from half_life import estimate_half_life
from zscore import compute_zscore, generate_signals, generate_postions
import matplotlib.pyplot as plt

close_prices = get_prices(["GS", "MS"], "2022-01-01")

alpha, beta, residuals = run_regression(close_prices, "GS", "MS")
print(f"Alpha: {alpha}, Beta: {beta}")

test_statistic, p_value = run_adf_test(residuals)
print(f"ADF Test Statistic: {test_statistic}, p-value: {p_value}")

is_cointegrated = check_cointegration(p_value)
print(f"Are the two series cointegrated? {'Yes' if is_cointegrated else 'No'}")

johansen_result = run_johansen(close_prices)
print("Trace statistics:", johansen_result.lr1)
print("Critical values:", johansen_result.cvt)

estimated_half_life = estimate_half_life(residuals)
print(f"Estimated Half-Life: {estimated_half_life}")

test_statistic_coint, p_value_coint = run_coint_test(close_prices, "GS", "MS")
print(f"Cointegration Test Statistic: {test_statistic_coint}, p-value: {p_value_coint}")

zscore = compute_zscore(residuals, window=30)

signal = generate_signals(zscore, entry=2, exit=0.1)

print("Generated Signals:", signal)

gs_shares_list, ms_shares_list = generate_postions(signal, close_prices, beta, 100000, "GS", "MS")
print("GS shares (first 60 days):", gs_shares_list[:60])
print("MS shares (first 60 days):", ms_shares_list[:60])

#plotting zscores
plt.figure(figsize=(10, 5))

plt.plot(zscore)
plt.axhline(0, color='black', lw=2,ls='--')
plt.axhline(2, color='red', lw=2, ls='--')
plt.axhline(-2, color='green', lw=2, ls='--')
plt.title("GS/MS Rolling Z-Score (30-day window)")
plt.xlabel("Time")
plt.ylabel("Z-Score")
plt.show()