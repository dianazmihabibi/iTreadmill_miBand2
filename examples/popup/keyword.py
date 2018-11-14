#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14N
# In conjunction with Tcl version 8.6
#    May 24, 2018 07:53:28 PM

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

import keyword_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Keyword (root)
    keyword_support.init(root, top)
    root.mainloop()

w = None
def create_Keyword(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Keyword (w)
    keyword_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Keyword():
    global w
    w.destroy()
    w = None


class Keyword:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}' 
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2' 
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font11 = "-family {DejaVu Sans} -size 16 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"

        top.geometry("600x450+650+150")
        top.title("Keyword")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.23, rely=0.38, height=31, width=89)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="wheat")
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font=font12)
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Button1''')
        if (root.tk.call('tk', 'windowingsystem')=='aqua'):
            self.Button1.bind('<Button-2>', lambda e: self.popup1(e,which=1))
            self.Button1.bind('<Control-1>', lambda e: self.popup1(e,which=1))
        else:
            self.Button1.bind('<Button-3>', lambda e: self.popup1(e,which=1))

        self.Button2 = Button(top)
        self.Button2.place(relx=0.68, rely=0.38, height=31, width=89)
        self.Button2.configure(activebackground="#f4bcb2")
        self.Button2.configure(background="wheat")
        self.Button2.configure(disabledforeground="#b8a786")
        self.Button2.configure(font=font12)
        self.Button2.configure(highlightbackground="wheat")
        self.Button2.configure(text='''Button2''')
        if (root.tk.call('tk', 'windowingsystem')=='aqua'):
            self.Button2.bind('<Button-2>', lambda e: self.popup2(e))
            self.Button2.bind('<Control-1>', lambda e: self.popup2(e))
        else:
            self.Button2.bind('<Button-3>', lambda e: self.popup2(e))

        self.menubar = Menu(top,font=font10,bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=keyword_support.quit,
                font=font11,
                foreground="#000000",
                label="Quit")


    @staticmethod
    def popup1(event, *args, **kwargs):
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        Popupmenu1 = Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#ffffcd")
        Popupmenu1.configure(background="#dda0dd")
        Popupmenu1.configure(disabledforeground="#b8a786")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=keyword_support.this,
                font=font12,
                foreground="#000000",
                label="This")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=keyword_support.that,
                font=font12,
                foreground="#000000",
                label="That")
        Popupmenu1.add_separator(
                background="wheat")
        also = Menu(Popupmenu1,tearoff=0)
        Popupmenu1.add_cascade(menu=also,
                activebackground="#f4bcb2",
                activeforeground="#111111",
                background="wheat",
                font=font12,
                foreground="#000000",
                label="Also")
        also.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=keyword_support.then,
                font=font12,
                foreground="#000000",
                label="Then")
        also.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=keyword_support.there,
                font=font12,
                foreground="#000000",
                label="There")
        Popupmenu1.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="wheat",
                command=lambda:keyword_support.which(kwargs['which']),
                font=font10,
                foreground="#000000",
                label="Which")
        Popupmenu1.post(event.x_root, event.y_root)

    @staticmethod
    def popup2(event, *args, **kwargs):
        font10 = "-family {DejaVu Sans} -size 14 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font12 = "-family {DejaVu Sans} -size 12 -weight normal -slant"  \
            " roman -underline 0 -overstrike 0"
        font9 = "-family {DejaVu Sans Mono} -size 14 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        Popupmenu2 = Menu(root, tearoff=0)
        Popupmenu2.configure(activebackground="#ffffcd")
        Popupmenu2.configure(background="wheat")
        Popupmenu2.configure(disabledforeground="#b8a786")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="plum",
                command=keyword_support.how,
                font=font9,
                foreground="#000000",
                label="How")
        Popupmenu2.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="plum",
                command=keyword_support.now,
                font=font9,
                foreground="#000000",
                label="Now")
        Popupmenu2.add_separator(
                background="plum")
        browncow = Menu(Popupmenu2,tearoff=0)
        Popupmenu2.add_cascade(menu=browncow,
                activebackground="#f4bcb2",
                activeforeground="#111111",
                background="plum",
                font=font9,
                foreground="#000000",
                label="BrownCow")
        browncow.add_command(
                activebackground="#f4bcb2",
                activeforeground="#000000",
                background="plum",
                command=keyword_support.moo,
                font=font9,
                foreground="#000000",
                label="Moo")
        Popupmenu2.post(event.x_root, event.y_root)






if __name__ == '__main__':
    vp_start_gui()



