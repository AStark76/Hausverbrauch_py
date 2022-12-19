from enum import Enum

"""_summary_
"""
class LOGTYPE(Enum):
    ERROR = 0
    WARNING = 1
    INFO = 2
    

def get_name(in_data) ->str:
    result = str(in_data)
    return result