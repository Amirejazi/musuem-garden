from django.contrib import admin
from .models import Memory, Memory_Gallery


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'register_date', 'user_registered', 'is_active')


@admin.register(Memory_Gallery)
class MemoryGalleryAdmin(admin.ModelAdmin):
    list_display = ('image_name', 'memory')
