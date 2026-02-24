from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product, Contacts

# Create your views here.
def home_page(request):
    products = Product.objects.all()
    context = {"products" : products}
    return render(request, "home_page/home.html", context=context)


def contact(request):
    support = Contacts.objects.get(name="Техническая поддержка")
    sales_team = Contacts.objects.get(name="Отдел продаж")
    context = {
        "support" : support,
        "sales_team" : sales_team
    }
    if request.method == "POST":
        return HttpResponse("<div><h1>Данные успешно отправлены</h1></>")
    return render(request, "contact/contacts.html", context=context)


def one_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product" : product}
    return render(request, "product/product.html", context=context)

def add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        category = request.POST.get("category")
        description = request.POST.get("description")

        category_obj, is_created_category = Category.objects.get_or_create(name=category.title())

        product, created = Product.objects.get_or_create(
            name=name,
            defaults={
                "price": price,
                "category": category_obj,
                "description": description
            }
        )

        if created:
            return HttpResponse("<div><h1>Данные успешно отправлены</h1></div>")
        else:
            return HttpResponse("<div><h1>Данные об этом товаре уже есть.</h1></div>")

    return render(request, "product/add_product.html")
