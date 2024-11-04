from django.shortcuts import render

#Phúc Tấn 03/11 Thêm các thư viện cần thiết cho thanh toán
import stripe
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.shortcuts import redirect
stripe.api_key = 'sk_test_51QH2duG6ioceCuONjBIvdJJCSr8z7Lo7s0vRd8eDQT0iAZh9i5qpQTbUdKW3RjooRKWwfPbR2a74UIsEb9dQaBfs00PRwhWbI3'



def cart_summary(request):
	return render(request, 'cart/cart-summary.html', )



#Phúc Tấn Thêm Hàm xử lý thanh toán 
def success(request):
	return render(request, 'cart/success.html', )
def cancel(request):
	return render(request, 'cart/cancel.html', )
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        # Không cần lấy từ request.body nữa vì chúng ta sẽ gán cố định
        try:
            # Tạo phiên thanh toán
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': "Phúc Tấn Đang ở đây đợi nè",  # Gán tên sản phẩm cố định
                            'description': "Sản phẩm thương hiệu thời trang nổi tiếng",  # Gán mô tả sản phẩm cố định
                        },
                        'unit_amount': 10000,  # Gán giá sản phẩm cố định (tính bằng cents)
                    },
                    'quantity': 1,  # Gán số lượng sản phẩm cố định
                }],
                mode='payment',
                success_url='http://127.0.0.1:8000/cart/success/',
                cancel_url='http://127.0.0.1:8000/cart/cancel/',
            )
            return redirect(checkout_session.url)  # Trả về ID của phiên thanh toán
        except stripe.error.StripeError as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request'}, status=400)



def cart_add(request, product_id):
	pass


def cart_delete(request, product_id):
	pass


def cart_update(request, product_id):
	pass
