import json

import requests

from core.connection import URL, HEADERS, AUTH

from core.timeCalculation import calculate_time


def get_broadcasts(quantity_of_broadcasts=10, offset=0):
    """
    Get info about broadcasts

    :param quantity_of_broadcasts: quantity of broadcasts
    :param offset: offset for the list of broadcasts
    :type quantity_of_broadcasts: int
    :type offset: int
    :return assets: list of broadcasts
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_broadcasts",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_broadcasts, 'order_by': 'block_index', 'order_dir': 'DESC',
                         'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    data = calculate_time(data)

    return json.dumps(data['result'])
