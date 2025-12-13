# Censys API Example
import requests
import json


def return_ip_info_censys(url):
    api = f"https://search.censys.io/api/v1/search?query={url}&page=1"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.get(api,headers=headers)
    return response.json()




