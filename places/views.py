import os
from django.shortcuts import render
from .models import Place, Image
# from pathlib import Path
from where_to_go.settings import BASE_DIR


# BASE_DIR = Path(__file__).resolve()


def start(request):
    places = []
    for place in Place.objects.all():
        images = []
        for image in place.images.all():
            # images.append(os.path.join(BASE_DIR, image.image.url[1:]))
            images.append(os.path.join('C:/PythonProjects/where_to_go/', image.image.url[1:]))
        one_place = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.lng, place.lat]
            },
            'properties': {
                'title': place.short_title,
                'placeId': place.placeId,
                'detailsUrl': {
                    "title": place.title,
                    "imgs": images,
                    "description_short": place.description_short,
                    "description_long": place.description_long,
                    "coordinates": {
                        "lng": str(place.lng),
                        "lat": str(place.lat)
                    }
                }
            }
        }
        places.append(one_place)
    all_places = {
        'type': 'FeatureCollection',
        'features': places
    }


    print(all_places)
    return render(request, 'index.html', {'all_places': all_places})
