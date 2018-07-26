from dateutil.relativedelta import relativedelta
import datetime


def calculate_time(data, type=None):
    # Calculate date and datealt for broadcast
    now = datetime.datetime.utcnow()

    for i in data['result']:
        if type == 'blocks':
            broadcast_time = datetime.datetime.utcfromtimestamp(i['block_time'])
        else:
            broadcast_time = datetime.datetime.utcfromtimestamp(i['timestamp'])

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

    return data
