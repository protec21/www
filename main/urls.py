"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from www import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('company/', views.company),
    path('vision/', views.vision),
    path('history/', views.history),
    path('orgnation/', views.orgnation),
    path('certificate/', views.certificate),
    path('map/', views.map),
    path('stocknotice/', views.stocknotice),
    path('stock/', views.stock),
    path('product/', views.product),
]

