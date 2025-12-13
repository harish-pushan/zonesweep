import requests
from  modules.apikeys import return_apikeys 



def dns_info_security_trails(url):
    api = return_apikeys('security_trails')
    custom_headers = {
        "apikey" : api
    }
    r = requests.get(f'https://api.securitytrails.com/v1/domain/{url}',headers=custom_headers)
    print(r.json())