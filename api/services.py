import csv
import random

from api.models import Car, Location
from config.settings import BASE_DIR


def check_float(cell):
    try:
        float(cell)
    except ValueError:
        return False
    return True


def add_location():
    locations_csv = f"{BASE_DIR}/api/uszips.csv"
    with open(locations_csv) as f:
        reader_f = csv.reader(f)
        for row in reader_f:
            if (
                check_float(row[0])
                and check_float(row[1]
                and check_float(row[2]))
            ):
                location, created = Location.objects.update_or_create(
                    zip_code=int(row[0]),
                    latitude=float(row[1]),
                    longitude=float(row[2]),
                    city=row[3],
                    state_name=row[5],
                    country_name=row[11],
                )


def add_car():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    location = Location.objects.all()
    for car in range(1, 20):
        number, char = random.randint(1000, 9999), random.choice(char)
        car_number = f"{number}{char}"
        location = random.choice(location) if location else None
        load_capacity = random.randint(1, 1000)
        car = Car.objects.create(
            car_number=car_number,
            load_capacity=load_capacity,
        )
        car.location.add(location)
