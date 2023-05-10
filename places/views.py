from django.shortcuts import render
from .models import Place, Image


def start(request):
    places = Place.objects.all()
    # places_serialization =
    print(places)
    return render(request, 'index.html')
