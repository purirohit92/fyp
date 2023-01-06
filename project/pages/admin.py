from dataclasses import fields
from django.contrib import admin
from .models import *
from django import forms
from .models import BlogPost,BlogImage,projects,contact

admin.site.register(BlogPost)
admin.site.register(BlogImage)
admin.site.register(projects)
admin.site.register(contact)