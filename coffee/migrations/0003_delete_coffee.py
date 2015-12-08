# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_auto_20151127_0016'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coffee',
        ),
    ]
