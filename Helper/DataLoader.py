from Helper import Data as d
from Helper.sqlConnection import DatabaseHelper


class DataLoader:
    
    def __init__(self, in_category) -> None:
        self.category = in_category
        self.sql = DatabaseHelper('.\Data\Haushalt.db')
    
    def load_default(self, in_cat: str)->list[d.Data]:
        data = self.get_data(in_cat)
        result = self.get_delta(data)
        
        return result
            

    def get_data(self,in_cat: str = "Strom")->list[d.Data]:
        result : list[d.Data]= []
        where_clause = 'cat_id=(Select Id from categories where cat_name = "{category}")'.format(category=in_cat)
        sql_result = self.sql.select("data", in_where=where_clause)
        
        for data_row in sql_result:
            result.append(d.Data(id = data_row[0], date=data_row[2], value=data_row[3]))
        
        return result
    
    def get_delta(self, in_data: list[d.Data]) -> list[d.Data]:
        result : list[d.Data]= in_data
        count_max = len(result)
        for counter in range(count_max):
            if(0 == counter):
                in_data[counter].delta = 0
                continue
            result[counter].delta = result[counter].value-result[counter-1].value
        
        return result