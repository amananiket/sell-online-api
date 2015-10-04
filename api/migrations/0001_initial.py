# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='store',
            fields=[
                ('storeID', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('storeName', models.CharField(max_length=50)),
                ('storeLat', models.FloatField()),
                ('storeLong', models.FloatField()),
                ('storeAddress', models.TextField()),
                ('storeOpenTime', models.CharField(max_length=4)),
                ('storeCloseTime', models.CharField(max_length=4)),
                ('storePhone', models.CharField(max_length=10)),
                ('storeKeywords', models.TextField()),
            ],
        ),
    ]
