# ========================
# The Tech Academy - Python Course Drill to design a basic GUI layout
#
# Author: Allan Reitan - 2/22/2019
#
# Tested OS: This Code was written and tested on Windows 10
# ========================
from tkinter import *
import tkinter as tk

# Be sure to import other component files
import DrillGui_Lsyout

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define or master frame configuration
        self.master = master
        self.master.minsize(200,300) # (Height, Width)
        self.master.maxsize(500, 700)

        # Use a method to center the window on the screen
        DrillGui_Layout.center_window(self,200,300)



if __init__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()