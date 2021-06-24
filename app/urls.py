from django.urls import path
from app import views

urlpatterns = [
    path('', views.main, name="main"),
    path("legal_notice/", views.get_legal_notice, name="legal_notice"),
    path("contact/", views.get_contact, name="contact"),
    path("explore/", views.explore, name="product_list"),
]
