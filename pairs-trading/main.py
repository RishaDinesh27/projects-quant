from data_pull import get_prices
from engle_granger import run_regression, run_adf_test, check_cointegration, run_coint_test
from johansen import run_johansen
from half_life import estimate_half_life


close_prices = get_prices(["XOM", "CVX"], "2020-01-01")

alpha, beta, residuals = run_regression(close_prices, "XOM", "CVX")
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

test_statistic_coint, p_value_coint = run_coint_test(close_prices, "XOM", "CVX")
print(f"Cointegration Test Statistic: {test_statistic_coint}, p-value: {p_value_coint}")