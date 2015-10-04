# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_store_storepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='itemPic',
            field=models.ImageField(upload_to=b'/home/aaniket/dev/storeDiscoveryAPI/media/images'),
        ),
    ]
