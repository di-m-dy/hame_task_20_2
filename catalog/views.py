from django.shortcuts import render, get_object_or_404
from catalog.models import Category, Product, StoreContacts, UserContacts


def index(request):
    """
    Контроллер для главной страницы
    """
    product_data = list(Product.objects.all())[-3:]
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


def products(request):
    category_id = request.GET.get("category_id")
    if category_id:
        category_data = get_object_or_404(Category, id=category_id)
        product_data = Product.objects.filter(category_id=category_id)

    else:
        category_data = None
        product_data = Product.objects.all()

    context = {
        "category": category_data,
        "products": product_data,
        "categories": Category.objects.all()
    }
    return render(request, 'catalog/products.html', context=context)


def product(request, product_id):
    product_data = get_object_or_404(Product, id=product_id)
    context = {
        "product": product_data
    }
    return render(request, 'catalog/product.html', context=context)


def add_product(request):
    if request.method == "POST":
        category = request.POST.get("category")
        product_name = request.POST.get("product_name")
        product_description = request.POST.get("product_description")
        product_image = request.POST.get("product_image")
        product_price = request.POST.get("product_image")
        warning_text = ''
        if all(
            [
                product_name,
                product_description,
                product_image,
                product_price
            ]
        ):
            if not product_price.is_digit():
                warning_text = "В поле цена необходимо ввести числовое значение"
                return render(request, 'catalog/add_product.html', context={"warning": warning_text})

            product_data = Product(
                name=product_name,
                category=category,
                description=product_description,
                image=product_image,
                price=product_price
            )
            product_data.save
            return render(
                request,
                'catalog/success_adding_product.html',
                context={"product": product_data}
            )
    else:
        warning_text = 'Неверный ввод'
    return render(request, 'catalog/add_product.html', context={"warning": warning_text})
