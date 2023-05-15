from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    short_title = models.CharField(max_length=30, verbose_name='короткое название')
    placeId = models.CharField(max_length=30, verbose_name='уникальный идентификатор')
    description_short = models.TextField(verbose_name='короткое описание')
    description_long = models.TextField(verbose_name='полное описание')
    lng = models.FloatField(verbose_name='долгота')
    lat = models.FloatField(verbose_name='широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    sequence_number = models.IntegerField(verbose_name='позиция')
    title = models.CharField(max_length=200, default='no title', verbose_name='название')
    image = models.ImageField(verbose_name='картинка')
    place = models.ForeignKey('Place', related_name='images', null=True, on_delete=models.SET_NULL,
                              verbose_name='относится к')
    
    class Meta:
        ordering = ['sequence_number']

    def __str__(self):
        return f'{self.sequence_number} {self.place}'
