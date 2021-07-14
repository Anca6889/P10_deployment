from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from django.contrib.auth.models import User
from app.models import Product, Category
from app import views
from app.service import Service
from app.views import SearchResults
service = Service()


class UrlsTests(SimpleTestCase):

    def test_main_url_is_resolved(self):
        url = reverse("main")
        self.assertEquals(resolve(url).func, views.main)

    def test_legals_url_is_resolved(self):
        url = reverse("legal_notice")
        self.assertEquals(resolve(url).func, views.get_legal_notice)

    def test_contact_url_is_resolved(self):
        url = reverse("contact")
        self.assertEquals(resolve(url).func, views.get_contact)

    def test_explore_url_is_resolved(self):
        resolver = resolve(reverse("product_list"))
        self.assertEquals(resolver.func.__name__,
                          SearchResults.as_view().__name__)

    def test_substitutes_url_is_resolved(self):
        url = reverse("substitutes", kwargs={"product_id": 1})
        self.assertEquals(resolve(url).func, views.get_substitutes)

    def test_product_url_is_resolved(self):
        url = reverse("product", kwargs={"product_id": 1})
        self.assertEquals(resolve(url).func, views.get_product_details)

    def test_add_favorite_url_is_resolved(self):
        url = reverse("add_favorite", kwargs={"product_id": 1})
        self.assertEquals(resolve(url).func, views.add_favorite)

    def test_favorites_url_is_resolved(self):
        url = reverse("favorites",)
        self.assertEquals(resolve(url).func, views.favorites_list)


class ServiceTests(TestCase):

    def setUp(self):

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
        self.mock_category3= Category.objects.create(
            id='3',
            name='testcategory3'
        )
        self.mock_category4 = Category.objects.create(
            id='4',
            name='testcategory4'
        )

    def test_manage_get_product(self):
        service.manage_get_product(1)
        self.assertEqual(self.mock_product.product_name_fr, 'testname')

    def test_manage_get_product_category(self):
        self.mock_product.categories.set("1")
        product_category = service.manage_get_product_category(
            self.mock_product)
        items = []
        for values in product_category.values():
            for value in values.values():
                items.append(value)
        self.assertIn('testcategory', items)

    def test_manage_get_potentials_substitutes(self):
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
        self.mock_product.favorites.add("1")
        products = [self.mock_product, self.mock_product2]
        service.manage_sort_out_user_favorite_products(products, self.mock_user)
        self.assertEqual(self.mock_product.is_fav, True)
        self.assertEqual(self.mock_product2.is_fav, False)

    def test_manage_setup_get_substitutes_context(self):
        product_to_replace = self.mock_product
        substitutes = [self.mock_product2]
        context = service.manage_setup_get_substitutes_context(product_to_replace, substitutes)
        for keys, vals in context.items():
            for key in keys:
                if key == "product":
                    self.assertEqual(vals, self.mock_product)
                elif key == "substitutes":
                    self.assertEqual(vals, self.mock_product2)
    
    def test_manage_sort_out_if_product_is_favorite_is_true(self):
        self.mock_product.favorites.add("1")
        service.manage_sort_out_if_product_is_favorite(
            self.mock_product, self.mock_user)
        self.assertEqual(self.mock_product.is_fav, True)

    def test_manage_sort_out_if_product_is_favorite_is_false(self):
        service.manage_sort_out_if_product_is_favorite(
            self.mock_product, self.mock_user)
        self.assertEqual(self.mock_product.is_fav, False)

    def test_manage_setup_get_product_details_context(self):
        context = service.manage_setup_get_product_details_context(
            self.mock_product)
        for keys, vals in context.items():
            for key in keys:
                if key == "product":
                    self.assertEqual(vals, self.mock_product)

    def test_manage_setup_favorites_list_context(self):
        favorites = [self.mock_product, self.mock_product2]
        context = service.manage_setup_get_product_details_context(
            favorites)
        for keys, vals in context.items():
            for key in keys:
                if key == "favorites":
                    self.assertEqual(vals, favorites)

    def test_manage_add_favorite(self):
        service.manage_add_favorite(self.mock_product2, self.mock_user)
        for value in self.mock_product.favorites.values():
            self.assertEqual(value, self.mock_user.id)

    def test_manage_remove_favorite(self):
        service.manage_add_favorite(self.mock_product2, self.mock_user)
        for value in self.mock_product.favorites.values():
            self.assertEqual(value, None)
