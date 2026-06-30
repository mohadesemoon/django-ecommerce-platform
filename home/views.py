from django.shortcuts import get_object_or_404, render
from django.views import View
from unicodedata import category

from orders.form import CartAddForm
from .models import Product, Category

class HomeView(View):
    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)
        if category_slug:
            category = Category.objects.get(slug = category_slug)
            products = Product.objects.filter(category=category)
        return render(request, 'home/home.html', {'products': products , 'categories': categories})


class ProductDetailView(View):
    def get(self, request, slug):
        form = CartAddForm()
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'home/detail.html', {'product':product, 'form':form})




