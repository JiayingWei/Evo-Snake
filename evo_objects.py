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

	def __init__(self, size, color, x = 0, y = 0, ):
		self.size = [20,20]
		self.x = x
		self.y = y
		self.width = self.size[0]
		self.height = self.size[1]
		self.color = color

	def toggle(self, position = 1, pos_1_x, pos_1_y, dy):  #jiaying

		self.position = position
		if position == 1:
			self.x = pos_1_x
			self.y = pos_1_y
		if position == 2:
			self.y = pos_1_y + dy
		if position == 3:
			self.y = pos_1_y + 2*dy

	def move(self, dx, dy): #anna
		self.dx = dx
		self.dy = dy


	def sound():	#jiaying

	def environment(): 	
