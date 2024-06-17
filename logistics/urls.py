from django.urls import path

from logistics.apps import LogisticsConfig
from logistics.views import HomePageView, ItineraryListView, ItineraryCreateView, ItineraryPlanListView, \
    ItineraryUpdateView, ItineraryDeleteView

app_name = LogisticsConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('itineraries/', ItineraryListView.as_view(), name='itineraries_list'),  # список разгрузок
    path('itinerary_create/', ItineraryCreateView.as_view(), name='itinerary_create'),
    path('itinerary_update/<int:pk>/', ItineraryUpdateView.as_view(), name='itinerary_update'),
    path('itinerary_delete/<int:pk>/', ItineraryDeleteView.as_view(), name='itinerary_delete'),
    path('planing_itineraries/', ItineraryPlanListView.as_view(), name='itineraries_plan_list'),
    ]
