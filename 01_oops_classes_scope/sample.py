


class Area:

	def __init__(self, length, width):
		self.length = length
		self.width = width

	def calculate_area(self):
		return self.length * self.width

	def __str__(self):
		return "The Area is {}".format(self.length * self.width)

	def __add__(self, other_area):
		l = self.length + other_area.length
		w = self.width + other_area.width
		return Area(l, w)

rect1 = Area(5, 6)
rect2 = Area(2, 3)

# This will invoke the __add__() method which will "add" the two instances and return a third that represents addition
rect3 = rect1 + rect2
print(rect1)
print(rect2)
print(rect3)