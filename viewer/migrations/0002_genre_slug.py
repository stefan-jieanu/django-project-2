# Generated by Django 4.2 on 2024-11-16 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
            preserve_default=False,
        ),
    ]
