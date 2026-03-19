"""Stock data visualization module."""

import matplotlib.pyplot as plt
from src.indicators import TechnicalIndicators


class StockVisualizer:
    """Generate charts for stock data and technical indicators."""

    def __init__(self, data, ticker=""):
        """Initialize with stock DataFrame.

        Args:
            data: pandas DataFrame with OHLCV data.
            ticker: Stock ticker for chart titles.
        """
        self.data = data
        self.ticker = ticker
        self.indicators = TechnicalIndicators(data)

    def plot_price(self, save_path=None):
        """Plot closing price over time.

        Args:
            save_path: Optional file path to save the chart.
        """
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data["Close"], label="Close Price")
        plt.title(f"{self.ticker} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_price_with_sma(self, windows=None, save_path=None):
        """Plot closing price with Simple Moving Averages.

        Args:
            windows: List of SMA windows (default: [20, 50]).
            save_path: Optional file path to save the chart.
        """
        if windows is None:
            windows = [20, 50]

        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data["Close"], label="Close Price")
        for w in windows:
            sma = self.indicators.sma(window=w)
            plt.plot(self.data.index, sma, label=f"SMA {w}")
        plt.title(f"{self.ticker} Price with SMA")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_rsi(self, period=14, save_path=None):
        """Plot RSI indicator.

        Args:
            period: RSI period.
            save_path: Optional file path to save the chart.
        """
        rsi = self.indicators.rsi(period=period)

        plt.figure(figsize=(12, 4))
        plt.plot(self.data.index, rsi, label=f"RSI ({period})", color="purple")
        plt.axhline(y=70, color="r", linestyle="--", alpha=0.5, label="Overbought (70)")
        plt.axhline(y=30, color="g", linestyle="--", alpha=0.5, label="Oversold (30)")
        plt.fill_between(self.data.index, 70, 100, alpha=0.1, color="red")
        plt.fill_between(self.data.index, 0, 30, alpha=0.1, color="green")
        plt.title(f"{self.ticker} RSI")
        plt.xlabel("Date")
        plt.ylabel("RSI")
        plt.legend()
        plt.grid(True, alpha=0.3)
        if save_path:
            plt.savefig(save_path)
        plt.show()

    def plot_bollinger_bands(self, window=20, save_path=None):
        """Plot price with Bollinger Bands.

        Args:
            window: Bollinger Band window.
            save_path: Optional file path to save the chart.
        """
        upper, middle, lower = self.indicators.bollinger_bands(window=window)

        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data["Close"], label="Close Price")
        plt.plot(self.data.index, upper, label="Upper Band", linestyle="--", alpha=0.7)
        plt.plot(self.data.index, middle, label="Middle Band", linestyle="--", alpha=0.7)
        plt.plot(self.data.index, lower, label="Lower Band", linestyle="--", alpha=0.7)
        plt.fill_between(self.data.index, upper, lower, alpha=0.1, color="blue")
        plt.title(f"{self.ticker} Bollinger Bands")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.grid(True, alpha=0.3)
        if save_path:
            plt.savefig(save_path)
        plt.show()
