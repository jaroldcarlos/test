from django.contrib import admin
from django.urls import path

from place.views import PlaceView, endpoint

app_name = 'place'

urlpatterns = [
    path('endpoint', endpoint, name="endpoint"),
    path('', PlaceView.as_view(), name="geoposition"),
]   
