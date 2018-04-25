import json
import requests
from core.connection import URL, HEADERS, AUTH

# Get all assets list
def get_assets(count):

    # Payload template
    payload = {
        'method': 'get_assets',
        'params': {},
        'jsonrpc': '2.0',
        'id': 0,
    }

    # Update params
    payload['params'] = {
        'limit': count,
    }

    # Forming response
    response = requests.post(
        URL,
        data=json.dumps(payload),
        headers=HEADERS,
        auth=AUTH
    )

    # Print raw response to console
    print(response.text)