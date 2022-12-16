
"""_summary_
"""

import sqlite3 as sql
from . import loggingHelper
from . import DataObject
from . import LogType


class DatabaseHelper:
    
    """_summary_
    """
    def __init__(self, in_Db:str) -> None:
        self.Db = in_Db
        self.open()
        self.logger = loggingHelper.Log()
        
    """_summary_
    """
    def open(self):
        self.connection = sql.connect('.\haushalt.db')
        self.cursor = self.connection.cursor()
    
    def close(self) -> None:
        self.connection.close()
        
    """_summary_
    """
    def insert_category(self, in_category: str) -> bool:
        query: str
        if(None is in_category):
            raise Exception("in_Category can't be none.")
            return False
        try:
            self.open()
            query = "Insert into categories ( cat_name )  values ('"+in_Category +"');"
            result = self.cursor.execute(query)
            self.connection.commit()
            self.close()
            return None is not result
        except TypeError:
            self.logger.log("Error", "Failed: \n" + query)
        return True
        
        """_summary_
        """
    def select(self, in_table: str, in_columns: str = "*")-> list:
        if (ch):
            raise Exception("in_table can't be none.")
        self.open()
        query : str = 'select {columns} from "{table}" ;'.format(columns=in_columns, table=in_table)
        data  = self.cursor.execute(query)
        result = data.fetchall()
        self.close();
        return result

    """_summary_
    """
    def insert(self, in_table:str, in_data: DataObject) -> bool:
        result = False
        if(None is in_table):
            self.logger.error(LogType.Error, "\n in_table can't be None.")
            raise Exception("in_table can't be None.")
        if(None is in_data):
            self.logger.error(LogType.Error, "\n in_data can't be None.")
            raise Exception("in_data can't be None.")
        
        