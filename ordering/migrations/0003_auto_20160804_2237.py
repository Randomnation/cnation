# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-04 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0002_auto_20160804_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
