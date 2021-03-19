from django.contrib import admin
from .models import Notice, NoticeAttach

class NoticeAttachInline(admin.TabularInline):
    model = NoticeAttach

class NoticeCustom(admin.ModelAdmin):
    list_display = ['title', 'date']
    inlines = [NoticeAttachInline,]

admin.site.register(Notice, NoticeCustom)
