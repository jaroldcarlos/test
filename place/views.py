from django.shortcuts import render
from django.http import HttpResponse
from decimal import Decimal

from django.shortcuts import redirect
from django.views.generic import TemplateView
from place.models import Place
from place.utils import calcular_distancia, list_of_nearby_places_by_distance2, nearby_locations2


def nearby_locations(user_latitude:float, user_longitude:float)->list:
    if not user_longitude and not user_longitude: return None
    places = Place.objects.all()
    list_place = list(map(lambda item: (item.id, item.name, calcular_distancia(item.latitude, item.longitude, user_latitude, user_longitude)), places))
    list_place_sorted = sorted(list_place, key=lambda x: x[2])    
    return list_place_sorted


class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self,*args, **kwargs):
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['items'] = Place.objects.all()
        return context


def list_places_nearby(request, latitude, longitude):
    if not latitude and not longitude: 
        list_places =  ''
    else:
        list_places = nearby_locations(Decimal(latitude), Decimal(longitude))

    print(list_places)
    
    context = {
        'list_places':list_places
    }
    return render(request, 'list_places_nearby.html', context)



def register_place(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        latitud = request.POST.get('latitud')
        longitud = request.POST.get('longitud')
        item = Place()
        item.name=nombre
        item.latitude=latitud
        item.longitude=longitud
        item.save()
        return redirect('place:register_place')
    return render(request, 'register_place.html', {'items':Place.objects.all()})


def endpoint(request):
    latitude = request.GET.get('latitude', '')
    longitude = request.GET.get('longitude', '')
    id_place = request.GET.get('id_place', '')
    if id_place:
        origin = Place.objects.get(id=id_place)
    else:
        origin = Place.objects.first()
    distance = round(calcular_distancia(origin.latitude, origin.longitude, Decimal(latitude), Decimal(longitude)))
    html = f'<p>Distancia de {distance} metros<p/><br><br><p>Tu posición: Latitud: {latitude} - Longitud: {longitude}</p><p>Origen {origin.name}: Latitud: {origin.latitude} - Longitud: {origin.longitude}</p>'
    return HttpResponse(html)


def delete_place(request, uuid):
    item = Place.objects.filter(uuid=uuid)
    if item:
        item.delete()
    return redirect('place:register_place')


def detail_place(request, uuid):
    template_name = 'location_place.html'
    return render(request, template_name, {'place': Place.objects.get(uuid=uuid)})

