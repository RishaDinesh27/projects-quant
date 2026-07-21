import statsmodels.api as sm #regression
from statsmodels.tsa.stattools import adfuller , coint #adf testing


def run_regression(close_prices, ticker_x, ticker_y):
    y = close_prices[ticker_y]
    x = close_prices[ticker_x]
    
    x_with_const = sm.add_constant(x) #add constant 1 whihc lets for an actual estimate to be added

    model = sm.OLS(y,x_with_const).fit()

    alpha = model.params['const']
    beta = model.params[ticker_x]
    residuals = model.resid

    return alpha, beta, residuals


def run_adf_test(residuals):
    results = adfuller(residuals)
    test_statistic = results[0]
    p_value = results[1]

    return test_statistic, p_value

def check_cointegration(p_value, significance_level = 0.05):
    return p_value < significance_level

def run_coint_test(close_prices, ticker_x, ticker_y):
    y = close_prices[ticker_y]
    x = close_prices[ticker_x]

    results = coint(y, x)
    test_statistic = results[0]
    p_value = results[1]

    return test_statistic, p_value
