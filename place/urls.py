from django.contrib import admin
from django.urls import path

from place.views import PlaceView

app_name = 'place'

urlpatterns = [
    path('', PlaceView.as_view(), name="geoposition"),
]   
