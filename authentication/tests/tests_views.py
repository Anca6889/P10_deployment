"""This module will test the authentication views"""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class ViewsTests(TestCase):
    """
    This class test all the autentication views.
    It'neccesary need to mock a user.
    """

    def setUp(self):
        """Setup the mocks"""

        self.client = Client()
        self.mock_user = User.objects.create(
            username='Hello_test',
            email='hello.test@hellotest.com',
            password='Coverate8462',
        )

    def test_sign_in_url(self):
        """Test the registering url"""

        response = self.client.get(reverse("sign_in"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/sign_in.html")

    def test_login_url(self):
        """Test the login url"""

        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "authentication/login.html")

    def test_register_an_user(self):
        """
        Test to create a 2nd fake user, if 2nd user is created properly,
        Then there should be two user in the fake database.
        """

        response = self.client.post(
            reverse("sign_in"),
            data={
                "email": "hello.test2@hellotest2.com",
                "username": "Hello_test2",
                "password1": "Globalshoot46",
                "password2": "Globalshoot46",
            }
        )
        self.assertEqual(response.status_code, 302)
        users_list = get_user_model().objects.all()
        self.assertEqual(users_list.count(), 2)

    def test_login_an_user(self):
        """Test to login the 1st mock user"""

        self.client.post(
            reverse("login"),
            data={
                "email": "hello.test@hellotest.com'",
                "password": "Coverate8462",
            }
        )
        self.assertTrue(self.mock_user.is_authenticated)
