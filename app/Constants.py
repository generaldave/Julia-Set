'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
color = namedtuple('color', ['r', 'g', 'b'])
resolution = namedtuple('resolution', ['width', 'height'])

screen_resolution = resolution(width = 360, height = 360)

app_title = "Julia Set"
fps = 60

julias = []
julias.append((0, 0))   # Mandelbrot
julias.append((0.285, 0.01))
julias.append((0.45, 0.1428))
julias.append((-0.70176, -0.3842))
julias.append((-0.835, -0.2321))
julias.append((-0.8, 0.156))
julias.append((-0.7269, 0.1889))
julias.append((0, 0.8))
