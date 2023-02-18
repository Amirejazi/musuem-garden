from django.contrib import admin

from .models import *


@admin.register(Place)
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('place_name', 'place_image', 'visiting_day', 'visiting_hour', 'register_date')


@admin.register(VisitorType)
class VisitorTypeAdmin(admin.ModelAdmin):
    list_display = ('type_name',)


@admin.register(TicketPrice)
class TicketPriceAdmin(admin.ModelAdmin):
    list_display = ('place', 'visitor', 'price')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message', 'is_seen', 'register_date')
