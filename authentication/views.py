"""
This module contains all the views necessary to run the autenthication
Note: The django authentication engine have been modified to allow a user to
login with is email OR with his username. This changes can be found in:
authentication/backend.py
"""

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import SignInForm, LoginForm


def sign_in(request):
    """This view manage the creation of an user account and allow him to
    login"""

    form = SignInForm()

    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            messages.success(
                request, "Votre compte a été crée avec succès !")
            user = form.save()
            login(request, user,
                  backend='authentication.backend.AuthenticationBackend')
            return redirect(reverse('login'))
        else:
            print(form.errors)
            for field in form.errors:
                print(field)

    context = {'form': form}
    return render(request, "authentication/sign_in.html", context)


def sign_up(request):
    """This view allow an user to authenticate himself and login"""

    form = LoginForm()

    if request.method == "POST":
        email_or_user = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, username=email_or_user, password=password)

        if user is not None:
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return render(request, "base/home.html")
        else:
            messages.error(request, "L'email ou le mot de passe est incorrect")

    context = {'form': form}
    return render(request, "authentication/login.html", context)


@login_required()
def account(request):
    """This view return the user account page with his informations"""

    actual_user = request.user
    context = {"user": actual_user}
    return render(request, "authentication/account.html", context)


@login_required()
def sign_out(request):
    """This view logout the user"""

    logout(request)
    return render(request, "base/home.html")
