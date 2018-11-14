#! /usr/bin/env python
#
# Support module generated by PAGE version 4.8a
# In conjunction with Tcl version 8.6
#    Sep 06, 2016 02:27:05 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def draw():
    cwidth = w.Canvas1.winfo_width()     # canvas width
    cheight = w.Canvas1.winfo_height()   # canvas height 
    halfwidth=int(cwidth/2)
    halfheight=int(cheight/2)
    qwidth=int(cwidth/4)
    qheight=int(cheight/4)
    ewidth=int(cwidth/8)
    eheight=int(cheight/8)
    #                       Some drawing on the canvas....
    #                       x,y, width, height
    w.Canvas1.create_line(0,0,cwidth,halfheight) 
    w.Canvas1.create_line(0,halfheight, cwidth, 0, fill="red", dash=(4, 4))
    w.Canvas1.create_rectangle(qwidth, halfheight-eheight,halfwidth+qwidth,eheight, fill="blue")
    w.Canvas1.create_rectangle(0, halfheight, cwidth, cheight, fill="green")
    text1= w.Canvas1.create_text(halfwidth, halfheight+qheight)
    w.Canvas1.itemconfig(text1, text="Hello!", fill="white",font="Times 20 italic bold")
    
def quit():
    print('canvasc_support.quit')
    sys.stdout.flush()
    sys.exit()

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
    import canvasc
    canvasc.vp_start_gui()


