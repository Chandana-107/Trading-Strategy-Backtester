2# main.py

import yfinance as yf
import pandas as pd
from backtester.data.downloader import download_data

from backtester.strategies.rsi_strategy import RSI_Strategy
from backtester.strategies.sma_crossover import SMA_Crossover
from backtester.engine import BacktestEngine
from backtester.reporting import generate_report

def display_report(report):
    print(report)

def main():
    # Default values for stock ticker and date range
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2024-12-09"
def main():
    # User input for stock ticker and date range
    ticker = input("Enter stock ticker (e.g., AAPL): ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    # Download historical data
    print(f"Downloading data for {ticker}...")
    data = download_data(ticker, start_date, end_date)

    if data.empty:
        print("No data downloaded. Exiting.")
        return

    # Initialize strategies
    print("Running SMA Crossover Strategy...")
    sma_strategy = SMA_Crossover(data, fast_window=20, slow_window=50)
    
    print("Running RSI Strategy...")
    rsi_strategy = RSI_Strategy(data, rsi_period=14)

    # Backtest strategies
    engine_sma = BacktestEngine(data, sma_strategy, initial_capital=10000)
    sma_results = engine_sma.run()
    
    engine_rsi = BacktestEngine(data, rsi_strategy, initial_capital=10000)
    rsi_results = engine_rsi.run()

    # Generate reports
    print("\n" + "="*60)
    print("SMA CROSSOVER STRATEGY RESULTS")
    print("="*60)
    report_sma = generate_report(sma_results)
    display_report(report_sma)


    print("\n" + "="*60)
    print("RSI STRATEGY RESULTS")
    print("="*60)
    report_rsi = generate_report(rsi_results)
    display_report(report_rsi)

if __name__ == "__main__":
    main()