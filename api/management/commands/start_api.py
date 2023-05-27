from django.core.management.base import BaseCommand

from api.models import Car
from api.services import add_cars


class Command(BaseCommand):
    help = "Add 20 car to database"

    def handle(self, *args, **options):
        cars_count = Car.objects.count()
        if cars_count < 20:
            add_cars()
