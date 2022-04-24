from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomePage, name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    # path('booking', views.BookingView.as_view(), name='booking'),
    # path('contact', views.ContactView.as_view(), name='contact'),
    # path('about', views.AboutPage.as_view(), name='about'),
    # path('forget-pw', views.password_reset_request, name='password_reset'),
    path('register', views.RegisterView.as_view(), name='register'),
    # path('gallery', views.GalleryView.as_view(), name='gallery'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    # path('my-bookings', (views.MyBookingsView.as_view()), name='my_bookings'),
    # path('cancel-bookings', views.CancelBookingsView.as_view(), name='cancel'),
    path('product/<int:id>', views.Productdetails.as_view(), name='product'),
     path('cart', views.cart, name='cart'),
     path('add-to-cart/<int:product_id>', views.add_to_cart, name='add_to_cart'),
     path('remove-from-cart/<int:item_id>', views.remove_from_cart, name='remove_from_cart'),
     path('complete-payment/<int:item_id>', views.complete_payment, name='complete_payment'),
    # path('product', views.product, name='product'),
    # path('contactus', views.contactus, name='contactus'),
    # path('productdetails',views.productdetails, name='productdetails'),
    #path("password_reset", views.password_reset_request, name="password_reset")

]
