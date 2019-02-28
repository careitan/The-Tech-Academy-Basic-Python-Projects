# ========================================
#
# The Tech Academy Drill - Text Mover Tool
#
# Author: Allan Reitan  2/27/2019
#
# Built and tested on Windows 10 64-bit
#
# ========================================
from tkinter import *
import tkinter as tk

# Be sure to import other component files
import TextMover_gui
import TextMover_func

# Frame is the Tkinter base class object
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # define or master frame configuration
        self.master = master

        # Use a method to center the window on the screen
        TextMover_func.center_window(self, 600, 100)
        self.master.title("Move TXT Files")

        # load in the OUT widgets from a separate module,
        # keeping your code compartmentalized and clutter free
        TextMover_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()