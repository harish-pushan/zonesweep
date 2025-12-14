from modules.cli import process_arguments
from modules.wayback.wayback import way_back_assets
from modules.ip_info.censys import return_ip_info_censys

from modules.apikeys import return_apikeys
def main():
    process_arguments()

if __name__ == "__main__":
    main()