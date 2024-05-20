from django.urls import path

from logistics.apps import LogisticsConfig
from logistics.views import HomePageView, ItineraryListView, ItineraryCreateView

app_name = LogisticsConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('itineraries/', ItineraryListView.as_view(), name='itineraries_list'),
    path('itinerary_create/', ItineraryCreateView.as_view(), name='itinerary_create'),
    ]
