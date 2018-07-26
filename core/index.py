import json

import requests

from core.connection import URL, HEADERS, AUTH


def get_index_info(pagination_quantity=10, offset=3):
    payload = {"method": "get_element_counts",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    payload['method'] = "get_running_info"
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)

    data['result']['block_index'] = json.loads(response.text)['result']['last_block']['block_index']

    return json.dumps(data['result'])
