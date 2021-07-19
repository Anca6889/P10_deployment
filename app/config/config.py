"""
    This module contains the constants of the API call
    in app/management/commands/database.py
"""

CATEGORIES = [
    "aliments-et-boissons-a-base-de-vegetaux",
    "aliments-d-origine-vegetale",
    "boissons",
    "produits-de-la-mer",
    "sauces",
    "confiseries",
    "conserves",
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

FIELDS = "brands,product_name_fr,stores,nutriscore_grade,url,image_front_url,categories"

PAGE_SIZE = 60

PAYLOAD = {
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
