import datetime
import json

import requests
from dateutil.relativedelta import relativedelta

from core.connection import URL, HEADERS, AUTH


# Todo: understand how to calculate bet time
def get_bets(quantity_of_bets=10, offset=0):
    """
    Get info about bets

    :param quantity_of_bets: quantity of bets
    :param offset: offset for the list of bets
    :type quantity_of_bets: int
    :type offset: int
    :return assets: list of bets
    :rtype assets: list
    """
    # Preparing data
    payload = {"method": "get_bets",
               "params": {},
               "jsonrpc": "2.0",
               "id": 0
               }
    payload['params'] = {'limit': quantity_of_bets, 'order_by': 'block_index', 'order_dir': 'DESC', 'offset': offset}
    response = requests.post(URL, data=json.dumps(payload), headers=HEADERS, auth=AUTH)
    data = json.loads(response.text)

    # Calculate deadkine and deadlinealt for bet
    now = datetime.datetime.utcnow()
    for i in data['result']:
        bet_time = datetime.datetime.utcfromtimestamp(i['deadline'])
        i['deadline'] = bet_time.strftime('%Y-%m-%d %H:%M:%S')
        time = relativedelta(now, bet_time)
        if time.years:
            if time.years == 1:
                i['deadline_time'] = 'a year ago'
            else:
                i['deadline_time'] = str(time.years) + ' years ago'
        elif time.months:
            if time.months == 1:
                i['deadline_time'] = 'a month ago'
            else:
                i['deadline_time'] = str(time.months) + ' months ago'
        elif time.days:
            if time.days == 1:
                i['deadline_time'] = 'a day ago'
            else:
                i['deadline_time'] = str(time.days) + ' days ago'
        else:
            if time.hours == 1:
                i['deadline_time'] = 'a hour ago'
            else:
                i['deadline_time'] = str(time.hours) + ' hours ago'

    return json.dumps(data['result'])
