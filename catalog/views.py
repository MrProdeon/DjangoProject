from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, "home_page/home.html")


def contact(request):
    if request.method == "POST":
        return HttpResponse("<div><h1>Данные успешно отправлены</h1></>")
    return render(request, "contact/contacts.html")


