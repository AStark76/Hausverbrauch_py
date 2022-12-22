"""_summary_

    Returns:
        _type_: _description_
    """
class DataObject:
        
    def __init__(self) -> None:
        self.columns = []
        self.values = []
        self.table = ""
    
    
    def add_key_value(self, in_key:str, in_value:str)->None:
        if((in_key not in self.columns)):
            self.columns.append(in_key)
        self.values.append(in_value)
        
    def set_table(self, in_table:str)->None:
        self.table = self.table = in_table
    
    def set_columns(self, in_columns: list[str])->None:
        self.columns = in_columns
        
    def set_values(self, in_values)->None:
        self.values = in_values
        
    def set_data(self, in_data: dict[str,str])->None:
        self.columns = in_data.keys
        self.values = in_data.values
        
    
    def get_columns(self) -> str:
        result = ','.join(self.columns)
        return result
    
    def get_values(self) -> str:
        result = ','.join(self.values)
        return result
    
    def get_table(self) -> str:
        return self.table
    
    def get_value(self, in_column:str) -> str:
        data = zip(self.columns, self.values)
        return data[in_column]