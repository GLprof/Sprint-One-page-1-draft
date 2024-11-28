from django.urls import path

from .views import api_view, submitData

urlpatterns = [path('geo/', api_view(submitData)), ]
