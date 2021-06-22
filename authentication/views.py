from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import SignInForm, LoginForm

def sign_in(request):
    form = SignInForm()

    if request.method == "POST":
        form = SignInForm(request.POST)

        if form.is_valid():
            messages.success(
                request, "Votre compte a été crée avec succès !")
            user = form.save()
            login(request, user, backend='authentication.backend.AuthenticationBackend')
            return redirect(reverse('login'))
        else:
            print(form.errors)
            for field in form.errors:
                print(field)

    context = {'form' : form}
    return render(request, "authentication/sign_in.html", context)

def sign_up(request):
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

    context = {'form' : form}

    return render(request, "authentication/login.html", context)

@login_required()
def account(request):
    actual_user = request.user
    context = {"user": actual_user}
    return render(request, "authentication/account.html", context)

@login_required()
def sign_out(request):
    logout(request)
    return render(request, "base/home.html")
