import json
import requests
from core.connection import URL, HEADERS, AUTH

# Get all assets list
def get_assets(count):
    # Preparing data
    payload = {'method': 'get_assets', 'params': {}, 'jsonrpc': '2.0', 'id': 0}
    payload['params'] = {'limit': count}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    assets = []
    for i in data['result']:
        id = i['asset_id']
        longname = i['asset_longname']
        name = i['asset_name']
        index = i['block_index']
        assets.append(i)
    return assets