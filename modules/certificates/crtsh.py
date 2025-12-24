#!/bin/python3
import json 

import requests
from modules.utils import change_the_url


def requests_cert_from_crtsh(domain):
    domain = change_the_url(domain)
    try:
        raw_resopnse = requests.get(f'https://crt.sh/json?q={domain}')
        if raw_resopnse.status_code == 502:
            print("Server side error with crt.sh can't get any certificates")
            print(raw_resopnse.json())
            
        response = raw_resopnse.json()
        for i in response:
            if  i.get('issuer_ca_id') and i.get('issuer_name') and i.get('common_name') and i.get('entry_timestamp') and i.get('not_before') and i.get('not_after'):
                print(f"Issuer ID\t:{i.get('issuer_ca_id')}")
                print(f"Issuer Name\t:{i.get('issuer_name')}")
                print(f"Comman Name\t:{i.get('common_name')}")
                print(f"Entry Timestamp\t:{i.get('entry_timestamp')}")
                print(f"Not Before\t:{i.get('not_before')}")
                print(f"Not After\t:{i.get('not_after')}")
                print("\n\n")



    except(requests.exceptions.JSONDecodeError):
        print("Server side error with crt.sh can't get any certificates")

        


