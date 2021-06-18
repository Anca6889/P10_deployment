from django.core.management.base import BaseCommand
from app.models import Product, Category

import requests


class Command(BaseCommand):

    def request_off_api(self):
        help = 'feel the database with OFF products'

        # SETTING BEGIN
        CATEGORIES = [
            "pates-a-tartiner",
            "petit-dejeuners",
            "sodas",
            "snacks",
            "aperitif",
            "produits-laitiers",
            "plats-prepares",
            "desserts",
            "complements-alimentaires",
            "snacks-sucres",
            "charcuteries",
            "fromages",
            "condiments",
            "surgeles",
            "pizzas"
        ]

        URL = "https://fr.openfoodfacts.org/cgi/search.pl"

        FIELDS = "brands,product_name_fr,stores,nutriscore_grade,url"

        PAGE_SIZE = 100
        # SETTING END

        payload = {
            "search_simple": 1,
            "action": "process",
            "tagtype_0": "categories",
            "tag_contains_0": "contains",
            "tag_0": None,
            "sort_by": "unique_scans_n",
            "page_size": PAGE_SIZE,
            "json": 1,
            "fields": FIELDS
        }
        products = []

        for category in CATEGORIES:
            payload["tag_0"] = category

            try:
                data = requests.get(URL, params=payload)
                results = data.json()
                print(results)
                return results

            except ValueError as err:
                print("Error: {}".format(err))


