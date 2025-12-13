from modules.apikeys import return_apikeys
from modules.sub_domains.securitytrails import change_the_url


import requests

def get_subdomain_form_virustotal(domain):
    domain = change_the_url(domain)
    apikey = return_apikeys('virustotal')


    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    params = {'apikey':apikey,'domain':domain}
    try:
        response = requests.get(url, params=params)
        jdata = response.json()
        domains = sorted(jdata['subdomains'])
        return domains
    except(KeyError):
        return f"No domains found for {domain}" 
        
# returns a list so i am only returing 
    # for domain in domains:
    #     print(domain)
