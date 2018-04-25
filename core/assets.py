import json

import requests

from core.connection import URL, HEADERS, AUTH


# Get all assets list
def get_assets_names(count, offset):
    """
    Get names of assets.

    :param count: number of assets
    :param offset: offset for the list of assets
    :type count: int
    :type offset: int
    :return assets: list of assets names
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_assets",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'order_by': 'asset_id', 'limit': count, 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    assets_names = []
    for i in data['result']:
        id = i['asset_id']
        longname = i['asset_longname']
        name = i['asset_name']
        index = i['block_index']
        assets_names.append(name)
    return assets_names


def get_assets(count=10, offset=3):
    """
    Get info about assets. Offset is equals 3 to exclude BTC,XCP,FTPT assets

    :param count: number of assets
    :param offset: offset for the list of
    :type count: int
    :type offset: int
    :return data: JSON string which includes: asset (string): The assets of the asset itself
                                              asset_longname (string): The subasset longname, if any
                                              owner (string): The address that currently owns the asset
                                              divisible (boolean): Whether the asset is divisible or not
                                              locked (boolean): Whether the asset is locked
                                              total_issued (integer): The quantities of the asset issued, in total
                                              description (string): The asset’s current description
                                              issuer (string): The asset’s original owner (i.e. issuer)
    :rtype data: JSON
    """
    list_of_assets_names = get_assets_names(count, offset)
    payload = {"method": "get_asset_info",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'assets': list_of_assets_names}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)
    return json.dumps(data['result'])
