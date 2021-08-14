
import tkinter
from tkinter import *
#import sqlite3
import os
from tkinter import messagebox

# Using new-style classes: create empty base class object
# for compatibility with older python interps
#if sys.version_info < (2, 2):
#    class object:
#        pass

class Aboutus(object):
    _images = [] # Holds image refs to prevent GC
    def __init__(self, root):
        self._images.append(tkinter.PhotoImage('about.gif', file = os.path.dirname(__file__) + '/about.gif'))


        # Widget Initialization
        self._labelframe_1 = tkinter.LabelFrame(root,
            background = "#5ed5d5",
            font = "{Lucida Sans Unicode} 8 bold",
            foreground = "#ffffff",
            text = "License",
        )
        self._label_4 = tkinter.Label(root,
            activebackground = "#5ed5d5",
            background = "#5ed5d5",
            borderwidth = 0,
            image = "about.gif",
            text = "_label_4",
        )
        self._label_5 = tkinter.Label(root,
            activebackground = "#5ed5d5",
            activeforeground = "#000000",
            background = "#5ed5d5",
            borderwidth = 0,
            font = "Century 10 bold",
            foreground = "#000000",
            text = u"""Cab Booking System designed by Parnasree Das and Akash Kumar.
 \uD83D\uDC8C Email ID - pujadas2481@gmail.com
 \uD83D\uDCDE Phone number - +91-7973277319
 \uD83C\uDF10 Whats app - +91-7973277319""")
        self._label_1 = tkinter.Label(self._labelframe_1,
            activebackground = "#5ed5d5",
            activeforeground = "#000000",
            background = "#5ed5d5",
            font = "{MS Sans Serif} 8 bold",
            foreground = "#000000",
            justify = "left",
            text = """All Rights Reserved.
 
The author and publisher have taken care in the preparation of this software, but make no expressed or implied warranty of any kind and assume no responsibility
for errors or omissions. No liability is assumed for incidenttal or consequential damages in connection with or arising out of the use of the information or programs
contained herein.

This software is protected by copyright, and permission must be obtained from the publisher prior to any prohibited reproduction, storage in a retrieval system, or 
transmission in any form or by any means, electronic, mechanical, photocopying, recording, or likewise.

For more information regarding permissions, write us to or call: +91-7973277319.""")


        # Geometry Management
        self._labelframe_1.grid(
            in_    = root,
            column = 1,
            row    = 3,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "news"
        )
        self._label_4.grid(
            in_    = root,
            column = 1,
            row    = 1,
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
            row    = 2,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 1,
            sticky = "nsew"
        )
        self._label_1.grid(
            in_    = self._labelframe_1,
            column = 1,
            row    = 1,
            columnspan = 1,
            ipadx = 0,
            ipady = 0,
            padx = 0,
            pady = 0,
            rowspan = 3,
            sticky = "nsew"
        )


        # Resize Behavior
        root.grid_rowconfigure(1, weight = 0, minsize = 155, pad = 0)
        root.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        root.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        root.grid_columnconfigure(1, weight = 0, minsize = 5, pad = 0)
        self._labelframe_1.grid_rowconfigure(1, weight = 0, minsize = 40, pad = 0)
        self._labelframe_1.grid_rowconfigure(2, weight = 0, minsize = 40, pad = 0)
        self._labelframe_1.grid_rowconfigure(3, weight = 0, minsize = 40, pad = 0)
        self._labelframe_1.grid_columnconfigure(1, weight = 0, minsize = 40, pad = 0)


