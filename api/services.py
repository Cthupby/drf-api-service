import random

from api.models import Car, Location


def add_cars():
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # location = Location.objects.all()
    for car in range(1, 20):
        car_number = f"{random.randint(1000, 9999)}{random.choice(char)}"
        # location = random.choice(location) if location else None
        load_capacity = random.randint(1, 1000)
        Car.objects.create(
            car_number=car_number,
            # location=location,
            load_capacity=load_capacity,
        )
