#!/python*

import tkinter as tk
from tkinter.ttk import *
from Helper.loggingHelper import *

class Window(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Starks Hausverbrauchkontrolle")
        
        Log().log("error", "Hallo Welt")
        
        



if __name__ == "__main__":
    window = Window()
    window.mainloop()