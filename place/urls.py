from django.contrib import admin
from django.urls import path

from place.views import HomeView, endpoint, register_place, delete_place, detail_place, list_places_nearby

app_name = 'place'

urlpatterns = [
    path('endpoint', endpoint, name="endpoint"),
    path('places_nearby/<latitude>/<longitude>', list_places_nearby, name="places_nearby"),
    path('register_place', register_place, name="register_place"),
    path('delete_place/<uuid:uuid>', delete_place, name="delete_place"),
    path('<uuid:uuid>/', detail_place, name="detail_place"),
    path('', HomeView.as_view(), name="home"),
]   
