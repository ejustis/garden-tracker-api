# Generated by Django 3.0.5 on 2021-04-11 04:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SunExposure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 4, 10, 21, 37, 30, 518635))),
                ('garden_id', models.CharField(max_length=100)),
                ('lux_value', models.IntegerField()),
            ],
        ),
    ]