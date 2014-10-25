import sys, pygame, os, random, time
from PIL import Image
from pygame.locals import *

class EvoSnakeModel:
	"""Encodes the game state
	"""
	def __init__(self,backgroundColor = (0,0,0),screenstate = 'Minimized', gamestate = 'Menuing'):
		self.backgroundColor = backgroundColor
		self.menu = ScreenGUI()
		self.screenstate = screenstate	#state of the screen size (default vs fullscreen)
		self.gamestate = gamestate	#state of the game (in menu vs in game)
		self.timestart = time.time()

class Boxy:
	"""Encodes the state of a boxy in the game
	"""
	def __init__(self, color = (255, 255, 255), x = 0, y = 0, position = 1, stage = 1):
		self.size = (20,20)
		self.width = self.size[0]
		self.height = self.size[1]
		self.color = color
		self.x = x
		self.y = y
		self.pos = (self.x,self.y)
		self.position = position
		self.stage = 1
		self.counter = 1
		self.orchestra = []

	def move(self, dx, dy): #anna
		"""Moves boxy dx and dy
		"""
		self.x = self.x + dx
		self.y = self.y + dy

	def menuToggle(self, direction, dy, position):
		"""Encodes the state and location of the menu boxy
		"""
		if direction == 'up': 
			if self.position == 1:
				self.move(0, 2*dy)
				self.position = 3
			elif self.position == 2:
				self.move(0, -dy)
				self.position = 1
			elif self.position == 3:
				self.move(0, -dy)
				self.position = 2
		if direction == 'down':
			if self.position == 1:
				self.move(0, dy)
				self.position = 2
			elif self.position == 2:
				self.move(0, dy)
				self.position = 3
			elif self.position == 3:
				self.move(0, -2*dy)
				self.position = 1

	def randomMove(self, screenWidth, screenHeight):
		"""Creates a random boxy on screen
		"""
		self.x = random.randrange(0, screenWidth, self.width)
		self.y = random.randrange(0, screenHeight, self.width)

	def randomColor(self):
		if self.stage == 1:
			stage1Colors = (255, 255, 255)
			self.bgcolor = (0, 0, 0)
			self.color = stage1Colors
		if self.stage == 2:
			stage2Colors = [(255, 204, 204), 
							(255, 255, 204),
							(204, 255, 204),
							(204, 255, 255),
							(229, 204, 255)]
			self.bgcolor = (0, 0, 0)
			self.color = stage2Colors[random.randrange(0,len(stage2Colors))]
		if self.stage == 3:
			stage3Colors = [(255, 153, 153), 
							(255, 255, 153),
							(153, 255, 153),
							(153, 255, 255),
							(204, 153, 255)]
			self.bgcolor = [(51, 0, 0),
							(0, 51, 0),
							(0, 0, 51),
							(51, 0, 25)]
			self.bgcolor = self.bgcolor[random.randrange(0, len(self.bgcolor))]
			self.color = stage3Colors[random.randrange(0,len(stage3Colors))]
		if self.stage == 4:
			stage4Colors = [(255, 102, 102), 
							(255, 255, 102),
							(102, 255, 102),
							(102, 255, 255),
							(178, 102, 255)]
			self.bgcolor = [(153, 0, 0),
							(0, 153, 0),
							(0, 0, 153),
							(153, 0, 153)]
			self.bgcolor = self.bgcolor[random.randrange(0, len(self.bgcolor))]
			self.color = stage4Colors[random.randrange(0,len(stage4Colors))]

	def randomMusic(self, stage = 1, counter = 0):
		if self.stage == 1:
			if self.counter == 0:
				self.counter = self.counter + 1
			elif self.counter == 1:
				self.music = []
				self.counter = self.counter + 1
			elif self.counter == 2:
				self.counter = self.counter + 1
			elif self.counter == 3:
				self.counter = self.counter + 1
			elif self.counter == 4:
				self.counter = self.counter + 1
			elif self.counter == 5:
				self.counter = self.counter + 1
			elif self.counter == 6:
				self.music.append('music/percussion/base/')
				self.counter = self.counter + 1
			elif self.counter == 7:
				self.counter = self.counter + 1
			elif self.counter == 8:
				self.stage = self.stage + 1
				self.counter = 0
		if self.stage == 2:
			if self.counter == 0:
				self.counter = self.counter + 1
			elif self.counter == 1:
				self.counter = self.counter + 1
			elif self.counter == 2:
				self.counter = self.counter + 1
			elif self.counter == 3:
				self.counter = self.counter + 1
			elif self.counter == 4:
				self.music.append('music/percussion/extra/')
				self.counter = self.counter + 1
			elif self.counter == 5:
				self.counter = self.counter + 1
			elif self.counter == 6:
				self.counter = self.counter + 1
			elif self.counter == 7:
				self.counter = self.counter + 1
			elif self.counter == 8:
				self.music.append('music/accompaniment/major/')
				self.stage = self.stage + 1
				self.counter = 0
		if self.stage == 3:
			if self.counter == 0:
				self.counter = self.counter + 1
			elif self.counter == 1:
				self.counter = self.counter + 1
			elif self.counter == 2:
				self.counter = self.counter + 1
			elif self.counter == 3:
				self.counter = self.counter + 1
			elif self.counter == 4:
				self.counter = self.counter + 1
			elif self.counter == 5:
				self.counter = self.counter + 1
			elif self.counter == 6:
				self.counter = self.counter + 1
			elif self.counter == 7:
				self.music.append('music/melody/major/')
				self.counter = self.counter + 1
			elif self.counter == 8:
				self.stage = self.stage + 1
				self.counter = 0

class Snake:
	"""Encodes the state of the snake in the game
	"""
	def __init__(self, length = 1, direction = 'right', starting = (0,0)):
		self.length = length
		self.direction = direction
		self.boxlist = [Boxy((255,255,255), starting[0], starting[1])]
		self.x = self.boxlist[0].x
		self.y = self.boxlist[0].y

	def move(self,direction):
		""" Moves the snakes
		"""
		increment = 20
		if direction == 'up':
			self.boxlist.insert(0,Boxy(None, self.boxlist[0].x, self.boxlist[0].y - increment , None, None))
		elif direction == 'down':
			self.boxlist.insert(0,Boxy(None, self.boxlist[0].x, self.boxlist[0].y + increment , None, None))
		elif direction == 'left':
			self.boxlist.insert(0,Boxy(None, self.boxlist[0].x - increment, self.boxlist[0].y, None, None))
		elif direction == 'right':
			self.boxlist.insert(0,Boxy(None, self.boxlist[0].x + increment, self.boxlist[0].y, None, None))
		self.boxlist.remove(self.boxlist[-1])

	def nomnom(self, color = (255,255,255)):
		""" Increases snake length when omnoms
		"""
		self.boxlist.append(Boxy(color))

	def collisions(self,boxlist1,boxlist2,screenwidth,screenheight):		#where boxlist1 is the snake and boxlist2 is whatever box we're checking against
		""" Detects for different types of collisions
		"""
		if boxlist1[0].x < 0 or boxlist1[0].x + 20 > screenwidth or boxlist1[0].y < 0 or boxlist1[0].y > screenheight: 
			return 'ouch'
		elif len(boxlist2) > 2:	#checks if the collision is snake self collision
			for boxy in boxlist2:
				for box in boxlist1:
					if box != boxy and box.x == boxy.x and box.y == boxy.y:
						return 'ouch'
		elif len(boxlist2) == 1 and boxlist1[0].x == boxlist2[0].x and boxlist1[0].y == boxlist2[0].y:
			self.nomnom(boxlist2[0].color)
			return 'noms'
		else:
			return False

class menuItem:
	"""Encodes the state of a menu item in the game
	"""
	def __init__(self, text, menuWidth, menuHeight, dy = 0):
		self.font = pygame.font.Font('Square.ttf',40)
		self.text = self.font.render(text, True, (255, 255, 255))
		self.size = self.text.get_size()
		self.width = self.size[0]
		self.height = self.size[1]
		self.x = centerWidth(menuWidth, self.width)
		self.y = centerHeight(menuHeight, self.height) + dy


class ScreenGUI:
	"""Encodes the state of a ScreenGUI in the game
	"""
	def __init__(self, width = 400, height = 400, textColor = (255,255,255)):
		self.width = width
		self.height = height
		self.textColor = (255, 255, 255)
		self.font = pygame.font.Font('Square.ttf',40)
		self.display_resolution = pygame.display.Info()

	def Minimized(self):
		"""Encodes the screenstate of a minimized screen in the game
		"""
		self.width = 400
		self.height = 400

		self.item1 = menuItem("fullscreen",self.width, self.height)
		self.item2 = menuItem("start",self.width, self.height - 2*self.item1.height)
		self.item3 = menuItem("quit",self.width, self.height + 2*self.item1.height)

		self.boxy = Boxy()
		self.boxy = Boxy((255,255,255), self.item1.x - 2*self.boxy.width, centerHeight(self.item2.height,  self.boxy.height) + self.item2.y)

	def Fullscreen(self):
		"""Encodes the state of a fullscreen in the game
		"""
		self.width = self.display_resolution.current_w
		self.height = self.display_resolution.current_h

		self.item1 = menuItem("minimize",self.width, self.height)
		self.item2 = menuItem("start",self.width, self.height - 2*self.item1.height)
		self.item3 = menuItem("quit",self.width, self.height + 2*self.item1.height)

		self.boxy = Boxy()
		self.boxy = Boxy((255,255,255), self.item1.x - 2*self.boxy.width, centerHeight(self.item2.height,  self.boxy.height) + self.item2.y)

	def Loading(self):
		"""Encodes the state of the loading screen in the game
		"""
		self.lboxy = Boxy()  #creates a Loading boxy
		self.font = pygame.font.Font('Square.ttf',50)
		self.text = self.font.render('Loading', True, self.textColor)
		self.textsize = self.text.get_size()
		self.textwidth = self.textsize[0]
		self.textheight = self.textsize[1]
		self.textx = centerWidth(self.width, self.textwidth)
		self.texty = centerHeight(self.height, self.textheight) - 2 * self.boxy.height

	def Gaming(self):
		"""Encodes the state of the game as its running
		"""
		self.surpriseBoxy = Boxy()
		self.surpriseBoxy.randomMove(self.width, self.height)
		self.snake = Snake(starting = (int(20 * round(float(self.boxy.x)/20)), int(20 * round(float(self.boxy.y)/20))))

class EvoSnakeView:
	"""A view of Evo-Snake rendered in a pygame window
	"""
	def __init__(self, model, controller):
		self.model = model
		self.controller = controller
		self.numSongs = 0
		self.now = 0
		self.snaketimer = self.model.timestart
		self.colorlist = [(255,255,255)]

	def drawLoading(self):
		"""Draws the loading bar
		"""
		os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window
		
		self.model.menu.Minimized()
		self.screen = pygame.display.set_mode((self.model.menu.width, self.model.menu.height))

		self.screen.fill(model.backgroundColor)
		self.model.menu.Loading()
		self.screen.blit(self.model.menu.text, (self.model.menu.textx, self.model.menu.texty))

		pygame.display.update()

		for i in range(0,10):
			loading_boxy_start = centerObject(self.model.menu.width, self.model.menu.height, self.model.menu.lboxy.width * 10, self.model.menu.lboxy.height)
			loading_boxy_start = [loading_boxy_start[0] + self.model.menu.lboxy.width * i, loading_boxy_start[1]]
			pygame.draw.rect(self.screen, self.model.menu.lboxy.color, (loading_boxy_start,self.model.menu.lboxy.size),0)
			pygame.display.update()
			pygame.time.wait(300)
		
	def drawMenu(self):	
		"""Draws the main menu
		"""

		if self.model.screenstate == 'Minimized' and self.model.menu.width != 400:
			self.model.menu.Minimized()
			self.screen = pygame.display.set_mode((self.model.menu.width, self.model.menu.height))
		elif self.model.screenstate == 'Fullscreen' and self.model.menu.width != self.model.menu.display_resolution.current_w:
			self.model.menu.Fullscreen()
			self.screen = pygame.display.set_mode((model.menu.width, model.menu.height), pygame.FULLSCREEN)

		self.screen.fill((0,0,0))

		self.screen.blit(self.model.menu.item1.text, (self.model.menu.item1.x, self.model.menu.item1.y))
		self.screen.blit(self.model.menu.item2.text, (self.model.menu.item1.x, self.model.menu.item2.y))
		self.screen.blit(self.model.menu.item3.text, (self.model.menu.item1.x, self.model.menu.item3.y))

		pygame.draw.rect(self.screen, self.model.menu.boxy.color, ((self.model.menu.boxy.x, self.model.menu.boxy.y), self.model.menu.boxy.size),0)

		pygame.display.update()
		
	def drawGame(self):
		"""Draws the game
		"""
		self.screen.fill(model.backgroundColor)

		pygame.draw.rect(self.screen, self.model.menu.surpriseBoxy.color, ((self.model.menu.surpriseBoxy.x, self.model.menu.surpriseBoxy.y), self.model.menu.surpriseBoxy.size),0)

		#below draws the snake boxies
		for box in range(len(self.model.menu.snake.boxlist) - 1):
			pygame.draw.rect(self.screen, self.colorlist[box] , ((self.model.menu.snake.boxlist[box].x , self.model.menu.snake.boxlist[box].y), self.model.menu.snake.boxlist[box].size) ,0)
		pygame.time.delay(100)
		self.model.menu.snake.move(self.model.menu.snake.direction)

		#resets to menu states
		if self.model.menu.snake.collisions(self.model.menu.snake.boxlist, self.model.menu.snake.boxlist, self.model.menu.width, self.model.menu.height) == 'ouch':
			self.model.gamestate = 'Menuing'
			self.drawMenu()
			self.model.menu.surpriseBoxy.stage = 1
			self.model.menu.surpriseBoxy.counter = 0
			self.model.backgroundColor = (0,0,0)
			self.model.menu.surpriseBoxy.music = []
			self.model.menu.surpriseBoxy.orchestra = []
			self.colorlist = [(255,255,255)]
			pygame.mixer.fadeout(500)

		#checks for whether or not there is music queded up 
		if hasattr(self.model.menu.surpriseBoxy, 'music') == True and now - self.model.timestart > 6 and len(self.model.menu.surpriseBoxy.music) >= 1:
			self.model.timestart = now
			self.model.menu.surpriseBoxy.orchestra.append(pygame.mixer.Sound(self.model.menu.surpriseBoxy.music[-1]))
			pygame.mixer.Channel(len(self.model.menu.surpriseBoxy.music)).play(self.model.menu.surpriseBoxy.orchestra[-1],-1)
			
		#checks for food collisions
		elif self.model.menu.snake.collisions(self.model.menu.snake.boxlist, [self.model.menu.surpriseBoxy], self.model.menu.width, self.model.menu.height) == 'noms':
			self.model.menu.surpriseBoxy.randomMove(self.model.menu.width, self.model.menu.height)
			self.colorlist.append(self.model.menu.surpriseBoxy.color)
			self.model.menu.surpriseBoxy.randomColor()
			self.model.menu.surpriseBoxy.randomMusic()
			self.model.backgroundColor = self.model.menu.surpriseBoxy.bgcolor
			if len(self.model.menu.surpriseBoxy.music) >= 1 and 'wav' not in self.model.menu.surpriseBoxy.music[-1]: 
				self.model.menu.surpriseBoxy.music[-1] = self.loadRandomSong(self.model.menu.surpriseBoxy.music[-1])
				print self.model.menu.surpriseBoxy.music[-1]
		pygame.display.update()

	def loadRandomSong(self, sheetMusic):
		if 'percussion' in sheetMusic and 'base' in sheetMusic:
			path = sheetMusic + str(random.randrange(1,4)) + '.wav'
		elif 'percussion' in sheetMusic and 'extra' in sheetMusic:
			path = sheetMusic + str(random.randrange(1,9)) + '.wav'
		elif 'accompaniment' in sheetMusic and 'major' in sheetMusic: 
			path = sheetMusic + str(random.randrange(1,4)) + '.wav'
		elif 'melody' in sheetMusic and 'major' in sheetMusic: 
			path = sheetMusic + str(random.randrange(1,10)) + '.wav'
		elif 'jazz' in sheetMusic[song]: 
			path = sheetMusic + str(random.randrange(1,7)) + '.wav'
		return path

class EvoSnakeController:
	"""Defines all the inputs that Evo-Snake takes
	"""
	def __init__(self,model):
		self.model = model

	def handle_menu_key_event(self, event):
		"""Handles all of the key events while in the main menu
		"""
		if event.type != KEYDOWN:
			return
		if event.key == pygame.K_UP or event.key == pygame.K_w:
			self.model.menu.boxy.menuToggle('up', self.model.menu.item1.height, self.model.menu.boxy.position)
		if event.key == pygame.K_DOWN or event.key == pygame.K_s:
			self.model.menu.boxy.menuToggle('down', self.model.menu.item1.height, self.model.menu.boxy.position)
		if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_RETURN:
			if self.model.menu.boxy.position == 1:
				self.model.gamestate = 'Gaming'
				self.model.menu.Gaming()
			elif self.model.menu.boxy.position == 2 and self.model.screenstate == 'Minimized':
				self.model.screenstate = 'Fullscreen'
			elif self.model.menu.boxy.position == 2 and self.model.screenstate == 'Fullscreen':
				self.model.screenstate = 'Minimized'
			elif self.model.menu.boxy.position == 3:
				pygame.quit()
		if event.key == K_ESCAPE:
			pygame.quit()

	def handle_game_key_event(self,event):
		"""Handles all of the key events while in Gaming mode
		"""

		if event.type != KEYDOWN:
			return
		if event.key == pygame.K_a or event.key == pygame.K_LEFT and self.model.menu.snake.direction != 'right':
			self.model.menu.snake.direction = 'left'
		if event.key == pygame.K_d or event.key == pygame.K_RIGHT and self.model.menu.snake.direction != 'left':
			self.model.menu.snake.direction = 'right'
		if event.key == pygame.K_s or event.key == pygame.K_DOWN and self.model.menu.snake.direction != 'up':
			self.model.menu.snake.direction = 'down'
		if event.key == pygame.K_w or event.key == pygame.K_UP and self.model.menu.snake.direction != 'down':
			self.model.menu.snake.direction = 'up'
		if event.key == K_ESCAPE:
			pygame.quit()




def centerWidth(widthOuter, widthInner):
	"""Returns the x location of the upper left corner of the item you want to center horizontally in a larger item
	"""
	return widthOuter/2 - widthInner/2

def centerHeight(heightOuter, heightInner):
	"""Returns the y location of the upper left corner of the item you want to center vertically in a larger item
	"""
	return heightOuter/2 - heightInner/2

def find_center(width, height):
	"""Finds the center of an object with a width and height
	"""
	originx = width/2
	originy = height/2
	return [originx,originy]

def centerObject(width_outter, height_outter, width_inner, height_inner):
	"""Returns the (x,y) location of the upper left corner of the item you want to center in a larger box
	"""
	center_outter = find_center(width_outter, height_outter)
	center_inner = find_center(width_inner, height_inner)
	upper_left_corner = [center_outter[0] - center_inner[0], center_outter[1] - center_inner[1]]
	return upper_left_corner



if __name__ == '__main__':
	pygame.init()
	pygame.mixer.init(channels = 8)
	pygame.font.init()

	model = EvoSnakeModel()
	controller = EvoSnakeController(model)
	view = EvoSnakeView(model,controller)

	running = True

	view.drawLoading()
	view.drawMenu()
	while running:
		while model.gamestate == 'Menuing' and running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == KEYDOWN:
					controller.handle_menu_key_event(event)
					view.drawMenu()
		while model.gamestate == 'Gaming' and running:
			now = time.time()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == KEYDOWN:
					controller.handle_game_key_event(event)
			view.drawGame()

	pygame.quit()
