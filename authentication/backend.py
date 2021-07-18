"""
This module is a modification of the authentication engine allowing user to
login with his email OR with his username. Used in the views.
"""

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class AuthenticationBackend(ModelBackend):
    """
    This class will convert the input (user email or user username) of the user
    in the user username. Username is the request value for login.
    """

    def authenticate(self, request,  username=None, password=None, **kwargs):
        usermodel = get_user_model()
        print(usermodel)

        try:
            user = usermodel.objects.get(Q(username__iexact=username) | Q(
                email__iexact=username))
            if user.check_password(password):
                return user
        except usermodel.DoesNotExist:
            pass
