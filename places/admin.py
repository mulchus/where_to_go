from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from adminsortable2.admin import SortableTabularInline, SortableAdminBase, SortableAdminMixin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'get_preview', 'sequence_number')
    ordering = ('sequence_number', )
    readonly_fields = ('get_preview', )
    extra = 0

    @staticmethod
    def get_preview(obj):
        return format_html(f'<img src="{mark_safe(obj.image.url)}" height="200px" />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = [ImageInline, ]
    extra = 0


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('sequence_number', 'get_preview', 'title', 'place', )
    ordering = ('place', 'sequence_number',)
    extra = 0

    @staticmethod
    def get_preview(obj):
        return format_html(f'<img src="{mark_safe(obj.image.url)}" height="50px" />')
