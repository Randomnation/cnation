# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_auto_20160804_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_number',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
