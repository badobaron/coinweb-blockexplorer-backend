import json

import requests

from core.connection import URL, HEADERS, AUTH


# Get all assets list
def get_all_assets(quantity_of_assets=10, offset=3):
    """
    Get all assets. Offset is equals 3 to exclude BTC,XCP,FRYE assets

    :param quantity_of_assets: quantity of assets
    :param offset: offset for the list of assets
    :type quantity_of_assets: int
    :type offset: int
    :return assets: JSON string of all assets
    :rtype assets: JSON
    """
    # Preparing data
    payload = {"method": "get_assets",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'order_by': 'asset_id', 'limit': quantity_of_assets, 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    assets_names = []
    for i in data['result']:
        assets_names.append(i['asset_name'])

    return get_assets_info(assets_names)


# Function which is used in get_all_assets, get_named_assets, get_sub_assets, get_numeric_assets.
# Return description about given assets names
def get_assets_info(names):
    """
    Get info about given assets type.

    :param names: names of assets
    :type names: list of stings
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
    payload = {"method": "get_asset_info",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'assets': names}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)
    return json.dumps(data['result'])


# Get named assets list
def get_named_assets(quantity_of_assets=10, offset=0):
    """
        Get named assets.

        :param quantity_of_assets: quantity of assets
        :param offset: offset for the list of assets
        :type quantity_of_assets: int
        :type offset: int
        :return assets: JSON string of named assets
        :rtype assets: JSON
    """
    payload = {"method": "get_asset_names",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)
    for index, asset in enumerate(data['result']):
        if asset.isalpha():
            break
    # To exclude key error
    start = index + offset if index + offset < len(data['result']) else len(data['result'])
    end = start + quantity_of_assets if start + quantity_of_assets < len(data['result']) else len(data['result'])

    named_assets = data['result'][index:end]
    return get_assets_info(named_assets)


# Get subassets list
def get_sub_assets(quantity_of_assets=10, offset=0):
    """
    Get subassets.

    :param quantity_of_assets: quantity of subassets
    :param offset: offset for the list of subassets
    :type quantity_of_assets: int
    :type offset: int
    :return assets: JSON sting of subassets
    :rtype assets: JSON
    """
    # Preparing data
    payload = {"method": "get_assets",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'order_by': 'asset_longname', 'limit': quantity_of_assets, 'offset': offset,
                         "filters": [{"field": "asset_longname", "op": "!=", "value": "None"}]
                         }
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    assets_names = []
    for i in data['result']:
        name = i['asset_longname']
        assets_names.append(name)
    return get_assets_info(assets_names)


# Numeric assets
def get_numeric_assets(quantity_of_assets=10, offset=0):
    """
        Get numeric assets.

        :param quantity_of_assets: quantity of assets
        :param offset: offset for the list of assets
        :type quantity_of_assets: int
        :type offset: int
        :return assets: JSON string of numeric assets
        :rtype assets: JSON
    """
    payload = {"method": "get_asset_names",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    for index, asset in enumerate(data['result']):
        if asset.isalpha():
            break
    # To exclude key error
    start = offset if offset < index else index
    end = start + quantity_of_assets if start + quantity_of_assets < index else index

    numeric_assets = data['result'][start:end]
    return get_assets_info(numeric_assets)
