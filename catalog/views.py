from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product, StoreContacts, UserContacts


def index(request):
    """
    Контроллер для главной страницы
    """
    product_data = list(Product.objects.all())[-6:]
    return render(request, 'catalog/index.html', {"products": product_data})


def contacts(request):
    """
    Контроллер для страницы контактов
    """
    contacts_data = StoreContacts.objects.all()
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        context = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email
        }
        UserContacts.objects.create(first_name=first_name, last_name=last_name, email=email)
        return render(request, 'catalog/thanx.html', context)
    return render(request, 'catalog/contacts.html', {"contacts": contacts_data})


def product(request, product_id):
    product_data = get_object_or_404(Product, id=product_id)
    context = {
        "product": product_data
    }
    return render(request, 'catalog/product.html', context=context)
