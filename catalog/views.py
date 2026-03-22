from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from catalog.models import Category, Product, Contacts
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from catalog.forms import ProductForm, ProductDeleteForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# # Create your views here.
# def home_page(request):
#     products = Product.objects.all()
#     context = {"products" : products}
#     return render(request, "home_page/home.html", context=context)

class ProductListView(ListView):

    model = Product
    template_name = "home_page/home.html"
    context_object_name = "products"



# def contact(request):
#     support = Contacts.objects.get(name="Техническая поддержка")
#     sales_team = Contacts.objects.get(name="Отдел продаж")
#     context = {
#         "support" : support,
#         "sales_team" : sales_team
#     }
#     if request.method == "POST":
#         return HttpResponse("<div><h1>Данные успешно отправлены</h1></>")
#     return render(request, "contact/contacts.html", context=context)

class Contact(LoginRequiredMixin, TemplateView):

    model = Contacts
    template_name = "contact/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["support"] = Contacts.objects.get(name="Техническая поддержка")
        context["sales_team"] = Contacts.objects.get(name="Отдел продаж")

        return context


# def one_product(request, pk):
#     product = Product.objects.get(id=pk)
#     context = {"product" : product}
#     return render(request, "product/product.html", context=context)

@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product/product.html"
    context_object_name = "product"

# def add_product(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         price = request.POST.get("price")
#         category = request.POST.get("category")
#         description = request.POST.get("description")
#
#         category_obj, is_created_category = Category.objects.get_or_create(name=category.title())
#
#         product, created = Product.objects.get_or_create(
#             name=name,
#             defaults={
#                 "price": price,
#                 "category": category_obj,
#                 "description": description
#             }
#         )
#
#         if created:
#             return HttpResponse("<div><h1>Данные успешно отправлены</h1></div>")
#         else:
#             return HttpResponse("<div><h1>Данные об этом товаре уже есть.</h1></div>")
#
#     return render(request, "product/add_product.html")
#


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/add_product.html"
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):

    model = Product
    form_class = ProductForm
    template_name = "product/add_product.html"
    success_url = reverse_lazy("catalog:home")

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])

        if product.owner != request.user:
            return HttpResponseForbidden("Вы не можете редактировать этот продукт")

        return super().get(request, *args, **kwargs)

class ProductDeleteView(LoginRequiredMixin, DeleteView):

    model = Product
    form_class = ProductDeleteForm
    template_name = "product/delete_product.html"
    success_url = reverse_lazy("catalog:home")

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])

        if product.owner != request.user and not request.user.has_perm("catalog.delete_product"):
            return HttpResponseForbidden("Вы не можете удалять этот продукт")

        return super().get(request, *args, **kwargs)

@login_required
@permission_required("catalog:can_unpublish_product", raise_exception=True)
def unpublish_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if product.is_publicated:
        product.is_publicated = False
    else:
        product.is_publicated = True

    product.save()

    return redirect("catalog:product", pk=product.id)