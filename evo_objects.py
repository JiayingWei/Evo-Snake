class Point(object):
	"""creates a point with location (x,y)
	"""
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Boxy(object):
	"""creates a boxy size 20x20px

	attributes: corner, color
	"""

	def __init__(self, corner, color):
		self.corner = Point(x,y)
		self.color = color
