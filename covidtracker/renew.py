import sqlite3
from datetime import date, timedelta
import requests

def get_maxdate():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql = "SELECT date_value FROM covidtracker_covid_data ORDER BY date_value desc"
    cursor.execute(sql)
    maxdate = str(cursor.fetchone()[0])
    return maxdate

def get_maxid():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql = "SELECT id FROM covidtracker_covid_data ORDER BY id desc"
    cursor.execute(sql)
    maxid = (cursor.fetchone()[0])
    return maxid


def get_data():
    conn = sqlite3.connect("db.sqlite3")
    i = 1
    renew_date = date.today() - timedelta(days=2)
    query = 'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/' + get_maxdate() + '/' + str(renew_date)
    resp = requests.get(query)
    resp = resp.json()
    resp = resp['data']
   
    for dkey in resp:
        for country in resp[dkey]:
            conn.execute("insert INTO covidtracker_covid_data VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (
            i,
            str(resp[dkey][country]['date_value']), 
            str(resp[dkey][country]['country_code']), 
            int(str(resp[dkey][country]['confirmed']).replace('None', '0')),
            int(str(resp[dkey][country]['deaths']).replace('None', '0')), 
            float(str(resp[dkey][country]['stringency_actual']).replace('None', '0')), 
            float(str(resp[dkey][country]['stringency']).replace('None', '0')) ))
            conn.commit()
            i = i + 1
    conn.close

print(get_maxid())