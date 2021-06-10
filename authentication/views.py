from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignInForm, LoginForm

def sign_in(request):
    form = SignInForm(request.POST)
    context = {'form' : form}
    return render(request, "authentication/sign_in.html", context)

def login(request):
    form = LoginForm(request.POST)
    context = {'form' : form}
    return render(request, "authentication/login.html", context)
