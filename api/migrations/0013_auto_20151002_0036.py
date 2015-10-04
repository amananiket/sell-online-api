# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20151002_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='storePic',
            field=models.ImageField(default=1, upload_to=b'/home/aaniket/dev/storeDiscoveryAPI/media/images'),
        ),
        migrations.AlterField(
            model_name='storeitem',
            name='itemPic',
            field=models.ImageField(default=1, upload_to=b'/home/aaniket/dev/storeDiscoveryAPI/media/images'),
        ),
    ]
