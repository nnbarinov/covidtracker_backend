import sqlite3
from datetime import date, timedelta
import requests


def get_data():
    conn = sqlite3.connect("db.sqlite3")
    first_date = '2022-01-31'
   # renew_date = date.today() - timedelta(days=2)
    query = 'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/' + first_date + '/2022-02-02' #+ str(renew_date)
    resp = requests.get(query)
    resp = resp.json()
    resp = resp['data']
   
    for dkey in resp:
        for country in resp[dkey]:
            conn.execute("replace INTO covidtracker_CVData VALUES (?, ?, ?, ?, ?, ?, ?)", 
            (
            str(resp[dkey][country]['date_value'])+str(resp[dkey][country]['country_code']),
            str(resp[dkey][country]['date_value']), 
            str(resp[dkey][country]['country_code']), 
            int(str(resp[dkey][country]['confirmed']).replace('None', '0')),
            int(str(resp[dkey][country]['deaths']).replace('None', '0')), 
            float(str(resp[dkey][country]['stringency_actual']).replace('None', '0')), 
            float(str(resp[dkey][country]['stringency']).replace('None', '0')) ))
            conn.commit()
    conn.close

get_data()