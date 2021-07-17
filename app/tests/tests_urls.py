"""This module will test all the urls"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from app.views import SearchResults
from app import views


class UrlsTests(SimpleTestCase):
    """
    This class will test the urls using resolve and reverse modules
    Each method name describe exactly which url is tested.
    """

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

    def test_add_or_remove_favorite_url_is_resolved(self):
        url = reverse("add_or_remove_favorite", kwargs={"product_id": 1})
        self.assertEquals(resolve(url).func, views.add_or_remove_favorite)

    def test_favorites_url_is_resolved(self):
        url = reverse("favorites",)
        self.assertEquals(resolve(url).func, views.favorites_list)
