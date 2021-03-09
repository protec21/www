from django.contrib import admin
from .models import Notice

class NoticeCustom(admin.ModelAdmin):
    list_display = ['title', 'date']

admin.site.register(Notice, NoticeCustom)
