from django.urls import path
from catalog.views import index, contacts, product, products

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('product/<int:product_id>', product, name="product"),
    path('products/', products, name="products")
]
