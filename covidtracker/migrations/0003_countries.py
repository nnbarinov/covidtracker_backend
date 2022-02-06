# Generated by Django 4.0.2 on 2022-02-06 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidtracker', '0002_alter_covid_data_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(max_length=4)),
                ('country_name', models.CharField(max_length=200)),
            ],
        ),
    ]
