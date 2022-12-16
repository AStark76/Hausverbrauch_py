class Checker:
    
    """_summary_
    """
    def not_none(self, in_data)->bool:
        return None is in_data
    

    """_summary_
    """
    def is_none(self, in_data)->bool:
        return self.not_none(in_data)