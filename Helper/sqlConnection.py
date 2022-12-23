
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
            connection = sql.connect(self.Db)
            cursor = connection.cursor()
            query = 'Insert into categories ( cat_name )  values ("{in_category}");'.format(in_category=in_category)
            result = cursor.execute(query)
            connection.commit()
            connection.close()
            return None is not result
        except TypeError:
            self.logger.Log("Error", "Failed: \n" + query)
        return True
        
    
        
        """_summary_
        """
    def select(self, in_table: str, in_columns: str = "*", in_where:str="None")-> list:
        if (None is in_table):
            raise Exception("in_table can't be none.")
    
        self.open()
        query : str = ('SELECT {columns} FROM {table}').format(columns=in_columns, table=in_table)
        if("None" != in_where):
            query = query + ' where {where}'.format(where=in_where)
        query = query + ";"
        data  = self.connection.execute(query)
        result = data.fetchall()
        self.close()
        return result

        """_summary_
        """
    def select_id(self, in_table: str, in_columns: str = "*", in_where:str="None") -> int:
        data = self.select(in_table=in_table, in_columns= in_columns, in_where=in_where)
        result = data[0][0]
        
        return result

    """_summary_
    """
    def insert(self, in_table:str, in_data: DataObject.DataObject) -> bool:
        result = False
        if(None is in_table):
            self.logger.log(LogType.LOGTYPE.ERROR, "\n in_table can't be None.")
            raise Exception("in_table can't be None.")
        if(None is in_data):
            self.logger.log(LogType.LOGTYPE.ERROR, "\n in_data can't be None.")
            raise Exception("in_data can't be None.")
        
        columns = in_data.get_columns()
        values = in_data.get_values()
        table = in_data.get_table()
        self.open()
        
        query = "INSERT INTO {table} ({columns}) VALUES ({values});".format(table=table, columns=columns, values=values)
        try:
            self.logger.log(LogType.LOGTYPE.INFO, query)
            self.connection.execute(query)
            self.connection.commit()
            self.close()
                        
            result =  True
        finally:
            return result
        
    def select_data(self, in_category: str):
        pass