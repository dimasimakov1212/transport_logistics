from django.urls import path

from company.apps import CompanyConfig
from company.views import DriversListView, DriverCreateView, DriverUpdateView, DriverDeleteView, VehicleListView, \
    VehicleCreateView, VehicleDeleteView, VehicleUpdateView

app_name = CompanyConfig.name

urlpatterns = [
    path('drivers/', DriversListView.as_view(), name='drivers_list'),
    path('driver_create/', DriverCreateView.as_view(), name='driver_create'),
    path('driver_update/<int:pk>/', DriverUpdateView.as_view(), name='driver_update'),
    path('driver_delete/<int:pk>/', DriverDeleteView.as_view(), name='driver_delete'),
    path('vehicles/', VehicleListView.as_view(), name='vehicles_list'),
    path('vehicle_create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicle_update/<int:pk>/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicle_delete/<int:pk>/', VehicleDeleteView.as_view(), name='vehicle_delete'),
    ]
