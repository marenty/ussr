from django.db import connection
from collections import namedtuple
import datetime

def get_calendar(service_code = "WOPO", start = datetime.datetime.now(), finish = datetime.datetime.now() + datetime.timedelta(days = 7)):
    cursor = connection.cursor()

    def namedtuplefetchall(cursor):
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM client") #get_calendar (%s %s %s)", [service_code, start, finish]);
    results = namedtuplefetchall(cursor)
    return results
