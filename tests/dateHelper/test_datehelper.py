import pytest
import datetime
from Helper.DateHelper import DateHelper as dh

def test_Convert_int_to_date()->None:
    test_data : int = 20220101
    expect : datetime = datetime.datetime(year=2022, month=1, day=1)
    
    result = dh.int_to_date(test_data)
    
    assert result == expect
    
    
def test_date_to_int()->None:
    test_data : str = datetime.datetime(year=2022, month=1, day=1).strftime("%d.%m.%Y")
    expect: int = 20220101
    result = dh.date_to_int(test_data)
    
    assert result == expect