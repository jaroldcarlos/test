from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal

from django.views.generic import TemplateView
from place.models import Place
from place.utils import calcular_distancia


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
    print(origin.latitude, origin.longitude, Decimal(latitude), Decimal(longitude))
    distance = calcular_distancia(origin.latitude, origin.longitude, Decimal(latitude), Decimal(longitude))
    html = f'<p>Tu posición: Latitud: {latitude} - Longitud: {longitude}</p><p>Origen {origin.name}: Latitud: {origin.latitude} - Longitud: {origin.longitude}</p><p>Distancia de {distance} metros<p/>'
    return HttpResponse(html)