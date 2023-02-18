from django.urls import path
from .views import *

app_name = 'workshop'
urlpatterns = [
    path('', ShowWorkshopList.as_view(), name='show_workshops'),
]