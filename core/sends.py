import json

import requests

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate sends time
def get_sends(quantity_of_sends=10, offset=0):
    """
    Get info about sends

    :param quantity_of_sends: quantity of sends
    :param offset: offset for the list of sends
    :type quantity_of_sends: int
    :type offset: int
    :return assets: list of sends
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_sends",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_sends, 'order_by': 'block_index', 'order_dir': 'DESC', 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    for i in data['result']:
        print(i)

    return json.dumps(data['result'])

if __name__ == '__main__':
    get_sends()