# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coffee',
            old_name='order_date',
            new_name='orderDate',
        ),
    ]
