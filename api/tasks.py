from config.celery import app

from api.models import Car
from api.services import add_cars, add_locations


@app.task
def start_api_task():
    add_locations()
    cars_count = Car.objects.count()
    if cars_count < 20:
        add_cars()
