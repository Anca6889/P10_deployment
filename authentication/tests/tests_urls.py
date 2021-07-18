"""This module will test all the urls"""

from django.test import SimpleTestCase
from django.urls import resolve, reverse
from authentication import views


class UrlsTests(SimpleTestCase):
    """
    This class will test the urls using resolve and reverse modules
    Each method name describe exactly which url is tested.
    """

    def test_sign_in_url_is_resolved(self):
        url = reverse("sign_in")
        self.assertEquals(resolve(url).func, views.sign_in)

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, views.sign_up)

    def test_account_url_is_resolved(self):
        url = reverse("account")
        self.assertEquals(resolve(url).func, views.account)

    def test_sign_out_url_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, views.sign_out)
