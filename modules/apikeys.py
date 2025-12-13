
def return_apikeys(api_key=None):

    API_KEYS = {
        "security_trails": "YOURAPI",
        "virustotal": "YOURAPI",
        "shodan": "YOURAPI",
        "builtwith": "YOURAPI",
        "way_back_access": "YOURAPI",
        "way_back_secret": "YOURAPI",
        "urlscan": "YOURAPI",
        "alienvault": "YOURAPI",
        "censys": "YOURSPI"
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
