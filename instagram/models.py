# -*- coding: utf-8 -*-

from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# from .models import Profile, Image, Comment, Follow, Unfollow, Likes
# from . forms import ProfileUploadForm,CommentForm,ProfileForm,ImageForm,ImageUploadForm
from django.conf import settings

class Profile(models.Model):
    bio = models.CharField(max_length =30)
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.bio
class tags(models.Model):
    name = models.CharField(max_length =30)
    

    def __str__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length = 30,null = True)
    caption = models.TextField(null = True)
    user = models.ForeignKey(User,null=True)

    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
    	return self.name

    def delete_image(self):
    	self.delete()

    def save_image(self):
    	self.save()

    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images 

    @classmethod
    def get_image(cls, id):
        image = cls.objects.get(id=id)
        return image
    
    def __str__(self):
    	return self.user.username

    
    @classmethod
    def search_by_name(cls,search_term):
        photos = cls.objects.filter(name__icontains=search_term)
        return photos

class PhotosLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField() 



class Comment(models.Model):
        user = models.ForeignKey(User,on_delete = models.CASCADE, null= True)
        image = models.ForeignKey(Image,on_delete = models.CASCADE, null= True,related_name='comment')
        comment= models.TextField( blank=True)
        
        def __str__(self):
            return self.comment


        def delete_comment(self):
            self.delete()

        def save_comment(self):
            self.save()


class Follow(models.Model):
	user = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete = models.CASCADE,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()


class Unfollow(models.Model):
	user = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
	follower = models.ForeignKey(User,on_delete = models.CASCADE,null=True)

	def __int__(self):
		return self.name


class Likes(models.Model):
	user = models.ForeignKey(Profile,on_delete = models.CASCADE,null=True)
	

	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save()     