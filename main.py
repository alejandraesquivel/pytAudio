# Simple enough, just import everything from tkinter.
from tkinter import *
from tkinter import filedialog
import os
from tkinter import ttk
import subprocess

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        self.respuesta=[]

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()


    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI Signal Proccesor")
        # self.minsize(640,400)

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.create_menu()
        self.create_tabs()

    def create_tabs(self):
        nb = ttk.Notebook(self)
        nb.grid(row=1, column=0, columnspan=400, rowspan=300, sticky='NESW')
         
        # Adds tab 1 of the notebook
        page1 = ttk.Frame(nb)
        nb.add(page1, text='ONE SIGNAL')
        nb.pack(expand=50,fill='both')
        B = Button(page1, text ="PLAY",command=self.playAudio1)
        B.pack(side='left',fill='y')

        # Adds tab 2 of the notebook
        page2 = ttk.Frame(nb)
        nb.add(page2, text='TWO SIGNAL')
        nb.pack(expand=50,fill='both')
        B1 = Button(page2, text ="PLAY AUDIO 1",command=self.playAudio1)
        B1.pack(side='left',fill='y')
        B2 = Button(page2, text ="PLAY AUDIO 2",command=self.playAudio2)
        B2.pack(side='right',fill='y')

        page3 = ttk.Frame(nb)
        nb.add(page3, text='FILTERS')
        nb.pack(expand=50,fill='both')
    
    def client_exit(self):
        exit()
    def dialog(self):
        my_filetypes = [('text files', '.wav')]

        # Ask the user to select a folder.
        # answer_1 = filedialog.askdirectory(parent=self,
        #                                  initialdir=os.getcwd(),
        #                                  title="Please select a folder:")

        # Ask the user to select a single file name.
        answer_2= filedialog.askopenfilename(parent=self,
                                            initialdir=os.getcwd(),
                                            title="Please select a file:",
                                            filetypes=my_filetypes)

        # Ask the user to select a one or more file names.
        answer_3 = filedialog.askopenfilenames(parent=self,
                                             initialdir=os.getcwd(),
                                             title="Please select one or more files:",
                                             filetypes=my_filetypes)

        # Ask the user to select a single file name for saving.
        # answer_4 = filedialog.asksaveasfilename(parent=self,
        #                                       initialdir=os.getcwd(),
        #                                       title="Please select a file name for saving:",
        #                                       filetypes=my_filetypes)
        self.respuesta.append(answer_2)
        self.respuesta.append(answer_3)
    
    def playAudio1(self):
        print('respuesta')
        p=self.respuesta[0]
        subprocess.call(['ffplay','-nodisp','-autoexit',p])

    def playAudio2(self):
        print('respuesta',self.respuesta[1])
        p=self.respuesta[1]
        
        subprocess.call(['ffplay','-nodisp','-autoexit',p])

    def create_menu(self):
        # creating a menu instance
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create the file object)
        file_menu = Menu(menubar, tearoff= 0)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open File",command=self.dialog)
        file_menu.add_command(label="Exit", command=self.client_exit)

        # added "file" to our menu
        # create the file object)
        edit = Menu(menubar, tearoff= 0)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Undo")

        # added "file" to our menu
        menubar.add_cascade(label="Edit", menu=edit)

        help_menu = Menu(menubar,tearoff = 0 )
        menubar.add_cascade(label="Help",menu=help_menu)



# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("900x600")

# creation of an instance
app = Window(root)



# mainloop
root.mainloop()
