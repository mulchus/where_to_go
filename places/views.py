from django.shortcuts import render
from .models import Place
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse


def start(request):
    serialized_places = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat],
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.pk,
                    'detailsUrl': reverse('place_api', args=[place.pk]),
                }
            } for place in Place.objects.all()
        ]
    }
    return render(request, 'index.html', {'serialized_places': serialized_places})


def place_view(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    details_url = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.lng,
            'lat': place.lat,
        }
    }
    return JsonResponse(details_url, json_dumps_params={'indent': 4, 'ensure_ascii': False})
