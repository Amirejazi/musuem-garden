from django.contrib import admin
from .models import *


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'family', 'email', 'is_active')


@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display = ('group_title',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'group', 'image', 'register_date', 'is_active')


@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display = ('article', 'image',)