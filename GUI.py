import sys, pygame, os
import evo_objects as eob
from PIL import Image
from pygame.locals import *

class screen(object):
    """ controls everything to do with the windows screen_size
        attributes: width, height, color
    """
    def __init__(self, width = 600, height = 400, color = (0, 0, 0)):
        self.width = width
        self.height = height
        self.color = color
        self.display_resolution = pygame.display.Info()     #gets the resolution of your computer monitor
        self.screen = pygame.display.set_mode((self.width, self.height))    #this statement might be causing problems with the centering during the 2nd minimize

    def loading_bar(self):
        """ launches the loading_bar which gives the user a visual of how much of the game has loaded
        """
        os.environ['SDL_VIDEO_CENTERED'] = '1'  #centers the starting postion of the window

        pygame.font.init()

        loading_bar_color = ( 255, 255, 255)
        squarefont = pygame.font.Font('Square.ttf',50)
        loading = squarefont.render("LOADING", True, loading_bar_color)
        self.screen = pygame.display.set_mode((self.width, self.height))
        loading_size = loading.get_size()
        loading_boxy = eob.Boxy([20,20],loading_bar_color)  #creates a loading boxy
        blit_loading = center_object(self.width, self.height, loading_size[0], loading_size[1])
        self.screen.blit(loading, (blit_loading[0], blit_loading[1] - 2*loading_boxy.height))
        pygame.display.update()

        for i in range(0,10):
            loading_boxy_start = center_object(self.width, self.height, loading_boxy.width * 10, loading_boxy.height)
            loading_boxy_start = [loading_boxy_start[0] + loading_boxy.width * i, loading_boxy_start[1]]
            pygame.draw.rect(self.screen, loading_boxy.color, (loading_boxy_start,loading_boxy.size),0)
            pygame.display.update()
            pygame.time.wait(300)

    def minimize_screen(self):
        """ minimizes Evo-Snake (should not change scale of the game)
        """
        pygame.font.init()
        text_color = ( 255, 255, 255)
        squarefont = pygame.font.Font('Square.ttf',40)
        self.screen = pygame.display.set_mode((600, 400))

        full = squarefont.render("fullscreen", True, text_color)
        full_size = full.get_size()
        blit_full = center_object(600, 400, full_size[0], full_size[1])     #the centering mechanism depends on the center of the middle text item
        self.screen.blit(full, (blit_full[0], blit_full[1]))

        start = squarefont.render("start", True, text_color)
        start_size = start.get_size()
        blit_start = [blit_full[0], blit_full[1] - full.get_height()]
        self.screen.blit(start, (blit_start[0], blit_start[1]))

        quit = squarefont.render("quit", True, text_color)
        quit_size = quit.get_size()
        blit_quit = [blit_full[0], blit_full[1] + full.get_height()]
        self.screen.blit(quit, (blit_quit[0], blit_quit[1]))
        pygame.display.update()

    def full_screen(self):
        """ puts Evo-Snake into full_screen (should not change scale of the game)
        """
        self.width = self.display_resolution.current_w
        self.height = self.display_resolution.current_h

        pygame.font.init()
        text_color = ( 255, 255, 255)
        squarefont = pygame.font.Font('Square.ttf',40)
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.FULLSCREEN)

        minimize = squarefont.render("minimize", True, text_color)
        full_size = minimize.get_size()
        blit_full = center_object(self.width, self.height, full_size[0], full_size[1])     #the centering mechanism depends on the center of the middle text item
        self.screen.blit(minimize, (blit_full[0], blit_full[1]))

        start = squarefont.render("start", True, text_color)
        start_size = start.get_size()
        blit_start = [blit_full[0], blit_full[1] - minimize.get_height()]
        self.screen.blit(start, (blit_start[0], blit_start[1]))

        quit = squarefont.render("quit", True, text_color)
        quit_size = quit.get_size()
        blit_quit = [blit_full[0], blit_full[1] + minimize.get_height()]
        self.screen.blit(quit, (blit_quit[0], blit_quit[1]))
        pygame.display.update()

    def screen_color(self):
        """ fills the screen with its own color
        """
        self.screen.fill(self.color)


def evo_container():
    """contains the entire evo universe
    """
    pygame.init()

    pygame.display.set_caption('Evo-Snake')

    evo_screen = screen()
    evo_screen.screen_color()
    evo_screen.loading_bar()

    pygame.time.wait(500)

    evo_screen.minimize_screen()

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_f:
                evo_screen.full_screen()
            elif event.type == KEYDOWN and event.key == K_m:
                evo_screen.minimize_screen()

def check_size(imagepath):
    """Returns the size in pixels of an image (width,height)
    """
    img = Image.open(imagepath)
    width,height = img.size
    return [width,height]

def find_center(width, height):
    """Finds the center of an object with a width and height
    """
    originx = width/2
    originy = height/2
    return [originx,originy]

def center_object(width_outter, height_outter, width_inner, height_inner):
    """Returns the (x,y) location of the upper left corner of the item you want to center in a larger box
    """
    center_outter = find_center(width_outter, height_outter)
    center_inner = find_center(width_inner, height_inner)
    upper_left_corner = [center_outter[0] - center_inner[0], center_outter[1] - center_inner[1]]
    return upper_left_corner

evo_container()

def launch_menu():
    """ launches the main menu of Evo-Snake
    """

def toggle_options():
    """ takes user input 'w,s' or 'up arrow key, down arrowkey' to toggle boxy between the menu options
    it would make sense to make the boxy a class boxy(object): and write all of the toggle boxy behaviors in the class.
    """

def quit_game():
    """ quits the game Evo-Snake
    """

def start_game():
    """ starts the game Evo-Snake
    """