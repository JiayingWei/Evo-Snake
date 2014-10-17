import sys, pygame
from PIL import Image
from pygame.locals import *

class Box(object):
    def __init__(self, center, width, height, color):
        self.center=center
        self.width=width
        self.height=height
        self.color=color
    def move(self,newcenter):
        self.center=newcenter
        
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
        y_displacement = 100
        pygame.font.init()
        white = (255, 255, 255)
        squarefont = pygame.font.Font('Square.ttf',38)
        squarefont2 = pygame.font.Font('Square.ttf',24)
        self.screen = pygame.display.set_mode((600, 400))

        start = squarefont.render("start                (Enter)", True, white)
        start_size = start.get_size()
        blit_start = center_object(600, 400 - y_displacement, start_size[0], start_size[1])     
        #I am a cheater and pretended to change the height of the screen in the centering function to displace the pieces of the menu (I will probably fix this)
        self.screen.blit(start, (blit_start[0], blit_start[1]))

        full = squarefont.render("full screen    (F)", True, white)
        full_size = full.get_size()
        blit_full = center_object(600, 400, start_size[0], start_size[1])     #the centering mechanism is hard coded in (should fix)
        self.screen.blit(full, (blit_full[0], blit_full[1]))

        quit = squarefont.render("quit                    (Esc)", True, white)
        quit_size = quit.get_size()
        blit_quit = center_object(600, 400 + y_displacement,  start_size[0], start_size[1])     #the centering mechanism is hard coded in (should fix)
        self.screen.blit(quit, (blit_quit[0], blit_quit[1]))
        pygame.display.update()

#        global box1
#        box1 = Box(center_object(550-start_size[0],300,10,10), 10, 10, (255, 255,255))
#        box1.color = (255, 255, 255)
#        box1.width = 10
#        box1.height=10
#        box1.center = center_object(550-start_size[0],300,box1.width[0],box1.width[1])
#        self.innerbox=pygame.Rect(box1.center[0],box1.center[1],box1.width[0], box1width[1])
#        box1.center = center_object(550-start_size[0],300,10,10)
#        box1.width = (10,10)
#        pygame.draw.rect(self.screen, (255,255,255), (box1.center,box1.width),0)
#        self.screen.blit(start, (blit_start[0], blit_start[1]))            
#        pygame.display.update()   
#        for event in pygame.event.get():
#            if event.type == KEYDOWN and event.key == K_DOWN:
#                Rect.move(box2,450,350)
            

    def loading_bar(self):
        """ launches the loading_bar which gives the user a visual of how much of the game has loaded
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
        class Box(object):
            """represents a box - attributes: width , corner, color, center"""
        box = Box()
        box.color = blue
        box.width = (10,10)
        x = 0
        for i in range(0,10):
            box.center = center_object(600-(loading_size[0])+x, 400+100, box.width[0], box.width[1]) #major hard coded :/
            pygame.draw.rect(self.screen, box.color, (box.center,box.width),0)
            pygame.display.update()
            pygame.time.wait(1000)
            x=x+40

    def full_screen(self):
        """ puts Evo-Snake into full_screen (should not change scale of the game)
        """
        self.width = self.display_resolution.current_w
        self.height = self.display_resolution.current_h
        self.screen = pygame.display.set_mode((self.width, self.height - 40))       #problem with maximize not stretching to fill the entire screen
        
        y_displacement = 100
        pygame.font.init()
        white = (255, 255, 255)
        squarefont = pygame.font.Font('Square.ttf',38)
        squarefont2 = pygame.font.Font('Square.ttf',24)

        start = squarefont.render("start                (Enter)", True, white)
        start_size = start.get_size()
        blit_start = center_object(self.width, self.height - 40 - y_displacement, start_size[0], start_size[1])     
        #I am a cheater and pretended to change the height of the screen in the centering function to displace the pieces of the menu (I will probably fix this)
        self.screen.blit(start, (blit_start[0], blit_start[1]))

        full = squarefont.render("Minimize             (M)", True, white)
        full_size = full.get_size()
        blit_full = center_object(self.width, self.height -40, start_size[0], start_size[1])     #the centering mechanism is hard coded in (should fix)
        self.screen.blit(full, (blit_full[0], blit_full[1]))

        quit = squarefont.render("quit                    (Esc)", True, white)
        quit_size = quit.get_size()
        blit_quit = center_object(self.width, self.height-40 + y_displacement,  start_size[0], start_size[1])     #the centering mechanism is hard coded in (should fix)
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
    
    global box2

    pygame.display.set_caption('Evo-Snake')

    evo_screen = screen()
    evo_screen.screen_color()
    evo_screen.loading_bar()

    pygame.time.wait(500)

    evo_screen.minimize_screen()

    pygame.display.flip()
    global box1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_f:
                evo_screen.full_screen()
            elif event.type == KEYDOWN and event.key == K_m:
                evo_screen.minimize_screen()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
#            elif event.type == KEYDOWN and event.key == K_DOWN:
#                box1.move(300,300)
#                evo_screen.screen.blit(evo_screen.screen, box1, pygame.draw.rect(evo_screen.screen, (255,255,255), (box1.center,box1.width),0))
#                pygame.display.update()    

                   

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

def start_game():
    """ starts the game Evo-Snake
    """
