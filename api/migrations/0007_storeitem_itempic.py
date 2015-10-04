# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_storeitem_itempic'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeitem',
            name='itemPic',
            field=models.ImageField(default=1, height_field=100, width_field=100, upload_to=b'media/images/'),
            preserve_default=False,
        ),
    ]
