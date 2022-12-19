
"""_summary_
"""

import sqlite3 as sql
from . import loggingHelper
from . import DataObject
from . import LogType


class DatabaseHelper:
    
    connection: sql.Connection
    cursor: sql.Connection.cursor
    """_summary_
    """
    def __init__(self, in_Db:str) -> None:
        if (None is in_Db):
            in_Db = 'haushalt.db'
        self.Db = in_Db
        self.logger = loggingHelper.Log()
    
    def open(self) -> None:
        self.connection = sql.connect(self.Db)
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
            connection = self.get_connection()
            cursor = connection.cursor()
            query = "Insert into categories ( cat_name )  values ('"+in_Category +"');"
            result = cursor.execute(query)
            connection.commit()
            connection.close()
            return None is not result
        except TypeError:
            self.logger.log("Error", "Failed: \n" + query)
        return True
        
    
        
        """_summary_
        """
    def select(self, in_table: str, in_columns: str = "*")-> list:
        if (None is in_table):
            raise Exception("in_table can't be none.")
        #self.open(self)
        self.open()
        query : str = ('SELECT {columns} FROM {table};').format(columns=in_columns, table=in_table)
        data  = self.cursor.execute(query)
        result = data.fetchall()
        self.close()
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
        
        