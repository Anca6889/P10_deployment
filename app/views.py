from django.shortcuts import render
from .models import Product


def main(request):
    return render(request, 'base/home.html')


def get_legal_notice(request):
    return render(request, "base/legal_notice.html")


def get_contact(request):
    return render(request, "base/contact.html")


def explore(request):
    
    if request.method == "POST":
        search = request.POST.get("q")
        products = Product.objects.filter(
            product_name_fr__contains=search.strip().lower().capitalize()
        )[:6]
        context = {
            "search": search,
            "products": products,
        }
        return render(request, "app/product_list.html", context)
