from django.urls import path
from .views import *

app_name = 'memory'
urlpatterns = [
    path('momories/', ShowMemory.as_view(), name='ShowMemory'),
    path('addmemory/', add_memory, name='addmemory'),
]