# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='storeItem',
            fields=[
                ('itemID', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('itemName', models.CharField(max_length=50)),
                ('itemPrice', models.FloatField()),
                ('itemPic', models.ImageField(height_field=100, width_field=100, upload_to=b'')),
                ('storeID', models.ForeignKey(to='api.store')),
            ],
        ),
    ]
