"""This module contains the specifics authentication formulars used in views"""

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignInForm(UserCreationForm):
    """This class will create the Sign in formular"""

    email = forms.EmailField(
        max_length=282,
        widget=forms.TextInput(
            attrs={
                "id": "email",
                "class": "form-control",
                "placeholder": "Adresse email",
            }
        ),
    )
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "id": "username",
                "class": "form-control",
                "placeholder": "Nom d'utilisateur",
            }
        ),
    )
    password1 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(
            attrs={
                "id": "password1",
                "class": "form-control",
                "placeholder": "Mot de passe",
            }
        ),
    )
    password2 = forms.CharField(
        max_length=16,
        widget=forms.PasswordInput(
            attrs={
                "id": "password2",
                "class": "form-control",
                "placeholder": "Confirmer votre mot de passe",

            }
        ),
    )

    class Meta:
        model = User
        fields = ["email", "username", "password1", "password2"]


class LoginForm(forms.Form):
    """This class will create the Sign in formular"""

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "id": "login_email",
                "class": "form-control",
                "placeholder": "Adresse email ou nom d'utilisateur",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "login_password",
                "class": "form-control",
                "placeholder": "Mot de passe",
            }
        )
    )
