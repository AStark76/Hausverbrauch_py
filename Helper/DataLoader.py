import Data
from Helper.sqlConnection import DatabaseHelper


class DataLoader:
    
    def __init__(self, in_category) -> None:
        self.category = in_category
        self.sql = DatabaseHelper('\Haushalt.db')
    
    def load_default(self)->list:
        result : list[Data]
        sql_result = self.sql.select("data")
        
        for data_row in sql_result:
            tmp = Data(id = sql_result[0], )