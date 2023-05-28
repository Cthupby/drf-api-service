from rest_framework import serializers

from api.models import (
    Location,
    Car,
    Cargo,
)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'zip_code',
        )


class CargoSerializer(serializers.ModelSerializer):
    #l_pickup = LocationSerializer(many=False)
    #l_delivery = LocationSerializer(many=False)
    class Meta:
        model = Cargo
        fields = (
            'location_pickup',
            'location_delivery',
            'cargo_weight',
            'cargo_description',
        )
