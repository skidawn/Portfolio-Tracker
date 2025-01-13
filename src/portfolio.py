import pandas

class Portfolio:
    """Interface for a general portfolio."""

    class Cash:
        """Interface for the cash and values in a Portfolio."""
        free = 0 # Free cash
        invested = 0 # Cash currently stored in assets, before price movements.
        profit = 0 # Net cash (or loss) after price movements.
        result = 0 # Realized cash gains or losses.
        total = 0 # Gross cash
        currency_code = "$"