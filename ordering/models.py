from __future__ import unicode_literals
from django.contrib.auth.models import User
from products.models import Product
from django.db import models


class CustomerOrder(models.Model):
    user = models.ForeignKey(User)
    products = models.CharField(max_length=10)
    notes = models.TextField(max_length=500, null=True)
    order_date = models.DateField(auto_now_add=True)
    order_number = models.CharField(max_length=9, unique=True)

    def __unicode__(self):
        return self.order_number
