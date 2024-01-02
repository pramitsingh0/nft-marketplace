from django.urls import path

from .views import create_product_view

app_name = "products"
urlpatterns = [
    path("create/", create_product_view, name="create_view"),
]
