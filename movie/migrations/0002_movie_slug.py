# Generated by Django 3.0.5 on 2020-04-09 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
