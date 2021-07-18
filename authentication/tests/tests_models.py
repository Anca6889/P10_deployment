"""This module test the models of authentication/models.py"""

from django.test import TestCase
from django.contrib.auth.models import User
from authentication.models import UserManager

test_um = UserManager()


class Modelstests(TestCase):
    """
    This class will mock a fake user and will tests if
    all the atributes from the fake database are matching.
    """

    def setUp(self):
        """Setup the mock"""

        self.mock_user = User.objects.create(
            id='1',
            username='Hello_test',
            email='hello.test@hellotest.com',
            password='Coverate8462',
        )

    def test_str(self):
        """Test if username is returned"""

        self.assertEquals(self.mock_user.__str__(), "Hello_test")

    def test_is_admin(self):
        """Test if user is an admin"""

        self.assertEquals(self.mock_user.is_superuser, False)

    def test_email(self):
        """Test if username is returned"""

        self.assertEquals(self.mock_user.email, "hello.test@hellotest.com")

    def test_password(self):
        """Test if password is returned"""

        self.assertEquals(self.mock_user.password, "Coverate8462")

    def test_id(self):
        """Test if id is returned"""

        self.assertEquals(self.mock_user.id, 1)
