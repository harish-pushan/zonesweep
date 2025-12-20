#!/bin/python3

import requests as req
from modules.apikeys import return_apikeys
import json

from modules.utils import change_the_url

def BuiltWithInfo(url):
    url = change_the_url(url)
    BuiltWithKey = return_apikeys('builtwith')
    

# we add xlsx csv and xml too
    apiurl = f"https://api.builtwith.com/free1/api.json?KEY={BuiltWithKey}&LOOKUP={url}"

    response = req.get(apiurl)
    response.raise_for_status()
    json_response = response.json()
    for keys,val in json_response.items():
        if keys =="groups":
            for i in val:
                name_of_service = i.get('name')
                categories = i.get('categories')
                if categories:
                    new_dict = categories[0]
                    service_vendor = new_dict.get('name')
                    print(f"Type of sevice: {name_of_service}\t\tService vendor: {service_vendor}")
               


