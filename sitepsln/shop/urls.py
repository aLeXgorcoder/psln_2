from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.shop, name='shop'),
    path('t-shirts/', views.t_shirts, name='t_shirts'),
    path('accessories/', views.accessories, name='accessories'),
    path('hoodies/', views.hoodies, name='hoodies'),
    path('audio/', views.audio, name='audio')
]