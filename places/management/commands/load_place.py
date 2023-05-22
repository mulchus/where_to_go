import requests

from urllib.parse import urlparse
from pathlib import Path
from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Добавить место на карту'

    def add_arguments(self, parser):
        parser.add_argument('url_about_place',
                            nargs='?',
                            type=str,
                            help='Добавить место на карту',
                            )

    def handle(self, *args, **options):
        response = requests.get(options['url_about_place'])
        response.raise_for_status()
        row_place = response.json()
        row_place_lng = row_place['coordinates']['lng']
        row_place_lat = row_place['coordinates']['lat']

        place, place_created = Place.objects.get_or_create(
            title=row_place['title'],
            lng=row_place_lng,
            lat=row_place_lat,
            defaults={'description_short': row_place['description_short'],
                      'description_long': row_place['description_long']},
        )

        if not place_created:
            print(f'Место "{row_place["title"]}" уже есть в базе данных.')
            return
        print(f'Добавлено место "{row_place["title"]}".')
        for image_num, image_url in enumerate(row_place['imgs']):
            response = requests.get(image_url)
            response.raise_for_status()
            image_name = Path(urlparse(image_url).path).name
            image_file = ContentFile(response.content, name=image_name)
            image, image_created = Image.objects.get_or_create(
                image=image_file,
                place_id=place.id,
                defaults={'sequence_number': image_num, },
            )
            if not image_created:
                print(f'Фотография "{image.image}" уже имеется в базе данных у данной локации.')
            else:
                print(f'Добавлена фотография "{image.image}".')
