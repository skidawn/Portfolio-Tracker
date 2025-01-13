import requests
from datetime import datetime

class Platform:
    """General Interface for Brokers and Exchanges subclasses to inherit."""
    BASE_URL = None

    def __init__(self, api_key : str, private_key : str = None):
        self.api_key = api_key
        self.private_key = private_key # Only used by exchanges.

    def request(self, method : str, path : str, body : dict = None) -> dict:
        """
        Make an API request to an endpoint and return the repsonse.

        Args:
            method (str): The action to be performed on data at the endpoint.
            path (str): Absolute url to the API's endpoint.
            body (dict): Data to be sent alongside the request.

        Returns:
            dict: The response, None if error.

        Raises:
            ValueError: method arguement is invalid.
        """
        url = self.base_url + path
        headers = self.generate_authorization_headers()

        try:
            response = {}
            if method == "GET":
                response = requests.get(url, headers=headers, params=body)

            elif method == "POST":
                response = requests.post(url, json=body, headers=headers)

            else:
                raise ValueError(f"'{method}' method is unknown.")
            
            return response
        
        except requests.RequestException as e:
            print(f"Error making API request: {e}")
            return {}

    def generate_authorization_headers(self) -> dict:
        """
        Return the appropiate authorization headers to be sent alongside an API request.

        Subclasses must override this method, as it will raise a `NotImplementedError`.
        """
        raise NotImplementedError

class Trading212(Platform):
    """
    Unabstracted API endpoints for the Trading212 Broker Platform.

    Website: https://app.trading212.com
    API Docs: https://t212public-api-docs.redoc.ly/#operation/accountCash
    """
    BASE_URL = "https://live.trading212.com"

    def generate_authorization_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": self.api_key
        }

    # Account Data
    def fetch_account_cash(self):
        return super().request("GET", "/api/v0/equity/account/cash")
    
    def fetch_account_metadata(self):
        return super().request("GET", "/api/v0/equity/account/info")

    # Personal Portfolio
    def fetch_all_open_positions(self):
        return super().request("GET", "/api/v0/equity/portfolio")

    def search_for_a_specific_position_by_ticker(self, ticker : str):
        return super().request("POST", "/api/v0/equity/portfolio/ticker", {"ticker": ticker})

    def fetch_a_specific_position(self, ticker : str):
        return super().request("GET", "/api/v0/equity/portfolio/" + ticker)

    # Historical Items
    def historical_order_data(self, cursor : int = 0, ticker : str = None, limit : int = 50):
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().request("GET", "/api/v0/equity/history/orders", query)

    def paid_out_dividends(self, cursor : int = 0, ticker : str = None, limit : int = 50):
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().request("GET", "/api/v0/history/dividends", query)

    def exports_list(self):
        return super().request("GET", "/api/v0/history/exports")

    def export_csv(self, 
                    includeDividends : bool = True,
                    includeInterest : bool = True,
                    includeOrders : bool = True,
                    includeTransactions : bool = True,
                    timeFrom : datetime = datetime(1970, 1, 1, 0, 0, 0),
                    timeTo : datetime = datetime.now()
                    ):
        payload = {
            "dataIncluded" : {
                "includeDividends": includeDividends,
                "includeInterest": includeInterest,
                "includeOrders": includeOrders,
                "includeTransactions": includeTransactions
            },
            "timeFrom": timeFrom,
            "timeTo": timeTo
        }
        return super().request("POST", "/api/v0/history/exports", payload)

    def transaction_list(self, cursor : int = 0, ticker : str = None, limit : int = 50):
        query = {
            "cursor": cursor,
            "ticker": ticker,
            "limit": limit
        }
        return super().request("GET", "/api/v0/history/transactions", query)