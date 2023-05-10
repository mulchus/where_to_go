from django.contrib import admin
from .models import Place, Image


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'lng', 'lat')


class ImageAdmin(admin.ModelAdmin):
    # list_display = ('title', 'place', )
    pass

# Register your models here.
admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
