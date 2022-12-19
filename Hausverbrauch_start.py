#!/python*

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import *
# own modules
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
        self.lable1 = ttk.Label(self, text=self.categoryCB.get())
        self.lable1.grid(column=0, row=2)
        
        self.build_calendar()
        self.selected_date =tk.StringVar()
        self.selected_date = time.strftime("%d.%m.%Y")
        self.lable2 = ttk.Label(self, text=self.selected_date)
        self.lable2.grid(column=1, row=3)
        

 #### Kategorie #####

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
        self.category_cb_lable.grid(column=0, row=0)
        self.my_category: str = tk.StringVar()
        self.comboBoxValue = self.get_categories()
        self.categoryCB = ttk.Combobox(
            self,
            textvariable=self.my_category,
            values=self.comboBoxValue
        )
        self.categoryCB.current(0)
        self.categoryCB.bind("<<ComboboxSelected>>", self.set_categorie)
        self.categoryCB.grid(column=0, row=1)

        """_summary_
        """

    def set_categorie(self, event):
        self.lable1["text"] = event.widget.get()

#### Datumsfeld ####
        """_summary_
        """

    def build_calendar(self):
        self.calendar = Calendar(self, selectmode='day',
                                 year=int(time.strftime('%Y')),
                                 month=int(time.strftime('%m')),
                                 day=int(time.strftime('%d')))
        self.calendar.grid(column=1, row=1)
        self.date_select_btn = tk.Button(
            self, text="Auswählen", command=self.set_date).grid(column=1,row=2)

    def set_date(self):
        self.selected_date = self.calendar.get_date()
        split_date = self.selected_date.split("/")
        self.selected_date = datetime(int(split_date[2]),int(split_date[0]),int(split_date[1])).strftime("%d.%m.%Y")
        self.lable2.config(text= self.selected_date)
        
        
        


if __name__ == "__main__":
    window = Window()

    window.mainloop()
