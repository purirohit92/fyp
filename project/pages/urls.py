from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('blog/<int:id>', views.BlogSingle, name='blog'),
    path('contact-us',views.contact_us,name='contact'),
    
    
]
