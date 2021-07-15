from django.test import TestCase
from django.contrib.auth.models import User
from authentication.models import UserManager

test_um = UserManager()


class Modelstests(TestCase):

    def setUp(self):

        self.mock_user = User.objects.create(
            id='1',
            username='Hello_test',
            email='hello.test@hellotest.com',
            password='Coverate8462',
        )

    def test_str(self):
        self.assertEquals(self.mock_user.__str__(), "Hello_test")

    def test_is_admin(self):
        self.assertEquals(self.mock_user.is_superuser, False)

    def test_email(self):
        self.assertEquals(self.mock_user.email, "hello.test@hellotest.com")

    def test_password(self):
        self.assertEquals(self.mock_user.password, "Coverate8462")

    def test_id(self):
        self.assertEquals(self.mock_user.id, 1)
