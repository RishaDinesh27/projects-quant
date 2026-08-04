from zscore import compute_zscore, generate_signals, generate_postions




def run_backtest(gs_shares_list, ms_shares_list, close_prices, ticker_x, ticker_y):
    daily_pnl = []

    for i in range(len(gs_shares_list)):
        if i ==0:
            daily_pnl.append(0)
        else:
            daily = gs_shares_list[i-1] * (close_prices[ticker_x].iloc[i] - close_prices[ticker_x].iloc[i-1]) + ms_shares_list[i-1] * (close_prices[ticker_y].iloc[i]-close_prices[ticker_y].iloc[i-1])
            daily_pnl.append(daily)

    return daily_pnl