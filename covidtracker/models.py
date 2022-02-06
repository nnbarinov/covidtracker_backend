from django.db import models

# Create your models here.
class covid_data(models.Model):
    class Meta:
        unique_together = (('date_value', 'country_code'),)
    date_value        = models.DateField()
    country_code      = models.CharField(max_length=4)
    confirmed         = models.IntegerField()
    deaths            = models.IntegerField()
    stringency_actual = models.DecimalField(max_digits=5,decimal_places=2)
    stringency        = models.DecimalField(max_digits=5,decimal_places=2)