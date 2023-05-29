import requests

from urllib.parse import urlparse
from pathlib import Path
from django.core.management.base import BaseCommand
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Добавить место на карту'

    def add_arguments(self, parser):
        parser.add_argument(
            'url_about_place',
            nargs='?',
            type=str,
            help='Добавить место на карту',
        )

    def handle(self, *args, **options):
        response = requests.get(options['url_about_place'])
        response.raise_for_status()
        raw_place = response.json()
        raw_place_lng = raw_place['coordinates']['lng']
        raw_place_lat = raw_place['coordinates']['lat']

        place, place_created = Place.objects.get_or_create(
            title=raw_place['title'],
            lng=raw_place_lng,
            lat=raw_place_lat,
            defaults={
                'description_short': raw_place.get('description_short', ''),
                'description_long': raw_place.get('description_long', '')
            },
        )

        if not place_created:
            print(f'Место "{raw_place["title"]}" уже есть в базе данных.')
            return
        print(f'Добавлено место "{raw_place["title"]}".')
        for image_num, image_url in enumerate(raw_place.get('imgs', [])):
            response = requests.get(image_url)
            response.raise_for_status()
            image_name = Path(urlparse(image_url).path).name
            image_file = ContentFile(response.content, name=image_name)
            image, image_created = Image.objects.create(
                image=image_file,
                place_id=place.id,
                defaults={'sequence_number': image_num, },
            )
            print(f'Добавлена фотография "{image.image}".')
