from django.shortcuts import render

from django.views.generic import TemplateView

class PlaceView(TemplateView):
    template_name = 'location.html'