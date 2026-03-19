"""Portfolio tracking and analysis module."""

import yfinance as yf


class Portfolio:
    """Track and analyze a stock portfolio."""

    def __init__(self):
        self.holdings = {}

    def add_stock(self, ticker, shares, purchase_price):
        """Add a stock to the portfolio.

        Args:
            ticker: Stock ticker symbol.
            shares: Number of shares purchased.
            purchase_price: Price per share at purchase.
        """
        self.holdings[ticker] = {
            "shares": shares,
            "purchase_price": purchase_price,
        }

    def remove_stock(self, ticker):
        """Remove a stock from the portfolio.

        Args:
            ticker: Stock ticker symbol to remove.
        """
        self.holdings.pop(ticker, None)

    def total_cost(self):
        """Calculate the total cost basis of the portfolio.

        Returns:
            Total amount invested.
        """
        return sum(
            h["shares"] * h["purchase_price"] for h in self.holdings.values()
        )

    def current_prices(self):
        """Fetch current prices for all holdings.

        Returns:
            Dict mapping ticker to current price.
        """
        prices = {}
        for ticker in self.holdings:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            if not hist.empty:
                prices[ticker] = hist["Close"].iloc[-1]
        return prices

    def total_value(self):
        """Calculate the current total portfolio value.

        Returns:
            Current market value of all holdings.
        """
        prices = self.current_prices()
        return sum(
            self.holdings[t]["shares"] * prices.get(t, 0)
            for t in self.holdings
        )

    def returns(self):
        """Calculate portfolio return percentage.

        Returns:
            Return as a percentage.
        """
        cost = self.total_cost()
        if cost == 0:
            return 0.0
        value = self.total_value()
        return ((value - cost) / cost) * 100

    def summary(self):
        """Get a summary of each holding.

        Returns:
            List of dicts with ticker, shares, cost, current value, and gain/loss.
        """
        prices = self.current_prices()
        result = []
        for ticker, info in self.holdings.items():
            current_price = prices.get(ticker, 0)
            cost = info["shares"] * info["purchase_price"]
            value = info["shares"] * current_price
            result.append({
                "ticker": ticker,
                "shares": info["shares"],
                "purchase_price": info["purchase_price"],
                "current_price": current_price,
                "cost": cost,
                "value": value,
                "gain_loss": value - cost,
            })
        return result
