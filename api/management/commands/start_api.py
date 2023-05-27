from django.core.management.base import BaseCommand

from api.tasks import start_api_task


class Command(BaseCommand):
    help = "Add locations and cars"

    def handle(self, *args, **options):
        start_api_task()
