
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """Create the formular for new user register"""

    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=60)

