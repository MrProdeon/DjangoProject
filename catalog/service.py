from config.settings import CACHE_ENABLED
from catalog.models import Product, Category
from django.shortcuts import render
from django.core.cache import cache

def get_products_by_category(request, pk):
    if CACHE_ENABLED:
        products_by_category = cache.get(f"products_by_category_{pk}")
        category = cache.get(f"category_{pk}")
        if not products_by_category:
            products_by_category = Product.objects.filter(category=pk)
            cache.set(f"products_by_category_{pk}", products_by_category, 60 * 15)
        if not category:
            category = Category.objects.get(id=pk)
            cache.set(f"category_{pk}", category, 60 * 15)
    else:
        products_by_category = Product.objects.filter(category=pk)
        category = Category.objects.get(id=pk)

    context = {f"products_by_category": products_by_category,
               f"category": category}
    return render(request, "product/product_by_category.html", context)