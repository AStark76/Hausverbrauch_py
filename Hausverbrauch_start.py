#!/python*

import tkinter as tk
from tkinter import ttk
from Helper.loggingHelper import *
from Helper.sqlConnection import *

class Window(tk.Tk):

    
    
    def __init__(self) -> None:
        super().__init__()
        self.sql = DatabaseHelper('.\Helper\haushalt.db')
        self.init_widgets()
        
        
    def init_widgets(self):
        self.title("Starks Hausverbrauchkontrolle")
        self.build_category_cb()

        self.lable1 = ttk.Label(self,text=self.categoryCB.get())
        self.lable1.grid(column=0,row=2)
        
    def get_categories(self):
        data = self.sql.select(in_table= "categories")
        result: list(str) =[]
        for date in data:
            value = date[1]
            result.append(value)
        return result
    
    def build_category_cb(self):
        self.category_cb_lable = ttk.Label(self, text="Kategorie")
        self.category_cb_lable.grid(column=0, row=0)
        self.my_category : str=tk.StringVar()
        self.comboBoxValue = self.get_categories()
        self.categoryCB = ttk.Combobox(
            self,
            textvariable = self.my_category,
            values = self.comboBoxValue
        )
        self.categoryCB.current(0)
        self.categoryCB.bind("<<ComboboxSelected>>", self.set_categorie)
        self.categoryCB.grid(column=0,row=1)
    
    
    def set_categorie(self, event):
        self.lable1["text"]=event.widget.get()

if __name__ == "__main__":
    window = Window()
    
    window.mainloop()