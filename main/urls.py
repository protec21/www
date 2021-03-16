from django.contrib import admin
from django.urls import path
from django.views.static import serve
from django.urls import re_path

from www import views
from main import settings

urlpatterns = [
    path('admin/',                  admin.site.urls,                name='admin'),
    path('',                        views.index,                    name='index'),
    path('company/about/',          views.company_about,            name='company_about'),
    path('company/vision/',         views.company_vision,           name='company_vision'),
    path('company/history/',        views.company_history,          name='company_history'),
    path('company/orgnation/',      views.company_orgnation,        name='company_orgnation'),
    path('company/certificate/',    views.company_certificate,      name='company_certificate'),
    path('company/map/',            views.company_map,              name='company_map'),
    path('product/dispenser/',      views.product_dispenser,        name='product_dispenser'),
    path('product/diebonder/',      views.product_diebonder,        name='product_diebonder'),
    path('product/attach/',         views.product_attach,           name='product_attach'),
    path('investment/disclosure/',  views.investment_disclosure,    name='investment_disclosure'),
    path('investment/stock/',       views.investment_stock,         name='investment_stock'),
    path('investment/finance/',     views.investment_finance,       name='investment_finance'),
    path('investment/notice/',      views.investment_notice,        name='investment_notice'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

admin.site.site_header = "관리자페이지" #"Django Administration"
admin.site.index_title = "Site administration"
admin.site.site_title = "Django site admin"
