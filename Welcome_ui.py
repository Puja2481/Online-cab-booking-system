""" Welcome_ui.py --

 UI generated by GUI Builder Build 146 on 2021-07-27 13:08:18 from:
    Welcome.ui
THIS IS AN AUTOGENERATED FILE AND SHOULD NOT BE EDITED.
The associated callback file should be modified instead.
"""

#import tkinter
#import os # needed for relative image paths
import tkinter
from tkinter import *
import sqlite3
import os
from tkinter import messagebox
# Using new-style classes: create empty base class object
# for compatibility with older python interps
#if sys.version_info < (2, 2):
#    class object:
#        pass

class Welcome(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('cab booking .gif', file = 'cab booking .gif'))
        self._images.append(tkinter.PhotoImage('lpu.gif', file = os.path.dirname(__file__) + '/lpu.gif'))


        # Widget Initialization
        self._frame_1 = tkinter.Frame(root,
            background = "#ffffff",
        )
        self._label_1 = tkinter.Label(root,
            activebackground = "#ffffff",
            background = "#ffffff",
            borderwidth = 1,
            cursor = "dotbox",
            font = "{MS Sans Serif} 24 bold",
            image = "cab booking .gif",
            text = "ONLINE CAB BOOKING",
        )
        self._label_3 = tkinter.Label(root,
            activebackground = "#ffffff",
            background = "#ffffff",
            borderwidth = 0,
            cursor = "arrow",
            image = "lpu.gif",
            text = "_label_3",
        )
        self._label_4 = tkinter.Label(root,
            activebackground = "#feebcd",
            activeforeground = "#ff0033",
            background = "#ffff80",
            font = "{MS Sans Serif} 13 bold italic",
            foreground = "#ff0033",
            text = u"\u00A9 copyright protected 2018-2019",
        )
        self.login = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "Login",
        )
        self.newuser = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "New User",
        )
        self._label_2 = tkinter.Label(root,
            activebackground = "#fff4d2",
            background = "#ffff80",
            borderwidth = 0,
            font = "{MS Sans Serif} 14 bold",
            text = u"""\uD83D\uDCAE \uD83D\uDCAE \uD83D\uDCAE This is a cab booking system in python .
            This cab booking system project in Python project mainly focus on
            dealing with customer’s booking details with their respective bill amounts.\uD83D\uDCAE \uD83D\uDCAE \uD83D\uDCAE """,
        )
        self.about = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "About",
        )
        self.exit = tkinter.Button(root,
            activebackground = "#c0c5fe",
            background = "#c0c5fe",
            borderwidth = 5,
            cursor = "hand2",
            font = "{Leelawadee UI} 10 bold",
            text = "Exit",
        )
        self._label_5 = tkinter.Label(root,
            activebackground = "#fff4d2",
            activeforeground = "#fb001a",
            background = "#ffff80",
            font = "{MS Sans Serif} 14 bold italic",
            foreground = "#fb001a",
            text = u" Made with \u2764  by Akash \uD83D\uDC68\uD83C\uDFFB\u200D  and Parnasree Das \uD83E\uDD35\uD83C\uDFFC ",
        )

        # widget commands

        self.login.configure(
            command = self.login_command
        )
        self.newuser.configure(
            command = self.newuser_command
        )
        self.about.configure(
            command = self.about_command
        )
        self.exit.configure(
            command = self.exit_command
        )


        # Geometry Management
        self._frame_1.grid(
            in_    = root,
            column = 5,
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._label_1.grid(
            in_    = root,
            column = 1,
            row    = 1,
            columnspan = 4,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 2,
            sticky = "nsew"
        )
        self._label_3.grid(
            in_    = root,
            column = 5,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_4.grid(
            in_    = root,
            column = 5,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.login.grid(
            in_    = root,
            column = 2,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.newuser.grid(
            in_    = root,
            column = 3,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_2.grid(
            in_    = root,
            column = 1,
            row    = 3,
            columnspan = 5,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.about.grid(
            in_    = root,
            column = 1,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self.exit.grid(
            in_    = root,
            column = 4,
            row    = 5,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_5.grid(
            in_    = root,
            column = 1,
            row    = 4,
            columnspan = 5,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )


        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 84, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 42, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 71, pad = 0)
        root.grid_rowconfigure(4, weight = 0, minsize = 36, pad = 0)
        root.grid_rowconfigure(5, weight = 1, minsize = 39, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 143, pad = 0)
        root.grid_columnconfigure(2, weight = 0, minsize = 147, pad = 0)
        root.grid_columnconfigure(3, weight = 0, minsize = 148, pad = 0)
        root.grid_columnconfigure(4, weight = 0, minsize = 40, pad = 0)
        root.grid_columnconfigure(5, weight = 0, minsize = 2, pad = 0)

