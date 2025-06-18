from config.celery import app

from api.models import Car
from api.services import add_car, add_location


@app.task
def start_api_task():
    add_location()
    cars_count = Car.objects.count()
    if cars_count < 20:
        add_car()
