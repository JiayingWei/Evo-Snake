Evo-Snake
=========

Homework 5 for Software Design 2015

GUI.py is the housing for all the GUI stuff currently -- evo_container may get moved further along the dev process
evo_objects.py would potentially hold objects required for the game
sandbox.py is just a sandbox for testing code so you don't have to change the GUI.py
images is the folder containing all the current graphics

Memo:
	-the menu text is in images because using fonts would cause compatability issues with computers w/o squarefont installed
	-it would make sense for the toggle feature to be methods inside a class called boxy (look in evo_objects.py for an example)
	-the methods inside the toggle feature would have to call the methods inside the object screen to fullscreen and minimize but should have its own methods for start and quit game
	-the loading bar could potentially become a method for the object screen -- though for now it should be tested as a seperate function

To operate the current state of GUI:
	-call evo_container() to run the GUI
	-press f to "full screen"
	-press m to minimize

Known Bugs:
	-location of the minimized menu has to be hard coded in
	-fullscreen is not stretching to fit computer screen

Things that could be fixed:
	-launched game should start centered...
	-"start_full_quit.png" and "start_min.quit.png" are not the same size

Useful resources that could help (feel free to append):

	Newbie Guide : http://www.pygame.org/docs/tut/newbieguide.html
	pygame window tutorial : http://www.petercollingridge.co.uk/pygame-physics-simulation/creating-pygame-window
