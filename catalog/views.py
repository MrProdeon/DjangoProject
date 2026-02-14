from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category, Product

# Create your views here.
def home_page(request):
    return render(request, "home_page/home.html")


def contact(request):
    if request.method == "POST":
        return HttpResponse("<div><h1>Данные успешно отправлены</h1></>")
    return render(request, "contact/contacts.html")


def one_product(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product" : product}
    return render(request, "product/product.html", context=context)


