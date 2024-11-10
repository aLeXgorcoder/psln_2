from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from psln.models import Concerts, MusicMenu, MusicMenuDetails, Songs

audio_main = [
    {'title': 'САМОЕ СВЕЖЕЕ МУЗЛО', 'url_slug': 'camoe_svejee_muzlo'},
    {'title': 'АЛЬБОМЫ', 'url_slug': 'albomy'},
    {'title': 'СИНГЛЫ', 'url_slug': 'singly'}
]


# def main(request):
#     context = {
#         'title': 'ПНЕВМОСЛОН - Официальный сайт'
#     }
#     return render(request, 'psln/main.html', context=context)

class Main(TemplateView):
    template_name = 'psln/main.html'
    extra_context = {
        'title': 'ПНЕВМОСЛОН - Официальный сайт'
    }


def concerts(request):
    concerts = Concerts.objects.all()
    context = {
        'title': 'Концерты',
        'concerts': concerts
    }
    return render(request, 'psln/concerts.html', context=context)


@login_required
def audio(request):
    music_menu = MusicMenu.objects.all()
    context = {
        'title': 'Аудио',
        'audio_main': audio_main,
        'music_menu': music_menu
    }
    return render(request, 'psln/audio.html', context=context)


def audio_detail(request, slug):
    music_menu = get_object_or_404(MusicMenu, slug=slug)
    music_menu_detail = MusicMenuDetails.objects.filter(menu=music_menu)
    context = {
        'music_menu': music_menu,
        'music_menu_detail': music_menu_detail
    }
    return render(request, 'psln/audio_detail.html', context=context)


def songs(request, slug):
    menu_detail = get_object_or_404(MusicMenuDetails, slug=slug)
    songs_from_same_album = Songs.objects.filter(menu_details=menu_detail)
    context = {
        'menu_detail': menu_detail,
        'songs_from_same_album': songs_from_same_album,
        'album_title': menu_detail.title,
        'image_menu_detail': menu_detail.image

    }
    return render(request, 'psln/songs.html', context=context)


def video(request):
    context = {
        'title': 'Видео'
    }
    return render(request, 'psln/video.html', context=context)
