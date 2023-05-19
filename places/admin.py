from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase
from .models import Place, Image


class ImageTabularInline(SortableTabularInline):
    model = Image
    fields = ('image', 'get_preview', 'sequence_number')
    ordering = ('sequence_number', )
    readonly_fields = ('get_preview', )
    extra = 0

    @staticmethod
    def get_preview(obj):
        return format_html(f'<img src="{mark_safe(obj.image.url)}" height="200px" />')


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    search_fields = ['title']
    inlines = [ImageTabularInline, ]
    extra = 0
