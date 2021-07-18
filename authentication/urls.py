"""
This module contain all the necessary urls of the authentication
"""

from django.urls import path
from authentication import views

urlpatterns = [
    path('sign_in/', views.sign_in, name="sign_in"),
    path('login/', views.sign_up, name="login"),
    path("account/", views.account, name="account"),
    path("logout", views.sign_out, name="logout"),
]
