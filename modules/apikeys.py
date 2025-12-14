import os 
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
load_dotenv(Path(".env"))

def return_apikeys(api_key=None):

    API_KEYS = {
        "security_trails": os.getenv("security_trails"),
        "virustotal": os.getenv('virustotal'),
        "shodan": os.getenv('shodan'),
        "builtwith": os.getenv('builtwith'),
        "way_back_access": os.getenv('way_back_access'),
        "way_back_secret": os.getenv('way_back_secret'),
        "urlscan": os.getenv('urlscan'),
        "alienvault": os.getenv('alienvault'),
        "censys": os.getenv('censys')
    }

    # Case 1: No key provided -> print all
    if api_key is None:
        for key, value in API_KEYS.items():
            print(f"{key}: {value}")
        return None

    # Case 2: Key provided but not in dictionary
    if api_key not in API_KEYS:
        raise KeyError(f"API key '{api_key}' not found.")

    # Case 3: Key valid -> return its value
    return API_KEYS[api_key]
