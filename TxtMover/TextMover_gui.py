import tkinter as tk
from tkinter import *

# Be sure to import other component files
import TextMover_main
import TextMover_func

def load_gui(self):

    # Buttons
    self.btn_browse1 = tk.Button(self.master, width=12,height=1,text='Source...', command=lambda: TextMover_func.get_sourcepath(self))
    self.btn_browse1.grid(row=0,column=0,padx=(25,0),pady=(40,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=12,height=1,text='Target...', command=lambda: TextMover_func.get_targetpath(self))
    self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(10,10),sticky=W)
    self.btn_check4files = tk.Button(self.master, width=12,height=2,text='Check for files...', command=lambda: TextMover_func.moveTXTFiles(self))
    self.btn_check4files.grid(row=2, column=0, padx=(25, 0), pady=(10, 10), sticky=W + S)
    self.btn_close = tk.Button(self.master, width=12,height=2,text='Close Program', command=lambda: TextMover_func.closeform(self))
    self.btn_close.grid(row=2, column=3, padx=(25, 0), pady=(10, 10), sticky=E + S)

    # Entry boxes
    self.txt_path1 = tk.Entry(self.master,text='',width=75)
    self.txt_path1.grid(row=0,column=2,rowspan=1, columnspan=2,padx=(25,0),pady=(40,10),sticky=N+E+W)
    self.txt_path2 = tk.Entry(self.master,text='',width=75)
    self.txt_path2.grid(row=1,column=2,rowspan=1, columnspan=2,padx=(25,0),pady=(10,10),sticky=N+E+W)

    # Labels
    self.lbl_spacer = tk.Label(self.master,text='')
    self.lbl_spacer.grid(row=3,column=0, columnspan=3)

    # Initalize Database action
    TextMover_func.initializeDB()