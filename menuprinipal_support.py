#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Nov 18, 2017 05:34:26 PM


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
    import menuprinipal
    menuprinipal.vp_start_gui()


