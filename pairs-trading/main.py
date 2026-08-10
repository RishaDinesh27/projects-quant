from data_pull import get_prices
from engle_granger import run_regression, run_adf_test, check_cointegration, run_coint_test
from johansen import run_johansen
from half_life import estimate_half_life
from zscore import compute_zscore, generate_signals, generate_postions
from backtest import compute_transaction_costs, run_backtest
from metrics import calculate_sharpe_ratio, compute_max_drawdown, compute_trade_duration, compute_win_rate, compute_turnover
from walk_forward import wak_forward_data_format, walk_forward_validation
import matplotlib.pyplot as plt
import pandas as pd


close_prices = get_prices(["GS", "MS"], "2022-01-01")

print("\n=== Cointegration Analysis ===")

alpha, beta, residuals = run_regression(close_prices, "GS", "MS")

print(f"Alpha: {alpha:.4f}, Beta: {beta:.4f}")

test_statistic, p_value = run_adf_test(residuals)
print(f"ADF Test Statistic: {test_statistic:.4f}, p-value: {p_value:.4f}")

is_cointegrated = check_cointegration(p_value)
print(f"Are the two series cointegrated(ADF-only)? {'Yes' if is_cointegrated else 'No'}")

johansen_result = run_johansen(close_prices)

print("Trace statistics:", johansen_result.lr1.round(4))
print("Critical values:", johansen_result.cvt.round(4))

estimated_half_life = estimate_half_life(residuals)
print(f"Estimated Half-Life: {estimated_half_life:.2f} days")

test_statistic_coint, p_value_coint = run_coint_test(close_prices, "GS", "MS")
print(f"Cointegration Test Statistic: {test_statistic_coint:.4f}, p-value: {p_value_coint:.4f}")



print("\n=== Signal and Backtesting ===")

zscore = compute_zscore(residuals, window=30)

signal = generate_signals(zscore, entry=2, exit=0.1)

gs_shares_list, ms_shares_list = generate_postions(signal, close_prices, beta, 100000, "GS", "MS")

daily_pnl = run_backtest(gs_shares_list, ms_shares_list, close_prices, "GS", "MS")

transaction_costs = compute_transaction_costs(signal, gs_shares_list, ms_shares_list, close_prices, "GS", "MS", transaction_cost=0.0005)

results = pd.DataFrame({
    "signal": signal,
    "gs_shares": gs_shares_list,
    "ms_shares": ms_shares_list,
    "daily_pnl": daily_pnl,
    "transaction_costs": transaction_costs
}, index=close_prices.index)

results["net_pnl"] = results["daily_pnl"] - results["transaction_costs"]
results["daily_returns"] = results["net_pnl"] / 100000 
print(results.round(2).iloc[35:55])

print("\n=== Metrics ===")

sharpe_ratio_full_period = calculate_sharpe_ratio(results["daily_returns"], results["signal"], full_period=True)
print(f"\nSharpe Ratio for the Full Period: {sharpe_ratio_full_period:.4f}")

sharpe_ratio_active_period = calculate_sharpe_ratio(results["daily_returns"], results["signal"], full_period=False)
print(f"\nSharpe Ratio for the Active Period: {sharpe_ratio_active_period:.4f}")

max_drawdown = compute_max_drawdown(results["net_pnl"])
print(f"\nMaximum Drawdown: {max_drawdown:.2f}")

win_rate = compute_win_rate(results["net_pnl"], results["signal"])
print(f"\nWin Rate: {win_rate:.2%}")

turnover = compute_turnover(signal, gs_shares_list, ms_shares_list, close_prices, "GS", "MS", capital=100000)
print(f"\nTurnover: {turnover:.2f}x")

trade_duration_original = compute_trade_duration(results["signal"])
print(f"\nAverage Trade Duration: {trade_duration_original:.2f} days")

print("\n=== Walk-Forward Validation ===")
wf_res = walk_forward_validation(close_prices, "GS", "MS", train_wind=126, test_wind=21, buffer=30)
print(f"\nNumber of Walk-Forward Iterations: {len(wf_res)}")

wf_df = wak_forward_data_format(wf_res, close_prices, "GS", "MS")
wf_df["net_pnl"] = wf_df["daily_pnl"] - compute_transaction_costs(wf_df["signal"], wf_df["gs_shares"], wf_df["ms_shares"], close_prices, "GS", "MS", transaction_cost=0.0005)
wf_df["daily_returns"] = wf_df["net_pnl"] / 100000



print("\n=== Metrics - Walk-Forward ===")

wf_sharpe_ratio_full_period = calculate_sharpe_ratio(wf_df["daily_returns"], wf_df["signal"], full_period=True)
print(f"\nWalk-Forward Sharpe Ratio for the Full Period: {wf_sharpe_ratio_full_period:.4f}")

wf_sharpe_ratio_active_period = calculate_sharpe_ratio(wf_df["daily_returns"], wf_df["signal"], full_period=False)
print(f"\nWalk-Forward Sharpe Ratio for the Active Period: {wf_sharpe_ratio_active_period:.4f}")

wf_max_drawdown = compute_max_drawdown(wf_df["net_pnl"])
print(f"\nWalk-Forward Maximum Drawdown: {wf_max_drawdown:.2f}")

wf_win_rate = compute_win_rate(wf_df["net_pnl"], wf_df["signal"])
print(f"\nWalk-Forward Win Rate: {wf_win_rate:.2%}")

wf_turnover = compute_turnover(wf_df["signal"], wf_df["gs_shares"], wf_df["ms_shares"], close_prices, "GS", "MS", capital=100000)
print(f"\nWalk-Forward Turnover: {wf_turnover:.2f}x")

wf_trade_duration = compute_trade_duration(wf_df["signal"])
print(f"\nWalk-Forward Average Trade Duration: {wf_trade_duration:.2f} days")



print("\n=== Comparison ===")
wf_sharpe_ratio_full_period = calculate_sharpe_ratio(wf_df["daily_returns"], wf_df["signal"], full_period=True)
print(f"\nWalk-Forward Sharpe Ratio for the Full Period: {wf_sharpe_ratio_full_period:.4f}")

wf_sharpe_ratio_active_period = calculate_sharpe_ratio(wf_df["daily_returns"], wf_df["signal"], full_period=False)
print(f"\nWalk-Forward Sharpe Ratio for the Active Period: {wf_sharpe_ratio_active_period:.4f}")

sharpe_ratio_full_period = calculate_sharpe_ratio(results["daily_returns"], results["signal"], full_period=True)
print(f"\nSharpe Ratio for the Full Period: {sharpe_ratio_full_period:.4f}")

sharpe_ratio_active_period = calculate_sharpe_ratio(results["daily_returns"], results["signal"], full_period=False)
print(f"\nSharpe Ratio for the Active Period: {sharpe_ratio_active_period:.4f}")

gs_daily_return = close_prices["GS"].pct_change().dropna()
ms_daily_return = close_prices["MS"].pct_change().dropna()

buy_hold_return = (gs_daily_return  + ms_daily_return) / 2

buy_hold_sharpe_ratio = calculate_sharpe_ratio(buy_hold_return, results["signal"], full_period=True)
print(f"\nBuy-and-Hold Sharpe Ratio for the Full Period: {buy_hold_sharpe_ratio:.4f}")

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