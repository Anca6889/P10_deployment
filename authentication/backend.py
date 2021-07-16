from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

User = get_user_model()


class AuthenticationBackend(ModelBackend):
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
