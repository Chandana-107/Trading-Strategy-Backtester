class Portfolio:
    def __init__(self, initial_capital=10000):
        self.initial_capital = initial_capital
        self.positions = {}
        self.cash = initial_capital
        self.total_value = initial_capital
        self.trades = []

    def buy(self, ticker, amount, price):
        if ticker in self.positions:
            self.positions[ticker] += amount
        else:
            self.positions[ticker] = amount
        self.cash -= amount * price
        self.trades.append({'action': 'buy', 'ticker': ticker, 'amount': amount, 'price': price})

    def sell(self, ticker, amount, price):
        if ticker in self.positions and self.positions[ticker] >= amount:
            self.positions[ticker] -= amount
            self.cash += amount * price
            self.trades.append({'action': 'sell', 'ticker': ticker, 'amount': amount, 'price': price})
        else:
            raise ValueError("Not enough shares to sell")

    def calculate_total_value(self, current_prices):
        self.total_value = self.cash
        for ticker, amount in self.positions.items():
            self.total_value += amount * current_prices.get(ticker, 0)
        return self.total_value

    def get_portfolio_summary(self):
        return {
            'cash': self.cash,
            'positions': self.positions,
            'total_value': self.total_value,
            'trades': self.trades
        }