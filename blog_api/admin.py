from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)


# from django.contrib import admin
# from . import models

# @admin.register(models.Post)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'author', 'status', 'slug')
#     prepopulated_fields = {'slug': ('title',),}

# admin.site.register(models.Category)