import random
import string
from tokenize import Name
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class BlogPost(models.Model):# ani yo chai first ko js bhako wala ma ho haii
  title=models.CharField(max_length=500, blank=True,null=True)
  intro=models.CharField(max_length=500, blank=True, null=True)
  description=models.CharField(max_length=500, blank=True, null=True)
class BlogImage(models.Model):
    Image = models.ForeignKey(BlogPost,default=None,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return '-'

class projects(models.Model):#yo chai index ma chha eauta projects title vako tyesma halnu parney
    ProjectDuration = models.CharField(max_length=500,blank=True, null=True)
    ProjectTitle = models.CharField(max_length=500, blank=True, null=True)
    ProjectDescription = models.CharField(max_length=500,blank=True,null=True)


class contact(models.Model):#yo chai website bata get garera backend ma aaunu parney banauney la
    Name = models.CharField(max_length=50, blank=True, null=True)
    Email = models.EmailField(blank=True,null=True)
    Phone = models.IntegerField(null=True,blank=True)
    Message = models.CharField(max_length=1000,blank=True,null=True)