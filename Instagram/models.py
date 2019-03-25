# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Profile(models.Model):
     profile_photo=models.CharField(max_length=40)
     bio=models.CharField(max_length=50)  

class Image(models.Model):
    image = models.ImageField(upload_to = 'insta/')
    name = models.CharField(max_length =30)
    image_Caption = models.CharField(max_length=50)
    Profile = models..ForeignKey(Profile)
    likes = models.CharField(max_length=40)
    Comments = models.CharField(max_length=60)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def del_image(self):
        self.delete()
    def update_caption(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

class  Follow(models.Model):
    profile_id = models.IntField()
    user_id =models.IntField()
    def __str__(self):
        return self.name

   

class Comment(db.Model):

    id = models.IntField(primary_key = True)
    comment= models.CharField(max_length =30)
    image_id =models.ForeignKey('Image.id'))
    user_id = models.ForeignKey("users.id"))
    









  
