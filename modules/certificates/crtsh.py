#!/bin/python3


import requests


def requests_cert_from_crtsh(domain):
    
    try:
        raw_resopnse = requests.get(f'https://crt.sh/?q={domain}&output=json')
        if raw_resopnse.status_code == 502:
            print("Server side error with crt.sh can't get any certificates")
        response = raw_resopnse.json()

        raw_items = []
        for i in response:
            for j in i:
                raw_items.append(('issuer_name', j['issuer_name']))
                raw_items.append(('name_value', j['name_value']))
        final_items = list(set(raw_items))

        for i in final_items:
            print(i)
        #for i in final_items:
    except(requests.exceptions.JSONDecodeError):
        print("Server side error with crt.sh can't get any certificates")

        


