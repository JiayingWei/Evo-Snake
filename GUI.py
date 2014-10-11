import pygame
from pygame.locals import *
from pgu import gui


def evo_container():
	"""contains the entire evo universe
	"""
	# pygame.init()
	# fpsClock = pygame.time.Clock()
	# contains_snake = pygame.display.set_mode((640, 480))
	# pygame.display.update()

	pygame.init()

    size = width, height = 320, 240
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
 
    ball = pygame.image.load("ball.bmp")
    ballrect = ball.get_rect()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()

def launch_menu():
	""" launches the main menu of Evo-Snake
	"""

def quit_game():
	""" quits the game Evo-Snake
	"""

def start_game():
	""" starts the game Evo-Snake
	"""

def full_screen():
	""" puts Evo-Snake into full_screen (should not change scale of the game)
	"""

def minimize_screen():
	""" minimizes Evo-Snake (should not change scale of the game)
	"""

def loading_bar():
	""" launches the loading_bar which gives the user a visual of how much of the game has loaded
	"""

def toggle_options():
	""" takes user input 'w,s' or 'up arrow key, down arrowkey' to toggle boxy between the menu options
	"""

evo_container()