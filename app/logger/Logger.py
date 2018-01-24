'''
David Fuller

Error logging class - Logs to app_directory/logs/error.log.

10-15-2017
'''

import logging
import os

class Logger(object):
    '''
    Logs errors to a file
    '''
    
    def __init__(self, app_directory, mode):
        '''
        Logger's init method.

        Stores paths to log directory and log file. Stores file's open mode.
        Calls method to setup logger object.

        Args:
            app_directory (str): Representation of application directory.
            mode (str): Opening mode for log file (append or write).
        '''

        self.log_directory = app_directory + '/logs'
        self.log_file = self.log_directory + '/error.log'
        self.mode = mode   # Append or write over

        self.setup_logger()

    def setup_directory(self):
        '''
        Handles creating of path of log file.

        If the directory does not already exists, create it. Otherwise, do
        nothing.

        mode = 0o755 gives:
            file owner: read, write, and execute permissions
            file group: read and execute permissions
            file other: read and execute permissions
        '''
        
        if (not (os.path.isdir(self.log_directory))):
            os.makedirs(self.log_directory, mode = 0o755)

    def setup_file(self):
        '''
        Handles creating of log file in the given path.

        If the file does not already exists, create it. Otherwise, do
        nothing.
        '''
        
        if (not (os.path.exists(self.log_file))):
            file = open(self.log_file, self.mode)
            file.close()

    def setup_format(self):
        '''
        Handles setting up of log file format.        
        '''
        
        error_format = '%(asctime)s - %(levelname)s - %(message)s'
        date_format = '%m/%d/%Y %I:%M:%S %p'
        logging.basicConfig(filename = self.log_file,
                            filemode = self.mode,
                            level = logging.DEBUG,
                            format = error_format,
                            datefmt = date_format)

    def setup_logger(self):
        '''
        Handles setting up of logger object.

        Calls methods to set up directory, file, and logger formats.
        '''
        
        self.setup_directory()
        self.setup_file()
        self.setup_format()

    def createLog(self, message): 
        '''
        Creates a log file at the given path with the given format
        '''
        
        logging.exception(message)
            
