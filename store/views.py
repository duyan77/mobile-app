from itertools import product
from lib2to3.fixes.fix_input import context

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
