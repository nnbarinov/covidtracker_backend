import requests
import covidtracker
from covidtracker.models import CVData, Countries
from covidtracker.serialaizers import CVDataSerialaizer, CountriesSerialaizer
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sqlite3
from datetime import date, timedelta
import requests

# Create your views here.
class CVDataViewSet(ModelViewSet):
    queryset = CVData.objects.all()
    serializer_class = CVDataSerialaizer
    filter_backends  = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['country_code']
    ordering_fields = ['date_value']

class CountriesViewSet(ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerialaizer
    filter_backends  = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['country_name']
    ordering_fields = ['country_name']

def get_data():
    conn = sqlite3.connect("db.sqlite3")
    first_date = '2022-02-01'
    renew_date = date.today()
    query = 'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/' + first_date + '/' + str(renew_date)
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


@api_view(['GET', 'POST'])
def renew_data(request):
    get_data()
    return Response("Data has updated!")
