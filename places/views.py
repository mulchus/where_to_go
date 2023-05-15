import os
from django.shortcuts import render
from .models import Place
from pathlib import Path
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


BASE_DIR = Path(__file__).resolve().parent.parent


def start(request):
    serialized_places = []
    places = Place.objects.all()
    for place in places:
        details_url = f'/places/{place.pk}'
        one_place = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.short_title,
                "placeId": place.placeId,
                "detailsUrl": details_url,
            }
        }
        serialized_places.append(one_place)

    serialized_places = {
        "type": "FeatureCollection",
        "features": serialized_places
    }
    print(serialized_places)
    return render(request, 'index.html', {'serialized_places': serialized_places})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = []
    place_images = place.images.all().order_by('sequence_number')
    for image in place_images:
        images.append(image.image.url[1:])
    details_url = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': str(place.lng),
            'lat': str(place.lat)
        }
    }
    return JsonResponse(details_url, json_dumps_params={'indent': 4, 'ensure_ascii': False})
