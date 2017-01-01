########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Driver File: For Mandelbrot Set app                                  #
#                                                                      #
# Created on 2016-12-29                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

from   Logger import *   # Error logging
from   init   import *   # init Class
import os                # For filesystem operations

########################################################################
#                                                                      #
#                               DRIVER                                 #
#                                                                      #
########################################################################

def main():
    onePixel = init(appDirectory)

# Store app directory
appDirectory = os.path.dirname(os.path.realpath(__file__))

# Initialize error logging
logger = Logger(appDirectory, 'w')

# Attempt to run app, otherwise log error
try:
    main()
except:
    logger.createLog('')
