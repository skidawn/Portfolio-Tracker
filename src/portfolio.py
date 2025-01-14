import pandas

class Portfolio:
    """Interface for a general portfolio."""

    @staticmethod
    def percentage_change(old : float, new : float) -> float:
        """
        Returns a percentage of the increase of decrease from the old value to the new value.

        Attempting to divide by zero will just return zero.

        Args:
            old (float): The old value.
            new (float): The final value.

        Returns:
            float: The percentage of change or movement from the difference.
        """
        if old == 0: return 0 # ZeroDivisonError
        return ( (new - old) / old ) * 100

    class Cash:
        """Interface for the cash and values in a Portfolio."""
        free = 0 # Free cash
        invested = 0 # Cash currently stored in assets, before price movements.
        profit = 0 # Net cash (or loss) after price movements.
        result = 0 # Realized cash gains or losses.
        total = 0 # Gross cash
        currency_code = "$"