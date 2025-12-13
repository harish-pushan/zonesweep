import json
import requests


def way_back_assets(url,timestamp):
    api_url = f"http://archive.org/wayback/available?url={url}&timestamp={timestamp}"
    
    
    try:
        raw_response = requests.get(api_url)
        json_response = raw_response.json()
        response = json_response
        print(response["archived_snapshots"]["closest"]["url"])

    
    except(json.decoder.JSONDecodeError):
        print(f"Wayback doen't have a url on this timestamp {timestamp}")
    except:
        print(response)