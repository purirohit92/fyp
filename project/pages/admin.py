from django.contrib import admin\
    
from .models import Product,ProductImage,Cart,CartItem

# admin.site.register(Product)

class ProductImageAdmin(admin.StackedInline):
    	model = ProductImage




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	inlines=[ProductImageAdmin]

admin.site.register(Cart)
admin.site.register(CartItem)
