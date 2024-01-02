from django.shortcuts import render


# Create your views here.
#
#
def create_product_view(request):
    return render(request, "marketplace/products/create.html")
