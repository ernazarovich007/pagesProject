from django.urls import path
from .views import HomePageView, AboutPageView, RajuPageView, BoboPageView
urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    path('raju/', RajuPageView.as_view(), name='Raju'),
    path('bobo/', BoboPageView.as_view(), name='Bobo'),
]