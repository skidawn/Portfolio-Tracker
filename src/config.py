import configparser
import os
import json

_ROOT_DIR = os.getcwd()
_SRC_DIR = os.path.join(_ROOT_DIR, "src")
_LOCAL_DIR = os.path.join(_SRC_DIR, "local")

def _make_local_dir() -> None:
    """Create the local folder. Ignore if already exists."""
    os.makedirs(_LOCAL_DIR, exist_ok=True)

class Ini:
    """Abstract interface for handling .ini files."""
    parser = configparser.ConfigParser()
    _INI_PATH = os.path.join(_LOCAL_DIR, "keys.ini")

    def _make_ini_file(self):
        """Create the .ini file. Ignore if already exists."""
        if not os.path.exists(self.INI_PATH):
            open(self.INI_PATH, "x")
        self.read()

    def __init__(self):
        self._make_ini_file()

    def read(self):
        """Read .ini file to memory."""
        self.parser.read(self.INI_PATH)

    def write(self):
        """Write memory to disk."""
        with open(self.INI_PATH, "w") as ini_file:
            self.parser.write(ini_file)

    def set(self, platform : str, key_value : str, key_name : str = "api_key"):
        """
        Add an API key to the ini configuration, belonging to a platform.

        Args:
            platform (str): The Platform the API key belongs to.
            key_value (str): The API key string value.
            key_name (str): The API key's name. Defaults to 'api_key'. Generally either 'api_key' or 'private_key'.
        """
        if not self.has(platform):
            self.parser.add_section(platform)

        self.parser.set(platform, key_name, key_value)

    def get(self, platform : str, key_name : str = "api_key") -> str:
        """
        Get an API key from the ini configuration.

        Args:
            platform (str): The Platform the API key belongs to.
            key_name (str): The API key to retrieve. Defaults to 'api_key'.

        Returns:
            str: The API key.
        """
        self.parser.get(platform, key_name)
    
    def remove(self, platform : str):
        """
        Remove a Platform and therefore any associated keys.

        Args:
            platform (str): The Platform to remove.
        """
        self.parser.remove_section(platform)

    def has(self, platform : str) -> bool:
        """
        Checks whether the ini configuration has a Platform.

        Args:
            platform (str): The Platform to check for.

        Returns:
            bool: Whether an entry for the Platform exists.
        """
        return self.parser.has_section(platform)
    
class Json:
    """Abstract interface for handling .json files."""
    _JSON_DIR = os.path.join(_LOCAL_DIR, "portfolios")
    
    def _make_json_dir(self):
        """Create a json directory"""
        os.makedirs(self._JSON_DIR)

    def __init__(self):
        self._make_json_dir()


