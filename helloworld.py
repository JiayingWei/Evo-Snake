"""<title>Hello World</title>
The simplest possble gui app that can be made.
Unfortunately, you have to CTRL-C from the command line to quit it.
GUI will initialize the screen for you.
"""

import pygame
from pygame.locals import *

pygame.init()
fpsClock = pygame.time.Clock()

windowSurfaceObj = pygame.display.set_mode((640, 480))