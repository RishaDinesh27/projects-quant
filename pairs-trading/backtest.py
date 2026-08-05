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


def compute_transaction_costs(signals, gs_shares_list, ms_shares_list, close_prices, ticker_x, ticker_y, transaction_cost = 0.0005):
    transaction_costs = []

    for i in range(len(signals)):
        if i > 0 and signals[i] == 0 and signals[i-1] != 0:
                    cost = (abs(gs_shares_list[i-1] * close_prices[ticker_x].iloc[i]) + abs(ms_shares_list[i-1] * close_prices[ticker_y].iloc[i])) * transaction_cost
                    transaction_costs.append(cost)
        elif i > 0 and signals[i] != signals[i-1]:
                    cost = (abs(gs_shares_list[i] * close_prices[ticker_x].iloc[i]) + abs(ms_shares_list[i] * close_prices[ticker_y].iloc[i])) * transaction_cost
                    transaction_costs.append(cost)
        else:
            transaction_costs.append(0)

    return transaction_costs