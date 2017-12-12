import psycopg2
import os
import urllib.request
import json

def fetchExchangeRates():
    password = os.environ.get('AWS_DB_PASS')
    dbname = 'ussr'
    user = 'ks'
    host = 'ussr.ckcaelqjxpvo.eu-west-1.rds.amazonaws.com'
    conn = psycopg2.connect(dbname=dbname, user=user, host=host, password=password)

    rates = dict()
    cursor = conn.cursor()
    cursor.execute("SELECT id_currency FROM currrency")
    currencies = cursor.fetchall()
    
    for c in currencies:
        rates[c[0]] = 1;
    del rates['PLN']

    for k, v in rates.items():
        url = 'http://api.nbp.pl/api/exchangerates/rates/A/' + k + '/'
        sqlStmt =   """UPDATE currrency
                    SET ratio_to_main_currency = %s
                    WHERE id_currency = %s"""

        with urllib.request.urlopen(url) as res:
            data = json.loads(res.read().decode())
            rates[k] = (data['rates'][0]['mid'])
            cursor.execute(sqlStmt, [rates[k], k])

    conn.commit()
    cursor.close()
