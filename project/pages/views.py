import datetime
from random import random
import string
from tokenize import Name
from urllib import request
from django.http import HttpResponse
from .urls import *
from .models import BlogPost,BlogImage,Projects,Contact
from django.db.models import Prefetch
from django.shortcuts import render,redirect
from django import forms
from django.shortcuts import get_object_or_404
# Create your views here.


def HomePage(request):
    blog_queryset = BlogPost.objects.prefetch_related(Prefetch("blog_images",queryset=BlogImage.objects.all())).all()
    projects_queryset = Projects.objects.all()
    context={
        "blogs":blog_queryset,
        "projects":projects_queryset
    }
    return render(request, 'index.html',context=context)

def BlogSingle(request,id):
    queryset = get_object_or_404(BlogPost,id=id)
    photos = BlogImage.objects.filter(post=queryset)
    context={
        'blog':queryset,
        'photos':photos
        }
    return render(request, 'single-blog.html',context=context)


def contact_us(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get("message")
    Contact.objects.create(Name=name,Email=email,Phone=phone,Message=message)
    return redirect("index")
    