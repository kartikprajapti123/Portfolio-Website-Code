
from django.contrib import admin
from django.urls import path,include
from render import routers
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from render.views import custom_404_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(routers.router.urls)),
    path('',include('render.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'render.views.custom_404_view'