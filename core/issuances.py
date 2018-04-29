import json

import requests

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate issuances time
def get_issuances(quantity_of_issuances=10, offset=0):
    """
    Get info about issuances

    :param quantity_of_issuances: quantity of issuances
    :param offset: offset for the list of issuances
    :type quantity_of_issuances: int
    :type offset: int
    :return assets: list of issuances
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_issuances",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_issuances, 'order_by': 'block_index', 'order_dir': 'DESC',
                         'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    return json.dumps(data['result'])
