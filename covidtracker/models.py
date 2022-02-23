from django.db import models

# Create your models here.
class Countries(models.Model):
    country_code = models.CharField(max_length=4)
    country_name = models.CharField(max_length=200)

class CVData(models.Model):
    uni_key           = models.CharField(max_length=14,primary_key=True)
    date_value        = models.DateField()
    country_code      = models.CharField(max_length=4)
    confirmed         = models.IntegerField()
    deaths            = models.IntegerField()
    stringency_actual = models.DecimalField(max_digits=5,decimal_places=2)
    stringency        = models.DecimalField(max_digits=5,decimal_places=2)