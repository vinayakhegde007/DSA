"""Tests for the StockFetcher module."""

import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from src.fetcher import StockFetcher


class TestStockFetcher(unittest.TestCase):

    def setUp(self):
        self.fetcher = StockFetcher()

    @patch("src.fetcher.yf.Ticker")
    def test_get_stock_data_with_period(self, mock_ticker):
        mock_stock = MagicMock()
        mock_stock.history.return_value = pd.DataFrame({
            "Close": [150.0, 151.0, 152.0],
            "Open": [149.0, 150.0, 151.0],
            "High": [153.0, 154.0, 155.0],
            "Low": [148.0, 149.0, 150.0],
            "Volume": [1000, 1100, 1200],
        })
        mock_ticker.return_value = mock_stock

        data = self.fetcher.get_stock_data("AAPL", period="1mo")

        mock_ticker.assert_called_once_with("AAPL")
        mock_stock.history.assert_called_once_with(period="1mo")
        self.assertEqual(len(data), 3)

    @patch("src.fetcher.yf.Ticker")
    def test_get_stock_data_with_dates(self, mock_ticker):
        mock_stock = MagicMock()
        mock_stock.history.return_value = pd.DataFrame({"Close": [100.0]})
        mock_ticker.return_value = mock_stock

        data = self.fetcher.get_stock_data("TSLA", start="2025-01-01", end="2025-06-01")

        mock_stock.history.assert_called_once_with(start="2025-01-01", end="2025-06-01")

    @patch("src.fetcher.yf.Ticker")
    def test_get_multiple_stocks(self, mock_ticker):
        mock_stock = MagicMock()
        mock_stock.history.return_value = pd.DataFrame({"Close": [100.0]})
        mock_ticker.return_value = mock_stock

        results = self.fetcher.get_multiple_stocks(["AAPL", "GOOGL"])

        self.assertIn("AAPL", results)
        self.assertIn("GOOGL", results)
        self.assertEqual(len(results), 2)


if __name__ == "__main__":
    unittest.main()
