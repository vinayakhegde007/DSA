"""Tests for the Portfolio module."""

import unittest
from src.portfolio import Portfolio


class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.portfolio = Portfolio()

    def test_add_stock(self):
        self.portfolio.add_stock("AAPL", shares=10, purchase_price=150.0)
        self.assertIn("AAPL", self.portfolio.holdings)
        self.assertEqual(self.portfolio.holdings["AAPL"]["shares"], 10)
        self.assertEqual(self.portfolio.holdings["AAPL"]["purchase_price"], 150.0)

    def test_remove_stock(self):
        self.portfolio.add_stock("AAPL", shares=10, purchase_price=150.0)
        self.portfolio.remove_stock("AAPL")
        self.assertNotIn("AAPL", self.portfolio.holdings)

    def test_remove_nonexistent_stock(self):
        self.portfolio.remove_stock("FAKE")  # Should not raise

    def test_total_cost(self):
        self.portfolio.add_stock("AAPL", shares=10, purchase_price=150.0)
        self.portfolio.add_stock("GOOGL", shares=5, purchase_price=2800.0)
        expected = (10 * 150.0) + (5 * 2800.0)
        self.assertEqual(self.portfolio.total_cost(), expected)

    def test_total_cost_empty(self):
        self.assertEqual(self.portfolio.total_cost(), 0)

    def test_returns_empty_portfolio(self):
        self.assertEqual(self.portfolio.returns(), 0.0)


if __name__ == "__main__":
    unittest.main()
