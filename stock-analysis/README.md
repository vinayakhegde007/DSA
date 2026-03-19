# Stock Analysis

A Python-based stock analysis toolkit for fetching, analyzing, and visualizing stock market data.

## Features

- **Stock Data Fetching** — Retrieve historical stock data using Yahoo Finance API
- **Technical Indicators** — Calculate SMA, EMA, RSI, MACD, and Bollinger Bands
- **Portfolio Analysis** — Track portfolio performance with returns and risk metrics
- **Visualization** — Generate interactive charts for price trends and indicators

## Project Structure

```
stock-analysis/
├── src/
│   ├── __init__.py
│   ├── fetcher.py          # Stock data fetching
│   ├── indicators.py       # Technical indicator calculations
│   ├── portfolio.py        # Portfolio analysis
│   └── visualizer.py       # Chart generation
├── tests/
│   ├── __init__.py
│   ├── test_fetcher.py
│   ├── test_indicators.py
│   └── test_portfolio.py
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

```python
from src.fetcher import StockFetcher
from src.indicators import TechnicalIndicators
from src.visualizer import StockVisualizer

# Fetch stock data
fetcher = StockFetcher()
data = fetcher.get_stock_data("AAPL", period="1y")

# Calculate indicators
indicators = TechnicalIndicators(data)
data["SMA_20"] = indicators.sma(window=20)
data["RSI"] = indicators.rsi()

# Visualize
viz = StockVisualizer(data)
viz.plot_price_with_sma()
```

## Usage

### Fetching Stock Data

```python
fetcher = StockFetcher()
data = fetcher.get_stock_data("TSLA", start="2025-01-01", end="2025-12-31")
```

### Technical Indicators

```python
indicators = TechnicalIndicators(data)
indicators.sma(window=50)       # Simple Moving Average
indicators.ema(window=20)       # Exponential Moving Average
indicators.rsi(period=14)       # Relative Strength Index
indicators.macd()               # MACD
indicators.bollinger_bands()    # Bollinger Bands
```

### Portfolio Analysis

```python
from src.portfolio import Portfolio

portfolio = Portfolio()
portfolio.add_stock("AAPL", shares=10, purchase_price=150.0)
portfolio.add_stock("GOOGL", shares=5, purchase_price=2800.0)

print(portfolio.total_value())
print(portfolio.returns())
```

## License

MIT
