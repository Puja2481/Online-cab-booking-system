
from tkinter import *
from Welcome_ui import Welcome
import tkinter
#from tkinter import *
#import sqlite3
import os
from tkinter import messagebox

# BEGIN USER CODE global

# END USER CODE global

class CustomWelcome(Welcome):
    pass

    # BEGIN CALLBACK CODE
    # ONLY EDIT CODE INSIDE THE def FUNCTIONS.

    # about_command --
    #
    # Callback to handle about widget option -command
    
    def about_command(self, *args):
        print("About Button Pressed.")
        import aboutus
        self.newwindow = tkinter.Toplevel()
        self.demo=aboutus.CustomAboutus(self.newwindow)
        #newwindow.destroy()
        pass

    # exit_command --
    #
    # Callback to handle exit widget option -command
    def exit_command(self, *args):
        print("Exit Button Pressed.")
        msg = messagebox.askyesno("Exit","Are you sure you want to exit ?", icon='warning')
        if msg:
            print("Welcome Window Closed.")
            quit(0)
        pass

    # login_command --
    #
    # Callback to handle login widget option -command
    def login_command(self, *args):
        print("Login Button Pressed.")
        import Loginuser
        self.newwindow = tkinter.Toplevel()
        self.demo=Loginuser.CustomLogin(self.newwindow)
        pass

    # newuser_command --
    #
    # Callback to handle newuser widget option -command
    def newuser_command(self, *args):
        print("New User Button Pressed.")
        import newuser1
        self.newwindow = tkinter.Toplevel()
        self.demo = newuser1.CustomNewuser(self.newwindow)
        pass

    # END CALLBACK CODE

    # BEGIN USER CODE class

    # END USER CODE class

def main():
    # Standalone Code Initialization
    # DO NOT EDIT
    #try: userinit()
    #except NameError: pass
    root = Tk()
    demo = CustomWelcome(root)
    root.title('Welcome')
    #try: run()
    #except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
