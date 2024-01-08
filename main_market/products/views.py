import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Product


# Create your views here.
#
#

def create_product_view(request):
    return render(request, "marketplace/products/create.html")


def save_product(request):
    if request.method != "POST":
        return JsonResponse({"error": "Method Error! Only POST request allowed"})
    prod_name = request.POST.get("name")
    prod_handler = request.POST.get("handler")
    price = request.POST.get("price")
    product = Product(name=prod_name, handle=prod_handler, price=float(price))
    try:
        product.save()
        return HttpResponse(b"Product Saved", status=200)
        # return HttpResponseRedirect(reverse("products:product_listing"))
    except Exception as e:
        print(e)
        return JsonResponse({"error": "Error Saving product"}, status=500)
