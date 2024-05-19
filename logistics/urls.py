from django.urls import path

from logistics.apps import LogisticsConfig
from logistics.views import HomePageView

app_name = LogisticsConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    ]
