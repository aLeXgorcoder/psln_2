# Generated by Django 5.0.7 on 2024-08-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psln', '0008_alter_musicmenudetails_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicmenudetails',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
