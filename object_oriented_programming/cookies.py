class Cookie:
	# Constructor
	def __init__(self, name, shape, chips='Chocolate'):
		# Instance attributes
		self.name = name
		self.shape = shape
		self.chips = chips

	# The object is passing itself as a parameter
	def bake(self):
		print(f'This {self.name}, is being baked with the shape {self.shape} and chips of {self.chips}')
		print('Enjoy your cookie!')