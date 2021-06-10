from django.shortcuts import render
# from app.models import Product

def main(request):
    return render(request, 'base/home.html')


def get_legal_notice(request):
    return render(request, "base/legal_notice.html")


def get_contact(request):
    return render(request, "base/contact.html")

# def product(request):
#     product = Product.objects.all()
#     return render(request, "product.html")
