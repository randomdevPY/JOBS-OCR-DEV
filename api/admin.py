from django.contrib import admin
from django.utils.html import format_html
from .models import *

@admin.register(Provinces)
class ProvinceAdmin(admin.ModelAdmin):
    exclude = ('id',)

@admin.register(Emails)
class EmailAdmin(admin.ModelAdmin):
    exclude = ('id',)
    readonly_fields = ('created_at', 'province', 'address')
    list_filter = ('province',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    exclude = ('id',)
    readonly_fields = ('image', 'process',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False