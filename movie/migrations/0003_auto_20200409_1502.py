# Generated by Django 3.0.5 on 2020-04-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
