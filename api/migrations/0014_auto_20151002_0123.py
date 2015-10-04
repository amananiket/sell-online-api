# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20151002_0036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='storePic',
        ),
        migrations.RemoveField(
            model_name='storeitem',
            name='itemPic',
        ),
    ]
