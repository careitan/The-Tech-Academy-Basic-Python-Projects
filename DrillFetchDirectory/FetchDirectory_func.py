import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# Be sure to import other component files
import FetchDirectory_main
import FetchDirectory_func

def center_window(self, w, h): # pass in the Tkinter frame (maaster) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to psint the app on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def get_directorypath(self):
    # get path
    options = {}
    options['initialdir'] = None
    options['title'] = None
    options['mustexist'] = False
    var_path = filedialog.askdirectory(**options)
    if var_path == "":
        return None
    else:
        self.lbl_Path2.config(text=var_path)
        return var_path
