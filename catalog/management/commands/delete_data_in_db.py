from typing import Any, Optional
from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        Product.objects.all().delete()
        Category.objects.all().delete()
