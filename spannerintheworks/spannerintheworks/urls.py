from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found

from spannerintheworks import settings

handler404 = page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('spanner.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Сериалы, мультсериалы и все то, что придет вам в голову"