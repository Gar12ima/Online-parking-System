#! /usr/bin/env python 
#  -*- coding: utf-8 -*- 
# 
# Support module generated by PAGE version 4.26 
#  in conjunction with Tcl version 8.6 
#    Feb 12, 2020 06:38:55 PM +0530  platform: Windows NT 
import sys 
try: 
import Tkinter as tk 
except ImportError: 
import tkinter as tk 
try: 
import ttk 
py3 = False 
except ImportError: 
import tkinter.ttk as ttk 
py3 = True 
def exitt(): 
import sys 
sys.exit(0) 
def login(): 
root.destroy() 
import login_u_a 
login_u_a.vp_start_gui() 
def reg(): 
root.destroy() 
import newuser 
newuser.vp_start_gui() 
def init(top, gui, *args, **kwargs): 
global w, top_level, root 
w = gui 
top_level = top 
root = top 
def destroy_window(): 
# Function which closes the window. 
global top_level 
top_level.destroy() 
top_level = None 
if __name__ == '__main__': 
import start 
start.vp_start_gui() 
Connection.py