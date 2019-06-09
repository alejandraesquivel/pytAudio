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
        self.i=0
        self.amp=0
        self.modulacion=0
        self.f_pbaja_fir=[]
        self.f_altap_fir=[]
        self.f_pbanda_fir=[]
        self.f_rbanda_fir=[]
        self.f_pbaja_iir=[]
        self.f_altap_iir=[]
        self.f_pbanda_iir=[]
        self.f_rbanda_iir=[]

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

        # Adds tab 1 of the notebook contaminacion puro,
        # contaminacion gaussiano,submuestreo fs ,
        # modula,amplitud de la onda
        5
        page1 = ttk.Frame(nb)
        nb.add(page1, text='ONE SIGNAL')
        nb.pack(expand=50,fill='both')
        B = Button(page1, text ="PLAY",command=self.playAudio1,bg="pale turquoise", fg="black")
        B.pack(side='left',fill='y')
        Bd= Button(page1, text ="GRAPH",command=self.audio,bg="pale turquoise", fg="black")
        Bd.pack(side='right',fill='y')
        #self.create_canvas(page1)
        B8 = Button(page1, text ="Pure Tone Noise",command=self.conPuroAudio,width=15, height=1,bg="linen", fg="black")
        B8.place(x=60,y=3)
        #B4.pack()
        B9 = Button(page1, text ="Gaussian Noise",command=self.conGaussAudio,width=15, height=1, bg="linen", fg="black")
        B9.place(x=210,y=3)
        B0 = Button(page1, text ="Subsampling Fs",command=self.ask1,width=18, height=1, bg="linen", fg="black")
        B0.place(x=360,y=3)
        B10 = Button(page1, text ="Modulation",command=self.ask3,width=15, bg="linen", fg="black")
        B10.place(x=530,y=3)
        B11 = Button(page1, text ="Amplify",command=self.ask2,width=15, bg="linen", fg="black")
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
        B12 = Button(page2, text ="Addition", width=25,command=self.suma,height=1, bg="lavender", fg="black")
        B12.place(x=130,y=550)
        B13 = Button(page2, text ="Substaction", width=18,command=self.resta, height=1, bg="lavender", fg="black")
        B13.place(x=390,y=550)
        B14 = Button(page2, text ="Multiplication", width=25,command=self.multiplicacion, bg="lavender", fg="black")
        B14.place(x=600,y=550)


        #adds tab 3 of the notebook
        page3 = ttk.Frame(nb)
        nb.add(page3, text='FILTERS')
        nb.pack(expand=50,fill='both')
        B3 = Button(page3, text ="SELECT_CHANNEL",command=self.ask, bg="pale turquoise", fg="black")
        B3.pack(side='left',fill='y')
        B15 = Button(page3, text ="SELECT_5 Frecuencies to Noise",command=self.frec_noise, bg="pale turquoise", fg="black")
        B15.pack(side='right',fill='y')

        B16 = Button(page3, text ="FIR",command=self.win2, bg="pale turquoise", fg="black")
        B16.pack(side='top',fill='y')
        B17 = Button(page3, text ="IIR",command=self.pedir_frec_iir, bg="pale turquoise", fg="black")
        B17.pack(side='top',fill='y')

        B1 = Button(page3, text="Low Pass FIR", bg="linen", fg="black")
        B1.place(x=130, y=550)
        B2 = Button(page3, text="High Pass FIR", bg="linen", fg="black")
        B2.place(x=300, y=550)
        B3 = Button(page3, text="Pass Band FIR", bg="linen", fg="black")
        B3.place(x=480, y=550)
        B4 = Button(page3, text="Split Band FIR", bg="linen", fg="black")
        B4.place(x=650, y=550)

        B1 = Button(page3, text="Low Pass IIR", bg="linen", fg="black")
        B1.place(x=130, y=450)
        B2 = Button(page3, text="High Pass IIR", bg="linen", fg="black")
        B2.place(x=300, y=450)
        B3 = Button(page3, text="Pass Band IIR", bg="linen", fg="black")
        B3.place(x=480, y=450)
        B4 = Button(page3, text="Split Band IIR", bg="linen", fg="black")
        B4.place(x=650, y=450)


    def ask(self):
        #0 es Izquierdo y 1 es Derecho
        a=simpledialog.askinteger('Select the Channel', 'Select the Channel, 0 is for Left and 1 for Right')
        self.canal=a

    def ask1(self):
        a=simpledialog.askinteger('Value Fs', 'Select Fs:')
        self.i=a
        self.submuestroAudio()

    def ask2(self):
        a=simpledialog.askinteger('Value Amplify', 'Select value:')
        self.amp=a
        self.amplificarAudio()

    def ask3(self):
        a=simpledialog.askinteger('Value Fs', 'More than double:')
        self.modulacion=a
        self.modulacionAudio()

    def makeform(self, fields):
        entries = {}
        for field in fields:
            print(field)
            row = Frame(self)
            lab = Label(row, width=22, text=field + ": ", anchor='w')
            ent = Entry(row)
            ent.insert(0, "0")
            row.pack(side=TOP, fill=X, padx=5,pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT,
                     expand=YES,
                     fill=X)
            entries[field] = ent
        return entries

    def frec_noise(self):
        for i in range(5):
            a=simpledialog.askinteger('Frecuency to Noise', 'Put the Frecuency '+ str(i+1))
            self.frecuencias.append(a)


    ## Ventana Emergente con fondo amarillo
    def win2(self):

        tl = Toplevel(self, bg="linen")
        tl.title("Input Frecuency Data")
        tl.geometry('600x400')
        tl.focus_set()
        tl.grab_set()
        tl.transient(master=self)

        inf = IntVar(tl)
        entry1 = Entry(tl, textvariable=inf)
        entry1.grid(row=0, column=1)
        label1 = Label(tl, text='minimun frequency', bg="red")
        label1.grid(row=0, column=0)

        entry2 = Entry(tl, textvariable=inf)
        entry2.grid(row=1, column=1)
        label2 = Label(tl, text='maximun frequency', bg="red")
        label2.grid(row=1, column=0)



    def pedir_frec(self):
        a=0
        for i in range(2):
            if a==0:
                x=simpledialog.askinteger('Frecuency to FIR', 'Put the Maximum Frecuency')
            else:
                x=simpledialog.askinteger('Frecuency to FIR', 'Put the Minimum Frecuency')
            a=1
            self.f_pbaja_fir.append(x)
            self.f_altap_fir.append(x)
            self.f_pbanda_fir.append(x)
            self.f_rbanda_fir.append(x)

    def pedir_frec_iir(self):
        a=0
        for i in range(2):
            if a==0:
                x=simpledialog.askinteger('Frecuency to IIR', 'Put the Maximum Frecuency')
            else:
                x=simpledialog.askinteger('Frecuency to IIR', 'Put the Minimum Frecuency')
            a=1
            self.f_pbaja_iir.append(x)
            self.f_altap_iir.append(x)
            self.f_pbanda_iir.append(x)
            self.f_rbanda_iir.append(x)


    def create_canvas(self,frame):
        canvas = Canvas(frame,width=50, height=50)
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

    # Funciones Basicas para cargar y dibujar
    def loadAudio(self):
        audio = self.respuesta[0]
        y, Fs = librosa.load(audio, mono=True)
        return [y,Fs]

    def plotAudio(self,y,Fs):
        plt.figure(figsize=(14,5))
        librosa.display.waveplot(y, sr=Fs)
        plt.show()

    # Graficas para una sola señal
    def audio(self): #Audio Original
        audio = self.loadAudio()
        self.plotAudio(audio[0],audio[1])

    def conPuroAudio(self): #Audio con Ruido Puro
        audio = self.loadAudio()
        N = len(audio[0])
        f = 5
        x = np.arange(N)
        noise = np.sin(2 * np.pi * f)
        suma = audio[0] + noise
        self.plotAudio(suma,audio[1])

    def conGaussAudio(self): #Audio con Gaussiano
        audio = self.loadAudio()
        noise = np.random.normal(0,1,audio[0].shape)
        gauss = audio[0] + noise
        self.plotAudio(gauss,audio[1])

    def submuestroAudio(self): #Audio con Submuestreo
        audio = self.loadAudio()
        Fsub = self.i #pasar submuestro
        self.plotAudio(audio[0],Fsub)

    def amplificarAudio(self): #Audio Amplificado
        name = 'amplificar.wav'
        audio = self.loadAudio()
        A = self.amp
        amplificar = A * audio[0]
        self.plotAudio(amplificar,audio[1])

    def modulacionAudio(self): #Audio Modulacion
        audio = self.loadAudio()
        channel = audio[0]
        f = audio[1] * self.modulacion * 3
        N = len(channel)
        n = np.arange(N)
        mod = np.multiply(np.multiply(1.5,channel),np.cos(np.multiply(2*np.pi*f,n)))
        self.plotAudio(mod,f)

    # Funciones para dos señales
    def playAudio1(self):
        subprocess.call(['ffplay', '-nodisp', '-autoexit', self.respuesta[0]])

    def playAudio2(self):
        subprocess.call(['ffplay', '-nodisp', '-autoexit', self.respuesta[1][0]])

    def audio2(self):
        audio = self.respuesta[1][0]
        y, Fs = librosa.load(audio, mono=True)
        return [y,Fs]

    def suma(self): #Suma dos señales mono
        audio = self.loadAudio()
        audio2 = self.audio2()
        N = len(audio[0])
        M = len(audio2[0])
        if M > N:
            channel2 = audio2[0][:N]
            suma = audio[0] + channel2
        else:
            channel2 = audio[0][:M]
            suma = audio2[0] + channel2
        self.plotAudio(suma, audio[1])

    def resta(self): #Resta de dos señales mono
        audio = self.loadAudio()
        audio2 = self.audio2()
        name = 'resta.wav'
        N = len(audio[0])
        M = len(audio2[0])
        if M > N:
            channel2 = audio2[0][:N]
            resta = audio[0] - channel2
        else:
            channel2 = audio[0][:M]
            resta = audio2[0] - channel2

        #writeAudio(name,resta,Fs1)
        self.plotAudio(resta, audio[1])

    def multiplicacion(self): #Multiplicación de dos señales mono
        audio = self.loadAudio()
        audio2 = self.audio2()
        N = len(audio[0])
        M = len(audio2[0])
        if M > N:
            channel2 = audio2[0][:N]
            multiplicacion = audio[0] * channel2
        else:
            channel2 = audio[0][:M]
            multiplicacion = audio2[0] * channel2
        name = 'multiplicacion.wav'

        #writeAudio(name,multiplicacion,Fs1)
        self.plotAudio(multiplicacion, audio[1])

    def low_pass_filter(x, samples=20):
        """ fft based brute force low pass filter """
        a = np.fft.rfft(x)
        tot = len(a)
        for x in xrange(tot - samples):
            a[samples + x] = 0.0
        return np.fft.irfft(a)

root = Tk()

root.geometry("1024x960")

# creation of an instance
app = Window(root)



# mainloop
root.mainloop()
