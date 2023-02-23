import random
import string
from tokenize import Name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class BlogPost(models.Model):
  title=models.CharField(max_length=500, blank=True,null=True)
  intro=models.CharField(max_length=500, blank=True, null=True)
  description=models.TextField(blank=True, null=True)
 
  
class BlogImage(models.Model):
    post = models.ForeignKey(BlogPost,default=None,on_delete=models.CASCADE,related_name='blog_images')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return '-'

class Projects(models.Model):
    ProjectDuration = models.CharField(max_length=500,blank=True, null=True)
    ProjectTitle = models.CharField(max_length=500, blank=True, null=True)
    ProjectDescription = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='photos/projects/%Y/%m/%d/',null=True, blank=True)

class Contact(models.Model):
    Name = models.CharField(max_length=50, blank=True, null=True)
    Email = models.EmailField(blank=True,null=True)
    Phone = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=1000,blank=True,null=True)
    
    