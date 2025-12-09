import unittest
from src.backtester.engine import Backtester

class TestBacktester(unittest.TestCase):

    def setUp(self):
        self.backtester = Backtester()

    def test_initialization(self):
        self.assertIsNotNone(self.backtester)

    def test_run_backtest(self):
        # Assuming run_backtest method exists and returns a result
        result = self.backtester.run_backtest("AAPL", "2020-01-01", "2020-12-31")
        self.assertIn('final_profit_loss', result)
        self.assertIn('win_loss_rate', result)

    def test_trade_count(self):
        self.backtester.run_backtest("AAPL", "2020-01-01", "2020-12-31")
        self.assertGreater(self.backtester.trade_count, 0)

    def test_portfolio_returns(self):
        self.backtester.run_backtest("AAPL", "2020-01-01", "2020-12-31")
        self.assertIsInstance(self.backtester.portfolio_returns, float)

if __name__ == '__main__':
    unittest.main()