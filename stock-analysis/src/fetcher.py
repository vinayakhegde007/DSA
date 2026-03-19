"""Stock data fetching module using Yahoo Finance API."""

import yfinance as yf
import pandas as pd


class StockFetcher:
    """Fetches historical stock data from Yahoo Finance."""

    def get_stock_data(self, ticker, start=None, end=None, period="1y"):
        """Fetch historical stock data for a given ticker.

        Args:
            ticker: Stock ticker symbol (e.g., "AAPL").
            start: Start date string (YYYY-MM-DD). Overrides period if set.
            end: End date string (YYYY-MM-DD).
            period: Data period (e.g., "1d", "5d", "1mo", "1y", "max").

        Returns:
            pandas DataFrame with OHLCV data.
        """
        stock = yf.Ticker(ticker)
        if start:
            data = stock.history(start=start, end=end)
        else:
            data = stock.history(period=period)
        return data

    def get_multiple_stocks(self, tickers, start=None, end=None, period="1y"):
        """Fetch data for multiple tickers.

        Args:
            tickers: List of ticker symbols.
            start: Start date string.
            end: End date string.
            period: Data period.

        Returns:
            Dict mapping ticker to its DataFrame.
        """
        results = {}
        for ticker in tickers:
            results[ticker] = self.get_stock_data(ticker, start, end, period)
        return results

    def get_stock_info(self, ticker):
        """Get general info about a stock.

        Args:
            ticker: Stock ticker symbol.

        Returns:
            Dict with stock information.
        """
        stock = yf.Ticker(ticker)
        return stock.info
