from django.shortcuts import render
from app.models import Product

def product(request):
    product = Product.object.all()
    return render(request, "product.html")
    