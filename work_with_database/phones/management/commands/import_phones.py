import csv

from django.core.management.base import BaseCommand
from ...models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for var in phones:
            lst = var.values()
            res = Phone()
            res.id, res.name, res.image, res.price, res.release_date, res.lte_exists = lst
            res.save()

