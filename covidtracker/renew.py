import sqlite3

def get_maxdate():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    sql = "SELECT date_value FROM covidtracker_covid_data ORDER BY date_value desc"
    cursor.execute(sql)
    maxdate = str(cursor.fetchone())
    maxdate = maxdate[2:12]
    return maxdate
