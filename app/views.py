from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Product
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from app.service import Service

service = Service()

def main(request):
    return render(request, 'base/home.html')


def get_legal_notice(request):
    return render(request, "base/legal_notice.html")


def get_contact(request):
    return render(request, "base/contact.html")


class SearchResults(ListView):

    model = Product
    template_name = "app/product_list.html"

    def get_queryset(self):
        query = self.request.GET.get("search")
        return Product.objects.filter(
            Q(product_name_fr__icontains=query)
            )

def get_substitutes(request, product_id):

    user = request.user
    product_to_replace = service.manage_get_product(product_id)
    product_category = service.manage_get_product_category(product_to_replace)
    substitutes = service.manage_get_potentials_substitutes(product_to_replace, product_category)
    substitutes = service.manage_sort_out_user_favorite_products(substitutes, user)

    context = {
        "product": product_to_replace,
        "substitutes": substitutes
    }

    return render(request, "app/substitutes.html", context)


def get_product_details(request, product_id):

    product = Product.objects.get(pk=product_id)

    if product.favorites.filter(id=request.user.id).exists():
        product.is_fav = True
    else:
        product.is_fav = False

    context = {"product": product}

    return render(request, "app/product_details.html", context)


@login_required()
def add_favorite(request, product_id):

    product = Product.objects.get(pk=product_id)
    user = request.user

    if product.favorites.filter(id=user.id).exists():
        product.favorites.remove(user.id)
    else:
        product.favorites.add(user.id)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@login_required()
def favorites_list(request):
    user = request.user
    favorites = user.favorites.all()
    for favorite in favorites:
        if favorite.favorites.filter(id=request.user.id).exists():
            favorite.is_fav = True
        else:
            favorite.is_fav = False

    context = {"favorites": favorites}
    return render(request, "app/favorites.html", context)
