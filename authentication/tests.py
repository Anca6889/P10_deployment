from django.test import TestCase, SimpleTestCase
from django.urls import resolve, reverse
from authentication import views


class UrlsTests(SimpleTestCase):

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
