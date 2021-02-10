from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.urls import re_path

from www import views
from main import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('company/', views.company),
    path('vision/', views.vision),
    path('history/', views.history),
    path('orgnation/', views.orgnation),
    path('certificate/', views.certificate),
    path('map/', views.map),
    path('notice/', views.notice),
    path('stock/', views.stock),
    path('product/', views.product),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
