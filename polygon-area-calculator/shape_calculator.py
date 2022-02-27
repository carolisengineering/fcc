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
			picture_string = ''
			for x in range(self.height):
				for x in range(self.width):
					picture_string += '*'
				picture_string += '\n'
			return picture_string

	def get_amount_inside(self, other_rectangle):
		area = self.get_area()
		other_rectangle_area = other_rectangle.get_area()
		amount_inside = area // other_rectangle_area
		return amount_inside

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
