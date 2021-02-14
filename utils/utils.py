from datetime import datetime

def count_offset(date, offset_per_day):
    date = prepare_date(date)
    days_amount = datetime.now() - datetime(int(date['year']), int(date['month']), int(date['day']))
    days = days_amount.days + 1 #in case we have 0 days
    print('Days amount '+str(days))
    return days * int(offset_per_day)

def prepare_date(date):
    today = datetime.today()
    if not date['year']:
        date['year'] = today.year
    if not date['month']:
        date['month'] = today.month
    if not date['day']:
        date['day'] = today.day
    return date


def count_replies(messages):
    replies = {}
    forwards = {}
    for message in messages:
        print(message)
        if 'replies' in message and message['replies'] and message['replies']['replies'] > 2:
            id = message['id']
            reply = message['replies']
            replies[id] = reply['replies']
        if 'forwards' in message and message['forwards']:
            id = message['id']
            forwards[id] = message['forwards']
    return replies, forwards


async def generate_message(sorted, main, type, message):
    if type == 'replies':
        message += 'Most replied messages: \n'
    elif type == 'forwards':
        message += 'Most forwarded messages: \n'
    for key in sorted[:10]:
        item = main[key]
        message += 'https://t.me/lobsters_chat/' + str(key) + ' with result - ' + str(item) + ' ' + str(type) +' \n'
    return message
