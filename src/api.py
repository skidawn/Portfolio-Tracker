import requests

class Platform:
    """General Interface for Brokers and Exchanges subclasses to inherit."""
    # These should be overwritten
    api_key = None 
    private_key = None # Only used by exchanges
    base_url = None

    def request(self, method : str, path : str,) -> dict:
        """
        Make an API request to an endpoint and return the repsonse.

        Args:
            method (str): The action to be performed on data at the endpoint.
            path (str): Absolute url to the API's endpoint.

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
                requests.get(url, headers=headers)

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