def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss.replace(0, 1)  # Avoid division by zero
    rsi = 100 - (100 / (1 + rs))

    return rsi


class RSI_Strategy:
    def __init__(self, data, rsi_period=14, rsi_buy_threshold=30, rsi_sell_threshold=70):
        self.data = data
        self.rsi_period = rsi_period
        self.rsi_buy_threshold = rsi_buy_threshold
        self.rsi_sell_threshold = rsi_sell_threshold

    def generate_signals(self):
        rsi_values = calculate_rsi(self.data['Close'], self.rsi_period)
        buy_signals = (rsi_values < self.rsi_buy_threshold)
        sell_signals = (rsi_values > self.rsi_sell_threshold)

        return buy_signals, sell_signals