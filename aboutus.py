
import tkinter 
from tkinter import *
from aboutus_ui import Aboutus

# BEGIN USER CODE global

# END USER CODE global

class CustomAboutus(Aboutus):
    pass

    # BEGIN CALLBACK CODE
    # ONLY EDIT CODE INSIDE THE def FUNCTIONS.

    # close_command --
    #
    # Legacy command found in callback code. Add user comments inside body.
    def close_command(self):
        print("Close Buttton pressed.")
        print("About Us Window Closed.")
        quit(0)
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
    demo = CustomAboutus(root)
    root.title('aboutus')
    #try: run()
    #except NameError: pass
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__': main()
