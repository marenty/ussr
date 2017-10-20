from django.db import connection
from collections import namedtuple

def sqlSelect():
    cursor = connection.cursor()

    def namedtuplefetchall(cursor):
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]

    cursor.execute("SELECT * FROM client WHERE id_client = %s", ['1']);
    results = namedtuplefetchall(cursor)
    return results




