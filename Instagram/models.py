# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Profile(models.Model):
     profile_photo=models.CharField(max_length=40)
     bio=models.CharField(max_length=50)

     def __str__(self):
        return self.bio
class tags(models.Model):
    name = models.CharField(max_length =30)
    
    def __str__(self):
        return self.name 

class Image(models.Model):
    image = models.ImageField(upload_to = 'pics/', blank=True)
    name = models.CharField(max_length =30)
    image_Caption = models.TextField(null = True)
    post = HTMLField()
    Profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.CharField(max_length=40)
    Comments = models.CharField(max_length=60)
    user = models.ForeignKey(User,null=True)
    


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def del_image(self):
        self.delete()
    def update_caption(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs)

    def __str__(self):
    	return self.user.username

    
    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos   

class  Follow(models.Model):
    profile_id = models.IntegerField()
    user_id =models.IntegerField()
    def __str__(self):
        return self.name

   

# class Comment(models.Model):

#     id = models.IntegerField(primary_key = True)
#     comment= models.CharField(max_length =30)
#     image_id =models.ForeignKey('Image.id')
#     user_id = models.ForeignKey("users.id")
class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField() 
    









  
