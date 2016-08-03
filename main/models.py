from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save


class Product(models.Model):
    prod_name = models.CharField(max_length=10)
    prod_sku = models.CharField(max_length=100)
    prod_img = models.ImageField(upload_to='media/images', blank=True)
    prod_desc = models.CharField(max_length=200)
    prod_price = models.IntegerField()


cust_order_number = 

class CustomerOrder(models.Model):
    user = models.OneToOneField(User, related_name='user')
    products = models.CharField(max_length=10, choices=Product)
    order_date = models.DateField(auto_created=True)
    order_number = models.CharField(max_length=10, editable=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    address = models.TextField(blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: "
                                         "'+999999999'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, max_length=12)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)

    def __unicode__(self):
        return 'Profile of user: {}'.format(self.user.username)
