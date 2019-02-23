# ========================
# The Tech Academy - Python Course Drill to design a directory fetch
#
# Author: Allan Reitan - 2/22/2019
#
# Tested OS: This Code was written and tested on Windows 10
# ========================
from tkinter import *
import tkinter as tk

# Be sure to import other component files
import FetchDirectory_gui
import FetchDirectory_func

# Frame is the Tkinter base class object
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # define or master frame configuration
        self.master = master

        # Use a method to center the window on the screen
        FetchDirectory_func.center_window(self, 600, 100)
        self.master.title("Ask Directory")

        # load in the OUT widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        FetchDirectory_gui.load_gui(self)

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()