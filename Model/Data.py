import os
import logging

"""_summary_
    loads data from the data directory
"""
class Data:
    
    path: str = ""
    
    def __init__(self, in_path: str = None) -> None:
        self.path = in_path
        
    def loadFolder(self, in_path: str = None):
        if(None == in_path):
            in_path = self.path
        if(None == self.path):
            raise Exception("Es wurde kein Pfad angegeben.\n Beispiel 1:\n data = Data('c:\\DatenPfad')\n Beispiel 2:\n data = Data()\n data.loadFolder('c:\\DatenPfad')")
            
        try:
            os.chdir(self.path)
        except FileNotFoundError:
            logging.error(in_path + "not found.")