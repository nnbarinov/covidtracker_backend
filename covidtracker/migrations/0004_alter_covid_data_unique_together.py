# Generated by Django 4.0.2 on 2022-02-18 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidtracker', '0003_countries'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='covid_data',
            unique_together=set(),
        ),
    ]
