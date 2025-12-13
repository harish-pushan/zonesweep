#!/bin/python3

import requests as req
from modules.apikeys import return_apikeys
import json


def BuiltWithInfo(url):
    BuiltWithKey = return_apikeys('builtwith')
    BuiltWithKeyReturnData = {}

# we add xlsx csv and xml too
    ApiRequest = f'https://api.builtwith.com/v21/api.json?KEY={BuiltWithKey}&LOOKUP={url}'
    response = req.get(ApiRequest)
    JsonResponse = response.json()
    #print(JsonResponse['Results'][0]['Result']['Paths'][0]['Technologies'][0]['Name'])
    for value in JsonResponse['Results'][0]['Result']['Paths'][0]['Technologies']:
        #print(value['Name'])
        #print(value['Description'])
        BuiltWithKeyReturnData[value['Name']] = value['Description']
    print(BuiltWithKeyReturnData)

