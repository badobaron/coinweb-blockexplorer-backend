import json

import requests

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate orders time
def get_orders(quantity_of_orders=10, offset=0):
    """
    Get info about orders

    :param quantity_of_orders: quantity of orders
    :param offset: offset for the list of orders
    :type quantity_of_orders: int
    :type offset: int
    :return assets: list of orders
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_orders",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_orders, 'order_by': 'block_index', 'order_dir': 'DESC', 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    return json.dumps(data['result'])
