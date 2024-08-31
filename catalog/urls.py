from django.urls import path
from catalog.views import index, contacts, product, products, add_product, success_adding_product

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:product_id>', product, name="product"),
    path('products/', products, name="products"),
    path('add_product/', add_product, name="add_product"),
    path('sucess_adding_product/', success_adding_product, name="success_adding_product")
]
