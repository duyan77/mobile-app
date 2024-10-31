from django.http import JsonResponse
from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404

def cart_summary(request):
	return render(request, 'cart/cart-summary.html', )


def cart_add(request, product_id):
	cart = Cart(request)
	if request.POST.get('action') == 'POST':
		product_id = int(request.POST.get('product_id'))
		product_quantity = int(request.POST.get('product_quantity'))
		product = get_object_or_404(Product, id=product_id)

		cart.add(product=product, product_qty=product_quantity)
		return JsonResponse({'qty': cart.__len__()})


def cart_delete(request, product_id):
	pass


def cart_update(request, product_id):
	pass
