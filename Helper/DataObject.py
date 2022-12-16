from multipledispatch import dispatch
"""_summary_
"""
class DataObject:
    
    @dispatch(str, str)
    def __init__(self, in_table: str, in_columns :list[str], in_values:list[str]) -> None:
        self.table = in_table
        self.columns = in_columns
        self.values = in_values
        
    @dispatch(str, dict[str,str])
    def __init__(self, in_table:str, in_data: dict[str,str]) -> None:
        self.table = in_table
        self.data = in_data
        
        
    def get_columns(self) -> str:
        result = ','.join(self.data.keys)
        return result
    
    def get_values(self) -> str:
        result = ','.join(self.data.values)
        return result
    
    def get_table(self) -> str:
        return self.table
    
    def get_value(self, in_column:str) -> str:
        return self.data[in_column]