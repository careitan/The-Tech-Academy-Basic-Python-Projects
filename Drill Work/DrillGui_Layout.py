import os
import tkinter as tk
from tkinter import *

# Be sure to import other component files
import DrillGui_Main

def center_window(self, w, h): # pass in the Tkinter frame (maaster) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to psint the app on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def load_gui(self):

    # Buttons
    self.btn_browse1 = tk.Button(self.master, width=12,height=1,text='Browse...')
    self.btn_browse1.grid(row=0,column=0,padx=(25,0),pady=(40,10),sticky=W)
    self.btn_browse2 = tk.Button(self.master, width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,padx=(25,0),pady=(10,10),sticky=W)
    self.btn_check4files = tk.Button(self.master, width=12,height=2,text='Check for files...')
    self.btn_check4files.grid(row=2, column=0, padx=(25, 0), pady=(10, 10), sticky=W + S)
    self.btn_close = tk.Button(self.master, width=12,height=2,text='Close Program')
    self.btn_close.grid(row=2, column=3, padx=(25, 0), pady=(10, 10), sticky=E + S)

    # Entry boxes
    self.txt_path1 = tk.Entry(self.master,text='',width=40)
    self.txt_path1.grid(row=0,column=2,rowspan=1, columnspan=2,padx=(25,0),pady=(40,10),sticky=N+E+W)
    self.txt_path2 = tk.Entry(self.master,text='',width=40)
    self.txt_path2.grid(row=1,column=2,rowspan=1, columnspan=2,padx=(25,0),pady=(10,10),sticky=N+E+W)

    # Labels
    self.lbl_spacer = tk.Label(self.master,text='')
    self.lbl_spacer.grid(row=0,column=1)