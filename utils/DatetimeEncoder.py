import json
from datetime import date, datetime

class DateTimeEncoder(json.JSONEncoder):
    '''Класс для сериализации записи дат в JSON'''

    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, bytes):
            return list(o)
        return json.JSONEncoder.default(self, o)
