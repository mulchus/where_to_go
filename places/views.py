from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def start(request):
    serialized_places = []
    places = Place.objects.all()
    for place in places:
        details_url = f'{reverse("places_url")}{place.pk}'
        one_place = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat],
            },
            'properties': {
                'title': place.title,
                'placeId': place.pk,
                'detailsUrl': details_url,
            }
        }
        serialized_places.append(one_place)

    serialized_places = {
        'type': 'FeatureCollection',
        'features': serialized_places,
    }
    return render(request, 'index.html', {'serialized_places': serialized_places})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    images = []
    place_images = place.images.all()
    for image in place_images:
        images.append(image.image.url)
    details_url = {
        'title': place.title,
        'imgs': images,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        }
    }
    return JsonResponse(details_url, json_dumps_params={'indent': 4, 'ensure_ascii': False})
