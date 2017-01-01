########################################################################
#                                                                      #
# David Fuller                                                         #
#                                                                      #
# Error logging class: Logs to appDirectory/logs/error.log             #
#                                                                      #
# Created on 2016-12-27                                                #
#                                                                      #
########################################################################

########################################################################
#                                                                      #
#                          IMPORT STATEMENTS                           #
#                                                                      #
########################################################################

import logging   # Log errors
import os        # For filesystem paths

########################################################################
#                                                                      #
#                         ERROR LOGGING CLASS                          #
#                                                                      #
########################################################################

class Logger(object):
    # Constructors takes appDirectory
    def __init__(self, appDirectory, mode):
        self.appDirectory = appDirectory
        self.logDirectory = appDirectory      + "/logs"
        self.logFile      = self.logDirectory + "/error.log"
        self.mode         = mode   # Append or write over

        # Call method to set up logger
        self.setupLogger()

    # Method creates directory if it doesn't exist
    def setupDirectory(self):        
        if (not (os.path.isdir(self.logDirectory))):
            os.makedirs(self.logDirectory, mode = 0o755)

    # Method creates file if it doesn't exist
    def setupFile(self):
        if (not (os.path.exists(self.logFile))):
            file = open(self.logFile, 'w')
            file.close()

    # Method sets up logging format
    def setupFormat(self):
        errorFormat = '%(asctime)s - %(levelname)s - %(message)s'
        dateFormat = '%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(filename = self.logFile,  \
                            filemode = self.mode,     \
                            level    = logging.DEBUG, \
                            format   = errorFormat,   \
                            datefmt  = dateFormat)

    # Method setups logger
    def setupLogger(self):
        self.setupDirectory()
        self.setupFile()
        self.setupFormat()

    # Method creates log in file
    def createLog(self, message):       
        logging.exception(message)
            
