"""
    This module contains all the basic methods of app/views.py
    This way alow a optimise refactoring and make it easier to unittest.
"""

from app.models import Product, Category
from django.db.models import Count


class Service:
    """Contain all the methods of the app/views.py."""

    def manage_get_product(self, product_id):
        return Product.objects.get(pk=product_id)

    def manage_get_product_category(self, product):
        return Category.objects.filter(
            product__id=product.id)

    def manage_get_potentials_substitutes(self, product, category):
        return (
            Product.objects.filter(categories__in=category)
            .filter(nutriscore_grade__lt=product.nutriscore_grade)
            .annotate(nb_cat=Count("categories"))
            .filter(nb_cat__gte=4)
            .filter(nutriscore_grade__lt=product.nutriscore_grade)
            .order_by("nutriscore_grade")[:24]
        )

    def manage_sort_out_user_favorite_products(self, products, user):
        for product in products:
            if product.favorites.filter(id=user.id).exists():
                product.is_fav = True
            else:
                product.is_fav = False
        return products

    def manage_sort_out_if_product_is_favorite(self, product, user):
        if product.favorites.filter(id=user.id).exists():
            product.is_fav = True
        else:
            product.is_fav = False
        return product

    def manage_setup_get_substitutes_context(self, product_to_replace, substitutes):
        context = {
            "product": product_to_replace,
            "substitutes": substitutes
        }
        return context

    def manage_setup_get_product_details_context(self, product):
        context = {"product": product}
        return context

    def manage_setup_favorites_list_context(self, favorites):
        context = {"favorites": favorites}
        return context

    def manage_add_favorite(self, product, user):
        if product.favorites.filter(id=user.id).exists():
            product.favorites.remove(user.id)
        else:
            product.favorites.add(user.id)
