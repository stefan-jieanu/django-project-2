# Generated by Django 4.2 on 2024-11-22 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0002_genre_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='slug',
        ),
    ]
