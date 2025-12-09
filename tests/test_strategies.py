import unittest
from src.backtester.strategies.sma_crossover import SMA_Crossover
from src.backtester.strategies.rsi_strategy import RSI_Strategy

class TestTradingStrategies(unittest.TestCase):

    def setUp(self):
        self.sma_strategy = SMA_Crossover(fast_period=5, slow_period=20)
        self.rsi_strategy = RSI_Strategy(period=14)

    def test_sma_crossover_buy_signal(self):
        prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        signals = self.sma_strategy.generate_signals(prices)
        self.assertEqual(signals[-1], 'buy')

    def test_sma_crossover_sell_signal(self):
        prices = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        signals = self.sma_strategy.generate_signals(prices)
        self.assertEqual(signals[-1], 'sell')

    def test_rsi_strategy_buy_signal(self):
        prices = [10, 11, 12, 11, 10, 9, 8, 7, 6, 5]
        signals = self.rsi_strategy.generate_signals(prices)
        self.assertEqual(signals[-1], 'buy')

    def test_rsi_strategy_sell_signal(self):
        prices = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        signals = self.rsi_strategy.generate_signals(prices)
        self.assertEqual(signals[-1], 'sell')

if __name__ == '__main__':
    unittest.main()