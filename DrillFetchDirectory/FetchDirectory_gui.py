import tkinter as tk
from tkinter import *

# Be sure to import other component files
import FetchDirectory_main
import FetchDirectory_func

def load_gui(self):

    # Labels
    self.lbl_Path = tk.Label(self.master,text='Directory Path:')
    self.lbl_Path.grid(row=0, column=1,padx=(25,0),pady=(10,0),sticky=N+W)
    self.lbl_Path2 = tk.Label(self.master,text='', bg="white", width=50)
    self.lbl_Path2.grid(row=1, column=1,padx=(25,0),pady=(10,0),sticky=N+W)

    # Buttons
    self.btn_Directory = tk.Button(self.master, width=12, height=1,text='Browse...',command=lambda: FetchDirectory_func.get_directorypath(self))
    self.btn_Directory.grid(row=1,column=0,padx=(25,0),pady=(10,10),)



