from django.urls import path

from logistics.apps import LogisticsConfig
from logistics.views import HomePageView, ItineraryListView, CityListView, CityCreateView, CityUpdateView, \
    CityDeleteView

app_name = LogisticsConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cities/', CityListView.as_view(), name='cities_list'),
    path('city_create/', CityCreateView.as_view(), name='city_create'),
    path('city_update/<int:pk>/', CityUpdateView.as_view(), name='city_update'),
    path('city_delete/<int:pk>/', CityDeleteView.as_view(), name='city_delete'),
    path('itineraries/', ItineraryListView.as_view(), name='itineraries_list'),
    ]
