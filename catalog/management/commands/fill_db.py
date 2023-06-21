from typing import Any, Optional
from django.core.management import BaseCommand

from catalog.models import Product, Category

import json




class Command(BaseCommand):
    
    def handle(self, *args, **options) -> None:
        
        path = 'catalog_data.json'
        data = json_reader(path)

        for item in data:
            if item["model"] == "catalog.product":
                Product.objects.create(name=item["fields"]["name"],
                                       description=item["fields"]["description"],
                                       image_preview=item["fields"]["image_preview"],
                                       category=item["fields"]["category"],
                                       price=item["fields"]["price"],
                                       creation_date=item["fields"]["creation_date"],
                                       update_date=item["fields"]["update_date"]
                                       )
            
            elif item["model"] == "catalog.category":
                Category.objects.create(name=item["fields"]["name"],
                                        description=item["fields"]["description"]
                                        )


def json_reader(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data