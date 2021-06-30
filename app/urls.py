from django.urls import path
from app import views

urlpatterns = [
    path('', views.main, name="main"),
    path("legal_notice/", views.get_legal_notice, name="legal_notice"),
    path("contact/", views.get_contact, name="contact"),
    path("explore/", views.explore_products, name="product_list"),
    path("substitutes/<int:product_id>/",views.get_substitutes, name="substitutes"),
    path("product/<int:product_id>/", views.get_product_details, name="product"),
]
