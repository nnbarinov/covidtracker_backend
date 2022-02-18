import requests
import covidtracker
from covidtracker.models import covid_data, Countries
from covidtracker.serialaizers import covid_dataSerialaizer, CountriesSerialaizer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend #, OrderingFilter
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sqlite3
from datetime import date, timedelta
import requests

# Create your views here.
class covid_dataViewSet(ModelViewSet):
    queryset = covid_data.objects.all()
    serializer_class = covid_dataSerialaizer
    filter_backends  = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['country_code']
    ordering_fields = ['date_value']

class CountriesViewSet(ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerialaizer
    filter_backends  = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['country_name']
    ordering_fields = ['country_name']

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
    i = get_maxid()+1
    conn = sqlite3.connect("db.sqlite3")
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


@api_view(['GET', 'POST'])
def renew_data(request):
    get_data()
    return Response("Data has updated!")
