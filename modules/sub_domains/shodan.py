import shodan
from modules.apikeys import return_apikeys
from modules.sub_domains.securitytrails import change_the_url


def get_subdomains_from_shodan(url):
    url = change_the_url(url)
    api_key = return_apikeys('shodan')
    api = shodan.Shodan(api_key)
    try:
        # Search for subdomains of a specific domain
        domain_info = api.dns.domain_info(url)

        #print(f"Subdomains for {url}")
        return domain_info['subdomains']
        # for subdomain in domain_info['subdomains']:
        #     #print(subdomain)


    except shodan.APIError as e:
        return ["Error:", {e}]