#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Nov 04, 2018 04:07:33 PM WIB  platform: Linux

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import manual_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Treadmill (root)
    manual_support.init(root, top)
    root.mainloop()

w = None
def create_Treadmill(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Treadmill (w)
    manual_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Treadmill():
    global w
    w.destroy()
    w = None


class Treadmill:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#f5deb3'  # X11 color: 'wheat'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1024x600+0+0")
        top.title("Treadmill")
        top.attributes("-fullscreen", True)
        top.configure(highlightcolor="black")



##        self.speed_down = Button(top)
##        self.speed_down.place(relx=0.02, rely=0.9, height=45, width=280)
##        self.speed_down.configure(activebackground="#d9d9d9")
##        self.speed_down.configure(command=manual_support.speed_down)
##        self.speed_down.configure(text='''Speed Down''')
##
##        self.start = Button(top)
##        self.start.place(relx=0.303, rely=0.9, height=45, width=410)
##        self.start.configure(activebackground="#d9d9d9")
##        self.start.configure(command=manual_support.start)
##        self.start.configure(text='''Start''')
##
##        self.speed_up = Button(top)
##        self.speed_up.place(relx=0.713, rely=0.9, height=45, width=280)
##        self.speed_up.configure(activebackground="#d9d9d9")
##        self.speed_up.configure(command=manual_support.speed_up)
##        self.speed_up.configure(text='''Speed Up''')
        
        self.speed_down = Button(top)
        self.speed_down.place(relx=0.029, rely=0.9, height=45, width=172)
        self.speed_down.configure(activebackground="#d9d9d9")
        self.speed_down.configure(command=manual_support.speed_down)
        self.speed_down.configure(text='''▼''')
        self.speed_down.configure(width=172)

        self.mode_btn = Button(top)
        self.mode_btn.place(relx=0.215, rely=0.9, height=45, width=172)
        self.mode_btn.configure(activebackground="#d9d9d9")
        self.mode_btn.configure(text='''Mode''')

        self.start = Button(top)
        self.start.place(relx=0.41, rely=0.9, height=45, width=192)
        self.start.configure(activebackground="#d9d9d9")
        self.start.configure(text='''Start''')
        self.start.configure(command=manual_support.start)
        self.start.configure(width=192)

        self.auto_btn = Button(top)
        self.auto_btn.place(relx=0.625, rely=0.9, height=45, width=172)
        self.auto_btn.configure(activebackground="#d9d9d9")
        self.auto_btn.configure(text='''Auto''')

        self.speed_up = Button(top)
        self.speed_up.place(relx=0.811, rely=0.9, height=45, width=172)
        self.speed_up.configure(activebackground="#d9d9d9")
        self.speed_up.configure(command=manual_support.speed_up)
        self.speed_up.configure(text='''▲''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.0, rely=0.867, relwidth=1.0)

        self.menubar = Menu(top,font="TkMenuFont",bg='#d9d9d9',fg=_fgcolor)
        top.configure(menu = self.menubar)



        self.Labelframe2 = LabelFrame(top)
        self.Labelframe2.place(relx=0.029, rely=0.583, relheight=0.258
                , relwidth=0.293)
        self.Labelframe2.configure(relief=GROOVE)
        self.Labelframe2.configure(text='''Distance''')
        self.Labelframe2.configure(width=300)

        self.cov_val = Label(self.Labelframe2)
        self.cov_val.place(relx=0.067, rely=0.220, height=87, width=144
                , bordermode='ignore')
        self.cov_val.configure(activebackground="#f9f9f9")
        self.cov_val.configure(text='''0''',font=("Helvetica", 32))
        self.cov_val.configure(width=144)

        self.Label2_2 = Label(self.Labelframe2)
        self.Label2_2.place(relx=0.567, rely=0.323, height=57, width=94
                , bordermode='ignore')
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(text='''Km''')

        self.hrFrame = LabelFrame(top)
        self.hrFrame.place(relx=0.029, rely=0.317, relheight=0.258
                , relwidth=0.293)
        self.hrFrame.configure(relief=GROOVE)
        self.hrFrame.configure(text='''HeartRate''')
        self.hrFrame.configure(width=300)

        self.hr_val = Label(self.hrFrame)
        self.hr_val.place(relx=0.067, rely=0.258, height=87, width=134
                , bordermode='ignore')
        self.hr_val.configure(activebackground="#f9f9f9")
        self.hr_val.configure(font="TkFixedFont")
        self.hr_val.configure(text='''0''',font=("Helvetica", 32))
        self.hr_val.configure(width=134)

        self.Label2_3 = Label(self.hrFrame)
        self.Label2_3.place(relx=0.567, rely=0.323, height=57, width=94
                , bordermode='ignore')
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(text='''bpm''')

        self.Labelframe2_4 = LabelFrame(top)
        self.Labelframe2_4.place(relx=0.693, rely=0.317, relheight=0.258
                , relwidth=0.293)
        self.Labelframe2_4.configure(relief=GROOVE)
        self.Labelframe2_4.configure(text='''Burned Calories''')
        self.Labelframe2_4.configure(width=300)

        self.cal_val = Label(self.Labelframe2_4)
        self.cal_val.place(relx=0.067, rely=0.194, height=97, width=144
                , bordermode='ignore')
        self.cal_val.configure(activebackground="#f9f9f9")
        self.cal_val.configure(text='''0''',font=("Helvetica", 32))
        self.cal_val.configure(width=144)

        self.Label2_1 = Label(self.Labelframe2_4)
        self.Label2_1.place(relx=0.567, rely=0.323, height=57, width=94
                , bordermode='ignore')
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(text='''Cal''')

        self.Labelframe2_2 = LabelFrame(top)
        self.Labelframe2_2.place(relx=0.693, rely=0.583, relheight=0.258
                , relwidth=0.293)
        self.Labelframe2_2.configure(relief=GROOVE)
        self.Labelframe2_2.configure(text='''Steps''')
        self.Labelframe2_2.configure(width=300)

        self.step_value = Label(self.Labelframe2_2)
        self.step_value.place(relx=0.067, rely=0.194, height=97, width=144
                , bordermode='ignore')
        self.step_value.configure(activebackground="#f9f9f9")
        self.step_value.configure(text='''0''',font=("Helvetica", 32))
        self.step_value.configure(width=144)

        self.Label2_4 = Label(self.Labelframe2_2)
        self.Label2_4.place(relx=0.567, rely=0.323, height=57, width=94
                , bordermode='ignore')
        self.Label2_4.configure(activebackground="#f9f9f9")
        self.Label2_4.configure(text='''Steps''')

        self.Labelframe3 = LabelFrame(top)
        self.Labelframe3.place(relx=0.332, rely=0.317, relheight=0.525
                , relwidth=0.352)
        self.Labelframe3.configure(relief=GROOVE)
        self.Labelframe3.configure(text='''Speed''')
        self.Labelframe3.configure(width=360)

        self.speed_val = Label(self.Labelframe3)
        self.speed_val.place(relx=0.028, rely=0.095, height=147, width=324
                , bordermode='ignore')
        self.speed_val.configure(activebackground="#f9f9f9")
        self.speed_val.configure(text='''0''',font=("Helvetica", 50))

        self.Label3_4 = Label(self.Labelframe3)
        self.Label3_4.place(relx=0.028, rely=0.54, height=137, width=324
                , bordermode='ignore')
        self.Label3_4.configure(activebackground="#f9f9f9")
        self.Label3_4.configure(text='''Km/hr''')

        self.back = Button(top)
        self.back.place(relx=0.029, rely=0.033, height=45, width=62)
        self.back.configure(activebackground="#f4bcb2")
        self.back.configure(command=manual_support.destroy_window)
        self.back.configure(text='''Back''')

        self.recap = Button(top)
        self.recap.place(relx=0.928, rely=0.033, height=45, width=62)
        self.recap.configure(activebackground="#f4bcb2")
        self.recap.configure(command=manual_support.recap)
        self.recap.configure(text='''Recap''')

        self.Labelframe1 = LabelFrame(top)
        self.Labelframe1.place(relx=0.029, rely=0.133, relheight=0.175
                , relwidth=0.957)
        self.Labelframe1.configure(relief=GROOVE)
        self.Labelframe1.configure(text='''Timer''')
        self.Labelframe1.configure(width=980)

        self.timer = Label(self.Labelframe1)
        self.timer.place(relx=0.35, rely=0.276, height=50, width=300
                , bordermode='ignore')
        self.timer.configure(activebackground="#d9d9d9")
        self.timer.configure(text='''00:00:00''',font=("Helvetica", 50))






if __name__ == '__main__':
    vp_start_gui()



