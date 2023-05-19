from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    description_short = models.TextField(verbose_name='короткое описание', blank=True)
    description_long = HTMLField(verbose_name='полное описание', blank=True)
    lng = models.FloatField(verbose_name='долгота')
    lat = models.FloatField(verbose_name='широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    sequence_number = models.PositiveIntegerField(default=0, verbose_name='позиция')
    image = models.ImageField(verbose_name='картинка')
    place = models.ForeignKey('Place', related_name='images', null=True, on_delete=models.SET_NULL,
                              verbose_name='относится к')
    
    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return f'{self.sequence_number} {self.place}'
