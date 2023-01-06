import datetime
from random import random
import string
from django.http import HttpResponse
from .urls import *
from .models import BlogPost
from django.db.models import Prefetch
from django.shortcuts import render,redirect
from django import forms
# Create your views here.


def HomePage(request):
    return render(request, 'index.html')