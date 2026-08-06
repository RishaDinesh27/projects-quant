import numpy as np

def calculate_sharpe_ratio(daily_returns, signals, full_period = False):

    if full_period:
        return (daily_returns.mean() / daily_returns.std()) * np.sqrt(252)

    else:
        filtered_returns = daily_returns[signals != 0]

        if len(filtered_returns) == 0:
            return 0
        else:
            return (filtered_returns.mean() / filtered_returns.std()) * np.sqrt(252)

def compute_max_drawdown(net_pnl):
    cumulative_pnl = net_pnl.cumsum()
    running_peak = cumulative_pnl.cummax()
    drawdown = cumulative_pnl - running_peak
    max_drawdown = drawdown.min()

    return max_drawdown


def compute_win_rate(net_pnl,signal):
    trade_start = (signal != 0) & (signal.shift(1).fillna(0) == 0)
    trade_id = trade_start.cumsum()
    trade_curr = signal != 0
    trade_pnl = net_pnl[trade_curr].groupby(trade_id[trade_curr]).sum()
    win_rate = (trade_pnl > 0).mean()

    return win_rate

def compute_turnover(signals, gs_shares_list, ms_shares_list, close_prices, ticker_x, ticker_y, capital = 100000):
    total_dollar_traded = 0

    for i in range(len(signals)):
        if i > 0 and signals[i] == 0 and signals[i-1] != 0:
                    cost = (abs(gs_shares_list[i-1] * close_prices[ticker_x].iloc[i]) + abs(ms_shares_list[i-1] * close_prices[ticker_y].iloc[i]))
                    total_dollar_traded += cost
        elif i > 0 and signals[i] != signals[i-1]:
                    cost = (abs(gs_shares_list[i] * close_prices[ticker_x].iloc[i]) + abs(ms_shares_list[i] * close_prices[ticker_y].iloc[i]))
                    total_dollar_traded += cost
        else:
            total_dollar_traded += 0

    return total_dollar_traded / capital

