'''
David Fuller

App class: Initializes application

10-15-2017
'''

import pygame

from .Constants import screen_resolution, app_title, fps, julias
from .Julia import Julia


class App(object):
    '''
    Sets up and runs a Pygame application.
    '''
    
    def __init__(self, app_directory):
        '''
        App's init method.

        Stores application directory. Sets up the graphical user interface.
        Runs the applicaiton.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.app_directory = app_directory

        self.setup_GUI()

        self.run_app()

    def setup_GUI(self):
        '''
        Method sets up the graphical user interface.

        Initializes Pygame. Sets up the window size and title. Stores Pygame
        clock variable for setting frames per second.
        '''
        
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(app_title)
        self.clock = pygame.time.Clock()

        self.Julia = Julia()

    def run_app(self):
        '''
        Runs Pygame application.
        '''

        julia_index = 0   # Start with Mandelbrot set
        alt_down = False
        running = True
        while running:
            events = pygame.event.get()
            for event in events:
                
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

                # Handle ALT + F4
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LALT:
                        alt_down = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F4 and alt_down == True:
                        running = False
                    if event.key == pygame.K_LALT:
                        alt_down = True

            # Quit
            if running == False:
                break                    

            self.Julia.update(self.screen, screen_resolution, julia_index)
            self.Julia.show(self.screen, screen_resolution)
            julia_index = julia_index + 1
            if julia_index == len(julias):
                julia_index = 0

            # Update Screen
            pygame.display.update()
            self.clock.tick(fps)            

        # Close app cleanly
        pygame.quit()
