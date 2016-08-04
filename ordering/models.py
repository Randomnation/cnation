from __future__ import unicode_literals
from random import randint
from django.contrib.auth.models import User
from products.models import Product
from django.db import models


def order_gen(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

order_nbr = 'SO-' + str(order_gen(6))


class CustomerOrder(models.Model):
    user = models.ForeignKey(User)
    products = models.CharField(max_length=10)
    notes = models.TextField(max_length=500, null=True)
    order_date = models.DateField(auto_now_add=True)
    order_number = models.CharField(max_length=20, unique=True, default=order_nbr)

    def __unicode__(self):
        return self.order_number
