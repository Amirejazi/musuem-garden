from django.contrib import admin
from .models import *


@admin.register(WorkShopStatus)
class WorkShopStatusAdmin(admin.ModelAdmin):
    list_display = ('status_title', 'status_title')


@admin.register(WorkShop)
class WorkShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'teacher', 'status', 'is_active')

@admin.register(WorkShop_gallery)
class WorkShopGalleryAdmin(admin.ModelAdmin):
    list_display = ('workshop', 'image')

