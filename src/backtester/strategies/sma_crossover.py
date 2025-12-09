import sys
from pathlib import Path
import pandas as pd

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from backtester.strategies.rsi_strategy import RSI_Strategy
from backtester.data.downloader import download_data
from backtester.engine import BacktestEngine
from backtester.reporting import generate_report

def calculate_sma(prices, window):
    """Calculate Simple Moving Average"""
    return prices.rolling(window=window).mean()

class SMA_Crossover:
    def __init__(self, data, fast_window=20, slow_window=50):
        self.data = data
        self.fast_window = fast_window
        self.slow_window = slow_window

    def generate_signals(self):
        """Generate buy/sell signals based on SMA crossover"""
        fast_sma = calculate_sma(self.data['Close'], self.fast_window)
        slow_sma = calculate_sma(self.data['Close'], self.slow_window)

        # Buy signal: fast SMA crosses above slow SMA
        buy_signals = (fast_sma > slow_sma) & (fast_sma.shift(1) <= slow_sma.shift(1))
        
        # Sell signal: fast SMA crosses below slow SMA
        sell_signals = (fast_sma < slow_sma) & (fast_sma.shift(1) >= slow_sma.shift(1))

        return buy_signals, sell_signals

def main():
    # User inputs
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2024-12-09"
    initial_capital = 10000
    strategy_type = "sma"  # or "rsi"

    # Download data
    print(f"Downloading data for {ticker}...")
    data = download_data(ticker, start_date, end_date)

    # Select strategy
    if strategy_type == "sma":
        strategy = SMA_Crossover(data, fast_window=20, slow_window=50)
    else:
        strategy = RSI_Strategy(data, rsi_period=14)

    # Run backtest
    print("Running backtest...")
    engine = BacktestEngine(data, strategy, initial_capital)
    results = engine.run()

    # Generate report
    print("\n" + "="*50)
    generate_report(results)
    print("="*50)

if __name__ == "__main__":
    main()