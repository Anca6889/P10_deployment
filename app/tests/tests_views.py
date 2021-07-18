"""This module will test the views"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from app.models import Product


class Viewstests(TestCase):
    """
    This class test all the views
    As most of the methods of the views are contained in app/service.py,
    The only thing we still have to test is that the views return the correct
    templates. It'neccesary to mock a user, a product and catch all the urls.
    Each method name describe exactly which view is tested.
    """

    def setUp(self):
        """Setup the mocks and urls"""

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

        self.client = Client()
        self.main_url = reverse("main")
        self.legal_notice_url = reverse("legal_notice")
        self.contact_url = reverse("contact")
        self.substitutes_url = reverse("substitutes", args=[1])
        self.product_details_url = reverse("product", args=[1])
        self.add_or_remove_favorite_url = reverse("add_or_remove_favorite",
                                                  args=[1])
        self.favorites_list_url = reverse("favorites")
        self.explore_products_url = reverse("product_list")+"?search=testname"

    def test_main_view(self):
        response = self.client.get(self.main_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base/home.html")

    def test_legal_notice_view(self):
        response = self.client.get(self.legal_notice_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base/legal_notice.html")

    def test_contact_view(self):
        response = self.client.get(self.contact_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "base/contact.html")

    def test_get_substitutes_view(self):
        response = self.client.get(self.substitutes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/substitutes.html")

    def test_get_product_details_view(self):
        response = self.client.get(self.product_details_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/product_details.html")

    def test_get_add_or_remove_favorite_view(self):
        self.client.force_login(self.mock_user)
        response = self.client.get(self.add_or_remove_favorite_url)
        self.assertEqual(response.status_code, 302)

    def test_get_favorites_list_view(self):
        self.client.force_login(self.mock_user)
        response = self.client.get(self.favorites_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/favorites.html")

    def test_SearchResults_view(self):
        response = self.client.get(self.explore_products_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/product_list.html")
