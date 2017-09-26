class Product:
	price = 0
	count = 0
	tax = 1.25

	def __init__(self, price, count, tax):
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		return self.price * self.count * self.tax

Robot = Product(price = 900, count = 2, tax = 1.25)
Book = Product(price = 100, count = 1, tax = 1.06)

print(Robot.price_with_tax() + Book.price_with_tax())	