import pandas

class Portfolio:
    """Interface for a general portfolio."""

    @staticmethod
    def get_attributes(cls : object) -> dict:
        """
        Return the dict of attributes of a class, ignoring attributes starting with '_';
        Effectively returning only public attributes.

        Args:
            cls (object): The object to filter the attributes for.

        Returns:
            dict: Accepted attributes and their associated values.
        """
        attr = {}
        for key, value in cls.__dict__.items():
            # Ignore keys starting with '_'; values that are callable (functions)
            # BUG: 
            # Classmethod bypasses the callable check.
            if not key.startswith('_') and not callable(value):
                attr[key] = value

        return attr

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
        
        @classmethod
        def get(cls):
            return Portfolio.get_attributes(cls)
        
        @staticmethod
        def get_static():
            return Portfolio.get_attributes(Portfolio.Cash)

    class Stock:
        holdings = pandas.DataFrame(columns=[
            "Ticker",
            "Average Price",
            "Current Price"
            "Forex P&L",
            "P&L",
            "Quantity"
        ])

    class Crypto:
        holdings = pandas.DataFrame(columns=[
            "Ticker",
            "Average Price",
            "Current Price",
            "P&L",
            "Quantity"
        ])