#!/bin/python

import time 

import re
import requests

from modules.apikeys import return_apikeys 
from modules.utils import change_the_url

def get_subdomains_from_security_trails(url):
    url = change_the_url(url)
        
    securit_trails_ap = return_apikeys('security_trails')
    try:
        api_url = f'https://api.securitytrails.com/v1/domain/{url}/subdomains?apikey={securit_trails_ap}'
        response = requests.get(api_url)
        time.sleep(11)
        # So this is returned as dictionary 
        raw_dict = response.json()
        return raw_dict["subdomains"]
        # Implement this in the final run this is future Harish's problem fuck that guy 
    except:
        return ["Api quota ended"]
        


