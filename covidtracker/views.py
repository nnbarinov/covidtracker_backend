from rest_framework.viewsets import ModelViewSet
import covidtracker
from covidtracker.models import covid_data
from covidtracker.serialaizers import covid_dataSerialaizer
import requests
from django.shortcuts import render

# Create your views here.
class covid_dataViewSet(ModelViewSet):
    queryset = covid_data.objects.all()
    serializer_class = covid_dataSerialaizer

""" def get_covid_data(request):
    all_covid_data = {}
    if 'date_from' in request.GET:
        date_from = request.GET['date_from']
        url = 'https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/' + date_from + '/' + date_from
        response = requests.get(url)
        data = response.json()
        covid_data = data['covid_data']

        for i in covid_data:
            cvd_data = data(
                date_value = i['date_value'],
                country_code = i['country_code'],
                confirmed = i['confirmed'],
                deaths = i['deaths'],
                stringency_actual = i['stringency_actual'],
                stringency = i['stringency']
            )
            cvd_data.save()
            all_covid_data = data.objects.all().order_by('-id')

    return render (request, 'index.html', { "all_covid_data": 
    all_covid_data} ) """
