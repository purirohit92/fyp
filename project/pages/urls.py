from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('product/<int:id>', views.Productdetails.as_view(), name='product'),
     path('cart', views.cart, name='cart'),
     path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
     path('remove-from-cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
     path('complete-payment/<int:cart_id>', views.complete_payment, name='complete_payment'),
    path('product', views.product, name='product'),
    path('search', views.search, name='search'),

]
