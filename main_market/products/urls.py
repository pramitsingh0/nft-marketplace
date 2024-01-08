from django.urls import path

from .views import create_product_view, save_product

app_name = "products"
urlpatterns = [
    path("create/", create_product_view, name="create_view"),
    path("save-product/", save_product, name="save_product"),
]
