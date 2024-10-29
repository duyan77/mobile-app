class Cart:
	def __init__(self, request):
		self.session = request.session

		# return old user cart if exists or create a new one
		cart = self.session.get('session_key')
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		self.cart = cart
