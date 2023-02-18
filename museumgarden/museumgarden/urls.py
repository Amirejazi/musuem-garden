from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.main.urls', namespace='main'), name='main'),
    path('places/', include('apps.places.urls', namespace='places'), name='places'),
    path('blog/', include('apps.articles.urls', namespace='articles'), name='articles'),
    path('workshop/', include('apps.workshop.urls', namespace='workshop'), name='workshop'),
    path('account/', include('apps.accounts.urls', namespace='account'), name='account'),
    path('memory/', include('apps.memories.urls', namespace='memory'), name='memory'),
    ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
