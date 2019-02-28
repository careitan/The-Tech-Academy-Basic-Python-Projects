import os
import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import filedialog

# Be sure to import other component files
import TextMover_main
import TextMover_func

def initializeDB():
    conn = sqlite3.connect('TXTMove.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    col_fname TEXT, \
                    col_mtime TEXT \
                    )")
        conn.commit()
    conn.close()

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
        return var_path

def get_sourcepath(self):
    var_string = str(get_directorypath(self))
    if var_string != None:
        self.txt_path1.delete(0, END)
        self.txt_path1.insert(0, var_string)

def get_targetpath(self):
    var_string = str(get_directorypath(self))
    if var_string != None:
        self.txt_path2.delete(0, END)
        self.txt_path2.insert(0, var_string)

def closeform(self):
    self.master.destroy()

def moveTXTFiles(self):
    var_searchDir = str(self.txt_path1)

    return