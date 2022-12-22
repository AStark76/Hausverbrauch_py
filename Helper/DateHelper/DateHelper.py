"""_summary_

Returns:
    _type_: _description_
"""
from datetime import *

"""_summary_
"""
def date_to_int(in_time_parts: list[str])->int:
    time_parts= in_time_parts
    result = datetime(year=int(time_parts[2]), month=int(time_parts[1]), day=int(time_parts[0])).strftime("%Y%m%d")
    
    return result

"""_summary_
"""
def int_to_date(in_int_date: int)->datetime:
    time_string = str(in_int_date)
    result = datetime(year=int(str(time_string)[:4]), month=int(str(time_string)[4:6]), day=int(str(time_string)[6:]))
    
    return result