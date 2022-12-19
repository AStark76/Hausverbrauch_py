import logging
import os
import time
from Helper import LogType

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
        self.function_list = {LogType.get_name(LogType.LOGTYPE.WARNING) : self.warning, 
                              LogType.get_name(LogType.LOGTYPE.ERROR): self.error, 
                              LogType.get_name(LogType.LOGTYPE.INFO): self.info}   
        
    """_summary_
    """
    def log(self, type: LogType, message:str):
        zeit = time.ctime()
        self.function_list[LogType.get_name(type)](message,zeit)
        
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
        
   