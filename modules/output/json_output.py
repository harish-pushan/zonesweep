#Get the domain certificates
from modules.certificates.crtsh import requests_cert_from_crtsh
#Dns info
from modules.dns_info.securitytrails import dns_info_security_trails

#Ip info 
from modules.ip_info.censys import return_ip_info_censys

# #Buildwithinfo 
# took it out because ran out of credits
# from modules.tech_stack.builtwith import BuiltWithInfo

#Wayback info 
from modules.wayback.wayback import way_back_assets

#Urlscan
from modules.urlscan.urlscan import get_result_with_uuid_UrlScan

#Subdomains
from modules.sub_domains.concat_everything import get_all_subdomains


def get_all_the_api_output(url):
    all_subdomains = get_all_subdomains(url)
    
    cert_from_crtsh = requests_cert_from_crtsh(url)
    dns_info_from_securitytrails = dns_info_security_trails(url)


    urlscan_info = get_result_with_uuid_UrlScan(url)
    return all_subdomains,cert_from_crtsh,dns_info_from_securitytrails,urlscan_info

