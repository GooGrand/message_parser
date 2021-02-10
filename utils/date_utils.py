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


def save_data(date, offset):
    pass
