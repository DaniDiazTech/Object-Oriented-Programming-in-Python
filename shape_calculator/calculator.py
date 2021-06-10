from math import pi, sqrt

class Shape:
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def get_area(self):
		return self.side1 * self.side2

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'

class Rectangle(Shape):
	pass

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)

class Triangle(Rectangle):
	def __init__(self, base, height):
		super().__init__(base, height)

	def get_area(self):
		area = super().get_area()
		return area / 2

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius

	def get_area(self):
		return pi * (self.radius ** 2)


class Hexagon(Square):
	def get_area(self):
		return (3 * sqrt(3) * self.side1 ** 2) / 2

breakpoint()