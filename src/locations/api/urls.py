from django.urls import path

from locations.api.views import StateListView, StateDetailView, CitiesByStates, CityDetailView

app_name = 'locations_api'

urlpatterns = [
    path('states/', StateListView.as_view(), name='states-list'),
    path('states/<int:id>/', StateDetailView.as_view(), name='states-list'),
    path('cities/', CitiesByStates.as_view(), name='cities-list'),
    path('cities/<int:id>/', CityDetailView.as_view(), name='city-detail')

]
