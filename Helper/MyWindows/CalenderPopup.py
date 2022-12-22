"""_summary_
"""
from datetime import *
import time
import tkinter as tk
from tkinter import ttk as ttk
from tkcalendar import Calendar


class CalendarPopup(tk.Tk):
#### Datumsfeld ####
    
    def __init__(self, in_destination):
        self.popup = tk.Tk()
        self.popup.title("Kalendar")
        self.build_calendar()
        self.destination = in_destination


    def build_calendar(self):
        self.calendar = Calendar(self.popup, selectmode='day',
                                 year=int(time.strftime('%Y')),
                                 month=int(time.strftime('%m')),
                                 day=int(time.strftime('%d')))
        self.calendar.grid(column=1, row=2)
        self.date_select_btn = tk.Button(
            self.popup, text="Auswählen", command=self.set_date).grid(column=1,row=4, padx=5, pady=5)

    def set_date(self):
        self.selected_date = self.calendar.get_date()
        split_date = self.selected_date.split("/")
        self.selected_date = datetime(int(split_date[2]),int(split_date[0]),int(split_date[1])).strftime("%d.%m.%Y")
        self.destination(self.selected_date)
        self.popup.destroy()
        
        