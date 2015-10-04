# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_storeitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='storeCategoryID',
            field=models.CharField(default=None, max_length=2),
        ),
    ]
