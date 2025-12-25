import argparse
import sys
from modules.output.json_output import get_all_the_api_output
#Get the domain certificates
from modules.certificates.crtsh import requests_cert_from_crtsh
#Dns info
from modules.dns_info.securitytrails import dns_info_security_trails

#Ip info 
from modules.ip_info.censys import return_ip_info_censys

#Buildwithinfo 

from modules.tech_stack.builtwith import BuiltWithInfo

#Wayback info 
from modules.wayback.wayback import way_back_assets

#Urlscan
from modules.urlscan.urlscan import get_result_with_uuid_UrlScan

#Subdomains
from modules.sub_domains.concat_everything import get_all_subdomains

#Certificate 
from modules.certificates.crtsh import requests_cert_from_crtsh

#Api
from modules.apikeys import return_apikeys

def prease_arguments():
    praser = argparse.ArgumentParser(
        description="Zonesweep a simple passive recon tool")

    # adding arguments
    praser.add_argument("Url", help="Target to recon (google.com)")

    praser.add_argument("--subsonly", action='store_true',help="Subdomain enumation switch")

    praser.add_argument("--dnsinfo", action='store_true',help="DNS enumation switch")

    praser.add_argument("--certs", action='store_true', help="Certs switch")

    praser.add_argument("--ipinfo",action='store_true', help="IP Info switch")

    praser.add_argument("--githubleaks", action='store_true',help="Github leaks enumation switch")

    praser.add_argument("--techstack", action='store_true',help="Tech stack enumation switch")

    praser.add_argument("--urlscan", action='store_true',help="Urlscan enumation switch")

    praser.add_argument("--all", action='store_true',help="All option enable switch")

    praser.add_argument("--output", action='store_true',help="Output: --output")

    praser.add_argument("--config", action='store_true',help="Show all the API keys switch")
    
    praser.add_argument("--timestamp", type=int ,help="Timestamp for wayback")
    
    # Display the help menu when positional args is not given by default 
    if len(sys.argv)==1:
        praser.print_help(sys.stderr)
        sys.exit(1)
    

    return praser.parse_args()


def process_arguments():

 
    args = vars(prease_arguments())
    url = args.get("Url")
    timestamp = args.get("timestamp")
    
    for key, value in args.items():

        if key == "timestamp" and isinstance(timestamp,int):
            way_back_assets(url,timestamp)
            exit()
        if key == "subsonly" and value == True:
            get_all_subdomains(url)
            exit()
        if key == "techstack" and value == True:
            BuiltWithInfo(url)
            exit()
        if key == "dnsinfo" and value == True:
            dns_info_security_trails(url)
            exit()
        if key == "certs" and value == True:
            requests_cert_from_crtsh(url)
            exit()
        if key == "ipinfo" and value == True:
            return_ip_info_censys(url)
            exit()
        if key == "urlscan" and value == True:
            get_result_with_uuid_UrlScan(url)
            exit()
        if key == "all" and value == True:
            get_all_the_api_output(url)
            exit()
        if key == "certs" and value == True:
            requests_cert_from_crtsh(url)
            exit()

        

        

        
        


        


