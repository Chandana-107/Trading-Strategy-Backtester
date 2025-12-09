# Trading Strategy Backtester

## Overview

The Trading Strategy Backtester is a Python application designed to help traders and developers test their trading strategies using historical stock price data. This project implements various trading strategies, including the SMA Crossover and RSI strategies, allowing users to simulate trades and analyze performance metrics.

## Features

- Download historical stock price data using the `yfinance` library.
- Implement and backtest multiple trading strategies:
  - **SMA Crossover Strategy**
  - **RSI Strategy**
- Track portfolio performance, including:
  - Buy and sell points
  - Portfolio returns (percentage and dollar value)
  - Number of trades
- Generate detailed reports on backtesting results.

## Installation

To get started with the Trading Strategy Backtester, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/trading-backtester.git
   ```

2. Navigate to the project directory:

   ```
   cd trading-backtester
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

To run the backtester, execute the main script:

```
python src/backtester/main.py
```

You will be prompted to enter a stock ticker (e.g., "AAPL") and a date range for the backtest.

## Example

For a practical demonstration of how to use the backtester, refer to the Jupyter notebook located in the `examples` directory:

```
examples/backtest_example.ipynb
```

## Testing

Unit tests are provided to ensure the functionality and correctness of the backtesting engine and trading strategies. To run the tests, use:

```
pytest tests/
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.