import json

import requests

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate orders time
def get_blocks(quantity_of_blocks=10, offset=0):
    """
    Get info about blocks

    :param quantity_of_blocks: quantity of blocks
    :param offset: offset for the list of blocks
    :type quantity_of_blocks: int
    :type offset: int
    :return assets: list of blocks
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_blocks",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_blocks, 'order_dir': 'DESC', 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    return json.dumps(data['result'])
