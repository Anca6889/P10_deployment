from django.shortcuts import render
from django.db.models import Count
from .models import Product, Category


def main(request):
    return render(request, 'base/home.html')


def get_legal_notice(request):
    return render(request, "base/legal_notice.html")


def get_contact(request):
    return render(request, "base/contact.html")


def explore_products(request):
    
    if request.method == "POST":
        search = request.POST.get("q")
        products = Product.objects.filter(
            product_name_fr__contains=search.strip().lower().capitalize()
        )[:24]
        context = {
            "search": search,
            "products": products,
        }
        return render(request, "app/product_list.html", context)

def get_substitutes(request, product_id):
    
    product_to_replace = Product.objects.get(pk=product_id)

    product_category = Category.objects.filter(product__id=product_to_replace.id)

    substitutes = (
        Product.objects.filter(categories__in=product_category)
        .filter(nutriscore_grade__lt=product_to_replace.nutriscore_grade)
        .annotate(nb_cat=Count("categories"))
        .filter(nb_cat__gte=4)
        .filter(nutriscore_grade__lt=product_to_replace.nutriscore_grade)
        .order_by("nutriscore_grade")[:24]
    )

    context = {"product": product_to_replace, "substitutes": substitutes}

    return render(request, "app/substitutes.html", context)

def get_product_details(request, product_id):

    product = Product.objects.get(pk=product_id)
    context = {"product": product}

    return render(request, "app/product_details.html", context)
