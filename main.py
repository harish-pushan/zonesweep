from modules.cli import process_arguments
from modules.wayback.wayback import way_back_assets
from modules.ip_info.censys import return_ip_info_censys
def main():
    return_ip_info_censys('https://google.com')

if __name__ == "__main__":
    main()