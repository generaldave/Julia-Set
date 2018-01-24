'''
David Fuller

Julia class: Class to handle creating and displaying a Julia set.

1-24-2018
'''

import math
import colorsys

from .Constants import color, resolution, point, julias


class Pixel(object):
    '''
    Sets up a Pixel object.
    '''
    
    def __init__(self,
                 position = point(x = 0, y = 0),
                 size = resolution(width = 1, height = 1),
                 pixel_color = color(r = 0, g = 0, b = 0)):
        '''
        App's init method.

        Stores pixel attributes.

        Args:
            size (int): Height and width of a pixel.
            pixel_color (rgb): Default color of a pixel.
        '''

        self.position = position
        self.size = size
        self.color = pixel_color

    def show(self, surface):
        '''
        Shows pixel on a given surface at a given coordinate.

        Args:
            surface (pygame.surface): Surface to show pixel on.
        '''
        
        surface.fill(self.color, (self.position, self.size))

class Julia(object):
    '''
    Sets up a Julia object.
    '''
    
    def __init__(self):
        '''
        App's init method.

        Initializes pixel array.
        '''
        
        self.pixel_array = []

    @staticmethod
    def map_value(value, old_lower, old_upper, new_lower, new_upper):
        '''
        Maps a value from an old range into a new range.

        Args:
            value (int): Input value to map.
            old_lower (int): Lower boundary of old range.
            old_uppper (int): Upper boundary of old range.
            new_lower (int): Lower boundary of new range.
            new_lower (int): Lower boundary of new range.

        Returns:
            Int: The mapped value.
        '''
        
        old_range = old_upper - old_lower
        new_range = new_upper - new_lower
        return ((value - old_lower) / old_range) * new_range + new_lower

    def update(self, surface, surface_resolution, index):
        '''
        Creates the Julia set and stores pixels appropriately.

        Args:
            surface (pygame.surface): Surface to show pixel on.
            surface_resolution (width, height): Width and height of surface.
            index (int): Julia set index.
        '''

        self.pixel_array = []

        if index != 0:
            current_a = julias[index][0]
            current_b = julias[index][1]
        
        width = surface_resolution.width
        height = surface_resolution.height
        for x in range(width):
            self.pixel_array.append([])
            for y in range(height):
                a = Julia.map_value(x, 0, width, -2.5, 2.5)
                b = Julia.map_value(y, 0, height, -2.5, 2.5)

                if index == 0:
                    current_a = a
                    current_b = b

                iteration = 0

                while iteration < 100:
                    real = (a * a) - (b * b)
                    composite = 2 * a * b

                    if abs((real * real) + (composite * composite)) > 16:
                        break

                    a = real + current_a
                    b = composite + current_b

                    iteration = iteration + 1
                
                red = 0
                green = 0
                blue = 0
                if iteration != 100:
                    hue = math.sqrt(float(iteration) / 100)
                    new_color = tuple(int(i * 255) \
                                      for i in colorsys.hsv_to_rgb(hue, 1, 1))
                    red = new_color[0]
                    green = new_color[1]
                    blue = new_color[2]
                    
                pixel_color = color(r = red, g = green, b = blue)
                position = point(x = x, y = y)
                self.pixel_array[x].append(Pixel(position = position,
                                                 pixel_color = pixel_color))
                
    def show(self, surface, surface_resolution):
        '''
        Shows pixel on a given surface at a given coordinate.

        Args:
            surface (pygame.surface): Surface to show pixel on.
            surface_resolution (width, height): Width and height of surface.
        '''
        
        for x in range(surface_resolution.width):
            for y in range(surface_resolution.height):
                self.pixel_array[x][y].show(surface)
                
