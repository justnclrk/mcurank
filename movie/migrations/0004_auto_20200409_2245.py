# Generated by Django 3.0.5 on 2020-04-10 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200409_1502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['release_date', 'phase']},
        ),
    ]
