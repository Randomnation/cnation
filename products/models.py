from __future__ import unicode_literals
from django.db import models


class Product(models.Model):
    prod_name = models.CharField(max_length=10)
    prod_sku = models.CharField(max_length=100)
    prod_img = models.ImageField(upload_to='products/img')
    prod_desc = models.CharField(max_length=200)
    prod_price = models.DecimalField(max_digits=63, decimal_places=2)

    def __unicode__(self):
        return self.prod_name
