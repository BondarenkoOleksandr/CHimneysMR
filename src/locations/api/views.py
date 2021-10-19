from rest_framework.generics import ListAPIView, RetrieveAPIView

from locations.api.serializers import CitySerializer, CityDetailSerializer, StateSerializer, StateDetailSerializer
from locations.models import City, State


class CitiesListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        cities = City.objects.order_by('state')
        return cities


class CitiesByStates(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetailView(RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CityDetailSerializer
    lookup_field = 'slug'


class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetailView(RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateDetailSerializer
    lookup_field = 'slug'
