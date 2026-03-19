"""Technical indicator calculations for stock data."""

import pandas as pd
import numpy as np


class TechnicalIndicators:
    """Calculate common technical indicators from OHLCV data."""

    def __init__(self, data):
        """Initialize with a DataFrame containing at least a 'Close' column.

        Args:
            data: pandas DataFrame with stock OHLCV data.
        """
        self.data = data

    def sma(self, window=20):
        """Simple Moving Average.

        Args:
            window: Number of periods for the moving average.

        Returns:
            pandas Series with SMA values.
        """
        return self.data["Close"].rolling(window=window).mean()

    def ema(self, window=20):
        """Exponential Moving Average.

        Args:
            window: Number of periods for the moving average.

        Returns:
            pandas Series with EMA values.
        """
        return self.data["Close"].ewm(span=window, adjust=False).mean()

    def rsi(self, period=14):
        """Relative Strength Index.

        Args:
            period: Number of periods for RSI calculation.

        Returns:
            pandas Series with RSI values (0-100).
        """
        delta = self.data["Close"].diff()
        gain = delta.where(delta > 0, 0.0)
        loss = -delta.where(delta < 0, 0.0)

        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()

        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def macd(self, fast=12, slow=26, signal=9):
        """Moving Average Convergence Divergence.

        Args:
            fast: Fast EMA period.
            slow: Slow EMA period.
            signal: Signal line EMA period.

        Returns:
            Tuple of (macd_line, signal_line, histogram) as pandas Series.
        """
        ema_fast = self.data["Close"].ewm(span=fast, adjust=False).mean()
        ema_slow = self.data["Close"].ewm(span=slow, adjust=False).mean()
        macd_line = ema_fast - ema_slow
        signal_line = macd_line.ewm(span=signal, adjust=False).mean()
        histogram = macd_line - signal_line
        return macd_line, signal_line, histogram

    def bollinger_bands(self, window=20, num_std=2):
        """Bollinger Bands.

        Args:
            window: Moving average window.
            num_std: Number of standard deviations for the bands.

        Returns:
            Tuple of (upper_band, middle_band, lower_band) as pandas Series.
        """
        middle = self.sma(window)
        std = self.data["Close"].rolling(window=window).std()
        upper = middle + (std * num_std)
        lower = middle - (std * num_std)
        return upper, middle, lower
