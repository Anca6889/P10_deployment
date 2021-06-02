from django.shortcuts import render
# from app.models import Product

def main(request):
    return render(request, 'index.html')

# def product(request):
#     product = Product.objects.all()
#     return render(request, "product.html")
