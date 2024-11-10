from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


def shop(request):
    context = {
        'title': 'ПНЕВМОШОП'
    }
    return render(request, 'shop/shop.html', context=context)


def t_shirts(request):
    context = {
        'title': 'ФУТБОЛКИ'
    }
    return render(request, 'shop/t_shirts.html', context=context)


def accessories(request):
    context = {
        'title': 'АКСЕССУАРЫ'
    }
    return render(request, 'shop/accessories.html', context=context)


def hoodies(request):
    context = {
        'title': 'ТОЛСТОВКИ'
    }
    return render(request, 'shop/hoodies.html', context=context)


def audio(request):
    context = {
        'title': 'АУДИО'
    }
    return render(request, 'shop/audio.html', context=context)
