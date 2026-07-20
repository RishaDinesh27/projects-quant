from data_pull import get_prices
from engle_granger import run_regression, run_adf_test, check_cointegration
close_prices = get_prices(["XOM", "CVX"], "2020-01-01")

alpha, beta, residuals = run_regression(close_prices, "XOM", "CVX")
print(f"Alpha: {alpha}, Beta: {beta}")
test_statistic, p_value = run_adf_test(residuals)
print(f"ADF Test Statistic: {test_statistic}, p-value: {p_value}")
is_cointegrated = check_cointegration(p_value)
print(f"Are the two series cointegrated? {'Yes' if is_cointegrated else 'No'}")