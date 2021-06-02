from django.urls import path
from app import views

urlpatterns = [
    path('', views.main, name="main"),
]
