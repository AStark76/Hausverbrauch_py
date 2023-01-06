"""_summary_

Returns:
    _type_: _description_
"""
from datetime import *

"""_summary_
"""
def date_to_int(in_date: str)->int:
    time_parts= in_date.split('.')
    result = datetime(year=int(time_parts[2]), month=int(time_parts[1]), day=int(time_parts[0])).strftime("%Y%m%d")
    
    return int(result)

"""_summary_
"""
def int_to_date(in_int_date: int)->datetime:
    time_string = str(in_int_date)
    year :str = str(time_string)[0:4]
    month :str = str(time_string)[4:6]
    day : str = str(time_string)[6:]
    result = datetime(year=int(year), month=int(month), day=int(day))
    
    return result