from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePage, name='index'),
    
]
