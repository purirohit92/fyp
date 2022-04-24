from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Product(models.Model):
    TYPE_CHOICES = (('men','men'),
                        ('women','women'),
                        ('children','children'))
    name=models.CharField(max_length=100,blank=True,null=True)
    price = models.CharField(max_length=100,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    wishlist =  models.ManyToManyField(User,related_name='wishlist',blank=True)
    type = models.CharField(max_length=50,choices=TYPE_CHOICES,null=True,blank=True)
    
    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product,default=None,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return '-'

class Cart(models.Model):
    STATUS_CHOICES = ((0,'shopping'),(1,'complete'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default=0)
    def __str__(self):
        return  self.user.username

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product_cart_item')
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    
    def cart_total(self):
        return int(self.product.price) * self.quantity


    def __str__(self):
        return  self.product.name

