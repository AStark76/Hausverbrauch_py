from Helper.DateHelper import DateHelper as dh
from Helper.loggingHelper import Log
from Helper.LogType import LOGTYPE

"""_summary_
    loads data from the data directory
"""
class Data:
    
    def __init__(self, id: str, date: str, value: str) -> None:
        self.set_date(date)
        self.value = int(value)
        self.id = int(id)
        self.delta = 0
        self.log = Log()
    
    def set_date(self, in_date) -> None:
        try:
            self.date = dh.int_to_date(int(in_date))
        except ValueError:
            message = "{in_date} couldn't be converted to int.".format(in_date=in_date)
            self.log.log(LOGTYPE.ERROR, message)
    
    def set_value(self, in_value)->None:
        self.value = in_value
    
    def set_id(self, in_id)->None:
        self.id = in_id
        
    def set_delta(self, in_delta)->None:
        self.delta = in_delta
        