# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20151002_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='storePic',
            field=models.ImageField(upload_to=b'/home/aaniket/dev/storeDiscoveryAPI/media/images'),
        ),
    ]
