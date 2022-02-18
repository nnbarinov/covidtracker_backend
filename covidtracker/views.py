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

@api_view(['GET', 'POST'])
def hello_world(request):
    return Response({"message": "Hello, world!"})
