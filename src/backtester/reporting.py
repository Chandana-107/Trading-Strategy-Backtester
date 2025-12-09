from typing import Dict
import pandas as pd

def generate_report(results: Dict) -> pd.DataFrame:
    """
    Generates a report from backtest results.

    Parameters:
    results (dict): The output from BacktestEngine.get_results()

    Returns:
    pd.DataFrame: Summary metrics of the backtest performance.
    """

    trades = results["trades"]
    initial_capital = results["initial_capital"]
    final_value = results["final_portfolio_value"]
    profit = results["profit"]

    win_count = 0
    loss_count = 0

    # Count winning and losing trades
    for trade in trades:
        if trade["type"] in ("SELL", "FORCED SELL") and "profit" in trade:
            if trade["profit"] > 0:
                win_count += 1
            else:
                loss_count += 1

    total_closed_trades = win_count + loss_count
    win_rate = (win_count / total_closed_trades) if total_closed_trades > 0 else 0

    report_data = {
        "Initial Capital": [initial_capital],
        "Final Value": [final_value],
        "Net Profit / Loss": [profit],
        "Total Trades": [len(trades)],
        "Closed Trades Evaluated": [total_closed_trades],
        "Winning Trades": [win_count],
        "Losing Trades": [loss_count],
        "Win Rate (%)": [round(win_rate * 100, 2)]
    }

    return pd.DataFrame(report_data)


def display_report(report_df: pd.DataFrame) -> None:
    """Pretty print the report."""
    print("\n======================== Backtest Summary ========================\n")
    print(report_df.to_string(index=False))
    print("\n================================================================\n")
