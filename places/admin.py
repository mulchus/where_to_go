from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'sequence_number')
    extra = 0


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')
    inlines = [ImageInline, ]
    extra = 0


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('sequence_number', 'title', 'place', )
    ordering = ('place', 'sequence_number',)
    extra = 0
