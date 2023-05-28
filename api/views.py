from rest_framework import generics

from api.models import (
    Location,
    Car,
    Cargo,
)
from api.serializers import (
    #Location,
    #Car,
    CargoSerializer,
)


class CargoCreate(generics.CreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoList(generics.ListAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoUpdate(generics.UpdateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer


class CargoRemove(generics.RetrieveDestroyAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
