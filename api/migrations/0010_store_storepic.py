# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20151002_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='storePic',
            field=models.ImageField(default=1, upload_to=b'/media/images'),
            preserve_default=False,
        ),
    ]
