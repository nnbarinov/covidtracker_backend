from rest_framework.viewsets import ModelViewSet
import covidtracker
from covidtracker.models import covid_data
from covidtracker.serialaizers import covid_dataSerialaizer

# Create your views here.
class covid_dataViewSet(ModelViewSet):
    queryset = covid_data.objects.all()
    serializer_class = covid_dataSerialaizer