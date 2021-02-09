from datetime import datetime


def count_offset(date, offset_per_day):
    date = prepare_date(date)
    days_amount = datetime.today() - datetime(date['year'], date['month'], date['day'])
    return days_amount * offset_per_day

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
