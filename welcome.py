 
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
 
import welcome_support 
import os.path 
 
#----------------------------------------------------------------------- 
 
#--------------------------------------------------------------------------- 
 
def vp_start_gui(): 
    '''Starting point when module is the main routine.''' 
    global val, w, root 
    global prog_location 
    prog_call = sys.argv[0] 
    prog_location = os.path.split(prog_call)[0] 
    root = tk.Tk() 
    top = Toplevel1 (root) 
    welcome_support.init(root, top) 
    root.mainloop() 
 
w = None 
def create_Toplevel1(root, *args, **kwargs): 
    '''Starting point when module is imported by another program.''' 
    global w, w_win, rt 
    global prog_location 
    prog_call = sys.argv[0] 
    prog_location = os.path.split(prog_call)[0] 
    rt = root 
    w = tk.Toplevel (root) 
    top = Toplevel1 (w) 
    welcome_support.init(w, top, *args, **kwargs) 
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
        font12 = "-family {Segoe UI} -size 13 -weight bold -slant "  \ 
            "roman -underline 0 -overstrike 0" 
        font13 = "-family {Segoe UI} -size 9 -weight bold -slant roman"  \ 
            " -underline 0 -overstrike 0" 
        font15 = "-family {Segoe UI Semibold} -size 36 -weight bold "  \ 
            "-slant roman -underline 0 -overstrike 0" 
        self.style = ttk.Style() 
        if sys.platform == "win32": 
            self.style.theme_use('winnative') 
        self.style.configure('.',background=_bgcolor) 
        self.style.configure('.',foreground=_fgcolor) 
        self.style.configure('.',font="TkDefaultFont") 
        self.style.map('.',background= 
            [('selected', _compcolor), ('active',_ana2color)]) 
 
        top.geometry("936x450") 
        top.minsize(116, 1) 
        top.maxsize(1370, 750) 
        top.resizable(1, 1) 
        top.title("Register") 
        top.configure(background="#d9d9d9") 
 
        self.TFrame1 = ttk.Frame(top) 
        self.TFrame1.place(relx=0.032, rely=0.067, relheight=0.833 
                , relwidth=0.796) 
        self.TFrame1.configure(relief='groove') 
        self.TFrame1.configure(borderwidth="2") 
        self.TFrame1.configure(relief="groove") 
 
        self.Label1 = tk.Label(self.TFrame1) 
        self.Label1.place(relx=0.04, rely=0.053, height=51, width=699) 
        self.Label1.configure(background="#d9d9d9") 
        self.Label1.configure(disabledforeground="#a3a3a3") 
        self.Label1.configure(font=font15) 
        self.Label1.configure(foreground="#8000ff") 
        self.Label1.configure(text='''CAR PARKING SYSTEM''') 
 
        self.Label2 = tk.Label(self.TFrame1) 
        self.Label2.place(relx=0.067, rely=0.293, height=21, width=39) 
        self.Label2.configure(background="#d9d9d9") 
        self.Label2.configure(disabledforeground="#a3a3a3") 
        self.Label2.configure(font=font13) 
        self.Label2.configure(foreground="#000000") 
        self.Label2.configure(text='''Car No''') 
 
        self.Label3 = tk.Label(self.TFrame1) 
        self.Label3.place(relx=0.067, rely=0.427, height=21, width=58) 
        self.Label3.configure(background="#d9d9d9") 
        self.Label3.configure(disabledforeground="#a3a3a3") 
        self.Label3.configure(font=font13) 
        self.Label3.configure(foreground="#000000") 
        self.Label3.configure(text='''Name''') 
 
        self.Label4 = tk.Label(self.TFrame1) 
        self.Label4.place(relx=0.067, rely=0.56, height=21, width=49) 
        self.Label4.configure(background="#d9d9d9") 
        self.Label4.configure(disabledforeground="#a3a3a3") 
        self.Label4.configure(font=font13) 
        self.Label4.configure(foreground="#000000") 
        self.Label4.configure(text='''Mobile''') 
 
        self.Label5 = tk.Label(self.TFrame1) 
        self.Label5.place(relx=0.067, rely=0.693, height=21, width=44) 
        self.Label5.configure(background="#d9d9d9") 
        self.Label5.configure(disabledforeground="#a3a3a3") 
        self.Label5.configure(font=font13) 
        self.Label5.configure(foreground="#000000") 
        self.Label5.configure(text='''SloatNo''') 
 
        self.Text1 = tk.Text(self.TFrame1) 
        self.Text1.place(relx=0.201, rely=0.267, relheight=0.091, 
relwidth=0.354) 
 
        self.Text1.configure(background="white") 
        self.Text1.configure(font="-family {Segoe UI} -size 9") 
        self.Text1.configure(foreground="black") 
        self.Text1.configure(highlightbackground="#d9d9d9") 
        self.Text1.configure(highlightcolor="black") 
        self.Text1.configure(insertbackground="black") 
        self.Text1.configure(selectbackground="#c4c4c4") 
        self.Text1.configure(selectforeground="black") 
        self.Text1.configure(wrap="word") 
 
        self.Text2 = tk.Text(self.TFrame1) 
        self.Text2.place(relx=0.201, rely=0.4, relheight=0.091, 
relwidth=0.354) 
        self.Text2.configure(background="white") 
        self.Text2.configure(font="-family {Segoe UI} -size 9") 
        self.Text2.configure(foreground="black") 
        self.Text2.configure(highlightbackground="#d9d9d9") 
        self.Text2.configure(highlightcolor="black") 
        self.Text2.configure(insertbackground="black") 
        self.Text2.configure(selectbackground="#c4c4c4") 
        self.Text2.configure(selectforeground="black") 
        self.Text2.configure(wrap="word") 
 
        self.Text3 = tk.Text(self.TFrame1) 
        self.Text3.place(relx=0.201, rely=0.533, relheight=0.091, 
relwidth=0.354) 
 
        self.Text3.configure(background="white") 
        self.Text3.configure(font="-family {Segoe UI} -size 9") 
        self.Text3.configure(foreground="black") 
        self.Text3.configure(highlightbackground="#d9d9d9") 
        self.Text3.configure(highlightcolor="black") 
        self.Text3.configure(insertbackground="black") 
        self.Text3.configure(selectbackground="#c4c4c4") 
        self.Text3.configure(selectforeground="black") 
        self.Text3.configure(wrap="word") 
self.Text4 = tk.Text(self.TFrame1) 
self.Text4.place(relx=0.201, rely=0.667, relheight=0.091, 
relwidth=0.354) 
self.Text4.configure(background="white") 
self.Text4.configure(font="-family {Segoe UI} -size 9") 
self.Text4.configure(foreground="black") 
self.Text4.configure(highlightbackground="#d9d9d9") 
self.Text4.configure(highlightcolor="black") 
self.Text4.configure(insertbackground="black") 
self.Text4.configure(selectbackground="#c4c4c4") 
self.Text4.configure(selectforeground="black") 
self.Text4.configure(wrap="word") 
self.Button1 = tk.Button(self.TFrame1) 
self.Button1.place(relx=0.201, rely=0.827, height=44, width=187) 
self.Button1.configure(activebackground="#ececec") 
self.Button1.configure(activeforeground="#000000") 
self.Button1.configure(background="#0080ff") 
self.Button1.configure(command=self.newreg) 
self.Button1.configure(disabledforeground="#a3a3a3") 
self.Button1.configure(font=font12) 
self.Button1.configure(foreground="#ffffff") 
self.Button1.configure(highlightbackground="#d9d9d9") 
self.Button1.configure(highlightcolor="black") 
self.Button1.configure(pady="0") 
self.Button1.configure(text='''Submit''') 
#------------------ 
self.Button2 = tk.Button(self.TFrame1) 
self.Button2.place(relx=0.101, rely=0.827, height=44, width=127) 
self.Button2.configure(activebackground="#ececec") 
self.Button2.configure(activeforeground="#000000") 
self.Button2.configure(background="#0080ff") 
self.Button2.configure(command=welcome_support.viewcar) 
self.Button2.configure(disabledforeground="#a3a3a3") 
self.Button2.configure(font=font12) 
self.Button2.configure(foreground="#ffffff") 
self.Button2.configure(highlightbackground="#d9d9d9") 
self.Button2.configure(highlightcolor="black") 
self.Button2.configure(pady="0") 
self.Button2.configure(text='''View Parking ''') 
self.Label6 = tk.Label(self.TFrame1) 
self.Label6.place(relx=0.617, rely=0.213, height=271, width=254) 
self.Label6.configure(background="#d9d9d9") 
self.Label6.configure(disabledforeground="#a3a3a3") 
self.Label6.configure(foreground="#000000") 
photo_location = os.path.join(prog_location,"../Car Parking 
System/img/2.png") 
global _img0 
_img0 = tk.PhotoImage(file=photo_location) 
self.Label6.configure(image=_img0) 
self.Label6.configure(text='''Label''') 
def newreg(self): 
a = self.Text1.get("1.0", 'end-1c') 
b = self.Text2.get("1.0", 'end-1c') 
c = self.Text3.get("1.0", 'end-1c') 
d = self.Text4.get("1.0", 'end-1c') 
welcome_support.carpark(a, b, c, d) 
if __name__ == '__main__': 
vp_start_gui() 