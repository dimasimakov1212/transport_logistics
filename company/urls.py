from django.urls import path

from company.apps import CompanyConfig
from company.views import DriversListView, DriverCreateView, DriverUpdateView, DriverDeleteView

app_name = CompanyConfig.name

urlpatterns = [
    path('drivers/', DriversListView.as_view(), name='drivers_list'),
    path('driver_create/', DriverCreateView.as_view(), name='driver_create'),
    path('driver_update/<int:pk>/', DriverUpdateView.as_view(), name='driver_update'),
    path('driver_delete/<int:pk>/', DriverDeleteView.as_view(), name='driver_delete'),
    ]
