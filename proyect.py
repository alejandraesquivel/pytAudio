import matplotlib.pyplot as plt
import IPython.display as ipd
import scipy.io.wavfile as wf
import librosa.display
import subprocess
from tkinter import *
import tkinter as tk
import librosa
import numpy as np
import os

def playAudio(path):
    subprocess.call(['ffplay', path])

def plotAudio(y, Fs):
    plt.figure(figsize=(14,5))
    librosa.display.waveplot(y, sr=Fs)
    plt.show()

def conPuroAudio(N,y,Fs):
    f = 5
    Fs = Fs
    sample = N
    channel = y[0]
    name = 'contaminacionPuro,wav'
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f)
    suma = channel + y
    writeAudio(name,suma,Fs)
    plotAudio(suma, Fs)

def conGaussAudio(path):
    y, Fs = librosa.load(path, mono=False)
    channel = y[0]
    gauss = np.random.normal(0,1,channel.shape)
    plotAudio(gauss, Fs)

def submuestroAudio(Fs,path):
    Fsub = Fs
    name = 'submuestreo.wav'
    y, Fs = librosa.load(path, mono=False)
    channel = y[0]
    writeAudio(name,channel,Fsub)

def amplificarAudio(A,path):
    name = 'amplificar.wav'
    y, Fs = librosa.load(path, mono=False)
    channel = y[0]
    amplificar = A * channel
    writeAudio(name,amplificar,Fs)

def modulacionAudio(path):
    y, Fs = librosa.load(path, mono=False)
    x = y[0]
    f = 3 * Fs
    name = 'modulacion.wav'
    n = np.arange(len(x))
    mod = (1 + 0.5 * x) * np.cos(2 *  np.pi * f * n)
    writeAudio(name,mod,f)

def writeAudio(name,suma,Fs):
    librosa.output.write_wav(name, suma, Fs)

def main():
    audio = 'DrummerExample.wav'
    path = os.path.join('/Users/user/Desktop/PDS/ProyectoFinal/GUIPython/',audio)
    y, Fs = librosa.load(audio, mono=False)
    N = len(y[0])
    #playAudio(path)
    #plotAudio(y, Fs)
    #sumAudio(N,y,Fs)
    amplificarAudio(-8000,path)
    #modulacionAudio(path)
    #conGaussAudio(path)
    #submuestroAudio(10000,path)

if __name__ == '__main__':
    main()
