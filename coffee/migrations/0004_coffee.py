# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0003_delete_coffee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('freeText', models.CharField(max_length=200)),
                ('orderDate', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
