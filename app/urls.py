"""
This module contain all the necessary urls of the base and product research
"""

from django.urls import path
from app import views

urlpatterns = [
    path('', views.main, name="main"),
    path("legal_notice/", views.get_legal_notice, name="legal_notice"),
    path("contact/", views.get_contact, name="contact"),
    path("explore/", views.SearchResults.as_view(), name="product_list"),
    path("substitutes/<int:product_id>/",
         views.get_substitutes, name="substitutes"),
    path("product/<int:product_id>/",
         views.get_product_details, name="product"),
    path("add_or_remove_favorite/<int:product_id>/",
         views.add_or_remove_favorite, name="add_or_remove_favorite"),
    path("favorites/", views.favorites_list, name="favorites")
]
