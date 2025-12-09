import pandas as pd

class BacktestEngine:
    def __init__(self, data, strategy, initial_capital=10000):
        self.data = data
        self.strategy = strategy
        self.initial_capital = initial_capital
        self.cash = initial_capital
        self.position = None  # Track open position (None or dict)
        self.trades = []

    def _get_price(self, row):
        """Ensure price is always a single float."""
        value = row["Close"]

        if isinstance(value, pd.Series):
            return float(value.iloc[0])  # ensure scalar
        return float(value)

    def run(self):
        buy_signals, sell_signals = self.strategy.generate_signals()

        # --- Ensure signals are Series ---
        if isinstance(buy_signals, pd.DataFrame):
            buy_signals = buy_signals.iloc[:, 0]

        if isinstance(sell_signals, pd.DataFrame):
            sell_signals = sell_signals.iloc[:, 0]

        for i in range(len(self.data)):
            buy_signal = bool(buy_signals.iloc[i]) if not pd.isna(buy_signals.iloc[i]) else False
            sell_signal = bool(sell_signals.iloc[i]) if not pd.isna(sell_signals.iloc[i]) else False

            price = self._get_price(self.data.iloc[i])
            date = self.data.index[i]

            # --- BUY ---
            if buy_signal and self.position is None and self.cash >= price:
                self.position = {"entry_price": price, "date": date}
                self.cash -= price
                self.trades.append({
                    "type": "BUY",
                    "price": price,
                    "date": str(date)
                })

            # --- SELL ---
            elif sell_signal and self.position is not None:
                entry_price = self.position["entry_price"]
                self.cash += price
                self.trades.append({
                    "type": "SELL",
                    "price": price,
                    "date": str(date),
                    "profit": round(price - entry_price, 2)
                })
                self.position = None

        # --- Close open position at end ---
        if self.position is not None:
            final_price = self._get_price(self.data.iloc[-1])
            entry_price = self.position["entry_price"]
            self.cash += final_price

            self.trades.append({
                "type": "FORCED SELL",
                "price": final_price,
                "date": str(self.data.index[-1]),
                "profit": round(final_price - entry_price, 2)
            })

            self.position = None

        return self.get_results()

    def get_results(self):
        return {
            "initial_capital": self.initial_capital,
            "final_portfolio_value": round(self.cash, 2),
            "num_trades": len(self.trades),
            "profit": round(self.cash - self.initial_capital, 2),
            "trades": self.trades
        }
