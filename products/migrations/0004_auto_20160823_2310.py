# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-23 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20160823_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_img',
            field=models.ImageField(upload_to='products/img'),
        ),
    ]