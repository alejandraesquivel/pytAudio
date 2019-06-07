# Simple enough, just import everything from tkinter.
from tkinter import *


# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")
        # self.minsize(640,400)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.create_menu()


    def client_exit(self):
        exit()
    def create_menu(self):
        # creating a menu instance
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create the file object)
        file_menu = Menu(menubar, tearoff= 0)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File",command=self.client_exit)
        file_menu.add_command(label="Exit", command=self.client_exit)

        # added "file" to our menu



        # create the file object)
        edit = Menu(menubar, tearoff= 0)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        # added "file" to our menu
        menubar.add_cascade(label="Edit", menu=edit)
        play = Menu(menubar)
        menubar.add_cascade(label="Reproducir",menu=play)

        help_menu = Menu(menubar,tearoff = 0 )
        menubar.add_cascade(label="Ayuda",menu=help_menu)

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("400x300")

# creation of an instance
app = Window(root)

# mainloop
root.mainloop()
