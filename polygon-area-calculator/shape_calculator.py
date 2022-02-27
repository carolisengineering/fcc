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


