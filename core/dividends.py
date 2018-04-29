import json

import requests

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate dividends time
def get_dividends(quantity_of_dividends=10, offset=0):
    """
    Get info about dividends

    :param quantity_of_dividends: quantity of dividends
    :param offset: offset for the list of dividends
    :type quantity_of_dividends: int
    :type offset: int
    :return assets: list of dividends
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_dividends",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_dividends, 'order_by': 'block_index', 'order_dir': 'DESC',
                         'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    return json.dumps(data['result'])
