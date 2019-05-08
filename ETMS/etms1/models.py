# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofileinfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site =models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self .user .username

class Driver(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email = models.EmailField()
    driver_id = models.CharField(max_length=50)
    address = models.TextField()
    dl_no= models.CharField(max_length=20)

class Addbooking(models.Model):
    user_name = models.CharField(max_length=100)
    pickup_add = models.CharField(max_length=100)
    drop_add = models.CharField(max_length=100)
    date = models.CharField(max_length=20)
    time = models.CharField(max_length=10)
