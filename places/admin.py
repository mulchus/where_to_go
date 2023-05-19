from django.contrib import admin
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
    def get_preview(image_object):
        return format_html('<img src="{}" height="200px" />', image_object.image.url)


@admin.register(Place)
class SortablePlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    search_fields = ['title']
    inlines = [ImageTabularInline, ]
    extra = 0
