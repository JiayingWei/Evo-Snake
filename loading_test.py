import sys, pygame
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

    def minimize_screen(self):
        """ minimizes Evo-Snake (should not change scale of the game)
        """
        pygame.font.init()
        blue = ( 0, 0, 255)
        squarefont = pygame.font.Font('Square.ttf',50)
        loading = squarefont.render("LOADING", True, blue)
        self.screen = pygame.display.set_mode((600, 400))
        loading_size = loading.get_size()
        blit_loading = center_object(600, 400, loading_size[0], loading_size[1])     #the centering mechanism is hard coded in (should fix)
        self.screen.blit(loading, (blit_loading[0], blit_loading[1]))
        pygame.display.update()

    # def full_screen(self):
    #     """ puts Evo-Snake into full_screen (should not change scale of the game)
    #     """
    #     self.width = self.display_resolution.current_w
    #     self.height = self.display_resolution.current_h
    #     self.screen = pygame.display.set_mode((self.width, self.height - 40))       #problem with maximize not stretching to fill the entire screen
    #     menu_options = pygame.image.load("images/start_min_quit.png").convert()
    #     menu_options_size = check_size("images/start_full_quit.png")
    #     blit_menu_options = center_object(self.width, self.height, menu_options_size[0], menu_options_size[1])
    #     self.screen.blit(menu_options, (blit_menu_options[0], blit_menu_options[1]))
    #     pygame.display.update()

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
    evo_screen.minimize_screen()

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            # elif event.type == KEYDOWN and event.key == K_f:
            #     evo_screen.full_screen()
            elif event.type == KEYDOWN and event.key == K_m:
                evo_screen.minimize_screen()

def check_size(imagepath):
    """Returns the size in pixels of an image (width,height)
    """
    img = Image.open(imagepath)
    width,height = img.size
    return [width,height]

def check_surface_size(surface):
    size = surface.get_size()
    return size

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

# def loading_bar(self):
#     """ launches the loading_bar which gives the user a visual of how much of the game has loaded
#     """
#     pygame.font.init()
#     blue = ( 0, 0, 255)
#     squarefont = pygame.font.Font("Square.tff",50)
#     loading = squarefont.render("LOADING", True, blue)
#     self.screen = pygame.display.set_mode((600, 400))
#     loading_size = check_size("images/start_full_quit.png")
#     blit_loading = center_object(600, 400, menu_options_size[0], menu_options_size[1])     #the centering mechanism is hard coded in (should fix)
#     self.screen.blit(loading, (blit_loading[0], blit_loading[1]))
#     pygame.display.update()


    #pygame.draw.rect(surface, (255,255,255), pygame.Rect(left,top,maxwidth*progress,height))

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
