# Generated by Django 3.0.5 on 2020-04-10 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rank', '0006_auto_20200409_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='slug',
            field=models.SlugField(default='SLUG', unique=True),
            preserve_default=False,
        ),
    ]