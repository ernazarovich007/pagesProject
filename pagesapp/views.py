from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class RajuPageView(TemplateView):
    template_name = 'Raju.html'

class BoboPageView(TemplateView):
    template_name = 'Bobo.html'






