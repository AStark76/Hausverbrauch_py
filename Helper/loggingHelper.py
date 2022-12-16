import logging
import os
import time
import enum

"""_summary_
"""
class Log:
    log_file : str = os.curdir + "\log\log.txt"
    
    """_summary_
    """
    def __init__(self, file_name: str = None) -> None:
        if (None != file_name):
            self.log_file = file_name
            
        logging.basicConfig(filename=self.log_file)
        self.function_list = {"warning": self.warning, "error": self.error, "info": self.info}   
        
    """_summary_
    """
    def log(self, type: str, message:str):
        zeit = time.strftime("%d.%m.%Y - T %H:%M%:%S")
        self.function_list[type](message,zeit)
        
    """_summary_
    """
    def warning(self, message:str, zeit:str):        
        logging.warning('\t%s - %s' , zeit, message)
        
    """_summary_
    """
    def error(self, message:str, zeit:str):
        logging.error('%s - %s' , zeit, message)
        
    """_summary_
    """
    def info(self, message:str, zeit:str):
        logging.info('%s - %s' , zeit, message)
        
    
"""_summary_
"""
class LogType(enum.auto):
    Error = "Error"
    Warning = "Warning"
    Info = "Info"