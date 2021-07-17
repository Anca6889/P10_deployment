"""
This module contains all the views necessary to run the product research and
also the base templates. This module is mostly working with app/service.py
"""

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from app.service import Service

service = Service()  # Load all the necessary methods from service.py


def main(request):
    """Display the home page"""

    return render(request, 'base/home.html')


def get_legal_notice(request):
    """Display the legals page"""

    return render(request, "base/legal_notice.html")


def get_contact(request):
    """Display the contact page"""
    return render(request, "base/contact.html")


class SearchResults(ListView):
    """Will display the 1st products page results with input of user"""

    model = Product
    template_name = "app/product_list.html"

    def get_queryset(self):
        """
        Get the user input and return each product who contains the input
        in his name
        """

        query = self.request.GET.get("search")
        return Product.objects.filter(
            Q(product_name_fr__icontains=query)
        )


def get_substitutes(request, product_id):
    """
    Find out potentials substitutes with similar products what are
    sharing 4 similar categories and sort them out by nutriscore grade
    """

    user = request.user
    prod_to_replace = service.manage_get_product(product_id)
    product_categories = service.manage_get_product_categories(prod_to_replace)
    substitutes = service.manage_get_potentials_substitutes(
        prod_to_replace, product_categories)
    substitutes = service.manage_sort_out_user_favorite_products(
        substitutes, user)
    context = service.manage_setup_get_substitutes_context(
        prod_to_replace, substitutes)
    return render(request, "app/substitutes.html", context)


def get_product_details(request, product_id):
    """Display a specific page for the products with all the informations"""

    user = request.user
    product = service.manage_get_product(product_id)
    product = service.manage_sort_out_if_product_is_favorite(product, user)
    context = service.manage_setup_get_product_details_context(product)
    return render(request, "app/product_details.html", context)


@login_required()
def add_or_remove_favorite(request, product_id):
    """Add or remove a product in favorites list by clicking on heart"""

    user = request.user
    product = service.manage_get_product(product_id)
    service.manage_add_or_remove_favorite(product, user)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required()
def favorites_list(request):
    """Display the favorites product list page of the user"""

    user = request.user
    favorites = user.favorites.all()
    favorites = service.manage_sort_out_user_favorite_products(favorites, user)
    context = service.manage_setup_favorites_list_context(favorites)
    return render(request, "app/favorites.html", context)
