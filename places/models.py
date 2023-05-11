from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=30)
    placeId = models.CharField(max_length=30)
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    sequence_number = models.IntegerField()
    title = models.CharField(max_length=200, default='no title')
    image = models.ImageField()
    place = models.ForeignKey('Place', related_name='images', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.sequence_number} {self.title} {self.place}'
