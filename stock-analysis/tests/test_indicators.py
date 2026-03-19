"""Tests for the TechnicalIndicators module."""

import unittest
import pandas as pd
import numpy as np
from src.indicators import TechnicalIndicators


class TestTechnicalIndicators(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        prices = 100 + np.cumsum(np.random.randn(100) * 2)
        self.data = pd.DataFrame({
            "Close": prices,
            "Open": prices - 1,
            "High": prices + 2,
            "Low": prices - 2,
            "Volume": np.random.randint(1000, 10000, 100),
        })
        self.indicators = TechnicalIndicators(self.data)

    def test_sma(self):
        sma = self.indicators.sma(window=20)
        self.assertEqual(len(sma), 100)
        self.assertTrue(sma.iloc[:19].isna().all())
        self.assertFalse(sma.iloc[19:].isna().any())

    def test_ema(self):
        ema = self.indicators.ema(window=20)
        self.assertEqual(len(ema), 100)
        self.assertFalse(ema.isna().any())

    def test_rsi(self):
        rsi = self.indicators.rsi(period=14)
        self.assertEqual(len(rsi), 100)
        valid_rsi = rsi.dropna()
        self.assertTrue((valid_rsi >= 0).all() and (valid_rsi <= 100).all())

    def test_macd(self):
        macd_line, signal_line, histogram = self.indicators.macd()
        self.assertEqual(len(macd_line), 100)
        self.assertEqual(len(signal_line), 100)
        self.assertEqual(len(histogram), 100)

    def test_bollinger_bands(self):
        upper, middle, lower = self.indicators.bollinger_bands(window=20)
        valid_idx = middle.dropna().index
        self.assertTrue((upper[valid_idx] >= middle[valid_idx]).all())
        self.assertTrue((middle[valid_idx] >= lower[valid_idx]).all())


if __name__ == "__main__":
    unittest.main()
