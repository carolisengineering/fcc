class Rectangle:

	def __init__(self, width, height):
		"""Initializes a Rectangle with a width and a height"""
		self.width = width
		self.height = height

	def set_width(self, width):
		"""Sets a Rectangle's width to the input value"""
		self.width = width

	def set_height(self, height):
		"""Sets a Rectangle's height to the input value"""
		self.height = height

	def get_area(self):
		"""Computes the area of a Rectangle based on its width and height"""
		return self.width * self.height

	def get_perimeter(self):
		"""Computes the perimeter of a Rectangle based on its width and height"""
		return (2 * self.width + 2 * self.height)

	def get_diagonal(self):
		"""Computes the length of the diagonal of a rectangle based on its width and height"""
		return ((self.width ** 2 + self.height ** 2) ** .5)

	def get_picture(self):
		"""Draws a picture of a Rectangle using * to represent units of width and height"""
		picture = ''
		if self.width > 50 or self.height > 50:
			return 'Too big for picture.'
		else:
			for x in range(self.height):
				picture += ('*' * self.width + '\n')
			return picture

	def get_amount_inside(self, other_rectangle):
		"""
		Given another rectangle as input, returns the number of times the other rectangle
		would fit inside the original rectangle
		"""
		return self.get_area() // other_rectangle.get_area()

	def __str__(self):
		"""Creates a string representation of a Rectangle showing its width and height"""
		return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):

	def __init__(self, side_length):
		"""Initializes a Square as a Rectangle with the same width height"""
		Rectangle.__init__(self, side_length, side_length)

	def set_side(self, side_length):
		"""Sets a Square's width and height to the input value"""
		self.width = side_length
		self.height = side_length

	def set_width(self, side_length):
		"""Sets a Square's width and height to the input value"""
		self.width = side_length
		self.height = side_length

	def set_height(self, side_length):
		"""Sets a Square's width and height to the input value"""
		self.width = side_length
		self.height = side_length

	def __str__(self):
		"""Creates a string representation of a Square showing its side length"""
		return f'Square(side={self.width})'
