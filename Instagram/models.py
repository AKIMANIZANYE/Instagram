# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Image(models.Model):
   image = models.CharField(max_length =30)
    image_namr = models.CharField(max_length =30)
    image_Caption= models.CharField(max_length=50)
    Profile=models.CharField(max_length=50)
    likes=models.CharField(max_length=40)
    Comments= models.CharField(max_length=60)










 class Profile(models.Model):
     profile_photo=models.CharField(max_length=40)
     bio=models.CharField(max_length=50)    
