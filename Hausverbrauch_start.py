#!/python*


from datetime import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar


# own modules
from Helper.loggingHelper import *
from Helper.sqlConnection import *
from Helper.MyWindows import CalenderPopup as cp
from Helper.DateHelper import DateHelper as dh
from Helper.DataObject import DataObject
from Helper import DataLoader as dl
from Helper import Data as d

"""_summary_

Returns:
    _type_: _description_
"""
class Window(tk.Tk):

    def __init__(self) -> None:
        super().__init__()
        self.geometry("820x700")
        self.sql = DatabaseHelper('.\Data\Haushalt.db')
        self.init_widgets()

        """_summary_
        """
    def init_widgets(self):
        self.title("Starks Hausverbrauchkontrolle")

        self.build_category_cb()
        
        self.calender_button = tk.Button(self, text="Datum wählen", command=self.display_calendar)
        self.calender_button.grid(column=1, row=1, padx=5, sticky="w")
        
        self.selected_date =tk.StringVar()
        self.selected_date = time.strftime("%d.%m.%Y")
        
        self.lable1 = ttk.Label(self, text="Datum")
        self.lable1.grid(column=0, row=2, padx=5,sticky="w")
        self.date_label = ttk.Label(self, text=self.selected_date)
        self.date_label.grid(column=1, row=2, sticky="w")
                
        self.value_lable = tk.Label(text="Wert")
        self.value_lable.grid(column=0,row=4, sticky="w", padx=5)
        
        self.value = tk.StringVar()
        self.value_entry = tk.Entry(textvariable=self.value)
        self.value_entry.grid(column=1,row=4, padx=5, sticky="w")
        
        self.new_category = tk.StringVar()
        self.category_entry = tk.Entry(textvariable=self.new_category)
        self.category_entry.grid(column=2, row=1, padx=5,pady=5)
        
        self.save_new_category_btn = tk.Button(text="Kategorie speichern", command=self.save_new_category)
        self.save_new_category_btn.grid(column=3, row=1, padx=5)
        
        self.save_btn = tk.Button(text="Speicher", command=self.save_value)
        self.save_btn.grid(column=2, row=4, padx=5)
        
        self.reset_btn = tk.Button(text="Zurücksetzten", command=self.reset_form)
        self.reset_btn.grid(column=3, row=4, padx=5)

        self.build_treeview()
        self.build_plot_frame()
        self.plot(self.loaded_data)   
        self.select_btn = tk.Button(text="Auswählen", command=self.display_select())
        self.select_btn.grid(column=2, row=4, padx=5)
        
    
    def build_plot_frame(self, in_first_render: bool=False):
        if(in_first_render):
            self.plot_frame.destroy()
            
        self.plot_frame = ttk.LabelFrame(self, text="Graph")
        self.plot_frame.grid(columnspan=5, row=7, sticky="nsew")
        

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
        self.category_cb_lable.grid(column=0, row=0, sticky="w", padx=5)
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
        self.build_treeview()
        self.plot(self.loaded_data)

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
        self.build_treeview()
        

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


    def save_new_category(self):
        new_category = self.category_entry.get()
        self.sql.insert_category(new_category)
        self.build_category_cb()
    

    """_summary_
    """
    def reset_form(self):
        self.selected_date = time.strftime("%d.%m.%Y")
        self.value.set("")
        self.value_entry.delete(0,15)

    
    def build_treeview(self)-> None:
        dataloader = dl.DataLoader(self.categoryCB.get())
        self.loaded_data : list[d.Data]
        self.loaded_data = dataloader.load_default(self.categoryCB.get())
        self.tv_frame = ttk.LabelFrame(self, text=self.categoryCB.get())
        self.tv_frame.grid(columnspan=5,row=6, sticky="nsew", padx=5)
        self.tv = ttk.Treeview(self.tv_frame, selectmode='browse')
        self.tv.delete(*self.tv.get_children())
        self.tv["columns"] = ('Date', 'Value', 'Delta')
        self.tv.heading('#0',text="Nr")
        self.tv.column('#0', anchor="center",stretch=tk.NO)
        self.tv.heading('#1', text="Datum", anchor='center')
        self.tv.column('#1', anchor="center", stretch=tk.YES)
        self.tv.heading('#2', text="Wert", anchor='center')
        self.tv.column('#2', anchor="center", stretch=tk.YES)
        self.tv.heading('#3', text="Delta", anchor='center')
        self.tv.column('#3', anchor="center", stretch=tk.YES)
        counter = 0
        for item in self.loaded_data:
            self.tv.insert(parent='', index=counter, text=str(counter),iid=item.id, values=(item.datum.strftime("%d.%m.%Y"), item.value, item.delta))
            counter = counter + 1
        
        self.tv.grid(columnspan=3, rowspan=5, sticky="nsew", padx=5, pady=5)
        
        

    def plot(self, in_data:list[d.Data])-> None:
        y_data = self.get_y(in_data)
        x_data = self.get_x(in_data)
        self.plot_frame.destroy()
        self.build_plot_frame(True)  
        figure = Figure(figsize=(8,3),dpi=100)
        # figure = plt.figure(figsize=(8,3),dpi=100)
        plot1 = figure.add_subplot()
        plot1.scatter(x_data,y_data, color='red')
        plot1.plot(x_data,y_data)
                
        canvas = FigureCanvasTkAgg(figure,master=self.plot_frame)
        widget = canvas.get_tk_widget()
        widget.pack()#grid(column=0, row = 0, sticky="nsew", padx=5, pady=5)
        
        canvas.draw()
        
        
        
    def get_y(self, in_data:list[d.Data])->list[int]:
        result : list[int] = []
        for item in in_data:
            result.append(int(item.delta))
        return result
    
    def get_x(self, in_data:list[d.Data])->list[datetime]:
        result : list[datetime] = []
        for item in in_data:
            result.append(item.datum)
        return result
        
    def display_select(self):
        test = self.tv.selection_get
        print(test(0))

if __name__ == "__main__":
    window = Window()

    window.mainloop()
