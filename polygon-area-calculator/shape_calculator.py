class Rectangle:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def set_width(self, width):
		self.width = width

	def set_height(self, height):
		self.height = height

	def get_area(self):
		return self.width * self.height

	def get_perimeter(self):
		return (2 * self.width + 2 * self.height)

	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** .5)

	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return 'Too big for picture.'
		else:
			return 'this is a picture of a rectangle'

	def get_amount_inside(self, other_rectangle):
		return 'this is the number of times the other rectangle could fit inside this rectangle'

	def __str__(self):
		return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

	def __init__(self, side_length):
		Rectangle.__init__(self, side_length, side_length)

	def set_side(self, side_length):
		self.width = side_length
		self.height = side_length

	def set_width(self, side_length):
		self.width = side_length
		self.height = side_length

	def set_height(self, side_length):
		self.width = side_length
		self.height = side_length

	def __str__(self):
		return f'Square(side={self.width})'
