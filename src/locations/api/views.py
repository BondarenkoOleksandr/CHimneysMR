from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, get_object_or_404
from django.core import serializers

from locations.api.serializers import CitySerializer, StateSerializer
from locations.models import City
from core.utils import add_images_path
from locations.models import State


class CitiesListView(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        cities = City.objects.order_by('state')
        return cities


class CitiesByStates(ListAPIView):
    serializer_class = CitySerializer

    def get(self, request, *args, **kwargs):
        states = State.objects.all()
        data = []
        for state in states:
            data.append({state.name: [city for city in City.objects.filter(state=state).values('name')]})

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class CityDetailView(RetrieveAPIView):

    def get(self, request, id):
        city = get_object_or_404(City, id=id)
        data = model_to_dict(city, fields=['name'])
        data.update({'state': city.state.name, 'first_screen': model_to_dict(city.fscity, exclude=['image']),
                     'second_screen': model_to_dict(city.sscity),
                     'third_screen': model_to_dict(city.tscity, exclude=['image'])})

        data = add_images_path(request, city, data)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})


class StateListView(ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class StateDetailView(ListAPIView):

    def get(self, request, id):
        state = get_object_or_404(State, id=id)
        data = model_to_dict(state, fields=['name'])
        data.update({'first_screen': model_to_dict(state.fsstate, exclude=['image', 'state']),
                     'second_screen': model_to_dict(state.ssstate, exclude=['state']),
                     'third_screen': model_to_dict(state.tsstate, exclude=['image', 'state'])})
        data = add_images_path(request, state, data)

        return JsonResponse(data, safe=False, json_dumps_params={'indent': 2})