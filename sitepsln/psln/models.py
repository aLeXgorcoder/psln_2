from django.db import models


class Concerts(models.Model):
    date = models.DateField()
    program = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.club


class MusicMenu(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class MusicMenuDetails(models.Model):
    menu = models.ForeignKey(MusicMenu, on_delete=models.CASCADE, related_name='details')
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    date = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Songs(models.Model):
    menu_details = models.ForeignKey(MusicMenuDetails, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title
