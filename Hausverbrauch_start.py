#!/python*

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import *

# own modules
from Helper.loggingHelper import *
from Helper.sqlConnection import *
from Helper.MyWindows import CalenderPopup as cp
from Helper.DateHelper import DateHelper as dh
from Helper.DataObject import DataObject
from Helper import DataLoader as dl

"""_summary_

Returns:
    _type_: _description_
"""
class Window(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("820x600")
        self.sql = DatabaseHelper('.\Data\Haushalt.db')
        self.init_widgets()

        """_summary_
        """
    def init_widgets(self):
        self.title("Starks Hausverbrauchkontrolle")

        self.build_category_cb()
        dataloader = dl.DataLoader(self.categoryCB.get())
        loaded_data = dataloader.load_default()
        
        self.calender_button = tk.Button(self, text="Datum wählen", command=self.display_calendar)
        self.calender_button.grid(column=1, row=1, padx=5, sticky="w")
        
        self.selected_date =tk.StringVar()
        self.selected_date = time.strftime("%d.%m.%Y")
        
        self.lable1 = ttk.Label(self, text="Datum")
        self.lable1.grid(column=0, row=2, padx=5,sticky="w")
        self.date_label = ttk.Label(self, text=self.selected_date)
        self.date_label.grid(column=1, row=2, sticky="w")
        
        
        self.value_lable = tk.Label(text="Wert")
        self.value_lable.grid(column=0,row=4, sticky="w")
        
        self.value = tk.StringVar()
        self.value_entry = tk.Entry(textvariable=self.value)
        self.value_entry.grid(column=1,row=4, padx=5, sticky="w")
        
        self.save_btn = tk.Button(text="Speicher", command=self.save_value)
        self.save_btn.grid(column=2, row=4, padx=5)
        
        self.reset_btn = tk.Button(text="Zurücksetzten", command=self.reset_form)
        self.reset_btn.grid(column=3, row=4, padx=5)
 
        self.build_treeview()
        
        
        

    def get_categories(self):
        data = self.sql.select(in_table="categories")
        result: list(str) = []
        for date in data:
            value = date[1]
            result.append(value)
        return result

        """_summary_
        """

    def build_category_cb(self):
        self.category_cb_lable = ttk.Label(self, text="Kategorie")
        self.category_cb_lable.grid(column=0, row=0, sticky="w")
        self.my_category: str = tk.StringVar()
        self.comboBoxValue = self.get_categories()
        self.categoryCB = ttk.Combobox(
            self,
            textvariable=self.my_category,
            values=self.comboBoxValue
        )
        self.categoryCB.current(0)
        self.categoryCB.bind("<<ComboboxSelected>>", self.set_categorie)
        self.categoryCB.grid(column=0, row=1, padx=5, sticky="w")

        """_summary_
        """

    def set_categorie(self, event):
        self.lable1["text"] = event.widget.get()

    def display_calendar(self):
        self.calendar = cp.CalendarPopup(self.set_date)
        
    def set_date(self, in_data):
        self.selected_date = in_data
        self.date_label.config(text=in_data)
        
    def save_value(self):
        data = self.prepare_data()
        data.set_table("data")
        self.sql.insert(in_table="data", in_data=data)
        data = None
        self.reset_form()
        

    def prepare_data(self)->DataObject:
        result = DataObject()
        result.add_key_value("date", str(self.prepare_date()))
        result.add_key_value("value", str(self.value_entry.get()))
        where_part = 'cat_name = "{cat_name}"'.format(cat_name=self.categoryCB.get())
        result.add_key_value("cat_Id", str(self.sql.select_id(in_table= "categories", in_columns= "Id", in_where= where_part)))
        
        return result


    def prepare_date(self)->int:
        time_parts = self.selected_date.split(".")
        result = dh.date_to_int(time_parts)
        
        return result


    """_summary_
    """
    def reset_form(self):
        self.selected_date = time.strftime("%d.%m.%Y")
        self.value.set("")
        self.value_entry.delete(0,15)

    
    def build_treeview(self)-> None:
        self.tv_frame = ttk.LabelFrame(self, text=self.categoryCB.get())
        self.tv_frame.grid(columnspan=5,row=6, sticky="nsew", padx=5)
        self.tv = ttk.Treeview(self.tv_frame, selectmode='browse')
        self.tv["columns"] = ('Date', 'Value', 'Delta')
        self.tv.heading('#0', text="Nr.", anchor="w")
        self.tv.heading('Date', text="Datum", anchor='center')
        self.tv.heading('Value', text="Wert", anchor='center')
        self.tv.heading('Delta', text="Delta", anchor='center')
        
        
        self.tv.grid(columnspan=3, rowspan=5, sticky="nsew", padx=5, pady=5)
        
if __name__ == "__main__":
    window = Window()

    window.mainloop()
