import os
import json
from django.shortcuts import render
from .models import Place, Image
# from pathlib import Path
# from where_to_go.settings import BASE_DIR
from pathlib import Path
from django.utils.safestring import SafeString
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


BASE_DIR = Path(__file__).resolve().parent.parent


def start(request):
    serialized_places = []
    places = Place.objects.all()
    for place in places:
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
    # serialized_places = json.dumps(serialized_places, ensure_ascii=False, indent=4)
    print(serialized_places)
    return render(request, 'index.html', {'serialized_places': serialized_places})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = []
    place_images = place.images.all()
    for image in place_images:
        images.append(os.path.join(BASE_DIR, image.image.url[1:]))
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
