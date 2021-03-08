from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.urls import re_path

from www import views
from main import settings

urlpatterns = [
    path('admin/',                  admin.site.urls,                name='admin'),
    path('',                        views.index,                    name='index'),
    path('company/intro',           views.company_intro,            name='company_intro'),
    path('company/vision/',         views.company_vision,           name='company_vision'),
    path('company/history/',        views.company_history,          name='company_history'),
    path('company/orgnation/',      views.company_orgnation,        name='company_orgnation'),
    path('company/certificate/',    views.company_certificate,      name='company_certificate'),
    path('company/map/',            views.company_map,              name='company_map'),
    path('product/dispenser',       views.product_dispenser,        name='product_dispenser'),
    path('product/diebonder',       views.product_diebonder,        name='product_diebonder'),
    path('product/attach',          views.product_attach,           name='product_attach'),
    path('finance/notice/',         views.finance_notice,           name='finance_notice'),
    path('finance/disclosure',      views.finance_disclosure,       name='finance_disclosure'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]
