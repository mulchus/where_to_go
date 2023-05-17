import requests

from urllib.parse import urlparse
from pathlib import Path
from django.core.management.base import BaseCommand
from places.models import Place, Image
from where_to_go.settings import MEDIA_ROOT


class Command(BaseCommand):
    help = 'Добавить место на карту'

    def add_arguments(self, parser):
        parser.add_argument('place_short_title',
                            nargs='?',
                            type=str,
                            help='Короткое имя локации',
                            )
        parser.add_argument('url_about_place',
                            nargs='?',
                            type=str,
                            help='Добавить место на карту',
                            )

    def handle(self, *args, **options):
        response = requests.get(options['url_about_place'])
        response.raise_for_status()
        new_place = response.json()
        new_place_lng = new_place['coordinates']['lng']
        new_place_lat = new_place['coordinates']['lat']
        new_place_placeid = f"{new_place_lng}-{new_place_lat}"

        place, place_created = Place.objects.get_or_create(
            placeId=new_place_placeid,
            title=new_place['title'],
            defaults={'short_title': options['place_short_title'],
                      'description_short': new_place['description_short'],
                      'description_long': new_place['description_long'],
                      'lng': float(new_place_lng),
                      'lat': float(new_place_lat)},
        )

        if not place_created:
            print(f'Место "{place.title}", координаты {place.placeId} уже есть в базе данных.')
        else:
            print(f'Добавлено место "{place.title}", координаты {place.placeId}.')
            for image_num, image_url in enumerate(new_place['imgs']):
                response = requests.get(image_url)
                response.raise_for_status()
                image_name = Path(urlparse(image_url).path).name
                file_path = Path(MEDIA_ROOT).joinpath(image_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                image, image_created = Image.objects.get_or_create(
                    image=image_name,
                    place_id=place.id,
                    defaults={'sequence_number': image_num,
                              'title': 'no title'},
                )
                if not image_created:
                    print(f'Фотография "{image.image}" уже имеется в базе данных у данной локации.')
                else:
                    print(f'Добавлена фотография "{image.image}".')
