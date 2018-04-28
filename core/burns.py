import json

import requests

from core.connection import URL, HEADERS, AUTH


# Todo: undertand how to calculate burn time
def get_burns(quantity_of_bets=10, offset=0):
    """
    Get info about burns

    :param quantity_of_bets: quantity of burns
    :param offset: offset for the list of burns
    :type quantity_of_bets: int
    :type offset: int
    :return assets: list of burns
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_burns",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_bets, 'order_by': 'block_index', 'order_dir': 'DESC', 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    return json.dumps(data['result'])
