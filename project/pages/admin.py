from dataclasses import fields
from django.contrib import admin
from .models import *
from django import forms
from .models import BlogPost,BlogImage,Projects,Contact

# admin.site.register(BlogPost)
# admin.site.register(BlogImage)

class BlogImageAdmin(admin.StackedInline):
    model=BlogImage
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display=("id","title","intro","description")
    inlines=[BlogImageAdmin]


admin.site.register(Projects)
admin.site.register(Contact)