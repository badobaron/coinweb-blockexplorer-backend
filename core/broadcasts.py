import datetime
import json

import requests
from dateutil.relativedelta import relativedelta

from core.connection import URL, HEADERS, AUTH


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

    # Calculate date and datealt for broadcast
    now = datetime.datetime.utcnow()
    for i in data['result']:
        broadcast_time = datetime.datetime.utcfromtimestamp(i['timestamp'])
        i['timestamp'] = broadcast_time.strftime('%Y-%m-%d %H:%M:%S')
        time = relativedelta(now, broadcast_time)
        if time.years:
            if time.years == 1:
                i['time'] = 'a year ago'
            else:
                i['time'] = str(time.years) + ' years ago'
        elif time.months:
            if time.months == 1:
                i['time'] = 'a month ago'
            else:
                i['time'] = str(time.months) + ' months ago'
        elif time.days:
            if time.days == 1:
                i['time'] = 'a day ago'
            else:
                i['time'] = str(time.days) + ' days ago'
        else:
            if time.hours == 1:
                i['time'] = 'a hour ago'
            else:
                i['time'] = str(time.hours) + ' hours ago'

    return json.dumps(data['result'])
