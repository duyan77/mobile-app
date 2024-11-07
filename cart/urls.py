from django.urls import path

from . import views

urlpatterns = [
	path('', views.cart_summary, name='cart-summary'),

	path('add/', views.cart_add, name='cart-add'),

	path('delete/', views.cart_delete, name='cart-delete'),

	path('update/', views.cart_update, name='cart-update'),
	# Phúc Tấn 03/11 Thêm các url cần thiết cho trang thanh toán
	path('success/', views.success, name='success'),
	path('cancel/', views.cancel, name='cancel'),
	path('create-checkout-session/', views.create_checkout_session, name='create-checkout-session'),
]
