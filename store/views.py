from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Category, Product


# Create your views here.

def store(request):
	all_products = Product.objects.all()
	cont = {'all_products': all_products}
	return render(request, 'store/store.html', context=cont)


def categories(request):
	all_categories = Category.objects.all()
	return {'all_categories': all_categories}


def list_category(request, category_slug=None):
	category = get_object_or_404(Category, slug=category_slug)
	products = Product.objects.filter(category=category)
	return render(request, 'store/list-category.html',
				  context={'category': category, 'products': products})


def product_info(request, slug):
	product = get_object_or_404(Product, slug=slug)
	return render(request, 'store/product-info.html', context={'product': product})
