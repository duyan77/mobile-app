class Cart:
	def __init__(self, request):
		self.session = request.session

		# return old user cart if exists or create a new one
		cart = self.session.get('session_key')
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		self.cart = cart

	def add(self, product, product_qty):
		product_id = str(product.id)

		# check if product is already in cart
		if product_id in self.cart:  # if product is already in cart
			self.cart[product_id]['qty'] = product_qty  # modify the quantity
		else:
			self.cart[product_id] = {'price': str(product.price),
									 'qty': product_qty}  # add the product to cart
		self.session.modified = True  # save the session
