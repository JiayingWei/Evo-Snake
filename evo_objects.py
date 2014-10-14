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

	def __init__(self, size, color, x, y):
		self.size = [20,20]
		self.x = x
		self.y = y
		self.width = self.size[0]
		self.height = self.size[1]
		self.color = color

	def toggle(self, position = 1):  #jiaying
		self.position = position
		self.x = x
		self.y = y
		if position == 1:
			move to position 1
		if position == 2:
			move to position 2
		if position == 3:
			move to position 3

	def move(self, dx, dy): #anna
		self.dx = dx
		self.dy = dy


	def sound():	#jiaying

	def environment(): 	
