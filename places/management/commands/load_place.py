import requests
import os

from urllib.parse import urlparse
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from places.models import Place, Image
from where_to_go.settings import MEDIA_URL, BASE_DIR



class Command(BaseCommand):
    help = 'Добавить место на карту'

    def add_arguments(self, parser):
        parser.add_argument('file_path_about_place',
                            nargs='?',
                            type=str,
                            help='Добавить место на карту',
                            )

    def handle(self, *args, **options):
        response = requests.get(options['file_path_about_place'])
        response.raise_for_status()
        new_place = response.json()
        new_place_lng = new_place['coordinates']['lng']
        new_place_lat = new_place['coordinates']['lat']
        new_place_placeid = f"{new_place_lng}-{new_place_lat}"
        if False: # Place.objects.filter(placeId=new_place_placeid):
            print(f'Место c координатами {new_place_placeid} уже имеется в базе.')
        else:
            place = Place.objects.create(
                title=new_place['title'],
                short_title='',
                placeId=new_place_placeid,
                description_short=new_place['description_short'],
                description_long=new_place['description_long'],
                lng=float(new_place['coordinates']['lng']),
                lat=float(new_place['coordinates']['lat']),
            )
            print(f'Добавлено место "{place.title}"')
        for image_url in new_place['imgs']:
            print(image_url)
            response = requests.get(image_url)
            response.raise_for_status()
            # image_name = parse.urlsplit(image_url).path
            image_name = os.path.basename(urlparse(image_url))
            print(image_name)
            file_path = Path.joinpath(BASE_DIR, MEDIA_URL)

            with open(f'{file_path}{image_name}', 'wb') as file:
                file.write(response.content)
            exit()

        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Place.objects.get(pk=poll_id)
        #     except Place.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #     poll.opened = False
        #     poll.save()
        #
        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))