from django.urls import path
from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('concerts/', views.concerts, name='concerts'),
    path('audio/', views.audio, name='audio'),
    path('audio/<slug:slug>/', views.audio_detail, name='audio_detail'),
    path('songs/<slug:slug>/', views.songs, name='songs'),
    path('video/', views.video, name='video'),
]

