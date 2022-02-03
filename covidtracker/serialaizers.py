from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from covidtracker.models import covid_data

class covid_dataSerialaizer(ModelSerializer):
    class Meta:
        model = covid_data
        fields = '__all__'