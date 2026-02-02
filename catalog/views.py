from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, "catalog/catalog.html")


def contact(request):
    return render(request, "contact/contacts.html")


