import pytest
import datetime
from Helper.DateHelper import DateHelper as dh

def test_Convert_int_to_date()->None:
    test_data : int = 20220101
    expect : datetime = datetime.datetime(year=2022, month=1, day=1)
    
    result = dh.int_to_date(test_data)
    
    assert result == expect