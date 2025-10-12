import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from slugify import slugify


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        try:
            for phone in phones:
                ph = Phone(
                    id=phone['id'], 
                    name=phone['name'], 
                    price=phone['price'], 
                    image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists=phone['lte_exists'],
                    slug=slugify(phone['name']),
                )
                ph.save()
        except Exception as e:
            print(f"Импорт прошел с ошибкой: {e}")
