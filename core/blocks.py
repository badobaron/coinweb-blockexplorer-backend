import json

import requests

from core.connection import URL, HEADERS, AUTH

from core.timeCalculation import calculate_time


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
    payload = {"method": "get_running_info",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }

    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)
    last_block_index = data['result']['last_block']['block_index']
    blocks = [block for block in range(last_block_index, last_block_index - quantity_of_blocks, -1)]

    payload['method'] = 'get_blocks'
    payload['params'] = {
        'block_indexes': blocks
    }
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)

    data = json.loads(response.text)

    data = calculate_time(data, 'blocks')

    return json.dumps(data['result'])
