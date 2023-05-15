# Generated by Django 4.0 on 2023-05-15 14:13

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_placeid_place_short_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['sequence_number']},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='places.place', verbose_name='относится к'),
        ),
        migrations.AlterField(
            model_name='image',
            name='sequence_number',
            field=models.PositiveIntegerField(default=0, verbose_name='позиция'),
        ),
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='no title', max_length=200, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(verbose_name='короткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(verbose_name='широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(verbose_name='долгота'),
        ),
        migrations.AlterField(
            model_name='place',
            name='placeId',
            field=models.CharField(max_length=30, verbose_name='уникальный идентификатор'),
        ),
        migrations.AlterField(
            model_name='place',
            name='short_title',
            field=models.CharField(max_length=30, verbose_name='короткое название'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=200, verbose_name='название'),
        ),
    ]