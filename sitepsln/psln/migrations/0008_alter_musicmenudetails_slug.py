# Generated by Django 5.0.7 on 2024-08-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psln', '0007_remove_songs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicmenudetails',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]