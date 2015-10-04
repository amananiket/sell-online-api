# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_storeitem_itempic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeitem',
            name='itemPic',
            field=models.ImageField(upload_to=b'media/images/'),
        ),
    ]
