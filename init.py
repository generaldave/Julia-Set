########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# init class: App initializer                                          #
#                                                                      #
# Created on 2017-1-1                                                  #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Constants import *   # Constants file
from   Pixel     import *   # Pixel Class
import pygame               # For GUI
import math                 # For colour generating
import colorsys

########################################################################
#                                                                      #
#                              INIT CLASS                              #
#                                                                      #
########################################################################

class init(object):
    def __init__(self, appDirectory):
        self.appDirectory = appDirectory

        # Set up GUI
        self.setupGUI()

        # Set up pixel array
        self.setupPixelArray()        

        # Run app
        self.runApp()

    # Mehtod sets up GUI
    def setupGUI(self):
        # Screen attributes
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RESOLUTION)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()      # For frames per second
        self.mouse = pygame.mouse.get_pos()   # For mouse position

        # Initialize Pixel object
        self.pixel = Pixel(self.screen)

    # Method sets up pixel array
    def setupPixelArray(self):
        self.pixelArray = []
        for y in range(SCREEN_HEIGHT):
            for x in range(SCREEN_WIDTH):
                self.pixelArray.append((x, y))

    # Method maps to new range
    def Map(self, value, mini, maxi, tomini, tomaxi):
        oldRange = (maxi - mini)
        newRange = (tomaxi - tomini)
        return (((value - mini) * newRange) / oldRange) + tomini

    # Method draws Mandelbrot
    def drawJulia(self, index):
        # If not mandelbrot, decide Julia set
        if (index != ZERO):
            currenta = julias[index][ZERO]
            currentb = julias[index][ONE]
            
        for x in range(SCREEN_WIDTH):
            for y in range(SCREEN_HEIGHT):
                # f(z) = z^2 + c
                # c = a + bi
                # i = sqrt(-1)
                a = self.Map(x, ZERO, SCREEN_WIDTH,  MIN_RANGE, MAX_RANGE)
                b = self.Map(y, ZERO, SCREEN_HEIGHT, MIN_RANGE, MAX_RANGE)

                # If index is 0: Mandelbrot set
                if (index == ZERO):
                    currenta = a
                    currentb = b
                
                # iteration counter
                iteration = ZERO

                # Iterate toward 'infinity'
                while iteration < MAX_ITERATION:
                    # Store real and composite calculations
                    real      = (a * a) - (b * b)
                    composite = TWO * a * b

                    # Break if approaching 'infinity'
                    if abs((real * real) + (composite * composite)) > INFINITY:
                        break

                    # '+ c' part
                    a = real      + currenta
                    b = composite + currentb                    

                    # Increment iteration
                    iteration = iteration + ONE

                # If not part of Julia set, make colour black
                if iteration == MAX_ITERATION:
                    colour = Colour['BLACK']
                else:
                    # Colour generator part of Julia set
                    hu = math.sqrt(float(iteration) / MAX_ITERATION)
                    colour = tuple(int(i * COLOR_MAX) \
                                   for i in colorsys.hsv_to_rgb(hu, ONE, ONE))

                # Draw pixel
                coord = (x, y)
                self.pixel.drawPixel(coord, colour)
        
    # Method runs app
    def runApp(self):
        juliaIndex = ZERO   # Start with mandelbrot
        running = True
        while running:
            for event in pygame.event.get():

                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

            # Draw Mandelbrot set
            self.drawJulia(juliaIndex)

            # Increment juliaIndex
            juliaIndex = juliaIndex + ONE
            if (juliaIndex == len(julias)):
                juliaIndex = ZERO

            # Update Screen
            pygame.display.update()
            self.clock.tick(FPS)            

        # Close app cleanly
        pygame.quit()
        
