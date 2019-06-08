# Simple enough, just import everything from tkinter.
from PIL import Image as ImagePIL, ImageTk as itk
import matplotlib.pyplot as plt
from tkinter import filedialog
from tkinter import ttk, simpledialog
import librosa.display
from tkinter import *
import numpy as np
import subprocess
import librosa
import os

# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        self.respuesta = []
        self.canal=0
        self.frecuencias=[]

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
        nb.grid(row=2, column=2, columnspan=400, rowspan=300, sticky='NESW')

        # Adds tab 1 of the notebook contaminacio puro, conta gaussiano,submuestreo fs ,modula,amplitud 
        page1 = ttk.Frame(nb)
        nb.add(page1, text='ONE SIGNAL')
        nb.pack(expand=50,fill='both')
        B = Button(page1, text ="PLAY",command=self.playAudio1,bg="pale turquoise", fg="black")
        B.pack(side='left',fill='y')
        Bd= Button(page1, text ="Graph",command=self.playAudio1,bg="pale turquoise", fg="black")
        Bd.pack(side='right',fill='y')
        self.create_canvas(page1)
        B8 = Button(page1, text ="Pure Tone Noise",width=15, height=1,bg="linen", fg="black")
        B8.place(x=60,y=3)
        #B4.pack()
        B9 = Button(page1, text ="Gaussian Noise", width=15, height=1, bg="linen", fg="black")
        B9.place(x=210,y=3)
        B0 = Button(page1, text ="Subsampling Fs", width=18, height=1, bg="linen", fg="black")
        B0.place(x=360,y=3)
        B10 = Button(page1, text ="Modulation", width=15, bg="linen", fg="black")
        B10.place(x=530,y=3)
        B11 = Button(page1, text ="Amplify", width=15, bg="linen", fg="black")
        B11.place(x=660,y=3)


        # Adds tab 2 of the notebook
        page2 = ttk.Frame(nb)
        nb.add(page2, text='TWO SIGNAL')
        nb.pack(expand=50,fill='both')
        B1 = Button(page2, text ="PLAY AUDIO 1",command=self.playAudio1,bg="pale turquoise", fg="black")
        B1.pack(side='left',fill='y')
        B2 = Button(page2, text ="PLAY AUDIO 2",command=self.playAudio2,bg="pale turquoise", fg="black")
        B2.pack(side='right',fill='y')

        B4 = Button(page2, text ="Signal 1 Time Domain",width=18, height=1,bg="linen", fg="black")
        B4.place(x=105,y=3)
        #B4.pack()
        B5 = Button(page2, text ="Signal 1 Frecuency Domain", width=25, height=1, bg="linen", fg="black")
        B5.place(x=250,y=3)
        B6 = Button(page2, text ="Signal 2 Time Domain", width=18, height=1, bg="linen", fg="black")
        B6.place(x=450,y=3)
        B7 = Button(page2, text ="Signal 2 Frecuency Domain", width=25, bg="linen", fg="black")
        B7.place(x=600,y=3)
        B12 = Button(page2, text ="Addition", width=25, height=1, bg="lavender", fg="black")
        B12.place(x=130,y=550)
        B13 = Button(page2, text ="Substaction", width=18, height=1, bg="lavender", fg="black")
        B13.place(x=390,y=550)
        B14 = Button(page2, text ="Multiplication", width=25, bg="lavender", fg="black")
        B14.place(x=600,y=550)
       

        #adds tab 3 of the notebook
        page3 = ttk.Frame(nb)
        nb.add(page3, text='FILTERS')
        nb.pack(expand=50,fill='both')
        B3 = Button(page3, text ="SELECT_CHANNEL",command=self.ask, bg="pale turquoise", fg="black")
        B3.pack(side='left',fill='y')
        B15 = Button(page3, text ="SELECT_5 Frecuencies to Noise",command=self.frec_noise, bg="pale turquoise", fg="black")
        B15.pack(side='right',fill='y')

    
    def ask(self):
        #0 es Izquierdo y 1 es Derecho
        a=simpledialog.askinteger('Select the Channel', 'Select the Channel, 0 is for Left and 1 for Right')
        self.canal=a

    def frec_noise(self):
        for i in range(5):
            a=simpledialog.askinteger('Frecuency to Noise', 'Put the Frecuency '+ str(i+1))
            self.frecuencias.append(a)

    def create_canvas(self,frame):
            canvas = Canvas(frame,width=600, height=100)
            canvas.pack(side=LEFT,fill='y')
            img = ImagePIL.open('audio.png')
            canvas.image=itk.PhotoImage(img)
            canvas.create_image(0,0, anchor='nw', image=canvas.image)



    def client_exit(self):
        exit()

    def dialog(self):
        my_filetypes = [('text files', '.wav')]

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

        # play = Menu(menubar)
        # menubar.add_cascade(label="Reproducir",menu=play)

        help_menu = Menu(menubar,tearoff = 0 )
        menubar.add_cascade(label="Help",menu=help_menu)


        # Add more elements to the canvas, potentially on top of the figure
       # self.create_text(150, 50, text="Grafica en el Dominio de la Frecuencia", anchor="s")
        




    def play_audio(self):
        subprocess.call(['ffplay', '-nodisp', '-autoexit', self.respuesta[0]])

    def plotAudio(self):
        audio = self.respuesta[0]
        y, Fs = librosa.load(audio, mono=False)
        plt.figure(figsize=(5,5))
        librosa.display.waveplot(y, sr=Fs)
        plt.savefig('audio.png')

    #def menu(self):

# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()

root.geometry("900x600")

# creation of an instance
app = Window(root)



# mainloop
root.mainloop()
