from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from time import time

from django.core.validators import RegexValidator

# Create your models here.
from django.template.context_processors import request

def getImage(instance, filename):
    return "core/image_{0}_{1}".format(str(time()),filename)
     

product_type = (
        ('antique','Antique'),
        ('footwear','Footwear'),
        ('accessories','Accessories'),
        ('electronics','Electronics'),
        ('sports','Sports'),
        ('home appliances','Home Appliances'),
        ('books','Books'),
        ('furniture','Furniture'),
        ('tv & appliances','TV & Appliances')
    )


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=getImage)
    category = models.CharField(choices=product_type, max_length=100)
    description = models.TextField(max_length=300)
    minimum_price = models.IntegerField(null=True)
    bid_end_date = models.DateField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.product_name


class Seller(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.user_name)




class Dis(models.Model):
    disc = models.TextField(max_length=300)
    
    def __unicode__(self):
        return str(self.disc)






class Bidder(models.Model):
    numeric = RegexValidator(r'^[0-9]*$', 'Only numerics are allowed.')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    bid_amount = models.CharField(max_length=255, validators=[numeric])

    def __unicode__(self):
        return str(self.user_name)

