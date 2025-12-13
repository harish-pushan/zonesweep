from modules.sub_domains.securitytrails import get_subdomains_from_security_trails
from modules.sub_domains.virustotal import get_subdomain_form_virustotal
from modules.sub_domains.shodan import get_subdomains_from_shodan



def get_all_subdomains(url):
    sub_shodan = get_subdomains_from_shodan(url)
    sub_virustotal = get_subdomain_form_virustotal(url)
    sub_security_trails = get_subdomains_from_security_trails(url)
    all_the_subs = []
    list_of_subs = [sub_shodan,sub_security_trails,sub_virustotal]
    for i in list_of_subs:
        if isinstance(i,list):
            all_the_subs+=i
        else:
            continue


    for i in all_the_subs:
        print(i)
