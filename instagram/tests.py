# -*- coding: utf-8 -*-
from django.test import TestCase
from .models import Image,Comment, Follow, Profile,Likes

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.wecode= Image()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Image))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_image()
        caption= Image.objects.all()
        self.assertTrue(len(caption) > 0)

  
       
class CommentTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wecode= Comment()
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Comment))

   
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.wecode= Image( )
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.wecode,Image))

    # Testing Save Method
    def test_save_method(self):
        self.wecode.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0) 
    def update_image(self, **kwargs):
        self.objects.filter(id = self.pk).update(**kwargs) 