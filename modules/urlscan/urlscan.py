#!/bin/python3

import requests
from modules.apikeys import return_apikeys
import time


def get_scan_uuid(url):
    apikey = return_apikeys("urlscan")
    api_url = "https://urlscan.io/api/v1/scan"
    payload = {
        "url": url,
        "visibility": "public",
        "country": "de",
        "tags": ["iloveurlscan", "testing"],
    }
    headers = {"Content-Type": "application/json", "api-key": apikey}
    response = requests.post(api_url, json=payload, headers=headers)

    data = response.json()
    #print(data)
    return data.get("uuid")


def get_result_with_uuid_UrlScan(url):
    apikey = return_apikeys("urlscan")

    scan_id = get_scan_uuid(url)
    time.sleep(10)
    if scan_id:

        url = "https://urlscan.io/api/v1/result/" + scan_id + "/"

        headers = {"api-key": apikey}

        response = requests.get(url, headers=headers)

        data = response.json()
        print(data.get("certificates"))
        #print(data)
    else:
        print("Scan id not val")
