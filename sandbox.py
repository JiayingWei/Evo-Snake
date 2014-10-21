"""<title>Hello World</title>
The simplest possble gui app that can be made.
Unfortunately, you have to CTRL-C from the command line to quit it.
GUI will initialize the screen for you.
"""

import pygame, os, sys

pygame.init()
pygame.mixer.init(frequency = 1000)
path = "music/percussion/base/2.wav"
orchestra = pygame.mixer.Sound(path)
print(os.path.exists(path))


running = True

while running == True:
	orchestra.play()

	for event in pygame.event.get():
		if event.key == K_ESCAPE:
			pygame.quit()