import sys 
from conn import conn 
import easygui 
 
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
 
def newregister(a,b,c,d): 
 
    ct = conn() 
    sql = "INSERT INTO reg VALUES ('" + a + "', '" + b + "','" + c + "', '" + 
d + "')" 
    ct.mycursor.execute(sql) 
    ct.mydb.commit() 
 
    print(ct.mycursor.rowcount, "record inserted.") 
    a = easygui.msgbox("Record Inserted.", title="BOX") 
    root.destroy() 
 
    import start 
    start.vp_start_gui() 
 
 
   # sys.stdout.flush() 
 
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
import newuser 
newuser.vp_start_gui() 