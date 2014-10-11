import sys, pygame
from PIL import Image
from pygame.locals import *

def evo_container():
    """contains the entire evo universe
    """
    pygame.init()

    screen_size = [600,500]
    background_color = (0,0,0)

    screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
    pygame.display.set_caption('Evo-Snake')
    screen.fill(background_color)

    screen_mode = 'min_screen'

    if screen_mode == 'min_screen':
        menu_options = pygame.image.load("images/start_full_quit.png")
        menu_options_size = check_size("images/start_full_quit.png")
        blit_menu_options = center_object(screen_size[0], screen_size[1], menu_options_size[0], menu_options_size[1])
    else:
        menu_options = pygame.image.load("images/start_min_quit.png")

    screen.blit(menu_options, (blit_menu_options[0], blit_menu_options[1]))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

pygame.init()

# evo_container()

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
    display_resolution = pygame.display.Info()
    screen_size = [current_w.display_resolution, current_h.display_resolution]
    menu_options = pygame.image.load("images/start_min_quit.png")
    menu_options_size = check_size("images/start_full_quit.png")
    blit_menu_options = center_object(screen_size[0], screen_size[1], menu_options_size[0], menu_options_size[1])

def minimize_screen():
    """ minimizes Evo-Snake (should not change scale of the game)
    """
    screen_size = [600,500]
    menu_options = pygame.image.load("images/start_full_quit.png")
    menu_options_size = check_size("images/start_full_quit.png")
    blit_menu_options = center_object(screen_size[0], screen_size[1], menu_options_size[0], menu_options_size[1])

def loading_bar():
    """ launches the loading_bar which gives the user a visual of how much of the game has loaded
    """

def toggle_options():
    """ takes user input 'w,s' or 'up arrow key, down arrowkey' to toggle boxy between the menu options
    """

