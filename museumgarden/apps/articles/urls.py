from django.urls import path
from .views import *

app_name = 'articles'
urlpatterns = [
    path('', Show_articles, name='show_articles'),
    path('<str:slug>', Show_detail_articles, name='detail_articles'),
]