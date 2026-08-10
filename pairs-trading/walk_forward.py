import pandas as pd

from engle_granger import run_regression
from zscore import compute_zscore, generate_signals, generate_postions
from backtest import run_backtest

def walk_forward_validation(close_prices, ticker_x, ticker_y, train_wind = 126, test_wind = 21,buffer = 30):
    start = 0
    results = []

    while start + train_wind + test_wind <= len(close_prices):
        train_data =close_prices.iloc[start:start + train_wind]
        test_data = close_prices.iloc[start+train_wind:start + train_wind + test_wind]

        alpha,beta,residuals = run_regression(train_data, ticker_x, ticker_y)

        combined_data = close_prices.iloc[start+ train_wind - buffer :start + train_wind + test_wind]
        combined_resid = combined_data[ticker_y] - (alpha + beta * combined_data[ticker_x])
        combined_zscore = compute_zscore(combined_resid,buffer)
        test_zscore = combined_zscore[buffer:]

        signals = generate_signals(test_zscore)
        gs_shares_list, ms_shares_list = generate_postions(signals, test_data,beta, 100000, ticker_x, ticker_y)
        daily_pnl_test = run_backtest(gs_shares_list, ms_shares_list, test_data, ticker_x, ticker_y)
        results.append((signals, gs_shares_list, ms_shares_list, daily_pnl_test))
        start += test_wind

    return results

def wak_forward_data_format(wf_res, close_prices,ticker_x,ticker_y):

    signals = []
    gs_shares_list = []
    ms_shares_list = []
    daily_pnl = []

    for fold in wf_res:
        signals.extend(fold[0])
        gs_shares_list.extend(fold[1])
        ms_shares_list.extend(fold[2])
        daily_pnl.extend(fold[3])

    df = pd.DataFrame({
        "signal": signals,
        "gs_shares": gs_shares_list,
        "ms_shares": ms_shares_list,
        "daily_pnl": daily_pnl
    })

    return df
