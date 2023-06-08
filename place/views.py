from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal

from django.views.generic import TemplateView
from place.models import Place
from place.utils import haversine


class PlaceView(TemplateView):
    template_name = 'location.html'

    def get_context_data(self,*args, **kwargs):
        context = super(PlaceView, self).get_context_data(*args,**kwargs)
        context['place'] = Place.objects.first()
        return context


def endpoint(request):
    latitude = request.GET['latitude']
    longitude = request.GET['longitude']
    print(request.GET)
    print(latitude, longitude)
    origin = Place.objects.first()
    distance = haversine(Decimal(latitude), Decimal(longitude), origin.longitude, origin.latitude)
    html = f'<h3>Coordenadas recibidas:</h3><p>Latitud: {latitude}</p><p>Longitud: {longitude}</p><p>Distancia desde {origin.name} es de {distance} metros<p/>'
    return HttpResponse(html)