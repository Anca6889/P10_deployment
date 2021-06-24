from django.core.management.base import BaseCommand
from django.db.utils import DataError, IntegrityError
from app.models import Product, Category
from progress.bar import FillingSquaresBar

import requests


class Command(BaseCommand):

    def launch_process(self):

        print("regen database process launched...")
        self.clear_db()

    def clear_db(self):

        print("dropping actual database...")
        product_obj = Product.objects.all()
        product_obj.delete()

        cat_obj = Category.objects.all()
        cat_obj.delete()
        print("database cleared !")

        self.request_off_api()

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

        FIELDS = "brands,product_name_fr,stores,nutriscore_grade,url,image_front_url"

        PAGE_SIZE = 150
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
        with FillingSquaresBar(
            "Downloading products from OFF...",
                max=len(CATEGORIES), suffix="%(percent)d%%") as bar:
        
            for category in CATEGORIES:
                self.insert_category_in_db(category)
                payload["tag_0"] = category
                
                try:
                    data = requests.get(URL, params=payload)
                    results = data.json()
                    products.append(results['products'])
                    
                    
                except ValueError as err:
                    print("Error: {}".format(err))
                
                bar.next()
        bar.finish()

        self.delete_uncomplete_products(products)

    def insert_category_in_db(self, categories):

        Category.objects.get_or_create(
            name = categories
        )

    def delete_uncomplete_products(self, products):

        complete_products = []
        with FillingSquaresBar(
            "Removing corrupted products...",
                max=len(products), suffix="%(percent)d%%") as bar:

            for list in products:
                for p in list:
                    if (
                        p.get("product_name_fr")
                        and p.get("brands")
                        and p.get("nutriscore_grade")
                        and p.get("url")
                        and p.get('image_front_url')
                        and p.get("nutriscore_grade") is not None
                    ):
                        complete_products.append(p)

                    bar.next()
        bar.finish()

        self.insert_products_in_db(complete_products)

    def insert_products_in_db(self, products):
        
        with FillingSquaresBar(
            "Insering products in database...",
                max=len(products), suffix="%(percent)d%%") as bar:
            for product in products:

                try:
                    product_name_fr = product['product_name_fr']
                    brands = product['brands']
                    nutriscore_grade = product['nutriscore_grade']
                    stores = product['stores']
                    url = product['url']
                    image = product['image_front_url']

                    try:

                        Product.objects.get_or_create(
                            product_name_fr=product_name_fr,
                            brands=brands,
                            nutriscore_grade=nutriscore_grade,
                            stores=stores,
                            url=url,
                            image=image,
                        )
                    except KeyError:
                        pass

                    except DataError:
                        pass

                    except IntegrityError:
                        pass

                except KeyError:
                    pass
                bar.next()
        bar.finish()
        print("Process achieved with succsess !")
    def handle(self, *args, **options):

        self.launch_process()


