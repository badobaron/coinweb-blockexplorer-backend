import datetime
import json

import requests
from dateutil.relativedelta import relativedelta

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate mempool time
# Todo: add if statements in mempool.html for other categories
def get_mempool(quantity_of_mempool=10, offset=0):
    """
    Get info about mempool

    :param quantity_of_mempool: quantity of mempool
    :param offset: offset for the list of mempool
    :type quantity_of_mempool: int
    :type offset: int
    :return assets: list of mempool
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_mempool",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'order_by': 'category', 'order_dir': 'ASC', 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    now = datetime.datetime.utcnow()
    for i in data['result']:
        broadcast_time = datetime.datetime.utcfromtimestamp(i['timestamp'])
        i['date'] = broadcast_time.strftime('%Y-%m-%d %H:%M:%S')
        time = relativedelta(now, broadcast_time)
        if time.months:
            if time.months == 1:
                i['time'] = 'a month ago'
            else:
                i['time'] = str(time.months) + ' months ago'
        elif time.days:
            if time.days == 1:
                i['time'] = 'a day ago'
            else:
                i['time'] = str(time.days) + ' days ago'
        elif time.hours:
            if time.hours == 1:
                i['time'] = 'an hour ago'
            else:
                i['time'] = str(time.hours) + ' hours ago'
        elif time.minutes:
            if time.minutes == 1:
                i['time'] = 'a minute ago'
            else:
                i['time'] = str(time.minutes) + ' minutes ago'
        else:
            if time.seconds == 1:
                i['time'] = 'a second ago'
            else:
                i['time'] = str(time.seconds) + ' seconds ago'
    data = sorted(data['result'], reverse=True, key=lambda item: int(item['timestamp']))

    # To convert innerlevel string into JSON
    for i in data:
        i['bindings'] = json.loads(str(i['bindings']))

    return json.dumps(data) if data else json.dumps(False)
