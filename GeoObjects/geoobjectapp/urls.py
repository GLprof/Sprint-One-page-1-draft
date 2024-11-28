from django.urls import path

from .views import GeoApiView

urlpatterns = [path('geo/', GeoApiView.as_view(), name='geo_data')]
