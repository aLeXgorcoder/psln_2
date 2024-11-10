import generics
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics, viewsets


from drf.serializers import ConcertsSerializer
from psln.models import Concerts


class ConcertViewSet(viewsets.ModelViewSet):
    queryset = Concerts.objects.all()
    serializer_class = ConcertsSerializer

