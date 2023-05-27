from django.contrib import admin

from api.models import (
    Location,
    Car,
    Cargo,
)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'zip_code',
        'latitude',
        'longitude',
        'city',
        'state_name',
        'country_name',
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'car_number',
        'load_capacity',
    )
    
    
@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'cargo_weight',
        'cargo_description',
    )
