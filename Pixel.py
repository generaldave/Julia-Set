########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Pixel class: Draws one pixel to screen                               #
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
import pygame               # For GUI
import random               # For random integers

########################################################################
#                                                                      #
#                              PIXEL CLASS                             #
#                                                                      #
########################################################################

class Pixel(object):
    def __init__(self, screen):
        self.screen = screen   # Main screen
        
        # Pixel attributes
        self.block = (ONE, ONE)

   # Method draws a pixel
    def drawPixel(self, coord, colour):
        # Place pixel
        self.screen.fill(colour, (coord, self.block))
