import stripe
# Phúc Tấn 03/11 Thêm các thư viện cần thiết cho thanh toán
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal

from store.models import Product
from .cart import Cart

stripe.api_key = 'sk_test_51QH2duG6ioceCuONjBIvdJJCSr8z7Lo7s0vRd8eDQT0iAZh9i5qpQTbUdKW3RjooRKWwfPbR2a74UIsEb9dQaBfs00PRwhWbI3'


def cart_summary(request):
	cart = Cart(request)
	return render(request, 'cart/cart-summary.html', {'cart': cart})


def cart_add(request):
	cart = Cart(request)
	if request.POST.get('action') == 'post':
		product_id = int(request.POST.get('product_id'))
		product_quantity = int(request.POST.get('product_quantity'))
		product = get_object_or_404(Product, id=product_id)
		cart.add(product=product, product_qty=product_quantity)
		cart_quantity = cart.__len__()
		response = JsonResponse({'qty': cart_quantity})
		return response


def cart_delete(request):
	pass


# Phúc Tấn Thêm Hàm xử lý thanh toán
def success(request):
	return render(request, 'cart/success.html', )
def cancel(request):
	return render(request, 'cart/cancel.html', )

#Phúc Tấn hàm lấy danh sách sản phẩm đang có trong card
def list_produc(request):
	cart_instance = Cart(request)
	list_item = []
	for item in cart_instance:
		list_item.append({
			'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': item['product'].title,  # Tên sản phẩm từ giỏ hàng
                    'description': item['product'].description,  # Mô tả sản phẩm từ giỏ hàng (nếu có)
                },
                'unit_amount': int(item['price'] * Decimal(1)),  # Giá sản phẩm (cents)
            },
            'quantity': item['qty'],  # Số lượng sản phẩm từ giỏ hàng
		})
	return list_item

@csrf_exempt
def create_checkout_session(request):
	if request.method == 'POST':
		# Không cần lấy từ request.body nữa vì chúng ta sẽ gán cố định và sản phẩm từ trong card ra
		line_items = list_produc(request)
		try:
			# Tạo phiên thanh toán
			checkout_session = stripe.checkout.Session.create(
				payment_method_types=['card'],
				line_items = line_items,
				mode='payment',
				success_url='http://127.0.0.1:8000/cart/success/',
				cancel_url='http://127.0.0.1:8000/cart/cancel/',
			)
			return redirect(checkout_session.url)  # Trả về URL của phiên thanh toán
		except stripe.error.StripeError as e:
			return JsonResponse({'error': str(e)})
	return JsonResponse({'error': 'Invalid request'}, status=400)


def cart_update(request):
	pass


def cart_empty(request):
	return render(request, 'cart/cart-empty.html')
