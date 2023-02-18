from django.urls import path
from . import views

app_name = 'places'
urlpatterns = [
    path('history/', views.Show_history, name='history'),
    path('parts/', views.Show_garden_parts, name='parts'),
    path('part_detail/<int:id>', views.Show_part_detail, name='part_detail'),
    path('path_file/', views.Download_pathPdf, name='path_file'),
    path('time_rules/', views.time_rules, name='time_rules'),
    path('contact/', views.contact_view, name='contact'),
]