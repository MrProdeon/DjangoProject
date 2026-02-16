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
    pass
