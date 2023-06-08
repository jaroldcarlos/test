from django.contrib import admin
from django.urls import path

from place.views import PlaceView, endpoint, register_place, delete_place, detail_place

app_name = 'place'

urlpatterns = [
    path('endpoint', endpoint, name="endpoint"),
    path('register_place', register_place, name="register_place"),
    path('delete_place/<uuid:uuid>', delete_place, name="delete_place"),
    path('<uuid:uuid>/', detail_place, name="detail_place"),
    path('', PlaceView.as_view(), name="geoposition"),
]   
