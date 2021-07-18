"""This module will test all the methods in service.py used for the views"""

from django.test import TestCase
from django.contrib.auth.models import User
from app.models import Product, Category
from app.service import Service

service = Service()  # Load all the necessary methods from service.py


class ServiceTests(TestCase):
    """
    This class will use several mocks: 1 user, 2 products and 4 categories to
    test all the services functions.
    """

    def setUp(self):
        """Setup all the mocks"""

        self.mock_user = User.objects.create(
            id='1',
            username='Hello_test',
            email='hello.test@hellotest.com',
            password='Coverate8462'
        )

        self.mock_product = Product.objects.create(
            id='1',
            product_name_fr='testname',
            brands='testbrand', nutriscore_grade="e",
            stores='teststore',
            url='test/url.com',
            image='testimage'
        )

        self.mock_product2 = Product.objects.create(
            id='2',
            product_name_fr='testname2',
            brands='testbrand2', nutriscore_grade="a",
            stores='teststore2',
            url='test2/url.com',
            image='testimage2'
        )

        self.mock_category = Category.objects.create(
            id='1',
            name='testcategory'
        )
        self.mock_category2 = Category.objects.create(
            id='2',
            name='testcategory2'
        )
        self.mock_category3 = Category.objects.create(
            id='3',
            name='testcategory3'
        )
        self.mock_category4 = Category.objects.create(
            id='4',
            name='testcategory4'
        )

    def test_manage_get_product(self):
        """Test that method get the product with the Id"""

        service.manage_get_product(1)
        self.assertEqual(self.mock_product.product_name_fr, 'testname')

    def test_manage_get_product_categories(self):
        """Test that method get the assigned category of the product"""

        self.mock_product.categories.set("1")
        product_category = service.manage_get_product_categories(
            self.mock_product)
        items = []
        for values in product_category.values():
            for value in values.values():
                items.append(value)
        self.assertIn('testcategory', items)

    def test_manage_get_potentials_substitutes(self):
        """
        Test that the method get correctly the 2nd mock product wich have an
        better nutriscore than the 1st product
        With the 1st product and his categories as parameters
        """

        self.mock_product.categories.add("1", "2", "3", "4")
        self.mock_product2.categories.add("1", "2", "3", "4")
        product_category = "1", "2", "3", "4"
        substitutes = service.manage_get_potentials_substitutes(
            self.mock_product, product_category)
        items = []
        for values in substitutes.values():
            for value in values.values():
                items.append(value)
        self.assertIn('testname2', items)

    def test_manage_sort_out_user_favorite_products(self):
        """
        Test that the method will return correctly that the 1st product mock
        is in user mock favorites from a list with the two product mocks
        """

        self.mock_product.favorites.add("1")
        products = [self.mock_product, self.mock_product2]
        service.manage_sort_out_user_favorite_products(
            products, self.mock_user)
        self.assertEqual(self.mock_product.is_fav, True)
        self.assertEqual(self.mock_product2.is_fav, False)

    def test_manage_setup_get_substitutes_context(self):
        """Test that the context of the method is correctly set"""

        product_to_replace = self.mock_product
        substitutes = [self.mock_product2]
        context = service.manage_setup_get_substitutes_context(
            product_to_replace, substitutes)
        for keys, vals in context.items():
            for key in keys:
                if key == "product":
                    self.assertEqual(vals, self.mock_product)
                elif key == "substitutes":
                    self.assertEqual(vals, self.mock_product2)

    def test_manage_sort_out_if_product_is_favorite_is_true(self):
        """
        Test that the method will return correctly that a product mock
        is in user mock favorites
        """

        self.mock_product.favorites.add("1")
        service.manage_sort_out_if_product_is_favorite(
            self.mock_product, self.mock_user)
        self.assertEqual(self.mock_product.is_fav, True)

    def test_manage_sort_out_if_product_is_favorite_is_false(self):
        """
        Test that the method will return correctly that a product mock
        is NOT in user mock favorites
        """

        service.manage_sort_out_if_product_is_favorite(
            self.mock_product, self.mock_user)
        self.assertEqual(self.mock_product.is_fav, False)

    def test_manage_setup_get_product_details_context(self):
        """Test that the context of the method is correctly set"""

        context = service.manage_setup_get_product_details_context(
            self.mock_product)
        for keys, vals in context.items():
            for key in keys:
                if key == "product":
                    self.assertEqual(vals, self.mock_product)

    def test_manage_setup_favorites_list_context(self):
        """Test that the context of the method is correctly set"""

        favorites = [self.mock_product, self.mock_product2]
        context = service.manage_setup_get_product_details_context(
            favorites)
        for keys, vals in context.items():
            for key in keys:
                if key == "favorites":
                    self.assertEqual(vals, favorites)

    def test_manage_add_favorite(self):
        """Test that 2nd product mock is correctly insert in favorites"""

        service.manage_add_or_remove_favorite(
            self.mock_product2, self.mock_user)
        for value in self.mock_product.favorites.values():
            self.assertEqual(value, self.mock_user.id)

    def test_manage_remove_favorite(self):
        """
        Test that 2nd product mock is correctly remove from favorites
        METHOD IS SIMILAR THAN ABOVE, BECAUSE THE ABOVE METHOD INSERT
        PRODUCT IN FAVORITES, SO THE BELOW SIMILAR METHOD WILL REMOVE IT
        """

        service.manage_add_or_remove_favorite(
            self.mock_product2, self.mock_user)
        for value in self.mock_product.favorites.values():
            self.assertEqual(value, None)
