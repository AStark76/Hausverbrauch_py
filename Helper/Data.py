import datetime
from Helper.DateHelper import DateHelper as dh
from . import loggingHelper
from Helper.LogType import LOGTYPE

"""_summary_
    loads data from the data directory
"""
class Data:
    logger = loggingHelper.Log()
    def __init__(self, id: str, date: str, value: str) -> None:
        self.datum = self.set_date(date)
        self.value = int(value)
        self.id = int(id)
        self.delta = 0
        self.logger 
    
    def set_date(self, in_date) -> datetime:
        try:
            date = dh.int_to_date(in_date)
            result = date#.strftime("%d.%m.%Y")
            return result
        except ValueError:
            message = "{in_date} couldn't be converted to int.".format(in_date=in_date)
            self.logger.Log(LOGTYPE.ERROR, message)
    
    def get_date(self)->str:
        return self.datum
    
    def set_value(self, in_value)->None:
        self.value = in_value
    
    def get_value(self)->str:
        return self.value
    
    def set_id(self, in_id)->None:
        self.id = in_id
    
    def get_id(self)->str:
        return self.id
        
    def set_delta(self, in_delta)->None:
        self.delta = in_delta
        
    def get_delta(self)->str:
        return self.delta