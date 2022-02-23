from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from covidtracker.models import CVData, Countries

class CVDataSerialaizer(ModelSerializer):
    class Meta:
        model = CVData
        fields = '__all__'

class CountriesSerialaizer(ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'
