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
from PIL import Image, ImageTk 
import start_support 
import os.path 
def vp_start_gui(): 
global val, w, root 
global prog_location 
prog_call = sys.argv[0] 
prog_location = os.path.split(prog_call)[0] 
root = tk.Tk() 
top = Toplevel1 (root) 
start_support.init(root, top) 
root.mainloop() 
w = None 
def create_Toplevel1(root, *args, **kwargs): 
global w, w_win, rt 
global prog_location 
prog_call = sys.argv[0] 
prog_location = os.path.split(prog_call)[0] 
rt = root 
w = tk.Toplevel (root) 
top = Toplevel1 (w) 
start_support.init(w, top, *args, **kwargs) 
return (w, top) 
def destroy_Toplevel1(): 
global w 
w.destroy() 
w = None 
class Toplevel1: 
def __init__(self, top=None): 
        '''This class configures and populates the toplevel window. 
           top is the toplevel containing window.''' 
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85' 
        _fgcolor = '#000000'  # X11 color: 'black' 
        _compcolor = '#d9d9d9' # X11 color: 'gray85' 
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#ececec' # Closest X11 color: 'gray92' 
        font14 = "-family Vani -size 20 -weight bold -slant roman "  \ 
            "-underline 0 -overstrike 0" 
        self.style = ttk.Style() 
        if sys.platform == "win32": 
            self.style.theme_use('winnative') 
        self.style.configure('.',background=_bgcolor) 
        self.style.configure('.',foreground=_fgcolor) 
        self.style.configure('.',font="TkDefaultFont") 
        self.style.map('.',background= 
            [('selected', _compcolor), ('active',_ana2color)]) 
 
        top.geometry("866x511") 
        top.minsize(116, 1) 
        top.maxsize(1370, 750) 
        top.resizable(1, 1) 
        top.title("Car Parking System") 
        top.configure(background="#d9d9d9") 
 
        self.TFrame1 = ttk.Frame(top) 
        self.TFrame1.place(relx=0.012, rely=0.039, relheight=0.93 
                , relwidth=0.976) 
        self.TFrame1.configure(relief='groove') 
        self.TFrame1.configure(borderwidth="2") 
        self.TFrame1.configure(relief="groove") 
 
        self.TLabel1 = ttk.Label(self.TFrame1) 
        self.TLabel1.place(relx=0.012, rely=0.021, height=439, width=586) 
        self.TLabel1.configure(background="#d9d9d9") 
        self.TLabel1.configure(foreground="#000000") 
        self.TLabel1.configure(font="TkDefaultFont") 
        self.TLabel1.configure(relief="flat") 
        self.TLabel1.configure(text='''Tlabel''') 
        photo_location = os.path.join(prog_location,"../Car Parking 
System/img/1.png") 
        global _img0 
        _img0 = ImageTk.PhotoImage(file=photo_location) 
        self.TLabel1.configure(image=_img0) 
 
        self.Button1 = tk.Button(self.TFrame1) 
        self.Button1.place(relx=0.722, rely=0.211, height=44, width=217) 
        self.Button1.configure(activebackground="#ececec") 
        self.Button1.configure(activeforeground="#000000") 
        self.Button1.configure(background="#d9d9d9") 
        self.Button1.configure(command=start_support.login) 
        self.Button1.configure(disabledforeground="#a3a3a3") 
        self.Button1.configure(font=font14) 
        self.Button1.configure(foreground="#000000") 
        self.Button1.configure(highlightbackground="#d9d9d9") 
        self.Button1.configure(highlightcolor="black") 
        self.Button1.configure(pady="0") 
self.Button1.configure(text='''Login''') 
self.Button2 = tk.Button(self.TFrame1) 
self.Button2.place(relx=0.722, rely=0.4, height=44, width=214) 
self.Button2.configure(activebackground="#ececec") 
self.Button2.configure(activeforeground="#000000") 
self.Button2.configure(background="#d9d9d9") 
self.Button2.configure(command=start_support.reg) 
self.Button2.configure(disabledforeground="#a3a3a3") 
self.Button2.configure(font=font14) 
self.Button2.configure(foreground="#000000") 
self.Button2.configure(highlightbackground="#d9d9d9") 
self.Button2.configure(highlightcolor="black") 
self.Button2.configure(pady="0") 
self.Button2.configure(text='''Registration''') 
self.Button3 = tk.Button(self.TFrame1) 
self.Button3.place(relx=0.722, rely=0.589, height=44, width=217) 
self.Button3.configure(activebackground="#ececec") 
self.Button3.configure(activeforeground="#000000") 
self.Button3.configure(background="#d9d9d9") 
self.Button3.configure(command=start_support.exitt) 
self.Button3.configure(disabledforeground="#a3a3a3") 
self.Button3.configure(font=font14) 
self.Button3.configure(foreground="#000000") 
self.Button3.configure(highlightbackground="#d9d9d9") 
self.Button3.configure(highlightcolor="black") 
self.Button3.configure(pady="0") 
self.Button3.configure(text='''Exit''') 
if __name__ == '__main__': 
vp_start_gui() 