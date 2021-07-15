from django.test import TestCase
from app.models import Product, Category


class Modelstests(TestCase):

    def setUp(self):

        self.mock_product = Product.objects.create(
            id='1',
            product_name_fr='testname',
            brands='testbrand',
            nutriscore_grade="e",
            stores='teststore',
            url='test/url.com',
            image='testimage'
        )

        self.mock_category = Category.objects.create(
            id='1',
            name='testcategory'
        )

    def test_id_product(self):
        result = self.mock_product.id
        self.assertEqual(result, 1)

    def test_name_product(self):
        result = self.mock_product.product_name_fr
        self.assertEqual(result, 'testname')

    def test_brands_product(self):
        result = self.mock_product.brands
        self.assertEqual(result, 'testbrand')

    def test_nutriscore_grade_product(self):
        result = self.mock_product.nutriscore_grade
        self.assertEqual(result, 'e')

    def test_stores_product(self):
        result = self.mock_product.stores
        self.assertEqual(result, 'teststore')

    def test_url_product(self):
        result = self.mock_product.url
        self.assertEqual(result, 'test/url.com')

    def test_image_product(self):
        result = self.mock_product.image
        self.assertEqual(result, 'testimage')

    def test_str_product(self):
        result = self.mock_product.__str__()
        self.assertEqual(result, 'testname')

    def test_str_category(self):
        result = self.mock_category.__str__()
        self.assertEqual(result, 'testcategory')
